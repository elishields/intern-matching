class Session:

    # Constructor method with instance variables
    def __init__(self, interns):

        self.num_interns = len(interns)
        self.num_rounds = 12

    def __str__(self):
        return str("Session.")
