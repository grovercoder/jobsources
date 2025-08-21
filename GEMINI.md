# Gemini Development Guidelines

This document outlines the core principles, technologies, and architectural patterns for development. It is intended to guide the Gemini AI assistant in making informed decisions during development.

## Application Requirements

* If a `docs/requirements.md` file exists every session should start with re-reading this file to be aware of the intent of the project.  
* The requirements.md file should be update as the application/project is developed.  The file should reflect the current needs of the application as it grows.

## Key Technologies & Development Standards

Always review `docs/requirements.md` to understand the intent of the application.

*   **Language:** Python
*   **Package Management:** `uv` tool.
    *   Initialize: `uv init`
    *   Add dependencies: `uv add <package_name>`
    *   Run commands: `uv run <command>`
*   **Code Standards:**
    *   Formatting: `black`
    *   Style & Static Analysis: `pylint`
        *   Run: `./scripts/run_pylint.sh`
*   **Testing:** `pytest` for all unit and integration tests.
    *   Run tests: `uv run python -m pytest`

*   **Revision Control**
    *   Use `git`
    *   Use the "summary / body" structure for commit messages.
    *   When committing create a `commit.msg` file that contains the commit message.  Then use ```git commit -F commit.msg && rm commit.msg``` to commit the changes.

*   **Configuration (.env):** When `.env` files are used for configuration, an `example.env` file must be created. This file should contain all configuration elements in their default state, along with comments explaining the intent and usage of each item.

## Non-Functional Requirements

*   **Maintainability:** Modular design, clear separation of concerns.
*   **Observability:** Logging for application processes and errors.
