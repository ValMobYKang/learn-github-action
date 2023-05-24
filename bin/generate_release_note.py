import argparse
import logging
import json
from datetime import datetime

def create_header_section(project, repo, current_tag, previous_tag, previous_date):
    now = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
    author = "ODM-Team"
    link = f"https://github.com/vwdfive/{repo}/releases/tag/{current_tag}"
    return [
        f"# {project} - {current_tag}",
        "",
        "## Release Note",
        "",
        "| Release |         | ",
        "| ------- | ------- | ",
        f"| Project    | {project} |",
        f"| Repository | [{repo}]({link}) |",
        f"| Version | {current_tag} |",
        f"| Date   |  {now} |",
        f"| Author | {author} |",
        f"| Predecessor | {previous_tag} ({previous_date}) |",
    ]


def create_changes_section(changes):
    section = [
        "",
        "## Changes",
        ""
    ]
    section.extend([
            "| Number | Pull Request |",
            "| ------ |------------- |",
    ])
    section.extend([
        f"| {pr['number']} | [{pr['title']}]({pr['url']}) |" for pr in changes[::-1]
    ])
    return section


def create_blackDuck_section():
    section = []
    section.extend([
        "",
        "## BlackDuck Report",
        ""
    ])
    section.extend([
        "contents"
    ])
    return section


def create_sonarqube_section():
    section = []
    section.extend([
        "",
        "## SonarQube Report",
        ""
    ])
    section.extend([
        "contents"
    ])
    return section


def create_release_notes(project:str, repo:str, current_tag:str, previous_tag:str, previous_date:str, changes):
    content = ""
    header_section = create_header_section(project, repo, current_tag, previous_tag, previous_date)
    changes_section = create_changes_section(changes)
    sonarqube_section = create_sonarqube_section()
    black_duck_section = create_blackDuck_section()
    for line in (header_section+ changes_section+ sonarqube_section + black_duck_section):
        content += line + '\n'
    return content


if __name__ == "__main__":

    test_changes = '[{"number":3,"title":"add b","url":"https://github.com/ValMobYKang/learn-github-action/pull/3"},{"number":2,"title":"add a","url":"https://github.com/ValMobYKang/learn-github-action/pull/2"}]'

    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser("Create Release Notes from aggregated data")

    parser.add_argument("--project", help="project name", required=True)
    parser.add_argument("--repo", help="Repository name in Github", required=True)
    parser.add_argument("--current_tag", help="Current tag", required=True)
    parser.add_argument("--previous_tag", help="Previous tag", required=True)
    parser.add_argument("--previous_date", help="Previous date", required=True) 
    parser.add_argument("--changes", help="String of Changes from the last release", required=True)
    args = parser.parse_args()
    
    document = create_release_notes(project=args.project, 
                                    repo=args.repo, 
                                    current_tag=args.current_tag,
                                    previous_tag=args.previous_tag,
                                    previous_date=args.previous_date,
                                    changes=json.loads(test_changes))

    print(document)
    # with open(f"./docs/release_note/{args.current_tag}.md", "w", encoding="utf-8") as out:
    #     out.writelines()