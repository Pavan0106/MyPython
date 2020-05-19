##capitalize first letters ina word
s1 = "apple weird horses"
##name = s1.split()

final = ' '.join(word.capitalize() for word in s1.split())
print(final)

##OUtput  -> Apple Weird Horses