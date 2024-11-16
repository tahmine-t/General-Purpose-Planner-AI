from Action import Action
from State import State

class DepotsProblem:
    def __init__(self):
        self.crates = ['crate1', 'crate2']
        self.hoists = ['hoist1', 'hoist2']
        self.places = ['place1', 'place2']
        self.pallets = ['pallet1', 'pallet2']
        self.surfaces = self.pallets + self.crates


    def get_actions(self):
        actions = []

        # drive action
        for i in range(len(self.places)):
            for j in range(len(self.places)):
                if (i == j):
                    continue

                drive_action = Action(name='drive,' + self.places[i] + ',' + self.places[j], 
                    positive_preconditions=['at,truck,' + self.places[i]], 
                    negative_preconditions=[], \
                    add_list=['at,truck,' + self.places[j]], \
                    delete_list=['at,truck,' + self.places[i]])

                actions.append(drive_action)


        # lift actions
        for hoist in self.hoists:
            for crate in self.crates:
                for surface in self.surfaces:
                    for place in self.places:

                        lift_action = Action(name=f"lift,{hoist},{crate},{surface},{place}", \
                            positive_preconditions=[f'at,{hoist},{place}', f'available,{hoist}', f'at,{crate},{place}', \
                            f'on,{crate},{surface}', f'clear,{crate}', f'at,{surface},{place}'], \
                            negative_preconditions=[], \
                            add_list=[f'clear,{surface}', f'lifting,{hoist},{crate}'], \
                            delete_list=[f'on,{crate},{surface}', f'available,{hoist}'])

                        actions.append(lift_action)

        # drop actions
        for hoist in self.hoists:
            for crate in self.crates:
                for surface in self.surfaces:
                    for place in self.places:

                        drop_action = Action(name=f'drop,{hoist},{crate},{surface},{place}', \
                            positive_preconditions=[f'at,{hoist},{place}', f'at,{crate},{place}',\
                                f'lifting,{hoist},{crate}', f'clear,{surface}', f'at,{surface},{place}'], \
                            negative_preconditions=[], \
                            add_list=[f'on,{crate},{surface}', f'clear,{crate}', f'available,{hoist}'], \
                            delete_list=[f'lifting,{hoist},{crate}', f'clear,{surface}'])

                        actions.append(drop_action)


        # load actions
        for hoist in self.hoists:
            for crate in self.crates:
                for place in self.places:

                    load_action = Action(name=f'load,{hoist},{crate},truck,{place}', \
                        positive_preconditions=[f'at,{hoist},{place}', f'at,truck,{place}', f'at,{crate},{place}', f'lifting,{hoist},{crate}'], \
                        negative_preconditions=[], \
                        add_list=[f'at,{crate},truck', f'available,{hoist}'], \
                        delete_list=[f'lifting,{hoist},{crate}', f'at,{crate},{place}'])

                    actions.append(load_action)

        # unload actions
        for hoist in self.hoists:
            for crate in self.crates:
                for place in self.places:

                    unload_action = Action(name=f'unload,{hoist},{crate},truck,{place}', \
                        positive_preconditions=[f'at,{hoist},{place}', f'at,truck,{place}', f'at,{crate},truck', f'available,{hoist}'], \
                        negative_preconditions=[], \
                        add_list=[f'at,{crate},{place}', f'lifting,{hoist},{crate}'], \
                        delete_list=[f'at,{crate},truck', f'available,{hoist}'])

                    actions.append(unload_action)
        
        return actions

    def get_initial_state(self):
        positive_literals = []

        positive_literals.append('at,truck,place1')

        for i in range(len(self.places)):
            lit1 = f'clear,{self.pallets[i]}'
            lit2 = f'at,{self.pallets[i]},{self.places[i]}'
            lit3 = f'available,{self.hoists[i]}'
            lit4 = f'at,{self.hoists[i]},{self.places[i]}'

            positive_literals.append(lit1)
            positive_literals.append(lit2)
            positive_literals.append(lit3)
            positive_literals.append(lit4)

        crates_lits = ['at,crate1,place1', 'at,crate2,place1', \
            'on,crate1,pallet1', 'on,crate2,pallet1', \
            'clear,crate1', 'clear,crate2']
        
        positive_literals = positive_literals + crates_lits

        initial_state = State(None, None,
            positive_literals=positive_literals ,
            negative_literals=[])

        return initial_state

    def get_goal_state(self):
        positive_literals = [
            'on,crate2,pallet2',
            'on,crate1,crate2'
        ]

        goal_state = State(None, None,
            positive_literals=positive_literals,
            negative_literals=[])
        
        return goal_state


# problem = DepotsProblem()
# actions = problem.get_actions()

# for i in range(int(len(actions) / 2)):
#     print(actions[i].name)