import logging
import argparse
 
def retrieve_changes(repo:str, version:str, token:str):
    print(repo)
    print(version)
    print(token)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser(
        "Retrieve Pull Requests and associated Work Items between the given tag and the previous one.\nOutput is a dict where the keys are Pull Request Ids and the values are lists of associated Work Item Ids."
    )
    parser.add_argument("--repo", help="Repository Name", required=True)
    parser.add_argument(
        "--version",
        help="Current Tag from which the Pull Requests should be gathered for",
        required=True,
    )
    parser.add_argument(
        "--token",
        help="Access token for Azure DevOps with permission to read Git and Work Items",
        required=True,
    )

    data = retrieve_changes(**parser.parse_args().__dict__)
