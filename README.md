# genpark-differential-evolution-vector-optimizer-skill

> Differential Evolution (DE/rand/1/bin) continuous optimizer with donor vector mutation and binomial crossover.

Part of the **GenPark AI Agent Skills Matrix**. Production-ready, zero external dependencies, native Python 3.9+ standard library.

## Architecture

```mermaid
flowchart TD
    A[Initial Candidate Population] --> B[Evolutionary Selection & Variation]
    B --> C[Metaheuristic Swarm Optimization]
    C --> D[Optimal Global Solution]
    D --> E[MCP Protocol Endpoint]
```

## Features
- **Zero Third-Party Dependencies**: Pure Python standard library (`math`, `random`).
- **Robust Metaheuristics**: Genetic crossover/mutation, PSO swarm velocity, simulated annealing Metropolis criterion, and ACO stigmergy.
- **Native MCP Protocol Support**: Integrated JSON-RPC 2.0 stdio server ready for Claude Desktop, Cursor, and Windsurf.

## Installation

```bash
pip install genpark-differential-evolution-vector-optimizer-skill
```

Or clone directly:

```bash
git clone https://github.com/alphaparkinc/genpark-differential-evolution-vector-optimizer-skill.git
cd genpark-differential-evolution-vector-optimizer-skill
python example_usage.py
```

## Quick Start

```python
from client import *
# Refer to example_usage.py for end-to-end execution
```

## Model Context Protocol (MCP) Setup

Add to your `claude_desktop_config.json` or `cursor.json`:

```json
{
  "mcpServers": {
    "genpark-differential-evolution-vector-optimizer-skill": {
      "command": "python",
      "args": ["-m", "genpark-differential-evolution-vector-optimizer-skill.mcp_server"]
    }
  }
}
```

## License
MIT License. Copyright (c) 2026 AlphaPark Inc. & Alpha-Park.
