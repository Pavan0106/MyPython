##a string is given and number of characters 'k' is mentioned
##string is split into k characters and duplications of characters are removed from splitted strings

def merge_the_tools(string, k):
    newlist = list()
    mylist = list()
##str ="QelloWorld"
##str1 = ""

    for index in range(0,len(string),k):
        mylist.append((string[index:index+k]))
    
##print(mylist)
    for str1 in mylist:
        str2 = ""
        for i in range(0, len(str1)):
            for j in range(0,i+1):
                if str1[i] == str1[j]:
                    break;
            
        
            if i==j:
                str2 = str2 + str1[i]
                index = index + 1
        print(str2)    
        
        
    

if __name__ == '__main__':
    string = "zhgfeeefdjkggssd"
	k = 3 ##number of characters to be split into 
    merge_the_tools(string, k)