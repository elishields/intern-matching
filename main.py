from helperFunctions import *
from pairingFunctions import *

def main(raw_data):

    # get data
    table = loadExcel(raw_data)
    checkData(table)

    # create intern objects
    interns = createInterns()

    # set endorsers for each intern
    for intern in interns:
        setEndorsers(intern, interns)
        rankEndorsers(intern)
        pruneEndorsers(intern)
    getEndorsers(interns)

    # set endorser-endorsee pairs for each round
    setPairs(interns)
    getPairs(interns)
    # setPairs(interns)

main("../dataset.xlsx")
