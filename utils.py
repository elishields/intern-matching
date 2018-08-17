from tabulate import tabulate


def print_header(header):
    border = ''
    for i in range(len(header) + 4):
        border += '-'
    title = '  ' + header + '  '
    print()
    print(border)
    print(title)
    print(border)


def print_data(dataset):
    print(tabulate(dataset, headers='keys', tablefmt='psql'))


def get_rounds(interns, session):
    for round in range(session.num_rounds):
        filename = "../" + str(round+1) + ".txt"
        file = open(filename, "w")
        print_header(str(round + 1))
        matches_printed = []
        for intern in interns:
            matches_printed.append(intern.pairs[round][0])
            if intern.name not in matches_printed:
                file.write(intern.name + " & " + intern.pairs[round][0] + " (" + str(intern.pairs[round][1]) + ")")
                file.write("\n")