---
tags:
  - library
title: "dennisonbertram/claude-mac-guardian: macOS health, security, and performance monitoring plugin for Claude Code"
url: "https://github.com/dennisonbertram/claude-mac-guardian"
company: [personal]
topics: []
created: 2026-04-20
source_type: raindrop
raindrop_id: 1690976760
source_domain: "github.com"
source_type_raindrop: link
collection: "unsorted"
collection_id: -1
hydrated: true
hydrated_at: 2026-04-22
hydrated_via: github-api
---
## Excerpt

macOS health, security, and performance monitoring plugin for Claude Code - dennisonbertram/claude-mac-guardian

## Raw Content

<!-- Hydrated 2026-04-22 via github-api -->

# claude-mac-guardian

A Claude Code plugin that audits and maintains the health of a macOS machine. Runs read-only security, network, disk, performance, and connectivity checks and renders a unified dark-mode HTML dashboard you can open in any browser.

## Install

In Claude Code:

```
/plugin marketplace add dennisonbertram/claude-mac-guardian
/plugin install claude-mac-guardian@claude-mac-guardian
```

Or for local development:

```
git clone https://github.com/dennisonbertram/claude-mac-guardian
claude --plugin-dir ./claude-mac-guardian
```

## Skills

| Skill | Purpose |
| --- | --- |
| `machine-security-check` | SIP, Gatekeeper, FileVault, firewall, login items, launch agents, authorized_keys, shell rc anomalies |
| `malware-scan` | Heuristic scan for suspicious processes, persistence, unsigned binaries, recent writes in sensitive dirs |
| `network-diagnostics` | DNS, latency, packet loss, active interfaces, VPN state, listening ports |
| `wifi-debug` | SSID, RSSI, channel, noise, Tx rate, surrounding networks, recent disconnect events |
| `bluetooth-debug` | Paired and connected devices, battery levels, recent pairing events |
| `disk-usage` | Free space, largest directories, Time Machine snapshots, Xcode simulator footprint |
| `performance-check` | Load avg, memory pressure, swap, top CPU/mem, thermal state, battery health |
| `daily-health-report` | Orchestrates every skill, renders a unified HTML dashboard, opens in browser |
| `setup-health-cron` | Installs a launchd agent (or cron entry) to run the daily report on a schedule |

## Commands

- `/mac-health` — run the full suite and open the dashboard
- `/mac-daily-report` — render a dashboard from existing JSON (does not re-collect)
- `/mac-setup-cron [HH:MM]` — schedule the daily report via launchd

## How it works

Each skill writes a typed JSON result to `~/.mac-guardian/data/<skill>-<ISOdate>.json` with a shared schema:

```json
{
  "skill": "disk-usage",
  "timestamp": "2026-04-20T14:32:10Z",
  "severity": "ok",
  "summary": "One-line summary",
  "findings": [{ "id": "...", "severity": "warn", "title": "...", "detail": "..." }],
  "raw": { }
}
```

The `daily-health-report` skill aggregates all of today's JSON into `~/.mac-guardian/reports/report-<ISOdate>.html` and opens it. Only the last 30 reports are retained.

## Safety model

- All checks are read-only by default. Anything that would modify system state prompts first.
- No `sudo` unless explicitly scoped and narrated.
- `setup-health-cron` prompts before writing a launchd plist and shows the unload command.

## Screenshot

_Add a screenshot of `~/.mac-guardian/reports/report-*.html` here once generated._

## License

MIT — see [LICENSE](LICENSE).
