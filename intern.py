class Intern:

    # Constructor method with instance variables
    def __init__(self, row, name):

        self.row = row
        self.name = name

        self.team = ""
        self.position = ""
        self.product = ""
        self.skills = ""

        # self.endorsers = {'eli': 7}
        self.endorsers = {}
        # self.pairs = {round: [counterparty, rank, [proposed]]}
        self.pairs = {}

    def __str__(self):
        return str(self.name)
