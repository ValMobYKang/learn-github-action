import argparse
import logging
import json
def create_release_notes(project:str, repo:str, changes):
    return (project, repo, changes)


if __name__ == "__main__":
    abc = '[{"id":"PR_kwDOJYPIz85RI-W2","title":"add b","url":"https://github.com/ValMobYKang/learn-github-action/pull/3"},{"id":"PR_kwDOJYPIz85RI-Oi","title":"add a","url":"https://github.com/ValMobYKang/learn-github-action/pull/2"}]'
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser("Create Release Notes from aggregated data")

    parser.add_argument("--project", help="project name", required="True")
    parser.add_argument("--repo", help="Repository name in Github", required="True")
    parser.add_argument("--changes", help="String of Changes from the last release", required=True)
    args = parser.parse_args()

    document = create_release_notes(project=args.project, repo=args.repo, changes=json.loads())