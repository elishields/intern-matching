from helperFunctions import *

def main(raw_data):

    table = loadExcel(raw_data)
    checkData(table)
    interns = createInterns()
    setPairs(interns)
    getPairs(interns)

main("../dataset.xlsx")
