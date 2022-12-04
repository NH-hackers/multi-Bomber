from bomber import selectnode
number = ['8825322511','7836876098']
#number = ['9525461668']
number = ['7541946701']
number = ['6205762914']
for i in number:
    selectnode(mode='sms', num=i)
    selectnode(mode='call', num=i)
