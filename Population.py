from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='Custom')
def people(Pop, feature, parent):
    if int(Pop) < int(35000):
        b = 'low'
    elif int(Pop) >= int(35000) and int(Pop) < int(80000):
        b = 'medium'
    elif int(Pop) >= int(80000):
        b = 'high'
    #when 0 say null 
    else:
        b = 'null'
    return b