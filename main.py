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

    interns = createInterns(dataset)
    session = Session(interns)

    setEndorsers(session, interns)
    # getEndorsers(interns)
    setPairs(session, interns)
    printHeader("FINAL PAIRS")
    getPairs(interns)

main("dataset.xlsx")
