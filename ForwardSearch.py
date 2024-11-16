from State import State
from queue import PriorityQueue
import sys


def forward_search(goal_state, initial_state, actions):
    fringe = [initial_state]
    in_fringe = [initial_state.hash()]
    explored = []

    while fringe:
        current_state = fringe.pop(0)
        explored.append(current_state.hash())
        successors = get_successors(current_state, actions)

        for successor in successors:
            if goal_test(successor, goal_state):
                print_solution(successor)
                return
            else:
                if (successor.hash() not in explored) and \
                    (successor.hash() not in in_fringe):
                    fringe.append(successor)
                    in_fringe.append(successor.hash())

def forward_search_ignore_precond(goal_state, initial_state, actions):
    fringe = PriorityQueue()
    explored = []

    fringe.put((0, initial_state))

    while fringe:
        current_state = fringe.get()[1]
        explored.append(current_state.hash())
        successors = get_successors(current_state, actions)

        for successor in successors:
            if goal_test(successor, goal_state):
                print_solution(successor)
                return
            else:
                if successor.hash() not in explored:
                    h = ignore_precondition_heuristic(successor, goal_state, actions)
                    fringe.put((h, successor))

def forward_search_ignore_delete_list(goal_state, initial_state, actions):
    fringe = PriorityQueue()
    explored = []

    fringe.put((0, initial_state))

    while fringe:
        current_state = fringe.get()[1]
        explored.append(current_state.hash())
        successors = get_successors(current_state, actions)

        for successor in successors:
            if goal_test(successor, goal_state):
                print_solution(successor)
                return
            else:
                if successor.hash() not in explored:
                    h = ignore_delete_list_heuristic(successor, goal_state, actions)
                    fringe.put((h, successor))

def ignore_precondition_heuristic(current_state, goal_state, actions):
    h = 0
    fringe = [current_state]
    explored = []

    while fringe:
        current_state = fringe.pop(0)
        explored.append(current_state.hash())
        successors = get_successors_ignore_preconditions(current_state, actions)

        for successor in successors:
            if goal_test(successor, goal_state):
                h = get_tree_depth(successor)
                return h
            else:
                if successor.hash() not in explored:
                    fringe.append(successor)

    h = sys.maxsize
    return h

def ignore_delete_list_heuristic(current_state, goal_state, actions):
    h = 0
    fringe = [current_state]
    explored = []

    while fringe:
        current_state = fringe.pop(0)
        explored.append(current_state.hash())
        successors = get_successors_ignore_delete_list(current_state, actions)

        for successor in successors:
            if goal_test(successor, goal_state):
                h = get_tree_depth(successor)
                return h
            else:
                if successor.hash() not in explored:
                    fringe.append(successor)

    h = sys.maxsize
    return h

def get_tree_depth(node):
    d = 0

    while True:
        if bool(node.action) == False or bool(node.parent) == False:
            break
        d = d + 1
        node = node.parent

    return d

def get_successors(state, actions):
    result = []
    for action in actions:
        if(action.is_match(state)):
            successor = State(state, action, state.positive_literals, state.negative_literals)
            action.progress(successor)
            result.append(successor)

    return result

def get_successors_ignore_preconditions(state, actions):
    result = []
    for action in actions:
        successor = State(state, action, state.positive_literals, state.negative_literals)
        action.progress(successor)
        result.append(successor)

    return result

def get_successors_ignore_delete_list(state, actions):
    result = []
    for action in actions:
        if(action.is_match(state)):
            successor = State(state, action, state.positive_literals, state.negative_literals)
            action.progress_ignore_delete_list(successor)
            result.append(successor)

    return result

def goal_test(state, goal_state):
    for pos_lit in goal_state.positive_literals:
        if pos_lit not in state.positive_literals:
            return False

    for neg_lit in state.negative_literals:
        if neg_lit in goal_state.positive_literals:
            return False

    return True


def print_solution(state):
    while True:
        if bool(state.action) == False or bool(state.parent) == False:
            break
        print(state.action.to_string())
        state = state.parent