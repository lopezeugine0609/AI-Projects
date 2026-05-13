import argparse
from pprint import pprint

from intake_agent import ClientIntakeAgent


def parse_args():
    parser = argparse.ArgumentParser(description="Analyze a VA client inquiry")
    parser.add_argument("--name", required=True)
    parser.add_argument("--company", required=True)
    parser.add_argument("--message", required=True)
    parser.add_argument("--weekly-hours", type=int, default=10)
    parser.add_argument("--monthly-budget", type=int, default=800)
    return parser.parse_args()


def main():
    args = parse_args()
    agent = ClientIntakeAgent()
    brief = agent.analyze(
        {
            "name": args.name,
            "company": args.company,
            "message": args.message,
            "weekly_hours": args.weekly_hours,
            "monthly_budget": args.monthly_budget,
        }
    )
    pprint(brief.crm_payload)
    print("\nResponse draft:\n")
    print(brief.response_draft)


if __name__ == "__main__":
    main()
