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
