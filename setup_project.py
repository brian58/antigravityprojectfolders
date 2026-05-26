import os
import sys

def setup_antigravity_project():
    # 1. Enforce correct operational environment
    home_dir = os.path.expanduser("~")
    base_path = os.path.join(home_dir, "Documents", "antigravity")
    
    print(f"[*] Base workspace context target: {base_path}")

    # 2. Prompt user for project name input
    project_name = input("Enter the new project name: ").strip()
    if not project_name:
        print("[!] Error: Project name cannot be blank.")
        sys.exit(1)

    project_root = os.path.join(base_path, project_name)

    # 3. Define standard nested subdirectories 
    subdirectories = [
        os.path.join(".agents", ".skills", "my-skill", "scripts"),
        os.path.join(".agents", ".skills", "my-skill", "examples"),
        os.path.join(".agents", ".skills", "my-skill", "resources")
    ]

    print(f"[*] Provisioning project space: '{project_name}'...")

    # 4. Generate all directory pathways safely
    for sub_dir in subdirectories:
        full_path = os.path.join(project_root, sub_dir)
        os.makedirs(full_path, exist_ok=True)

    # 5. Define documentation-compliant skill boilerplate template
    skill_template_content = """---
name: skill-name-here
description: Provide a clear semantic description. The agent stays dormant and only loads this skill when a user request matches this description block.
---

# Skill Title

Detailed step-by-step guidance and technical actions the agent must execute.

## When to use this skill
* Specific scenarios when this playbook is required.

## How to use it
* Rules, commands, or execution paradigms for the agent.

## Constraints / Anti-Patterns
* Strict boundaries of what the agent must NEVER do while running this skill.
"""

    # 6. Inject the template text into the destination path
    skill_file_path = os.path.join(project_root, ".agents", ".skills", "my-skill", "SKILL.md")
    
    try:
        with open(skill_file_path, "w", encoding="utf-8") as skill_file:
            skill_file.write(skill_template_content)
        print(f"[+] Successfully wrote compliant template to: {skill_file_path}")
    except IOError as e:
        print(f"[!] Critical Error writing file template: {e}")
        sys.exit(1)

    # 7. Final Success Output Block
    print("\n" + "="*50)
    print(f"SUCCESS: Project workspace layout setup is complete.")
    print(f"Location: {project_root}")
    print("="*50)

if __name__ == "__main__":
    setup_antigravity_project()

