---
tags:
  - library
title: "vercel-react-native-skills by vercel-labs/agent-skills"
url: "https://skills.sh/vercel-labs/agent-skills/vercel-react-native-skills"
company: [personal]
topics: []
created: 2026-03-03
source_type: raindrop
raindrop_id: 1627033880
source_domain: "skills.sh"
source_type_raindrop: article
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

Install the vercel-react-native-skills skill for vercel-labs/agent-skills

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: vercel-react-native-skills by vercel-labs/agent-skills

URL Source: https://skills.sh/vercel-labs/agent-skills/vercel-react-native-skills

Markdown Content:
# vercel-react-native-skills by vercel-labs/agent-skills

[](https://vercel.com/ "Made with love by Vercel")[Skills](https://skills.sh/)

[Official](https://skills.sh/official)[Audits](https://skills.sh/audits)[Docs](https://skills.sh/docs)

[skills](https://skills.sh/)/[vercel-labs](https://skills.sh/vercel-labs)/[agent-skills](https://skills.sh/vercel-labs/agent-skills)/vercel-react-native-skills

# vercel-react-native-skills

Installation

`$ npx skills add https://github.com/vercel-labs/agent-skills --skill vercel-react-native-skills`

Summary

**React Native and Expo best practices for performant mobile apps across list rendering, animations, navigation, and native modules.**

*   Covers eight rule categories prioritized by impact: list performance (FlashList, memoization, callback stability), animations (GPU properties, derived values), navigation, UI patterns, state management, rendering, monorepo structure, and configuration
*   List performance rules address critical concerns like virtualizing large lists, optimizing images, and avoiding inline objects that trigger unnecessary re-renders
*   Animation guidance focuses on GPU-accelerated properties (transform, opacity) and Reanimated patterns; navigation recommends native stack and tab navigators over JavaScript alternatives
*   Includes rules for modern UI patterns: expo-image for all images, Pressable over TouchableOpacity, native modals, and safe area handling in ScrollViews

SKILL.md

# React Native Skills

Comprehensive best practices for React Native and Expo applications. Contains rules across multiple categories covering performance, animations, UI patterns, and platform-specific optimizations.

## When to Apply

Reference these guidelines when:

*   Building React Native or Expo apps
*   Optimizing list and scroll performance
*   Implementing animations with Reanimated
*   Working with images and media
*   Configuring native modules or fonts
*   Structuring monorepo projects with native dependencies

## Rule Categories by Priority

| Priority | Category | Impact | Prefix |
| --- | --- | --- | --- |
| 1 | List Performance | CRITICAL | `list-performance-` |
| 2 | Animation | HIGH | `animation-` |
| 3 | Navigation | HIGH | `navigation-` |
| 4 | UI Patterns | HIGH | `ui-` |
| 5 | State Management | MEDIUM | `react-state-` |
| 6 | Rendering | MEDIUM | `rendering-` |
| 7 | Monorepo | MEDIUM | `monorepo-` |
| 8 | Configuration | LOW | `fonts-`, `imports-` |

## Quick Reference

### 1. List Performance (CRITICAL)

*   `list-performance-virtualize` - Use FlashList for large lists
*   `list-performance-item-memo` - Memoize list item components
*   `list-performance-callbacks` - Stabilize callback references
*   `list-performance-inline-objects` - Avoid inline style objects
*   `list-performance-function-references` - Extract functions outside render
*   `list-performance-images` - Optimize images in lists
*   `list-performance-item-expensive` - Move expensive work outside items
*   `list-performance-item-types` - Use item types for heterogeneous lists

### 2. Animation (HIGH)

*   `animation-gpu-properties` - Animate only transform and opacity
*   `animation-derived-value` - Use useDerivedValue for computed animations
*   `animation-gesture-detector-press` - Use Gesture.Tap instead of Pressable

### 3. Navigation (HIGH)

*   `navigation-native-navigators` - Use native stack and native tabs over JS navigators

### 4. UI Patterns (HIGH)

*   `ui-expo-image` - Use expo-image for all images
*   `ui-image-gallery` - Use Galeria for image lightboxes
*   `ui-pressable` - Use Pressable over TouchableOpacity
*   `ui-safe-area-scroll` - Handle safe areas in ScrollViews
*   `ui-scrollview-content-inset` - Use contentInset for headers
*   `ui-menus` - Use native context menus
*   `ui-native-modals` - Use native modals when possible
*   `ui-measure-views` - Use onLayout, not measure()
*   `ui-styling` - Use StyleSheet.create or Nativewind

### 5. State Management (MEDIUM)

*   `react-state-minimize` - Minimize state subscriptions
*   `react-state-dispatcher` - Use dispatcher pattern for callbacks
*   `react-state-fallback` - Show fallback on first render
*   `react-compiler-destructure-functions` - Destructure for React Compiler
*   `react-compiler-reanimated-shared-values` - Handle shared values with compiler

### 6. Rendering (MEDIUM)

*   `rendering-text-in-text-component` - Wrap text in Text components
*   `rendering-no-falsy-and` - Avoid falsy && for conditional rendering

### 7. Monorepo (MEDIUM)

*   `monorepo-native-deps-in-app` - Keep native dependencies in app package
*   `monorepo-single-dependency-versions` - Use single versions across packages

### 8. Configuration (LOW)

*   `fonts-config-plugin` - Use config plugins for custom fonts
*   `imports-design-system-folder` - Organize design system imports
*   `js-hoist-intl` - Hoist Intl object creation

## How to Use

Read individual rule files for detailed explanations and code examples:

```text
rules/list-performance-virtualize.md
rules/animation-gpu-properties.md
```

Each rule file contains:

*   Brief explanation of why it matters
*   Incorrect code example with explanation
*   Correct code example with explanation
*   Additional context and references

## Full Compiled Document

For the complete guide with all rules expanded: `AGENTS.md`

Weekly Installs

93.5K

Repository

[vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills "vercel-labs/agent-skills")

GitHub Stars

25.3K

First Seen

Jan 26, 2026

Security Audits

[Gen Agent Trust Hub Pass](https://skills.sh/vercel-labs/agent-skills/vercel-react-native-skills/security/agent-trust-hub)[Socket Pass](https://skills.sh/vercel-labs/agent-skills/vercel-react-native-skills/security/socket)[Snyk Pass](https://skills.sh/vercel-labs/agent-skills/vercel-react-native-skills/security/snyk)

Installed on

opencode 72.7K

codex 72.0K

gemini-cli 70.7K

github-copilot 68.3K

cursor 65.4K

kimi-cli 61.6K
