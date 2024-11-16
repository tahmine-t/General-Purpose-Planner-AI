from Action import Action
from State import State

class TireProblem:

    def get_actions(self):
        actions = []

        tires = ["spare", "flat"]
        locations = ["axle", "trunk"]

        for tire in tires:
            put_action = Action(name="put" + tire + "axle", positive_preconditions=["at" + tire + "ground"], \
                                negative_preconditions=["atflataxle", "atspareaxle"], add_list=["at" + tire + "axle"], \
                                delete_list=["at" + tire + "ground"])
            actions.append(put_action)
            for location in locations:
                remove_action = Action(name="rem" + tire + location, positive_preconditions=["at" + tire + location], \
                                    negative_preconditions=[], add_list=["at" + tire + "ground"], delete_list=["at" + tire + location])
                actions.append(remove_action)

        return actions

    def get_initial_state(self):
        initial_state = State(None, None, positive_literals=["atflataxle", "atsparetrunk"], negative_literals=[])

        return initial_state

    def get_goal_state(self):
        goal_state = State(None, None, positive_literals=["atspareaxle"], negative_literals=[])

        return goal_state