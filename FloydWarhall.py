import xml
from xml.etree import ElementTree
import numpy
def FloydWarhall(n):
     b=[float("inf")]*n*n
     b=numpy.array(b)
     b.shape=(n,n)
     for i in range(n):
          b[i][i]=0
     ElementTypes=['resistor','capactor','diode']
     tree=ElementTree.parse("example_input_5_nodes.xml")
     vector=[]
     for x in ElementTypes:
          y=tree.findall('.//'+x)
          for z in y:
               t=z.attrib
               b[int(t['net_from'])-1][int(t['net_to'])-1]=1/(1/b[int(t['net_from'])-1][int(t['net_to'])-1]+1/float(t['resistance']))
               if x=='diode':
                    print()
                    b[int(t['net_to'])-1][int(t['net_from'])-1]=1/(1/b[int(t['net_to'])-1][int(t['net_from'])-1]+1/float(t['reverse_resistance']))
     return b
          
     
          
          
     
     #x=tree.findall(".//resistor")# searching
     #return(x[0].attrib) # получение аттрибутов
     
