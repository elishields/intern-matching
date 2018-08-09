from session import Session
from utils import print_header, print_data
from setData import load_excel, clean_data, check_data
from setInterns import create_interns, print_interns
from setEndorsers import set_endorsers, get_endorsers
from setPairs import *


def main(excel_file):

    print_header("LOADING DATA")

    dataset = load_excel(excel_file)
    check_data(dataset)

    dataset = clean_data(dataset)
    print_data(dataset)

    interns = create_interns(dataset)
    session = Session(interns)

    set_endorsers(session, interns)
    # get_endorsers(interns)

    set_pairs(session, interns)
    print_header("FINAL PAIRS")
    get_pairs(interns)


main("dataset.xlsx")
