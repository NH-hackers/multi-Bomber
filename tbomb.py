from bomber import selectnode
number = ['8825322511','7836876098']
for i in number:
    selectnode(mode='sms', num=i)
    selectnode(mode='call', num=i)
