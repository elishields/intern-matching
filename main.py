from utils import printHeader, printData, getRounds
from setData import loadExcel, checkData
from setInterns import createInterns
from setEndorsers import setEndorsers, getEndorsers
from setPairs import *

def main(excel_file):

    printHeader("LOADING DATA")
    dataset = loadExcel(excel_file)
    checkData(dataset)
    printData(dataset)

    printHeader("CREATING INTERN OBJECTS")
    interns = createInterns(dataset)

    printHeader("RANKING ENDORSERS")
    setEndorsers(interns)
    getEndorsers(interns)

    printHeader("SETTING PAIRS")
    rounds = getRounds(interns)
    setPairs(rounds, interns)
    # getPairs(interns)

    printHeader("END")

main("dataset.xlsx")
