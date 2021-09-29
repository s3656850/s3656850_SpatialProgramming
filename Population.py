from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='Custom')
#defining function
def people(Pop, feature, parent):
    #if the Pop value is less than 35,000 classify it low
    if int(Pop) < int(35000):
        b = 'low'
    #if the Pop value is between 35,000 and 80,000 classify it medium
    elif int(Pop) >= int(35000) and int(Pop) < int(80000):
        b = 'medium'
    #if the Pop value is greater than 80,000 classify it high
    elif int(Pop) >= int(80000):
        b = 'high'
    #if Pop is anything else classify it null 
    else:
        b = 'null'
    return b
