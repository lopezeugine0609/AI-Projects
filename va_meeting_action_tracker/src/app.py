import argparse
from pprint import pprint

from meeting_tracker import MeetingActionTracker


def parse_args():
    parser = argparse.ArgumentParser(description="Convert meeting notes into action items")
    parser.add_argument("--transcript", required=True)
    parser.add_argument("--default-owner", default="VA")
    return parser.parse_args()


def main():
    args = parse_args()
    tracker = MeetingActionTracker()
    summary = tracker.summarize(args.transcript, default_owner=args.default_owner)
    pprint(summary.task_board_payload)
    print("\nFollow-up email:\n")
    print(summary.follow_up_email)


if __name__ == "__main__":
    main()
