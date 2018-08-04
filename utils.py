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

def printInterns(interns):
    for intern in interns:
        print (intern)

# Max rounds is each intern pairing with every other intern
def getRounds(interns):
    return len(interns) - 1
