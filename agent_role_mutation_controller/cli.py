"""CLI for Role Mutation Controller."""
import argparse
from .core import RoleMutationController

def main():
    parser = argparse.ArgumentParser(description="Agent Role Mutation Controller CLI")
    parser.add_argument("--demo", action="store_true", help="Run role rebalance demo")
    args = parser.parse_args()

    ctrl = RoleMutationController(threshold=3)
    ctrl.register_agent("agent-1", "researcher")
    ctrl.set_queue_depth("researcher", 0)
    ctrl.set_queue_depth("tester", 8)

    muts = ctrl.rebalance()
    print("Executed Mutations:", muts)

if __name__ == "__main__":
    main()
