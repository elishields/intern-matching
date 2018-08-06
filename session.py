class Session:

    # Constructor method with instance variables
    def __init__(self, interns):

        self.num_interns = len(interns)
        self.num_rounds = len(interns) - 1
        self.is_chaotic = len(interns) % 2 != 0

    def __str__(self):
        return str("Some men just want to watch the world burn.")
