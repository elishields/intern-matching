from helperFunctions import *
from pairingFunctions import *

def main(raw_data):

    table = loadExcel(raw_data)
    checkData(table)
    interns = createInterns()
    for intern in interns:
        setEndorsers(intern, interns)
        rankEndorsers(intern)
        pruneEndorsers(intern)
    # setPairs(interns)
    getPairs(interns)

main("../dataset.xlsx")
