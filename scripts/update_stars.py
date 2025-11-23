#!/usr/bin/env python3
"""
Update total stars count in README.md
This script fetches all public repositories for a GitHub user,
calculates the total stars (excluding forks), and updates the README.md file.
"""

import os
import sys
import re
import requests
from typing import List, Dict, Any


def get_all_repos(username: str, token: str) -> List[Dict[str, Any]]:
    """
    Fetch all public repositories for a given username using pagination.
    
    Args:
        username: GitHub username
        token: GitHub token for authentication
    
    Returns:
        List of repository dictionaries
    """
    repos = []
    page = 1
    per_page = 100
    
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    while True:
        url = f'https://api.github.com/users/{username}/repos'
        params = {
            'type': 'public',
            'per_page': per_page,
            'page': page
        }
        
        print(f"Fetching page {page}...", file=sys.stderr)
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code != 200:
            print(f"Error fetching repos: {response.status_code}", file=sys.stderr)
            print(f"Response: {response.text}", file=sys.stderr)
            sys.exit(1)
        
        page_repos = response.json()
        
        if not page_repos:
            break
        
        repos.extend(page_repos)
        
        # Check if there are more pages
        if len(page_repos) < per_page:
            break
        
        page += 1
    
    return repos


def calculate_total_stars(repos: List[Dict[str, Any]], ignore_forks: bool = True) -> int:
    """
    Calculate total stars across all repositories.
    
    Args:
        repos: List of repository dictionaries
        ignore_forks: Whether to ignore forked repositories
    
    Returns:
        Total star count
    """
    total = 0
    
    for repo in repos:
        # Skip forks if requested
        if ignore_forks and repo.get('fork', False):
            continue
        
        stars = repo.get('stargazers_count', 0)
        total += stars
        
        if stars > 0:
            fork_status = " (fork)" if repo.get('fork', False) else ""
            print(f"  {repo['name']}: {stars} stars{fork_status}", file=sys.stderr)
    
    return total


def update_readme(readme_path: str, total_stars: int) -> bool:
    """
    Update the README.md file with the new total stars count.
    
    Args:
        readme_path: Path to README.md file
        total_stars: New total stars count
    
    Returns:
        True if file was modified, False otherwise
    """
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match: <!-- STARS_COUNT_START -->number<!-- STARS_COUNT_END -->
    pattern = r'<!-- STARS_COUNT_START -->(\d+)<!-- STARS_COUNT_END -->'
    
    match = re.search(pattern, content)
    
    if not match:
        print("Error: Could not find stars count placeholder in README.md", file=sys.stderr)
        print("Expected format: <!-- STARS_COUNT_START -->number<!-- STARS_COUNT_END -->", file=sys.stderr)
        sys.exit(1)
    
    old_count = int(match.group(1))
    
    if old_count == total_stars:
        print(f"No change needed. Total stars: {total_stars}", file=sys.stdout)
        return False
    
    new_content = re.sub(pattern, f'<!-- STARS_COUNT_START -->{total_stars}<!-- STARS_COUNT_END -->', content)
    
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Updated stars count: {old_count} → {total_stars}", file=sys.stdout)
    return True


def main():
    """Main function to update stars count."""
    # Get configuration from environment
    username = os.environ.get('GITHUB_REPOSITORY_OWNER', 'Daniele-Cangi')
    token = os.environ.get('GITHUB_TOKEN', '')
    readme_path = os.environ.get('README_PATH', 'README.md')
    ignore_forks = os.environ.get('IGNORE_FORKS', 'true').lower() == 'true'
    
    if not token:
        print("Error: GITHUB_TOKEN environment variable not set", file=sys.stderr)
        sys.exit(1)
    
    print(f"Fetching repositories for user: {username}", file=sys.stderr)
    print(f"Ignore forks: {ignore_forks}", file=sys.stderr)
    
    # Fetch all repositories
    repos = get_all_repos(username, token)
    print(f"\nFound {len(repos)} total repositories", file=sys.stderr)
    
    # Calculate total stars
    print("\nRepositories with stars:", file=sys.stderr)
    total_stars = calculate_total_stars(repos, ignore_forks)
    
    print(f"\nTotal stars: {total_stars}", file=sys.stderr)
    
    # Update README
    update_readme(readme_path, total_stars)
    
    # Exit successfully
    sys.exit(0)


if __name__ == '__main__':
    main()
