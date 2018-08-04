from utils import *
from setData import *
from setPairs import *
from setInterns import *
from setEndorsers import *

def main(excel_file):

    printHeader("LOADING DATA")
    dataset = loadExcel(excel_file)
    checkData(dataset)

    printHeader("PRINTING DATASET")
    printData(dataset)

    printHeader("CREATING INTERNS")
    interns = createInterns(dataset)
    print (interns)

    printHeader("RANKING ENDORSERS")
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
