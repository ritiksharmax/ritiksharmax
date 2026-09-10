import os
import urllib.request
import json
import re

USERNAME = "ritiksharmax"
README_PATH = "README.md"
START_MARKER = "<!-- AUTO_PROJECTS:START -->"
END_MARKER = "<!-- AUTO_PROJECTS:END -->"

def fetch_repositories():
    url = f"https://api.github.com/users/{USERNAME}/repos?sort=pushed&per_page=30"
    token = os.environ.get("GITHUB_TOKEN")
    headers = {"User-Agent": "Mozilla/5.0"}
    if token:
        headers["Authorization"] = f"token {token}"
        
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            repos = json.loads(resp.read().decode())
    except Exception as e:
        print(f"Error fetching repos: {e}")
        return []
        
    # Filter out profile repo and forks if needed
    filtered_repos = [
        r for r in repos 
        if r.get("name", "").lower() != USERNAME.lower() and not r.get("fork", False)
    ]
    return filtered_repos

def build_markdown(repos):
    if not repos:
        return "\n*No public repositories found.*\n"
        
    lines = ["\n"]
    for r in repos:
        name = r.get("name", "")
        url = r.get("html_url", "")
        desc = r.get("description") or "Machine learning & systems engineering project."
        lang = r.get("language")
        stars = r.get("stargazers_count", 0)
        
        meta = []
        if lang:
            meta.append(f"`{lang}`")
        if stars > 0:
            meta.append(f"⭐ {stars}")
            
        meta_str = f" {' '.join(meta)}" if meta else ""
        lines.append(f"- **[{name}]({url})**{meta_str} — {desc}")
        
    lines.append("\n")
    return "\n".join(lines)

def update_readme():
    repos = fetch_repositories()
    projects_md = build_markdown(repos)
    
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()
        
    pattern = re.compile(f"{re.escape(START_MARKER)}[\\s\\S]*?{re.escape(END_MARKER)}")
    replacement = f"{START_MARKER}\n{projects_md}\n{END_MARKER}"
    
    if pattern.search(content):
        updated_content = pattern.sub(replacement, content)
        with open(README_PATH, "w", encoding="utf-8") as f:
            f.write(updated_content)
        print("Successfully updated README.md with synced repositories.")
    else:
        print("Markers not found in README.md.")

if __name__ == "__main__":
    update_readme()
