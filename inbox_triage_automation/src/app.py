import argparse
from pprint import pprint

from inbox_triage import InboxTriageCopilot


def parse_args():
    parser = argparse.ArgumentParser(description="Triage an inbox email")
    parser.add_argument("--sender", required=True)
    parser.add_argument("--subject", required=True)
    parser.add_argument("--body", required=True)
    return parser.parse_args()


def main():
    args = parse_args()
    copilot = InboxTriageCopilot()
    result = copilot.triage({"sender": args.sender, "subject": args.subject, "body": args.body})
    pprint(result)


if __name__ == "__main__":
    main()
