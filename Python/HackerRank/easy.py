#Capitalize!
# input()   chris alan
# output()  Chris Alan
#soluction 1 

#def solve(s):
#    return " ".join([word.capitalize() for word in s.split()])

def capitalize_solve(s):
    result = ""
    for i in range(len(s)):
        if i == 0 or s[i-1] == " ":
            result += s[i].upper()
        else:  
            result += s[i]
    return result 

