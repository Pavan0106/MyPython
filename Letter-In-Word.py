##count the occurence of letter in a word
##EFFIECENT WAY
myword = 'pavanp'
mydict = dict()

for item in myword:
    mydict[item] = mydict.get(item, 0) + 1

print(mydict)