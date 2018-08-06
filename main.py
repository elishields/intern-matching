from session import Session
from utils import printHeader, printData, getRounds
from setData import loadExcel, cleanData, checkData
from setInterns import createInterns, releaseChaosIntern
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

    session = Session(interns)
    print (session)

    if session.is_chaotic:
        printHeader("RELEASING THE CHAOS_INTERN")
        interns = releaseChaosIntern(interns)

    printHeader("RANKING ENDORSERS")
    setEndorsers(session, interns)
    getEndorsers(interns)

    printHeader("SETTING PAIRS")
    setPairs(session, interns)
    printHeader("FINAL PAIRS")
    getPairs(interns)

    # printHeader("END")

main("dataset.xlsx")
