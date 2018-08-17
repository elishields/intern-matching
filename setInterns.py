from intern import Intern


# Create intern objects
def create_interns(dataset):
    interns = []
    for row in dataset.itertuples():
        newIntern = Intern(row.Index, row.NAME)
        interns.append(newIntern)
        send_attributes(dataset, newIntern, row.Index)
    # if len(interns) % 2 != 0:
    interns.append(release_chaos_intern(interns))
    return interns


# Set intern instance variables
def send_attributes(dataset, intern, location):
    for row in dataset.itertuples():
        if row.Index == location:
            intern.team = row.TEAM
            intern.position = row.POSITION
            intern.product = row.PRODUCT
            intern.skills = row.SKILLS


def release_chaos_intern(interns):
    row = len(interns)
    name = "chaos"
    chaos = Intern(row, name)
    for attribute in ["team", "position", "product", "skills"]:
        chaos.attribute = "generic"
    return chaos


def print_interns(interns):
    for intern in interns:
        print (intern.row, intern.name, intern.team)


def get_chaos_intern(interns):
    for intern in interns:
        if intern.name == "chaos":
            return intern
