from State import State
import BackwardSearch
import ForwardSearch
from tireproblem import TireProblem
from block_world import BlockWorld
from monkey_and_bananas import MonkeyProblem
from depots import DepotsProblem
import time

def main():
    print("Getting the set of all actions...")
    problem = DepotsProblem()

    actions = problem.get_actions()

    print("Planning...")
    initial_state = problem.get_initial_state()
    goal_state = problem.get_goal_state()

    # backward_search(goal_state, initial_state, actions)
    start_time = time.time()
    ForwardSearch.forward_search_ignore_delete_list(goal_state, initial_state, actions)
    finish_time = time.time()

    print(f"ELAPSED TIME: ({round(finish_time - start_time, 2)}) milliseconds")
    
if __name__ == "__main__":
    main()
