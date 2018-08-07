from tabulate import tabulate

def printHeader(header):
    border = ''
    for i in range(len(header) + 4):
        border += '-'
    title = '  ' + header + '  '
    print ()
    print (border)
    print (title)
    print (border)

def printData(dataset):
    print (tabulate(dataset, headers='keys', tablefmt='psql'))
