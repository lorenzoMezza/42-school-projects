*This project has been created as part of the 42 curriculum by lmezzaba.*

# NetPractice

## Description

NetPractice is a practical introduction to the basics of computer networking.
The goal of the project is to configure small simulated networks so that every
device can communicate correctly: assigning valid IP addresses, choosing the
right subnet masks, setting default gateways and defining routes through
routers.

The project consists of 10 levels of increasing difficulty. Each level shows a
non-working network diagram that must be fixed by editing the configurable
fields. The networks are simulated and are served through a training interface
that runs in the web browser.

## Instructions

### Running the training interface

1. Download the archive attached to the project page and extract it in any
   folder.
2. In that folder, run:
   ```bash
   ./run.sh
   ```
   This script launches a local web server and opens the interface in your
   default web browser.
3. If `run.sh` does not work, start the server manually:
   ```bash
   python3 -m http.server 49242
   ```
   then open `http://localhost:49242` in your browser (the port number can be
   changed).
4. Enter your login (`lmezzaba`) in the interface to use your personal
   configuration. Alternatively, the "evaluation" tab generates a random
   configuration, useful to practice for the defense.

### Solving a level

- Modify the unshaded fields until the network is correct.
- Use **[Check again]** to verify the configuration; the logs at the bottom of
  the page explain what is wrong (missing gateway, invalid IP, etc.).
- When a level is solved, a button appears to move on to the next one.

### Exporting configurations

- Before moving to the next level, click **[Get my config]** to download the
  configuration file of the level you just completed.

### Submission

- 10 exported configuration files (one per level) must be placed at the root
  of the repository, together with this `README.md`.
- During the defense, three random levels must be solved in a limited amount
  of time, without external tools (only a simple calculator such as `bc` is
  tolerated).

## Resources

### Networking concepts studied

- Subnet masks
- Network address, broadcast address and usable host range
- Routers and routing tables
- Switches

### References

- RFC 4632 – Classless Inter-domain Routing (CIDR)
- Articles and tutorials on IPv4 subnetting

### Use of AI

AI was used as a study aid to get explanations of networking concepts (subnet
masks, CIDR notation, gateways and routing) and to double-check my own
calculations. All the levels were solved and verified by me, and I am able to
explain every configuration submitted.
