---
applyTo:
  - "**/*.cypher"
  - "**/*.cql"
  - "**/*.graphql"
  - "**/*.gql"
---

# Graph Database and GraphQL Standards

## Neo4j/Graph Database Best Practices

- Use descriptive node labels and relationship types
- Follow naming conventions:
  - Node labels: PascalCase (e.g., `Person`, `Organization`)
  - Relationship types: UPPER_SNAKE_CASE (e.g., `WORKS_FOR`, `KNOWS`)
  - Properties: camelCase (e.g., `firstName`, `createdAt`)
- Create appropriate indexes for frequently queried properties
- Use parameters in Cypher queries to prevent injection
- Optimize queries for performance
- Document complex graph patterns and traversals

## GraphQL Schema Design

- Use clear, descriptive type and field names
- Follow GraphQL naming conventions (camelCase)
- Implement proper input validation
- Use interfaces for shared fields across types
- Design schemas that prevent N+1 query problems
- Document all types, fields, and arguments
- Use custom scalars for specific data types

## Query Optimization

- Implement pagination for large result sets
- Use DataLoader or similar batching solutions
- Cache frequently accessed data
- Limit query depth and complexity
- Profile and optimize slow queries

## Security

- Implement query complexity analysis
- Rate limit GraphQL endpoints
- Validate and sanitize all inputs
- Use proper authentication and authorization
- Never expose sensitive data in error messages
