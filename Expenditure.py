from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='Custom')
def money(Expend, feature, parent):
    if int(Expend) > int(0) and int(Expend) < int(30000000):
        b = 'low'
    elif int(Expend) >= int(30000000) and int(Expend) < int(90000000):
        b = 'medium'
    elif int(Expend) >= int(90000000):
        b = 'high'
    #when 0 say null 
    else:
        b = 'null'
    return b