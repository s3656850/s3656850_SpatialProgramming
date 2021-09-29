from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='Custom')
#defining function
def money(Expend, feature, parent):
    #if the Expend value is between 0 and 30,000,000 classify it low
    if int(Expend) > int(0) and int(Expend) < int(30000000):
        b = 'low'
    #if the Expend value is between 30,000,000 and 90,000,000 classify it medium
    elif int(Expend) >= int(30000000) and int(Expend) < int(90000000):
        b = 'medium'
    #if the Expend value is greater than 90,000,000 classify it high
    elif int(Expend) >= int(90000000):
        b = 'high'
    #if the Expend value is anything else classify it null 
    else:
        b = 'null'
    return b
