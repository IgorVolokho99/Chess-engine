# Architecture Overview

This project describes the project architecture.
It helps navigate in project effectively. You can find here folder structure with short description of files with code.
Also we put architecture of project's modules in this file, how they communicate.

## Project Root <br>
├── src/                        # Directory with all code <br>
│ ├── engine/                   # Directory with code of chess engine <br>
│ │ ├── coord.py                # File with coordinates logic(class Coord) <br>
│ │ ├── enums.py                # File with special enums of engine (color, figure etc) <br>
│ │ ├── fen_state.py            # File with Forsyth-Edwards notation logic <br>
│ │ ├── figure.py               # File with figure logic (class Figure )<br>
│ │ ├── node.py                 # File with MVP of generating chess-tree <br>
│ │ ├── position.py             # File with class Position, basically this file is input point of chess game <br>
│ ├── server/                   # Directory with code of server  <br>
│ │ ├── templates/              # Consist html-templates for Front Pages <br>
│ │ ├── app.py                  # Start <br>
├── tests/                      # Directory with tests of code, mainly for engine part <br>
│ ├── test_figure.py            # File with tests for class Figure <br>
│ ├── test_position.py          # File with tests for class Position <br>
├── README.md                   # Readme.md <br>
├── architecture.md             # File you are reading <br>
├── project_architecture.drawio # Drawio blocks with architecture of engine <br>

## Module responsibilities:
- engine
  - board state / posistion logic;
  - move generation;
  - move validation;
  - search and evaluation;
  - no web/HTML/DB logic.
- server
  - HTTP routes;
  - auth/session management;
  - request validation;
  - rendering templates / API responses;
  - calling engine via adapter;
  - DB read/write;
- db:
  - users, games, moves persistence;
  - migrations.

## Interaction of modules(current)<br>
![](/diagrams/Architecture_of_modules_current.png)

## Interaction of modules(target)<br>
![](/diagrams/Architecture_of_modules_target.png)

### Description of interaction:
- Client and server communicate using http-protocol;
- Server and DB communicate using SQL protocol;
- Communicate of engine and server:
  - In MVP, engine is used as a Python module import;
  - No separate HTTP service;
  - In the future, engine may be moved to a separate service;
- Server and engine will be scalable;
