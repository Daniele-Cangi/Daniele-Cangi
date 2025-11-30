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


def ensure_github_stats_section(content: str, username: str) -> str:
    """
    Ensure the GitHub stats and Top languages sections exist in README.
    
    Args:
        content: Current README content
        username: GitHub username for the stats URL
    
    Returns:
        Content with stats sections ensured
    """
    modified = False
    
    # Check for GitHub stats image
    stats_pattern = r'github-readme-stats\.vercel\.app/api\?username='
    if not re.search(stats_pattern, content):
        print("GitHub stats section missing, will be restored after ## Status & metrics", file=sys.stderr)
        # Find ## Status & metrics section and add stats after it
        status_pattern = r'(## Status & metrics\s*\n)'
        stats_section = '''## Status & metrics
<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username={username}&show_icons=true&theme=transparent&hide_border=true&cache_seconds=1800" alt="GitHub stats" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username={username}&layout=compact&theme=transparent&hide_border=true&cache_seconds=1800" alt="Top languages" />
</p>

'''.format(username=username)
        if re.search(status_pattern, content):
            content = re.sub(status_pattern, stats_section, content)
            modified = True
            print("GitHub stats section restored", file=sys.stderr)
    
    # Check for Top languages image
    top_langs_pattern = r'github-readme-stats\.vercel\.app/api/top-langs/'
    if not re.search(top_langs_pattern, content):
        print("Top languages section missing", file=sys.stderr)
        # If stats exist but top langs don't, add it after stats
        stats_img_pattern = r'(<img src="https://github-readme-stats\.vercel\.app/api\?[^"]*" alt="GitHub stats" />)'
        top_langs_img = '\n  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username={username}&layout=compact&theme=transparent&hide_border=true&cache_seconds=1800" alt="Top languages" />'.format(username=username)
        if re.search(stats_img_pattern, content) and not re.search(top_langs_pattern, content):
            content = re.sub(stats_img_pattern, r'\1' + top_langs_img, content)
            modified = True
            print("Top languages section restored", file=sys.stderr)
    
    return content


def update_readme(readme_path: str, total_stars: int, username: str = 'Daniele-Cangi') -> bool:
    """
    Update the README.md file with the new total stars count.
    Also ensures GitHub stats sections exist.
    
    Args:
        readme_path: Path to README.md file
        total_stars: New total stars count
        username: GitHub username for stats URLs
    
    Returns:
        True if file was modified, False otherwise
    """
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Ensure GitHub stats sections exist
    content = ensure_github_stats_section(content, username)
    
    # Pattern to match: <!-- STARS_COUNT_START -->number<!-- STARS_COUNT_END -->
    pattern = r'<!-- STARS_COUNT_START -->(\d+)<!-- STARS_COUNT_END -->'
    
    match = re.search(pattern, content)
    
    if not match:
        print("Warning: Could not find stars count placeholder in README.md", file=sys.stderr)
        print("Adding placeholder after Status & metrics section", file=sys.stderr)
        # Add the stars placeholder if missing
        stars_placeholder = '''
<p align="center">
  <strong>Total stars received:</strong> ⭐ <!-- STARS_COUNT_START -->{stars}<!-- STARS_COUNT_END -->
</p>
'''.format(stars=total_stars)
        # Try to add after the stats images
        stats_section_end = r'(</p>\s*)(## Collaboration|$)'
        if re.search(stats_section_end, content):
            content = re.sub(stats_section_end, r'\1' + stars_placeholder + r'\n\2', content, count=1)
        else:
            # Just append to end
            content += stars_placeholder
        
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added stars count placeholder with value: {total_stars}", file=sys.stdout)
        return True
    
    old_count = int(match.group(1))
    
    # Update the stars count
    content = re.sub(pattern, f'<!-- STARS_COUNT_START -->{total_stars}<!-- STARS_COUNT_END -->', content)
    
    # Check if anything changed
    if content == original_content:
        print(f"No change needed. Total stars: {total_stars}", file=sys.stdout)
        return False
    
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    if old_count != total_stars:
        print(f"Updated stars count: {old_count} → {total_stars}", file=sys.stdout)
    else:
        print("README sections restored/updated", file=sys.stdout)
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
    update_readme(readme_path, total_stars, username)
    
    # Exit successfully
    sys.exit(0)


if __name__ == '__main__':
    main()
