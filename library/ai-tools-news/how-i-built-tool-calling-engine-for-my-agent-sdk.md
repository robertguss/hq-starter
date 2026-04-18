---
tags:
  - library
title: "How I built tool calling engine for my agent SDK"
url: "https://parthshr370.github.io/blogs/how-i-built-tool-calling-engine-for-my-agent-sdk/"
company: [personal]
topics: []
created: 2026-04-13
source_type: raindrop
raindrop_id: 1683790800
source_domain: "parthshr370.github.io"
source_type_raindrop: link
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: How I built a tool calling engine for my Go agent SDK

URL Source: https://parthshr370.github.io/blogs/how-i-built-tool-calling-engine-for-my-agent-sdk/

Published Time: April 13, 2026

Markdown Content:
April 13, 2026 • 8 min read

Go Agent SDK series - Part 2

![Image 1: How I built tool calling engine for my agent SDK](https://parthshr370.github.io/blogs/how-i-built-tool-calling-engine-for-my-agent-sdk/toolcalling_painitng_banner_image.jpg)
**Prerequisites:** Part one of this series ([structs, messages, and history](https://parthshr370.github.io/blogs/how-i-built-my-own-langchain-from-scratch-in-go/)), basic understanding of Go reflection, and familiarity with JSON Schema. The post explains reflection as it comes up, so you don't need to be an expert.

This is part two of a multi-blog series on building a **Go Agent SDK from scratch**. Part one covered the backbone, the **structs** that map to the API schema, **message builders** that shape each turn, and how **history** is maintained as a growing `[]llm.Message` slice. If you haven't read that yet, start [here](https://parthshr370.github.io/blogs/how-i-built-my-own-langchain-from-scratch-in-go/). This part picks up where that left off, diving into the most complex piece of the whole system, **tool calling**.

Since the previous blog we had been building the 3/4 foundation of any agent SDK,

*   **Structs** to handle the API schema
*   **Messages** to wrap every event of conversation into something LLM can understand
*   **History** the append array that contains every message and all

## Playing with tools

Now comes the last and most complex part of this codebase which took a lot of my time tinkering and architecturing to get it right. **Tool calling**.

Tools might be my favourite part of the whole agentic ecosystem. They are, _functions that you can let the LLM trigger on your system_. The best example is Claude Code using a combination of bash tools to search and execute files on your system.

A general tool run in any system might look something like this.

![Image 2: Tool calling high level flow](https://parthshr370.github.io/blogs/how-i-built-tool-calling-engine-for-my-agent-sdk/tool-calling-vague-flow.excalidraw.png)
The LLM interprets these tools as JSON schema, something like:

```
{ // this is just a JSON version of a function if you look closely
  "type": "function",
  "function": {
    "name": "get_weather",
    "description": "Get current weather for a city",
    "parameters": {
      "type": "object", // the args come in as one JSON object
      "properties": {
        "city": {"type": "string", "description": "The city name"}
      },
      "required": ["city"]
    }
  }
} // we use JSON because its the most standardized way to deal with schemas, objects and functions
```

Now implementing this can be a bit complex in practice. The **core problem** is this: we define our tools in Go as regular functions, but the LLM only understands _JSON_. There's a translation layer sitting in between that needs to do two things.

*   _convert our Go function signatures into something the LLM can read_ so it knows what arguments to send
*   _convert the LLM's JSON response back into actual Go values_ we can use to call the function

These questions shape the fundamental building blocks for my tool calling engine in my agent-framework.

## What a tool looks like

Before anything else, we need a way to describe a tool (just like we did in our API structs). We define a few structs that hold the necessary information one needs to call a tool.

```
type Tool struct {
    Type     string              `json:"type"`     // always "function" for now
    Function FunctionDescription `json:"function"` // the actual function metadata lives here
}
```

`Type` is always `"function"` for now. `Function` wraps the _actual metadata_, the name, the description, and the parameters schema. We send these in the request so the LLM knows what's available.

```
type FunctionDescription struct {
    Name        string      `json:"name"`                  // what the LLM uses to call the tool
    Description string      `json:"description,omitempty"` // tells the LLM when to use it
    Parameters  interface{} `json:"parameters"`            // this is where the JSON Schema goes
}
```

Walk through the fields here. `Name` is the identifier the LLM uses to call the function, like `get_weather`. `Description` tells the LLM what this tool does, so it can decide when to use it. `Parameters` is the _interesting one_, its typed as `interface{}` because it holds a **JSON Schema object**, which is a nested dictionary with no fixed shape. Go doesn't have a "JSON object" type, so `interface{}` is our catch-all.

```
{
  "type": "object",
  "properties": {
    "city": {"type": "string", "description": "The city to get weather for"},
    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
  },
  "required": ["city"]
}
```

Tool is what gets sent in the `ChatRequest.Tools` field. The Parameters field holds a **JSON Schema object**, this is what tells the LLM what parameters to fill in in order to call this tool correctly.

Now when the LLM decides to call a tool it does not magically do so, rather it sends back a schema with the tool_name and its corresponding arguments to execute that function on our machine.

```
type ToolCall struct {
    ID       string       `json:"id"`       // unique id we must send back later
    Type     string       `json:"type"`
    Function FunctionCall `json:"function"`
}

type FunctionCall struct {
    Name      string `json:"name"`      // which tool the LLM wants
    Arguments string `json:"arguments"` // JSON string, not a nested object
}
```

`ID` is a _unique identifier_ for this specific tool call. We need to echo this back when sending the result, otherwise the LLM can't match which result goes with which call.

`Type` is always `"function"`, same as the Tool struct above.

`Function.Name` is which function the LLM wants to call, like `get_weather`.

`Function.Arguments` is the subtle but important detail. Arguments is a **string**, not a JSON object. The LLM sends something like `{"city": "Paris"}` as a JSON string inside JSON. This is OpenAI's format, and its counterintuitive, you'd expect a nested object, but its a serialized string. We'll need to parse this string separately when we execute the tool.

## Registering a tool

Now we have our structs. The next question is how does a Go function become something the LLM knows about?

Since I wanted this to be as seamless as possible, it would make sense for the tools to be written and executed in Go. The flow goes something like this.

The user writes a regular Go function:

```
type LookupArgs struct {
    Topic string `json:"topic" description:"The topic to look up"`
}

func LookupFact(args LookupArgs) string {
    return "some fact about " + args.Topic
}
```

And registers it:

`myAgent.RegisterTool("lookup_fact", "Look up facts about programming languages", LookupFact)`
What happens inside the `Register` function as a whole is where the gears actually move, it mainly does **three things**.

1.   **Validates the function** - checks that it's actually a function and has exactly one argument
2.   **Extracts the argument type** - so it knows the struct type to create later when the LLM calls this tool
3.   **Generates a JSON Schema** - this is how the LLM knows what parameters to send

Now the first point might raise a question of why exactly one argument? Is that a limitation?

Not quite. The function takes one struct, but that struct can have as many fields as you want:

```
type WeatherArgs struct {
    City    string `json:"city" description:"The city name"`
    Unit    string `json:"unit" description:"Temperature unit"`
    Country string `json:"country" description:"Country code"`
}

func GetWeather(args WeatherArgs) string {
    // all three fields available here
}
```

This is a _design choice I took_, which is in _line with what OpenAI and Anthropic expect tool call arguments as_(**a single JSON object with its properties**). One struct with N fields maps naturally to that.

You can group the related parameters into one struct and then the struct becomes the JSON object and the fields become the properties.

So Register does three things (validate, extract type, generate schema), but where does all of that actually get stored? We need something that holds everything required to both _describe the tool to the LLM_ and to _execute it later when the LLM comes back with arguments_. That's what Register builds and stores.

```
type ToolDefinition struct {
    Name        string
    Description string
    Func        reflect.Value
    ArgsType    reflect.Type
    Schema      map[string]any
}
```

**Side note:** reflection is something that is gonna be repeated here a lot. It is essentially the idea of peeking inside a function or a data structure and seeing its little details. `reflect` is the library at use and `Value` and `Type` tell the corresponding value and type of the function of concern.

`Func reflect.Value` is the _actual Go function_ stored via reflection. Since Go is statically typed we cannot store two functions in the same map. `reflect.Value` is the escape hatch that lets you hold any function regardless of its signature.

`ArgsType reflect.Type` tells us the type of the argument the function takes. If the function is `GetWeather(args WeatherArgs)`, ArgsType holds the type info for `WeatherArgs`. We need this because when the LLM calls this tool later, we need to create a fresh instance of this struct to unmarshal the JSON arguments into.

`Schema map[string]any` is the **JSON Schema** we generated from the struct. This goes straight into the API request. When its time to send tools to the LLM, we already have the schema ready to go.

```
type Registry struct {
    definitions map[string]ToolDefinition
}
```

Here `definitions` is a map that maps the function name to its `ToolDefinition`. Simple lookup by name, (O(1) access) when the LLM sends back a tool call and we need to find the right function fast.

`ToolDefinition` is our bridge to everything. It holds both sides of the translation layer, the LLM-facing metadata (**Name, Description, Schema**) and the execution-facing machinery (**Func, ArgsType**). Without both, you either can't describe the tool to the LLM or can't actually run it when the time comes.

## Making Go speak JSON

So we have our skeleton (`ToolDefinition`), but we haven't actually talked about how that Schema field gets built. Register extracts the argument type and then calls `jsonschema.GenerateSchema(argType)` to convert our Go struct into something the LLM can understand (JSON). This function is the other half of our translation layer.

The LLM needs to know what arguments to send, but it doesn't understand Go types. _JSON Schema is the contract language both sides agree on_. The function takes a `reflect.Type` and walks through it to produce a `map[string]any`.

```
func GenerateSchema(t reflect.Type) map[string]any {
    if t.Kind() == reflect.Ptr {
        t = t.Elem()
    }

    switch t.Kind() {
    case reflect.String:
        return map[string]any{"type": "string"}
    case reflect.Int, reflect.Int8, reflect.Int16, reflect.Int32, reflect.Int64:
        return map[string]any{"type": "integer"}
    }

    if t.Kind() == reflect.Struct {
        properties := make(map[string]any)
        required := []string{}

        for i := 0; i < t.NumField(); i++ {
            field := t.Field(i)
            jsonTag := field.Tag.Get("json")
            if jsonTag == "" || jsonTag == "-" {
                continue
            }
            fieldSchema := GenerateSchema(field.Type)
            if desc := field.Tag.Get("description"); desc != "" {
                fieldSchema["description"] = desc
            }
            properties[jsonTag] = fieldSchema
        }

        return map[string]any{
            "type":       "object",
            "properties": properties,
            "required":   required,
        }
    }

    return nil
}
```

**All the little things this loop is doing under the hood**

It reads the `json` tag. If there's no json tag or it's `"-"`, the field gets skipped.

It parses the json tag to get the property name. `json:"city"` means the property name is city and its required. `json:"city,omitempty"` means its optional.

It checks for a `description` tag. This is what makes the LLM actually understand what each parameter means, with its type.

Then it recursively calls `GenerateSchema` on the field's own type. This handles nested structs by going deeper until it hits a primitive type.

First it handles pointers by dereferencing them. Then come the _base cases_, primitives. String maps to `{"type": "string"}`, int maps to `{"type": "integer"}`, float64 maps to `{"type": "number"}`, bool maps to `{"type": "boolean"}`.

Then the _interesting part_, structs. This scary loop is where the **real work** happens. It walks over the fields of the struct, reads the tags on each field, and slowly builds the JSON object that will eventually get passed to the LLM.

```
type WeatherArgs struct {
    City string `json:"city" description:"The city name"`
    Unit string `json:"unit,omitempty" description:"Temperature unit"`
}
```

`GenerateSchema` does not care about the function body here. It only cares about the argument struct and the tags written on its fields. So when it walks through `WeatherArgs`, the output it builds looks like this:

```
{
  "type": "object",
  "properties": {
    "city": {
      "type": "string",
      "description": "The city name"
    },
    "unit": {
      "type": "string",
      "description": "Temperature unit"
    }
  },
  "required": ["city"]
}
```

This schema is what gets stored in `ToolDefinition.Schema` and _eventually sent to the LLM as part of the tool definition_. So the full flow of **Register** is validate the function, extract the ArgsType, generate a JSON Schema from that type via reflection, and store everything as a ToolDefinition in the Registry's map.

One call, and everything gets captured and stored in the Registry.

## Getting tools to the LLM

So now we have the schema generated and stored. But _the LLM still doesn't know about it_. The schema is sitting in our Registry's map, and _until we actually send it to the LLM as part of a request_, none of this matters. The LLM can't call a tool it doesn't know exists.

On our side, tools live in the Registry as `ToolDefinition` structs in a map. On the LLM's side, it expects a list of tools in the request payload, something it can scan through and decide what fits. _Two different formats, two different worlds_, and we need to bridge them.

```
[get_weather] Get current weather for a city
[lookup_fact] Look up facts about programming languages
[send_email] Send an email to a user
```

`GetAllTools()` does this. It iterates over all the definitions in the Registry's map, converts each one into an `llm.Tool`, and returns a slice.

`func (r *Registry) GetAllTools() []llm.Tool`
**Side note:** the result slice is initialized as `make([]llm.Tool, 0)`, not as a nil slice. In Go, a nil slice marshals to `null` in JSON, but an empty slice marshals to `[]`. Some providers will reject `null` for the tools field but accept `[]`.

This slice is what gets plugged into `ChatRequest.Tools` before every request. _Every single time we call the LLM_, the tools go along for the ride.

You can check the full function at [tools/registry.go:GetAllTools](https://github.com/parthshr370/Go-Agent-sdk/blob/main/tools/registry.go)

## The other way - executing a tool call

That covers the _outbound journey_. Our Go function is now a JSON Schema that the LLM can read. But what happens when the LLM talks back? **When it says "call get_weather with {city: Paris}",** how does that _JSON string become an actual Go function call on our machine_?

So the LLM just talked back. It decided to call a tool and sent us something _like that_. But that's a **JSON string**. We have an _actual Go function_ sitting in our Registry. How does that string become a function call on our machine?

This is the reverse of what we just built. Outbound was **Go** to **JSON**. Inbound is **JSON** back to **Go**. And reflection is the hinge again.

*   **Find** the function by name in our Registry
*   **Create** an empty struct of the right type to receive the arguments
*   **Fill** it with the JSON the LLM sent
*   **Call** the actual Go function
*   **Return** the result

`Execute(name string, argsJson string) (string, error)`
**Side note:****marshalling** converts a Go struct into JSON. **Unmarshalling** does the reverse, it takes a JSON string and writes it into a Go struct. The key thing about `json.Unmarshal` is that it needs a pointer to something, it needs an existing struct to fill. If you want a cleaner first-principles pass on this bit, I wrote more about it in [`JSON, Marshals and Go`](https://parthshr370.github.io/blogs/json-marshals-and-go/).

First it looks up the `ToolDefinition` by name. If the tool doesn't exist in the Registry, error out right there. Then `reflect.New(def.ArgsType)` creates a pointer to a zero-value instance of the argument type, something like `*WeatherArgs{City: ""}`. We need a pointer here because `json.Unmarshal` needs something it can write into.

Then the argsJson string gets converted to `[]byte` and unmarshalled into that empty struct. Now we have `*WeatherArgs{City: "Paris"}`.

Then `def.Func.Call()` runs the actual Go function. But here's a gotcha. `reflect.New` gives us a pointer, and `Call` needs the actual value. `.Elem()` dereferences the pointer so `*WeatherArgs` becomes `WeatherArgs`. Without `.Elem()` the function would receive a pointer instead of the struct.

**Side note:**`.Elem()` is needed because `reflect.New` returns a pointer but our function expects a value. Without it, the function gets a `*WeatherArgs` instead of `WeatherArgs` and panics at runtime.

![Image 3: Execute turns JSON into a Go call](https://parthshr370.github.io/blogs/how-i-built-tool-calling-engine-for-my-agent-sdk/tool-execution-after-trigger.excalidraw.png)
The function returns a string, we extract it from the reflect.Value and send it back.

You can check the full function at [tools/execution.go:Execute](https://github.com/parthshr370/Go-Agent-sdk/blob/main/tools/execution.go)

## Sending results back

The tool ran and we have a **result string**(or an error). But the LLM doesn't know that yet. We need to send that result back in a format it understands, and more importantly, in a way that _links back to the original tool call_.

If the tool succeeded, we wrap the result in a tool message:

`toolMsg = llm.NewToolResult(call.ID, call.Function.Name, result)`
This creates a _message with role_`tool`, the `tool_call_id` matching the original call, the function name, and the _result string as_`content`.

If the tool failed, we still send a message back, just formatted as an error:

`toolMsg = llm.NewToolError(call.ID, call.Function.Name, err)`
Same structure but the content becomes `"Error executing tool: <error>. Please fix your arguments."`. This is intentional. We are telling the LLM something went wrong and giving it a chance to try again with different arguments _(the LLM is surprisingly good at self-correcting when you give it a clear error message)_.

Now the `tool_call_id` here is the **critical linkage**. The LLM can request multiple tools in parallel in a single response, and each one gets a different ID. _When we send the results back, each tool result message carries the matching ID so the LLM knows to map the correct result with its corresponding request_.

And here's something that's easy to miss. Both the assistant's `tool_calls` message and the `tool result` messages _get appended to history before the next LLM call_. The LLM needs to see its own **request** and the **results** to make sense of what happened.

## The full picture

Now that we have all the pieces, let's trace a single tool call from registration to result.

You register `GetWeather`. `Register` validates it, extracts the ArgsType, generates the JSON Schema, stores it all as a `ToolDefinition`. One call, done.

Next time `Run()` fires, the agent builds a ChatRequest and throws `GetAllTools()` into the Tools field. The LLM sees the schema and thinks _I need weather data_. It responds with `finish_reason: "tool_calls"` and a ToolCall carrying `{"city": "Paris"}` as a string.

The _agent catches that, appends the assistant's `tool\_calls` message to history_, then calls **Execute** with the name and that JSON string.

*   Execute looks up the `ToolDefinition` by name
*   `reflect.New` creates an empty `WeatherArgs`
*   `json.Unmarshal` fills it with Paris
*   `.Elem()` dereferences the pointer
*   `Func.Call()` runs GetWeather for real. A string comes back

That **string** gets _wrapped in a tool result_ message with the matching `tool_call_id`, appended to history, and the agent recurses. _The LLM sees the full conversation including the tool result, and generates its final answer._

```
[Register]   reflection extracts type info -> JSON Schema generated -> stored as ToolDefinition
[Outbound]   GetAllTools -> []llm.Tool -> ChatRequest.Tools
[LLM]        sees tool list -> decides to call tool -> sends back ToolCall
[Execute]    lookup by name -> reflect.New -> json.Unmarshal -> .Elem() -> Func.Call()
[Result]     NewToolResult with tool_call_id -> appended to history
[LLM]        sees full history with tool result -> generates final answer
```

**Reflection** is the hinge on both sides of the translation. _**Outbound**_, it extracts type information to generate the schema. _**Inbound**_, it creates instances and calls functions dynamically based on what the LLM asked for.

## Function reference

*   **[`RegisterTool`](https://github.com/parthshr370/Go-Agent-sdk/blob/main/tools/registry.go)** - validates a Go function, extracts the ArgsType, generates its JSON Schema, and stores it all as a `ToolDefinition` in the Registry
*   **[`GenerateSchema`](https://github.com/parthshr370/Go-Agent-sdk/blob/main/tools/jsonschema/schema.go)** - walks a Go struct via reflection, reads json and description tags, and produces a JSON Schema object the LLM can understand
*   **[`GetAllTools`](https://github.com/parthshr370/Go-Agent-sdk/blob/main/tools/registry.go)** - converts all `ToolDefinition`s in the Registry into a `[]llm.Tool` slice that can be plugged into `ChatRequest.Tools`
*   **[`Execute`](https://github.com/parthshr370/Go-Agent-sdk/blob/main/tools/execution.go)** - looks up a tool by name, creates an empty args struct via reflection, unmarshals the LLM's JSON into it, calls the Go function, and returns the result string
*   **[`NewToolResult`](https://github.com/parthshr370/Go-Agent-sdk/blob/main/llm/messages.go)** - creates a tool result message with the matching `tool_call_id` and the output string
*   **[`NewToolError`](https://github.com/parthshr370/Go-Agent-sdk/blob/main/llm/messages.go)** - creates a tool error message that tells the LLM what went wrong and asks it to fix its arguments

## Bookend

So we started with the structs that describe tools to the LLM, then figured out how to register a Go function so the LLM knows it exists (reflection to extract type info, JSON Schema generation from struct tags), then built the reverse path where the LLM's JSON arguments become an actual Go function call (reflect.New, json.Unmarshal, .Elem(), Func.Call), and finally saw how tool results flow back to the LLM through properly linked messages.

But an agent that just registers tools and executes them in isolation is not very useful. The missing piece is the **conductor** that makes all of this work together as a loop, the `Run()` function. How does it decide whether the LLM wants to call a tool or is done responding? How does the recursion actually work? And what does the provider abstraction look like that lets this same loop work across OpenAI, Anthropic, and Gemini? That is what _part three_ is about.

* * *

### Further reading

If you want to keep going from here, these are the references that actually connect well with this post.

*   **[Go Agent SDK repo](https://github.com/parthshr370/Go-Agent-sdk)** - the full codebase behind this post
*   **[Agent SDK Blog 1](https://parthshr370.github.io/blogs/how-i-built-my-own-langchain-from-scratch-in-go/)** - the previous part covering structs, messages, and history
*   **[JSON, Marshals and Go](https://parthshr370.github.io/blogs/json-marshals-and-go/)** - useful if you want a cleaner mental model for marshalling, unmarshalling, and structs before revisiting this post
*   **[Anatomy of Subagents](https://parthshr370.github.io/blogs/anatomy-of-subagents/)** - another piece of the larger agent-systems picture
*   **[Go `reflect` docs](https://pkg.go.dev/reflect)** - the most relevant official reference for the registration and execution internals here
*   **[Go `encoding/json` docs](https://pkg.go.dev/encoding/json)** - useful for understanding the marshal / unmarshal side of the pipeline

The next natural continuation from here is _part three_, the actual `Run()` loop, provider abstraction, recursion, and how all of this stops being isolated pieces and starts behaving like one agent system.
