from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='Custom')
def EP(Pop_rate, Expend_rate, feature, parent):
    if Pop_rate == 'high' and Expend_rate == 'high':
        b = 'Priority 1'
    elif Pop_rate == 'high' and Expend_rate == 'medium':
        b = 'Priority 2'
    elif Pop_rate == 'medium' and Expend_rate == 'high':
        b = 'Priority 2'
    elif Pop_rate == 'medium' and Expend_rate == 'medium':
        b = 'Priority 3'
    elif Pop_rate == 'medium' and Expend_rate == 'low':
        b = 'Priority 4'
    elif Pop_rate == 'low' and Expend_rate == 'medium':
        b = 'Priority 4'
    elif Pop_rate == 'high' and Expend_rate == 'low':
        b = 'Priority 4'
    elif Pop_rate == 'low' and Expend_rate == 'high':
        b = 'Priority 4'
    elif Pop_rate == 'low' and Expend_rate == 'low':
        b = 'Priority 5'
    else:
        b = 'null'
    return b