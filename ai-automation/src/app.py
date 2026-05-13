import argparse
from automation import AutomationAgent


def parse_args():
    parser = argparse.ArgumentParser(description="Run AI automation planning")
    parser.add_argument("--task", required=True, help="Task intent to automate")
    return parser.parse_args()


def main():
    args = parse_args()
    agent = AutomationAgent()
    plan = agent.plan(args.task)

    print("Automation plan for:", args.task)
    for index, item in enumerate(plan, start=1):
        print(f"{index}. {item['task']}: {item['detail']}")


if __name__ == "__main__":
    main()
