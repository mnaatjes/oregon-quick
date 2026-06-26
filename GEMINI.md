# Oregon Trail Agentic Ruleset

## Directives

- Always teach the user
- Always check before taking an action. 
- Always explain to the user what you plan on doing.
- Track project status in section of GEMINI.md
- Track TODOs in section of GEMINI.md
- Be concise and direct with responses - user can always ask for more info. 
- Use bullet-points in responses when appropriate

## Architecture
- **State/Logic Separation:** Modular design where `src/models/` hold Pydantic data and `src/engine/` handles systems.
- **Observability-First:** Subsystems for Telemetry, Inspection, Spatial view, and Control are decoupled via `ObservabilityManager`.
- **State Machine:** Game phases managed by a Finite State Machine (FSM) in `src/engine/states/`.
- **Control System:** "God Mode" console allows real-time state injection via `KeyboardInterrupt`.

## Documentation

- All documentation in docs/ follows diataxis structure
- All markdown docs must have frontmatter including title, tags, created-at, updated-at

## TODOs
- [ ] Implement Spatial Visualization (Map View)
- [ ] Implement Random Event Dispatcher
- [ ] Expand models (Party, Inventory)
- [ ] Integrate Textual for full TUI experience

## Project Status
- **Engine Core:** Functional game loop with 1.0s tick mechanism.
- **Observability:** Live Dashboard (Rich), Structured Logging, and Command Console (`set_food`, etc.) are operational.
- **Initial Logic:** `TravelState` implements basic movement and resource consumption.
