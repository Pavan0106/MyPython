## get  count of emails in every hour
mydict = dict()
ls1 = list()
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
        hr = ls[5].split(':')
        mydict[hr[0]] = mydict.get(hr[0], 0) + 1

for key, values in list(mydict.items()):
    ls1.append((key, values))

print(type(ls1))

for key, value in ls1:
    print(key, value)