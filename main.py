from setData import *
from setPairs import *
from setEndorsers import *

def main(raw_data):

    dataset = loadExcel(raw_data)
    checkData(dataset)
    interns = createInterns(dataset)

    for intern in interns:
        setEndorsers(intern, interns)
        rankEndorsers(intern)
        pruneEndorsers(intern)
    getEndorsers(interns)

    # set endorser-endorsee pairs for each round
    # setPairs(interns)
    # getPairs(interns)

main("../dataset.xlsx")
