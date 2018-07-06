from setData import *
from setPairs import *
from setEndorsers import *

def main(raw_data):

    print ("\nSTART\n")

    dataset = loadExcel(raw_data)
    checkData(dataset)

    interns = createInterns(dataset)
    for intern in interns:
        setEndorsers(intern, interns)
        rankEndorsers(intern)
        pruneEndorsers(intern)
    endorsersHeader()
    getEndorsers(interns)


    pairsHeader()
    rounds = getRounds(interns)
    for round in range(rounds):
        setPairs(round, interns)
    getPairs(interns)

    print ("\nEND\n")

main("../dataset.xlsx")
