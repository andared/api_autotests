# API automation exercise

**Archived — no longer maintained.** This repository preserves a Python API testing exercise
from 2023. It is a historical example, and its dependencies and test environment are not
maintained for current use.

The tests demonstrate pytest fixtures, a small HTTP client, response schema checks, and CRUD
scenarios for a characters API. Running them requires the original test service and credentials;
the repository does not provide a standalone server.

- Test scenarios: [test-cases.txt](test-cases.txt)
- Test implementation: [src/tests](src/tests)
- Original dependency setup: [Pipfile](Pipfile)

The original test command was `pipenv run pytest` after configuring the service connection.
