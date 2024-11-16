from State import State

def backward_search(goal_state, initial_state, actions):
    fringe = [goal_state]
    explored = []

    while fringe:
        current_state = fringe.pop(0)
        explored.append(current_state.hash())
        successors = get_successors(current_state, actions)

        for successor in successors:
            if goal_test(successor, initial_state):
                print_solution(successor)
                return
            else:
                if successor.hash() not in explored:
                    fringe.append(successor)

    # planning unsuccessful
    return

def get_successors(state, actions):
    result = []
    for action in actions:
        if action.is_relevant(state):
            predeccessor = State(state, action, state.positive_literals, state.negative_literals)
            action.regress(predeccessor)
            result.append(predeccessor)

    return result

def goal_test(state, initial_state):
    for positive_literal in state.positive_literals:
        if positive_literal not in initial_state.positive_literals:
            return False

    for negative_literal in state.negative_literals:
        if negative_literal in initial_state.positive_literals:
            return False

    return True

def print_solution(state):
    while True:
        if bool(state.action) == False or bool(state.parent) == False:
            break
        print(state.action.to_string())
        state = state.parent