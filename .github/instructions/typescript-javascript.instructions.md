---
applyTo:
  - "**/*.ts"
  - "**/*.tsx"
  - "**/*.js"
  - "**/*.jsx"
  - "**/package.json"
  - "**/tsconfig.json"
---

# TypeScript/JavaScript Coding Standards

## Style and Formatting

- Use TypeScript for all new code
- Follow consistent naming conventions:
  - camelCase for variables and functions
  - PascalCase for classes and types
  - UPPER_CASE for constants
- Use ESLint and Prettier for code formatting
- Prefer const over let, avoid var
- Use arrow functions for callbacks and short functions

## TypeScript Best Practices

- Enable strict mode in tsconfig.json
- Define explicit types, avoid `any`
- Use interfaces for object shapes, types for unions/intersections
- Leverage generics for reusable components
- Use enums for fixed sets of values

## React Development

- Use functional components with hooks
- Implement proper prop types and interfaces
- Follow component composition patterns
- Use React.memo for performance optimization
- Handle async operations with proper loading and error states

## Node.js Best Practices

- Use async/await over callbacks
- Implement proper error handling middleware
- Use environment variables for configuration
- Validate inputs with libraries like Zod or Joi
- Log requests and errors appropriately

## GraphQL

- Define clear schema with proper types
- Implement efficient resolvers
- Use DataLoader for batching and caching
- Handle errors consistently
- Document queries and mutations

## Testing

- Use Jest for unit testing
- Use React Testing Library for component tests
- Mock external dependencies
- Test user interactions and edge cases
- Maintain high test coverage for critical paths

## Security

- Sanitize user inputs to prevent XSS
- Use parameterized queries to prevent injection attacks
- Implement proper authentication and authorization
- Keep dependencies up to date
- Follow OWASP security guidelines
