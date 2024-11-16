from Action import Action
from State import State

class MonkeyProblem:
    def get_actions(self):
        actions = []

        # go actions
        spots = ['A', 'B', 'C']
        objects = ['box', 'bananas', 'monkey']
        heights = ['low', 'high']

        for i in range(len(spots)):
            for j in range(len(spots)):

                go_action = Action(name='go,' + spots[i] + ',' + spots[j], \
                    positive_preconditions=['at,monkey,' + spots[i], 'height,monkey,low', \
                        'notequal,' + spots[i] + ',' + spots[j]], \
                    negative_preconditions=[], \
                    add_list=['at,monkey,' + spots[j]], \
                    delete_list=['at,monkey,' + spots[i]])

                actions.append(go_action)

        # push actions
        for object in objects:
            for i in range(len(spots)):
                for j in range(len(spots)):

                    push_action = Action(name='push,' + object + ',' + spots[i] + \
                        ',' + spots[j],
                        positive_preconditions=['at,monkey,' + spots[i], 'height,monkey,low', \
                            'at,' + object + ',' + spots[i], 'pushable,' + object, 'height,' + object + ',low', \
                            'notequal,' + spots[i] + ',' + spots[j]], \
                        negative_preconditions=[], \
                        add_list=['at,' + object + ',' + spots[j], 'at,monkey,' + spots[j]], \
                        delete_list=['at,' + object + ',' + spots[i], 'at,monkey,' + spots[i]])

                    actions.append(push_action)

        
        # climb actions
        for i in range(len(spots)):
            for object in objects:
                if object == 'monkey':
                    continue

                climb_action = Action(name='climbup,' + spots[i] + ',' + object, \
                    positive_preconditions=['at,monkey,' + spots[i], 'height,monkey,low', 'at,' + object + ',' + spots[i], \
                        'climbable,' + object, 'height,' + object + ',low'], \
                    negative_preconditions=[], \
                    add_list=['on,monkey,' + object, 'height,monkey,high'], \
                    delete_list=['height,monkey,low'])

                actions.append(climb_action)

        # grasp action
        for i in range(len(spots)):
            for object in objects:
                for height in heights:

                    grasp_action = Action(name='grasp,' + spots[i] + ',' + object + ',' + height, \
                        positive_preconditions=['at,monkey,' + spots[i], 'height,monkey,' + height, 'at,' + object + ',' + spots[i], \
                            'graspable,' + object, 'height,' + object + ',' + height], \
                        negative_preconditions=[], \
                        add_list=['have,monkey,' + object], \
                        delete_list=['at,' + object + ',' + spots[i], 'height,' + object + ',' + spots[i]])

                    actions.append(grasp_action)

        return actions


    def get_initial_state(self):
        initial_state = State(None, None, \
            positive_literals=['at,monkey,A', 'at,bananas,B', 'at,box,C', \
                'height,monkey,low', 'height,box,low', 'height,bananas,high', \
                'pushable,box', 'climbable,box', 'graspable,bananas', 'notequal,A,B', \
                'notequal,A,C', 'notequal,B,A', 'notequal,B,C', 'notequal,C,A', 'notequal,C,B'], \
            negative_literals=[])
        
        return initial_state

    def get_goal_state(self):
        goal_state = State(None, None, \
        positive_literals=['have,monkey,bananas'], \
        negative_literals=[])

        return goal_state

# problem = MonkeyProblem()
# acts = problem.get_actions()

# for act in acts:
#     print(act.name)