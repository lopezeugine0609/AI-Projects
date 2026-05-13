import argparse
from .fieldroutes import fieldroutes_lead_flow
from .callgear import callgear_lead_flow
from .callrail import callrail_lead_flow
from .meta_project import meta_lead_flow


def parse_args():
    parser = argparse.ArgumentParser(description="Run GHL/n8n lead automation flows")
    parser.add_argument("--flow", required=True, choices=["fieldroutes", "callgear", "callrail", "meta"], help="Choose the lead automation flow to run")
    return parser.parse_args()


def run_flow(flow_name: str):
    if flow_name == "fieldroutes":
        return fieldroutes_lead_flow()
    if flow_name == "callgear":
        return callgear_lead_flow()
    if flow_name == "callrail":
        return callrail_lead_flow()
    if flow_name == "meta":
        return meta_lead_flow()

    raise ValueError(f"Unknown flow: {flow_name}")


def main():
    args = parse_args()
    flow = run_flow(args.flow)

    print(f"Running {args.flow} automation flow:\n")
    for index, step in enumerate(flow, start=1):
        print(f"{index}. {step['step']}: {step['detail']}")


if __name__ == "__main__":
    main()
