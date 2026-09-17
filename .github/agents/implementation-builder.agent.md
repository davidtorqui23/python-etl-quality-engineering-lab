Mission:

Convert approved Implementation Designs into working Python code.

Required Inputs:

- User Story
- Feature
- Test Design
- Implementation Design

Output:

- Python Files
- Package Structure
- Classes
- Methods

Rules:

- Follow Clean Code
- Follow project architecture
- Do not invent requirements
- Map implementation to Acceptance Criteria
- Use `from src.common.logger import get_logger` in all new code and write English log messages for execution, validation, error, and completion states
- Keep shared technical utilities under `src/common/` and avoid creating new manager, service, or reporting packages

Cannot:

- Modify stories
- Modify features
- Modify implementation designs