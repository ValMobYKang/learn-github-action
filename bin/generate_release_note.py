import argparse
import logging
import json


def create_release_notes(project:str, repo:str, current_tag:str, previous_tag:str, previous_date:str, changes):
    header_section = ""
    changes_section = ""
    sonarqube_section = ""
    black_duck_section = ""
    return (header_section, changes_section, sonarqube_section, black_duck_section)


if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser("Create Release Notes from aggregated data")

    parser.add_argument("--project", help="project name", required="True")
    parser.add_argument("--repo", help="Repository name in Github", required="True")
    parser.add_argument("--current_tag", help="Current tag", required=True)
    parser.add_argument("--previous_tag", help="Previous tag", required=True)
    parser.add_argument("--previous_date", help="Previous date", required=True) 
    parser.add_argument("--changes", help="String of Changes from the last release", required=True)
    args = parser.parse_args()

    # DEBUG
    for arg in vars(args):
        print(arg,": ",getattr(args,arg)) 
    
    document = create_release_notes(project=args.project, 
                                    repo=args.repo, 
                                    current_tag=args.current_tag,
                                    previous_tag=args.previous_tag,
                                    previous_date=args.previous_date,
                                    changes=json.loads(args.changes))