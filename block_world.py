from Action import Action
from State import State

class BlockWorld:

    def __init__(self, number_of_blocks):
        self.number_of_blocks = number_of_blocks

    def get_actions(self):
        actions = []

        # move to block pre: 
        # precond: block(a), block(b), clear(a), clear(b), on(a, c)
        # effect: !on(a, c), on(a, b), !clear(b), clear(c)

        # move to table
        # precond: block(a), clear(a), on(a, b)
        # effect: !on(a, b), on(a, table), clear(b)

        # move from block to block actions
        for i in range(1, self.number_of_blocks + 1):
            for j in range(1, self.number_of_blocks + 1):
                for k in range(1, self.number_of_blocks + 1):
                    if (i == j) or (i == k) or (j == k):
                        continue

                    move_to_block_action = Action(name="movetoblock," + str(i) + \
                        ',' + str(j) + ',' + str(k), \
                        positive_preconditions=['block,' + str(i), 'block,' + str(k), \
                        'clear,' + str(k), 'on,' + str(i) + ',' + str(j)], \
                        negative_preconditions=[], \
                        add_list=['on,' + str(i) + ',' + str(k), 'clear,' + str(j)], \
                        delete_list=['on,' + str(i) + ',' + str(j), 'clear,' + str(k)])

                    actions.append(move_to_block_action)

        # move from table to block actions
        for i in range(1, self.number_of_blocks + 1):
            for j in range(1, self.number_of_blocks + 1):
                if (i == j):
                    continue

                move_from_table_to_block_action = Action(name="movetoblock," + str(i) + \
                    ',table,' + str(j), \
                    positive_preconditions=['block,' + str(i), 'block,' + str(j), \
                    'clear,' + str(j), 'on,' + str(i) + ',table'], \
                    negative_preconditions=[], \
                    add_list=['on,' + str(i) + ',' + str(j)], \
                    delete_list=['on,' + str(i) + ',table', 'clear,' + str(j)])

                actions.append(move_from_table_to_block_action)


        # move to table actions
        for i in range(1, self.number_of_blocks + 1):
            for j in range(1, self.number_of_blocks + 1):
                if (i == j):
                    continue

                move_to_table_action = Action(name='movetotable,' + str(i) + ',' + str(j), \
                    positive_preconditions=['block,' + str(i), 'clear,' + str(i), \
                        'on,' + str(i) + ',' + str(j)], \
                    negative_preconditions=[], \
                    add_list=['on,' + str(i) + ',table', 'clear,' + str(j)], \
                    delete_list=['on,' + str(i) + ',' + str(j)])

                actions.append(move_to_table_action)


        return actions

    def get_initial_state(self):
        initial_state = State(None, None, \
            positive_literals=['block,1', 'block,2', 'block,3', \
                'on,2,table', 'on,1,table', 'on,3,1', \
                'clear,2', 'clear,3'], \
            negative_literals=[])

        return initial_state

    def get_goal_state(self):
        goal_state = State(None, None, \
            positive_literals=['on,1,2', 'on,2,3', 'on,3,table'], \
            negative_literals=[])

        return goal_state


# problem = BlockWorld(3)
# action_lst = problem.get_actions()

# for action in action_lst:
#     print(action.name)