class Action:
    def __init__(self, name, positive_preconditions, negative_preconditions, add_list, delete_list):
        self.name = name
        self.positive_preconditions = positive_preconditions
        self.negative_preconditions = negative_preconditions
        self.add_list = add_list
        self.delete_list = delete_list

    def regress(self, state):
        # regressing positive literals
        g = set(state.positive_literals)
        g = g - set(self.add_list)
        g = g | set(self.positive_preconditions)

        state.positive_literals = list(g)

        # regressing negative literals
        g = set(state.negative_literals)
        g = g - set(self.delete_list)
        g = g | set(self.negative_preconditions)

        state.negative_literals = list(g)

        # doesn't return anything
        return

    def is_relevant(self, state):
        if not self.is_unified(state):
            return False

        if self.is_conflicting(state):
            return False

        return True

    def is_unified(self, state):

        for lit in self.add_list:
            if lit in state.positive_literals:
                return True

        for lit in self.delete_list:
            if lit in state.negative_literals:
                return True

        return False

    def is_conflicting(self, state):

        # conflicting if add list items are not in state positive literals
        for lit in self.add_list:
            if lit in state.negative_literals:
                return True

        # conflicting if delete list items are in state positive literals
        for lit in self.delete_list:
            if lit in state.positive_literals:
                return True

        return False

    def to_string(self):
        return f'action, name: {self.name}, positive preconditions: {self.positive_preconditions}, negative preconditions: {self.negative_preconditions}, add list: {self.add_list}, delete list: {self.delete_list}'

    def progress(self, state):
        pos_lits_set = set(state.positive_literals)
        neg_lits_set = set(state.negative_literals)
        add_list_set = set(self.add_list)
        delete_list_set = set(self.delete_list)

        # progressing positive literals
        new_pos_lits_set = (pos_lits_set | add_list_set) - delete_list_set

        state.positive_literals = list(new_pos_lits_set)

        # progressing negative literals
        new_neg_lits_set = (neg_lits_set | delete_list_set) - add_list_set 

        state.negative_literals = list(new_neg_lits_set)

    def progress_ignore_delete_list(self, state):
        pos_lits_set = set(state.positive_literals)
        neg_lits_set = set(state.negative_literals)
        add_list_set = set(self.add_list)
        delete_list_set = set(self.delete_list)

        # progressing positive literals
        new_pos_lits_set = (pos_lits_set | add_list_set)

        state.positive_literals = list(new_pos_lits_set)

        # progressing negative literals
        new_neg_lits_set = neg_lits_set - add_list_set 

        state.negative_literals = list(new_neg_lits_set)

    def is_match(self, state):
        for lit in self.positive_preconditions:
            if lit not in state.positive_literals:
                return False

        for lit in self.negative_preconditions:
            if lit in state.positive_literals:
                return False

        return True