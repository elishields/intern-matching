# intern.py
import helperFunctions

class Intern:

    def __init__(self, row, name):

        self.row = row

        self.name = name
        self.team = ""
        self.position = ""
        self.product = ""
        self.skills = ""

        self.endorsers = {}

        self.team, self.position, self.product, self.skills = helperFunctions.getAttributes(self.row)

    def __str__(self):
        att_list = [self.name,self.team,self.position,self.product,self.skills]
        return str(att_list)
    def setInterns(newInterns):
        interns = newInterns
    def getInterns():
        return interns

# print matching words
