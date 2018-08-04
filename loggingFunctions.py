from tabulate import tabulate

def printHeader(header):
    border = ''
    for i in range(len(header) + 4):
        border += '-'
    title = '  ' + header + '  '
    print (border)
    print (title)
    print (border)

def printDataset(dataset):
    print (tabulate(dataset, headers='keys', tablefmt='psql'))

def printInterns(interns):
    for intern in interns:
        print (intern)
