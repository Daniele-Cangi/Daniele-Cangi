# Stars Count Update Script

This directory contains the script that automatically updates the total stars count in the README.md file.

## Overview

The `update_stars.py` script:
- Fetches all public repositories for the specified GitHub user
- Calculates the total number of stars received across all repositories
- Excludes forked repositories from the count (configurable)
- Updates the README.md file with the new count
- Only commits changes if the count has changed

## Prerequisites

- Python 3.11 or higher
- `requests` library: `pip install requests`
- GitHub token with `repo` scope (for API access)

## Usage

### Running Locally

1. **Set environment variables:**

```bash
export GITHUB_TOKEN="your_github_token_here"
export GITHUB_REPOSITORY_OWNER="Daniele-Cangi"
export README_PATH="README.md"
export IGNORE_FORKS="true"
```

2. **Run the script:**

```bash
python scripts/update_stars.py
```

### Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `GITHUB_TOKEN` | GitHub personal access token | - | Yes |
| `GITHUB_REPOSITORY_OWNER` | GitHub username | `Daniele-Cangi` | No |
| `README_PATH` | Path to README file | `README.md` | No |
| `IGNORE_FORKS` | Ignore forked repositories | `true` | No |

### Getting a GitHub Token

For local testing, you can create a Personal Access Token:

1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Give it a descriptive name (e.g., "Stars Counter Local")
4. Select scopes: `public_repo` (for public repositories)
5. Click "Generate token"
6. Copy the token immediately (you won't be able to see it again)

**Note:** In the GitHub Actions workflow, the `GITHUB_TOKEN` is automatically provided and doesn't need manual configuration.

## How It Works

1. **API Pagination:** The script uses GitHub's REST API to fetch repositories with pagination (100 per page) to handle users with many repositories.

2. **Star Calculation:** For each repository:
   - If `IGNORE_FORKS=true`, forked repositories are skipped
   - The `stargazers_count` is summed up

3. **README Update:** The script looks for a specific placeholder in README.md:
   ```
   <!-- STARS_COUNT_START -->30<!-- STARS_COUNT_END -->
   ```
   
   It replaces the number between the HTML comments with the new total.

4. **Change Detection:** If the count hasn't changed, the script exits without modifying the file.

## Testing

To test the script without modifying your README:

```bash
# Create a test README
cp README.md README.test.md

# Run with test file
export README_PATH="README.test.md"
python scripts/update_stars.py

# Check the changes
diff README.md README.test.md
```

## Troubleshooting

### "Could not find stars count placeholder"

Ensure your README.md contains the placeholder:
```markdown
<!-- STARS_COUNT_START -->0<!-- STARS_COUNT_END -->
```

### API Rate Limiting

- With authentication: 5,000 requests/hour
- Without authentication: 60 requests/hour

The script uses authentication via `GITHUB_TOKEN` to avoid rate limits.

### "Error fetching repos: 401"

Your `GITHUB_TOKEN` is invalid or expired. Generate a new token.

## GitHub Actions Workflow

The script is automatically run by the GitHub Actions workflow (`.github/workflows/update-stars.yml`):

- **Trigger:** Daily at 00:00 UTC, on push to main, or manually via workflow_dispatch
- **Process:** 
  1. Checks out the repository
  2. Sets up Python 3.11
  3. Installs dependencies
  4. Runs the update script
  5. Creates a PR with changes (if any)

The workflow uses `peter-evans/create-pull-request@v5` to automatically create a PR when the count changes, allowing you to review before merging.
