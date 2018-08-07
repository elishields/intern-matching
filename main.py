from session import Session
from utils import printHeader, printData
from setData import loadExcel, cleanData, checkData
from setInterns import createInterns, printInterns
from setEndorsers import setEndorsers, getEndorsers
from setPairs import *

def main(excel_file):

    printHeader("LOADING DATA")
    dataset = loadExcel(excel_file)
    checkData(dataset)
    dataset = cleanData(dataset)
    printData(dataset)

    printHeader("CREATING INTERN OBJECTS")
    interns = createInterns(dataset)
    printHeader("RELEASING THE CHAOS_INTERN")

    session = Session(interns)

    printHeader("RANKING ENDORSERS")
    setEndorsers(session, interns)
    # getEndorsers(interns)

    printHeader("SETTING PAIRS")
    setPairs(session, interns)
    printHeader("FINAL PAIRS")
    getPairs(interns)

    printHeader("END")

main("dataset.xlsx")
