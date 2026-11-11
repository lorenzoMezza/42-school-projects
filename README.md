# My 42 projects

The projects I built at [42](https://www.42network.org/), a peer-to-peer programming school with no teachers and no lectures: every project is a specification to implement on my own, then reviewed and tested by other students before it counts.

This is the **Common Core**, the first part of the curriculum. It starts with C written from scratch and moves to Python, systems, networks, AI and a final full-stack team project.

> The code is being added project by project: folders marked *Code coming soon* describe what the project is and will hold my solution.

## At a glance

| Area | Projects | Skills |
|---|---|---|
| **[C foundations](c-foundations)** | [Libft](c-foundations/libft), [ft_printf](c-foundations/ft_printf), [get_next_line](c-foundations/get_next_line), [push_swap](c-foundations/push_swap), [Codexion](c-foundations/codexion) | C, memory management, algorithms, POSIX threads |
| **[Python](python)** | [Python Modules 00-10](python/python-modules), [A-Maze-ing](python/a-maze-ing), [Fly-in](python/fly-in), [Pac-Man](python/pac-man) | Typed Python, OOP, packaging, Pydantic, graph algorithms, games |
| **[AI and LLMs](ai)** | [Call Me Maybe](ai/call-me-maybe), [RAG against the machine](ai/rag-against-the-machine), [Agent Smith](ai/agent-smith) | LLM function calling, RAG, code agents, MCP |
| **[Systems, DevOps and networks](systems-and-networks)** | [Born2beroot](systems-and-networks/born2beroot), [NetPractice](systems-and-networks/netpractice), [Inception](systems-and-networks/inception), [The Answer Protocol](systems-and-networks/the-answer-protocol), [tree_nity](systems-and-networks/tree_nity) | Linux, Docker, TCP/IP, concurrent servers in Go |
| **[Web](web)** | [ft_transcendence](web/ft_transcendence) | Full-stack web, team work |
| **[Career](career)** | [ft_resume](career/ft_resume) | Professional writing, interviews |

## All projects

### C foundations

| Project | What it is | Language / tools | Status |
|---|---|---|---|
| [Libft](c-foundations/libft) | My own C standard library, reused in every later C project. | C | Code coming soon |
| [ft_printf](c-foundations/ft_printf) | A reimplementation of printf. | C | Code coming soon |
| [get_next_line](c-foundations/get_next_line) | Read a file one line at a time, from any file descriptor. | C | Code coming soon |
| [push_swap](c-foundations/push_swap) | Sort numbers with two stacks and the fewest operations possible. | C | Code coming soon |
| [Codexion](c-foundations/codexion) | A concurrency simulation: coders competing for a limited number of shared resources. | C, POSIX threads | Code coming soon |

### Python

| Project | What it is | Language / tools | Status |
|---|---|---|---|
| [Python Modules 00-10](python/python-modules) | Thirteen modules (00 to 10, plus two bis modules) that take Python from the basics to professional practice. | Python 3, mypy, flake8, Pydantic | Code coming soon |
| [A-Maze-ing](python/a-maze-ing) | A maze generator with a visual display. | Python 3 | Code coming soon |
| [Fly-in](python/fly-in) | Route a fleet of drones through a network of zones in as few turns as possible. | Python 3 | Code coming soon |
| [Pac-Man](python/pac-man) | A complete, playable Pac-Man game. | Python 3 | Code coming soon |

### AI and LLMs

| Project | What it is | Language / tools | Status |
|---|---|---|---|
| [Call Me Maybe](ai/call-me-maybe) | Teach a language model to answer with function calls a program can run. | Python 3, LLM | Code coming soon |
| [RAG against the machine](ai/rag-against-the-machine) | Retrieval-augmented generation: a model that answers from a set of documents. | Python 3, LLM, RAG | Code coming soon |
| [Agent Smith](ai/agent-smith) | An AI agent that solves coding challenges on its own. | Python 3, LLM, MCP, Docker | Code coming soon |

### Systems, DevOps and networks

| Project | What it is | Language / tools | Status |
|---|---|---|---|
| [Born2beroot](systems-and-networks/born2beroot) | Set up and secure a Linux server in a virtual machine. | Linux, virtualisation | Code coming soon |
| [NetPractice](systems-and-networks/netpractice) | Configure small networks so that every machine can reach the others. | TCP/IP | Code coming soon |
| [Inception](systems-and-networks/inception) | A small web infrastructure built from my own Docker images. | Docker, Docker Compose | Code coming soon |
| [The Answer Protocol](systems-and-networks/the-answer-protocol) | A multiplayer text adventure: a TCP server and two clients, one command-line and one graphical. | Go (C, C++, Rust or Zig allowed) | Code coming soon |
| [tree_nity](systems-and-networks/tree_nity) | A message queue with topics, producers and consumers. | Go or C++ | Code coming soon |

### Web

| Project | What it is | Language / tools | Status |
|---|---|---|---|
| [ft_transcendence](web/ft_transcendence) | The final team project: a complete web application. | Full stack, Docker | Code coming soon |

### Career

| Project | What it is | Language / tools | Status |
|---|---|---|---|
| [ft_resume](career/ft_resume) | A resume written to answer a real job offer, defended in an interview. | Writing | Code coming soon |

## The path through the Common Core

At 42 the projects unlock in circles, each building on the previous ones:

- **Core:** Libft
- **Circle 1:** ft_printf, get_next_line, push_swap
- **Circle 2:** Python Modules 00-10, A-Maze-ing, Born2beroot
- **Circle 3:** Codexion, Fly-in, Call Me Maybe
- **Circle 4:** Pac-Man, RAG against the machine, NetPractice
- **Circle 5:** Agent Smith, Inception, The Answer Protocol, tree_nity
- **Circle 6:** ft_transcendence, ft_resume

## How the repository is organised

```
c-foundations/          Libft, ft_printf, get_next_line, push_swap, Codexion
python/                 Python Modules 00-10, A-Maze-ing, Fly-in, Pac-Man
ai/                     Call Me Maybe, RAG against the machine, Agent Smith
systems-and-networks/   Born2beroot, NetPractice, Inception, The Answer Protocol, tree_nity
web/                    ft_transcendence
career/                 ft_resume
```

Every project folder has a README with what the project is, what it shows and how to run it.

## About the subjects

The project subjects belong to 42 and are not included here: each README describes the project in my own words.
