import xml
from xml.etree import ElementTree
import time
import sys


def div(a, b):
    try:
        c = a / b
    except ZeroDivisionError:
        c = float("inf")
    return c


ElementTypes = ['resistor', 'capactor', 'diode']
try:
    tree = ElementTree.parse(sys.argv[1])  # Reading file
except FileNotFoundError:
    print("No such file")
    sys.exit()
print("File has been read")
n = len(tree.findall('.//net'))
b = [[float("inf")] * n for i in range(n)]
tm = time.clock()
for i in range(n):
    b[i][i] = 0
vector = []
for x in ElementTypes:
    y = tree.findall('.//' + x)
    for z in y:
        t = z.attrib
        b[int(t['net_from']) - 1][int(t['net_to']) - 1] = div(1, (
            div(1, b[int(t['net_from']) - 1][int(t['net_to']) - 1]) + div(1, float(t['resistance']))))
        if x == 'diode':
            b[int(t['net_to']) - 1][int(t['net_from']) - 1] = div(1, (
                div(1, b[int(t['net_to']) - 1][int(t['net_from']) - 1]) + div(1, float(t['reverse_resistance']))))
        else:
            b[int(t['net_to']) - 1][int(t['net_from']) - 1] = div(1, (
                div(1, b[int(t['net_to']) - 1][int(t['net_from']) - 1]) + div(1, float(t['resistance']))))

            # last part of the alorithm
            # start
for k in range(n):
    for i in range(n):
        for j in range(n):
            b[i][j] = div(1, (div(1, b[i][j]) + div(1, (b[i][k] + b[k][j]))))
file = open(sys.argv[2], 'w')
for i in range(n):
    if i > 0:
        file.write('\n')
    for j in range(n):
        file.write(str(round(b[i][j], 7)) + ',')
file.close()
print(time.clock() - tm)
