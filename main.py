from setData import *
from setPairs import *
from setEndorsers import *
from loggingFunctions import *

def main(excel_file):

    printHeader("LOADING DATA")
    dataset = loadExcel(excel_file)
    interns_count = checkData(dataset)

    printHeader("PRINTING DATASET")
    printData(dataset)

    printHeader("CREATING INTERNS")
    interns = createInterns(dataset)

    printHeader("RANKING ENDORSERS")
    # for intern in interns:
    #     setEndorsers(intern, interns)
    #     rankEndorsers(intern)
    #     pruneEndorsers(intern)
    #
    # printHeader("ENDORSERS")
    # getEndorsers(interns)
    #
    # printHeader("PAIRS")
    # rounds = getRounds(interns)
    # setPairs(rounds, interns)
    # getPairs(interns)
    #
    # printHeader("END")

main("../dataset.xlsx")
