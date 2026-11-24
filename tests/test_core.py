"""Tests for RoleMutationController."""
import unittest
from agent_role_mutation_controller.core import RoleMutationController

class TestRoleMutationController(unittest.TestCase):
    def test_mutation_trigger(self):
        ctrl = RoleMutationController(threshold=4)
        ctrl.register_agent("a1", "idle_worker")
        ctrl.set_queue_depth("idle_worker", 0)
        ctrl.set_queue_depth("hot_queue", 10)

        muts = ctrl.rebalance()
        self.assertEqual(len(muts), 1)
        self.assertEqual(muts[0]["to_role"], "hot_queue")
        self.assertEqual(ctrl.agents["a1"].current_role, "hot_queue")
