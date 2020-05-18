## occurence of email domains
mydict = dict()
try:
    fh = open('file1.txt')
except:
    print("cant open the file")
    exit()
for line in fh:
    line = line.rstrip()
    if not line.startswith("From"):
        continue
    ls = line.split()
    if len(ls) > 2:
        mydict[ls[1][(ls[1].find('@')) + 1:]] = mydict.get(ls[1][(ls[1].find('@')) + 1:], 0) + 1


print(mydict)
