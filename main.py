from utils import *
from setData import *
from setPairs import *
from setInterns import *
from setEndorsers import *

def main(excel_file):

    printHeader("LOADING DATA")
    dataset = loadExcel(excel_file)
    checkData(dataset)
    printData(dataset)

    printHeader("CREATING INTERN OBJECTS")
    interns = createInterns(dataset)

    printHeader("RANKING ENDORSERS")
    setEndorsers(interns)
    print (interns[4].endorsers)

    # for intern in interns:
    #     setEndorsers(intern, interns)
    #     rankEndorsers(intern)
    #     pruneEndorsers(intern)
    #
    # printHeader("ENDORSERS")
    # getEndorsers(interns)
    #
    # printHeader("SETTING PAIRS")
    # rounds = getRounds(interns)
    # setPairs(rounds, interns)
    # getPairs(interns)
    #
    # printHeader("END")

main("dataset.xlsx")
