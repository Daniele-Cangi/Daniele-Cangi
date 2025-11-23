---
applyTo:
  - "**/*.py"
  - "**/pyproject.toml"
  - "**/requirements*.txt"
  - "**/setup.py"
---

# Python Coding Standards

## Style and Formatting

- Follow PEP 8 style guide
- Use type hints for all function signatures and class attributes
- Limit line length to 88 characters (Black formatter default)
- Use descriptive variable and function names in snake_case
- Use UPPER_CASE for constants

## Best Practices

- Always use type annotations (PEP 484)
- Prefer pathlib over os.path for file operations
- Use context managers (with statements) for resource management
- Implement proper error handling with specific exception types
- Use dataclasses or Pydantic models for structured data

## AI/ML Specific

- Document model architectures and hyperparameters
- Include data preprocessing steps and assumptions
- Use logging for training metrics and debugging
- Implement proper model versioning and checkpointing
- Consider memory efficiency for large-scale operations

## Frameworks

- **FastAPI/Flask**: Use dependency injection, implement proper validation, include API documentation
- **PyTorch/TensorFlow**: Follow framework conventions, use GPU efficiently, implement reproducibility
- **LLM/Agentic AI**: Implement proper prompt engineering, handle API rate limits, log interactions

## Testing

- Use pytest for testing
- Mock external dependencies and API calls
- Test edge cases and error conditions
- Include integration tests for AI pipelines

## Security

- Sanitize all user inputs
- Never commit API keys or credentials
- Use environment variables for sensitive configuration
- Validate data before processing
- Implement rate limiting for APIs
