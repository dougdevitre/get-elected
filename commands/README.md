# Commands

Slash command reference for instant document generation. Type any command to generate the specified artifact using your campaign context.

```mermaid
flowchart TD
    A["User Input"] --> B["Command Router"]
    B --> C["Getting Started"]
    B --> D["Fundraising"]
    B --> E["Messaging"]
    B --> F["Social Media"]
    B --> G["Compliance"]
    B --> H["GOTV"]
    B --> I["Strategy"]
    C --> J["Generated Artifact"]
    D --> J
    E --> J
    F --> J
    G --> J
    H --> J
    I --> J
```

## Files

- [commands.md](commands.md) -- Complete list of all slash commands with descriptions and usage

See also: [/commands.md](../commands.md) in the repository root for the top-level command reference.
