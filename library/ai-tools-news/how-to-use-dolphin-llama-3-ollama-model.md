---
tags:
  - library
title: "How to use Dolphin Llama 3 Ollama Model"
url: "https://www.gsnetwork.com/how-to-use-the-dolphin-llama-3-ollama-model/"
company: [personal]
topics: []
created: 2025-10-11
source_type: raindrop
raindrop_id: 1383803292
source_domain: "gsnetwork.com"
source_type_raindrop: article
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

The video below shows how to download ... Read more

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: How to use Dolphin Llama 3 Ollama Model

URL Source: https://www.gsnetwork.com/how-to-use-the-dolphin-llama-3-ollama-model/

Published Time: 2025-02-19T13:22:06+00:00

Markdown Content:
The video below shows how to download and run the Dolphin Llama 3 model.

## Ollama Program for Windows.

First download the ollama program files from ollama.com.

[https://ollama.com/](https://ollama.com/)

Next, we need to pull the dolphin-llama3 model.

This process starts by opening two terminals, one for the server and the other for the program. In the first terminal type **ollama serve**This will make it so the base Ollama server program is running.

In the second terminal, type**ollama run dolphin-llama3**

Close both terminals and run the commands again to ensure the uncensored model is running.

You can type in a question that would typically be censored to see if it is working.

The program is now running from the primary hard drive and we will discuss how to transfer it to an external drive.

I will be transferring the program and model to a [**SanDisk 128 GB USB 3.0 flash drive.**](https://amzn.to/444L7Eu)

First right click the flash drive, select format and under file system, select NTFS. This will make it so we can transfer files larger than 4GB. If you are using a large hard drive you can skip this step as it will be NTFS by default. Note that if you do select the new format it will delete anything you previously had saved on the flash drive. So do this when first using a new flash drive.

Transfer the ollama files from C:\Ollama to the external hard drive or flash drive.

We also need to copy over the base ollama server program that interfaces the model.

 To find where this is located you can type.

**Get-Command ollama**

In this case it was located here.

 C:\Users\cody\AppData\Local\Programs\Ollama

 We need to copy the files located within the ollama folder to the ollama folder on the external hard drive.

Now we can run the model from the external drive which could be the D:, E:, G:, H: or I: drive.

## Run Dolphin Llama 3 From an External Drive on Windows.

Now we will run the program from the external drive.

 Step 1:

 To run the program from the external drive first open two PowerShell terminals.

In the first terminal, we will run the server. Start by changing the directory to the external drive

 by typing **cd h:\**and then pressing Enter.

**cd h:\**

To change the environmental variables and set the model path this command is used.

**$env:OLLAMA_MODELS = “H:\ollama\models”**

Then start the server with the serve command.

**ollama\ollama.exe serve**

Step 2:

 In the second terminal, we will run the program.

Again change the directory to the external drive

**cd h:\**

Then type in the run command.

**ollama\ollama.exe run dolphin-llama3**

The first time this runs it might take a minute to initialize.

We can now type a question that would typically be censored to see if the model is working.

It gave an appropriate response so the model is not censored.

## **AnythingLLM Interface for Windows.**

Step 1.

The first step is to run the server within the PowerShell the same way as before.

We will set the path and then enter the serve command.

 Change directory

**cd h:\**

**$env:OLLAMA_MODELS = “H:\ollama\models”**

Then enter the serve command.

**ollama\ollama.exe serve**

Now go to [AnythingLLM.com](https://anythingllm.com/) and download the program.

For the path use the external drive\anythingllm

It will take a few minutes for the program to install.

Before opening the program a .env file needs to be added within the anythingllm folder. Open a text document and save this code to the folder location as a .env file. Make sure the model path is correct and in this case, is set to the h drive.

**OLLAMA_HOST=http://127.0.0.1:11434**

**LLM_PROVIDER=ollama**

**MODEL_BACKEND=dolphin-llama3**

**OLLAMA_MODEL_PATH=H:\Ollama\models**

Now start the program.

Pick Ollama: Run LLMs locally on your own machine.

The Ollama model should be

dolphin-llama3:latest

Once the program opens you can type in a question that would typically be censored to make sure that it is working.

### Open the program with just one click using a batch file on Windows.

Once installed you can run the program with one click if you add this one File 1: shown below to the external drive’s root folder. That means placing the file in the external drive’s main location, not in a folder.

File 1:

 Make the file name: start.bat

**@echo off**

**set DRIVE_LETTER=%~d0**

**set OLLAMA_MODELS=%DRIVE_LETTER%\ollama\models**

**echo Starting Ollama…**

**start “” %DRIVE_LETTER%\ollama\ollama.exe serve**

**:waitloop**

**rem Change the 11434 below to whatever port is actually used by ollama server**

**netstat -an | find “LISTENING” | find “:11434” >nul 2>&1**

**if errorlevel 1 (**

**timeout /t 1 /nobreak >nul goto waitloop**

**)**

**echo Starting AnythingLLM…**

**start “” %DRIVE_LETTER%\anythingllm\AnythingLLM.exe**

Once you place this file in the root folder just click start and it will open the server and AnythingLLM program. This makes it so you do not have to remember the run commands. This batch file code was provided by Alien Wise, from TAG Software in the Netherlands. Thank you very much for providing this code to help viewers more easily run the program. Also provided was the code below which makes it so when the USB drive is placed in the USB port, it automatically brings up a dialog, asking the user if they want to run Dolphin LLM.

File 2:

 Make the file name: autorun.inf

**[Autorun]**

**label=Dolphin LLM**

**shellexecute=start.bat**

**icon=customicon.ico**

**action=Start local Dolphin LLM**

Also, you could make a custom icon. Adjust the autorun.inf file to match the icon name and location.

Note: There are other dolphin programs that can be downloaded from Ollama.com. There is a smaller TinyDolphin model that can be used when your computer or device has less than 8GB of RAM. The 8B parameter Dolphin Llama 3 model requires 5.9 GiB of RAM available. There is also a Dolphin 3 model which uses the newer Llama 3.1 model. The process to download and use the models is very similar.

If you want to save this offline LLM for long term storage you can save it on a flash drive, [**Solild State Drive**](https://amzn.to/438Modb), [**Hard Disk Drive**](https://amzn.to/4hCepNO), or Blue-ray. Most of these storage types should save the program for 5-10 years. [**Blue-ray**](https://amzn.to/44y3xgU) is is actually the best option as it can cast store data for 20 plus years. Just like you store values in a safe it is not a bad idea to keep drives in [**farday box**](https://amzn.to/41j8nfX) to prevent damage.

## Dolphin Llama3 model on Linux

*   Create a local directory in your home folder: `mkdir -p ~/ollama/bin`
*   Place the ollama binary there and make it executable: `chmod +x ~/ollama/bin/ollama`
*   Add to your PATH: `export PATH=$HOME/ollama/bin:$PATH`

### Running the Model on Linux

**Terminal 1 (Server):**

bash

```
# Set the models directory to your home folder
export OLLAMA_MODELS="$HOME/ollama/models"

# Start the server
ollama serve
```

**Terminal 2 (Client):**

bash

```
# Pull and run the model
ollama run dolphin-llama3
```

### External Drive Setup (Linux)

For running from an external drive (assuming it’s mounted at `/media/username/drive_name`):

**Terminal 1:**

bash

```
cd /media/username/your_drive_name
export OLLAMA_MODELS="/media/username/your_drive_name/ollama/models"
./ollama serve
```

**Terminal 2:**

bash

```
cd /media/username/your_drive_name
./ollama run dolphin-llama3
```

### One-Click Startup Script for Linux

**File: start.sh**

bash

```
#!/bin/bash

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export OLLAMA_MODELS="$SCRIPT_DIR/ollama/models"

echo "Starting Ollama..."
"$SCRIPT_DIR/ollama" serve &

# Wait for server to start
echo "Waiting for Ollama server to start..."
while ! netstat -tuln | grep -q ":11434 "; do
    sleep 1
done

echo "Starting AnythingLLM..."
# For AppImage
if [ -f "$SCRIPT_DIR/anythingllm/AnythingLLM.AppImage" ]; then
    "$SCRIPT_DIR/anythingllm/AnythingLLM.AppImage" &
# For extracted application
elif [ -f "$SCRIPT_DIR/anythingllm/AnythingLLM" ]; then
    "$SCRIPT_DIR/anythingllm/AnythingLLM" &
# Try to find it in common locations
else
    echo "AnythingLLM executable not found. Please check the path."
fi

echo "Both services started successfully!"
```
 Make it executable: `chmod +x start.sh`
### Alternative Version or Linux (if netstat isn’t available)

Some minimal Linux distributions might not have `netstat`. Here’s an alternative:

**File: start.sh**

bash

```
#!/bin/bash

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export OLLAMA_MODELS="$SCRIPT_DIR/ollama/models"

echo "Starting Ollama..."
"$SCRIPT_DIR/ollama" serve &

# Wait for server to start using curl or wget
echo "Waiting for Ollama server to start..."
while ! curl -s http://localhost:11434 >/dev/null 2>&1; do
    sleep 1
done

echo "Starting AnythingLLM..."
if [ -f "$SCRIPT_DIR/anythingllm/AnythingLLM.AppImage" ]; then
    "$SCRIPT_DIR/anythingllm/AnythingLLM.AppImage" &
elif [ -f "$SCRIPT_DIR/anythingllm/AnythingLLM" ]; then
    "$SCRIPT_DIR/anythingllm/AnythingLLM" &
else
    echo "AnythingLLM executable not found. Please check the path."
fi

echo "Both services started successfully!"
```

### Start file usage on Linux

*   Place the `start.sh` file in the root of your external drive (same level as the ollama and anythingllm folders)
*   Make it executable: `chmod +x start.sh`
*   Double-click the file or run `./start.sh` from terminal

Key Differences from Windows Version:

1.   **No registry/system installation** – everything runs from user directories
2.   **Use forward slashes** instead of backslashes for paths
3.   **Use `export`** instead of `$env:` for environment variables
4.   **Mount points** instead of drive letters (like H:)
5.   **Executable permissions** need to be set with `chmod +x`
6.   **No .exe extension** needed

The core concept remains the same – you’re setting a custom models directory and running the ollama binary from a location you control, rather than requiring system-wide installation.

## Dolphin Llama3 model on Mac

**Download and Setup:**

*   Download the macOS version from ollama.com
*   Create a local directory in your home folder: `mkdir -p ~/ollama/bin`
*   Place the ollama binary there and make it executable: `chmod +x ~/ollama/bin/ollama`
*   Add to your PATH: `export PATH=$HOME/ollama/bin:$PATH`

### Running the Model on Mac

**Terminal 1 (Server):**

bash

```
# Set the models directory to your home folder
export OLLAMA_MODELS="$HOME/ollama/models"

# Start the server
ollama serve
```

**Terminal 2 (Client):**

bash

```
# Pull and run the model
ollama run dolphin-llama3
```
External Drive Setup (macOS) For running from an external drive (typically mounted at `/Volumes/DriveName`): **Terminal 1:**
bash

```
cd /Volumes/YourDriveName
export OLLAMA_MODELS="/Volumes/YourDriveName/ollama/models"
./ollama serve
```

**Terminal 2:**
bash

```
cd /Volumes/YourDriveName
./ollama run dolphin-llama3
```

### AnythingLLM Setup for macOS

**Step 1:** Start the server as above, then download AnythingLLM from AnythingLLM.com (choose the macOS version)

**Step 2:** Create the `.env` file in the AnythingLLM folder:

OLLAMA_HOST=http://127.0.0.1:11434
LLM_PROVIDER=ollama
MODEL_BACKEND=dolphin-llama3
OLLAMA_MODEL_PATH=/Volumes/YourDriveName/ollama/models
### One-Click Startup Script for macOS

Create a shell script instead of a batch file:

**File: start.sh**

bash

```
#!/bin/bash

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export OLLAMA_MODELS="$SCRIPT_DIR/ollama/models"

echo "Starting Ollama..."
"$SCRIPT_DIR/ollama/ollama" serve &

# Wait for server to start
while ! nc -z localhost 11434; do
    sleep 1
done

echo "Starting AnythingLLM..."
open "$SCRIPT_DIR/anythingllm/AnythingLLM.app"
```

Make it executable: `chmod +x start.sh`

### Key Differences from Windows to Mac:

1.   **Forward slashes** for all paths
2.   **`export`** instead of `$env:` for environment variables
3.   **`/Volumes/DriveName`** instead of drive letters
4.   **Shell script (.sh)** instead of batch file (.bat)
5.   **`open` command** to launch applications
6.   **`nc` (netcat)** to check if port is listening
7.   **No autorun.inf** – macOS doesn’t support autorun from external drives for security reasons

The process is very similar to Linux, with the main difference being how external drives are mounted (`/Volumes/` instead of `/media/`).

![Image 1: Cody Wabiszewski](https://www.gsnetwork.com/wp-content/uploads/2025/05/Cody-Wabiszewski.jpg)

Cody started the Global Science Network with the idea people should be focusing more time, energy, and resources on useful projects. He has a bachelor’s degree in aerospace engineering and a master’s degree in mechanical engineering. Cody has worked for the US federal government, a university, a large corporation, small businesses, and for himself. He has done human brain computer interface research and is currently working towards creating non-biological human consciousness.
