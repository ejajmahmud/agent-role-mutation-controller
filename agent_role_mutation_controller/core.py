"""Core Role Mutation Controller implementation."""
from typing import Dict, List, Optional

class AgentProfile:
    def __init__(self, agent_id: str, current_role: str):
        self.agent_id = agent_id
        self.current_role = current_role
        self.mutation_history: List[str] = [current_role]

class RoleMutationController:
    def __init__(self, threshold: int = 5):
        self.threshold = threshold
        self.agents: Dict[str, AgentProfile] = {}
        self.queue_depths: Dict[str, int] = {}

    def register_agent(self, agent_id: str, role: str):
        self.agents[agent_id] = AgentProfile(agent_id, role)

    def set_queue_depth(self, role: str, depth: int):
        self.queue_depths[role] = depth

    def rebalance(self) -> List[Dict[str, str]]:
        mutations = []
        # Find overburdened role
        overburdened = [r for r, d in self.queue_depths.items() if d >= self.threshold]
        if not overburdened:
            return mutations

        target_role = overburdened[0]
        # Find agent with low queue depth
        for aid, profile in self.agents.items():
            curr_role = profile.current_role
            if curr_role != target_role and self.queue_depths.get(curr_role, 0) == 0:
                profile.current_role = target_role
                profile.mutation_history.append(target_role)
                mutations.append({"agent_id": aid, "from_role": curr_role, "to_role": target_role})
                break
        return mutations
