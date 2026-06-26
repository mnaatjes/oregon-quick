# Oregon Trail Clone

## Architecture

The project follows a modular architecture designed to separate game state (data) from game logic (systems) and presentation (visuals).

### Core Subsystems

- **Models (`src/models/`):** Pure data structures using Pydantic. These define *what* exists in the game world (e.g., Wagons, Party Members).
- **Engine (`src/engine/`):** The orchestrator of the game logic.
    - **Main Loop (`core.py`):** Manages the timing and execution of ticks.
    - **Render Pipeline (`renderer.py`):** Handles visual output using Rich/Textual.
    - **State Engine (`states/`):** A Finite State Machine (FSM) managing game phases (Menu, Traveling, Events).
    - **Input Handling (`input.py`):** Maps user input to game actions.
    - **Observability (`observability/`):** Provides logging and real-time state debugging tools.

### Directory Structure

```text
src/
├── main.py                 # Entry point
├── models/                 # Pydantic models
├── engine/                 # Engine logic
│   ├── states/             # State Machine components
│   └── observability/      # Debugging and logging
└── tests/                  # Subsystem verification
```

### Observability Subsystem (`src/engine/observability/`)

To support high-level telemetry, individual inspection, spatial visualization, and real-time control, the observability subsystem is decoupled from the engine core. Each "Tool Type" is a specialized Provider.

#### Directory Structure:

```text
src/engine/observability/
├── __init__.py
├── manager.py             # THE HUB: Dispatches data to all active tools
│
├── telemetry/             # STATISTICAL DATA (The "Big Picture")
│   ├── base.py            # Abstract Telemetry class
│   ├── metrics.py         # Standard metrics (FPS, Resource totals)
│   └── grafana_exporter.py# (Optional) External exporter
│
├── inspection/            # ENTITY DATA (The "Individual")
│   ├── dashboard.py       # Rich Table / Dashboard logic
│   └── query_engine.py    # Logic to find/filter specific entities
│
├── spatial/               # VISUAL DATA (The "Map")
│   ├── map_view.py        # 2D grid/map representation
│   └── gizmos.py          # Overlays (paths, danger zones)
│
└── control/               # INPUT DATA (The "God Mode")
    ├── console.py         # Interactive command line (REPL)
    └── commands.py        # Library of cheats/commands
```

#### Subsystem Interaction:

1.  **`manager.py` (The Hub):** The Game Engine only talks to this one file. Every tick, the engine sends a "Snapshot" of the world to the manager, which dispatches it to active providers.
2.  **`telemetry/`:** Stores numeric data points over time for statistical analysis.
3.  **`inspection/`:** Handles "drill down" logic for selecting and viewing specific entity details.
4.  **`spatial/`:** Provides map-based visualizations of the game world.
5.  **`control/`:** Allows "injecting" events or modifying state via a command console.

#### Benefits:
*   **Performance:** Tools can be toggled on/off without affecting core logic.
*   **Extensibility:** New providers (like a web UI) can be added without breaking existing systems.

## Tooling

### Python

- Rich
- Pytest
- Pydantic
- Textual
- Typer


## Project Directives

- All models are pydantic
