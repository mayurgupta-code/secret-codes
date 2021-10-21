def printstr(string):
    return f'string is {string}'

def addnum(num1, num2):
    return num1 + num2 + 5

print('and the value of name is', __name__)
if __name__ == '__main__':    
    print(printstr('ye meri string hai'))
    a = addnum(4, 6) 
    print(a)
    print('ye abhi name1 me hai')       
    print(__name__)
# ye if __name__ == '__main__' 
# walli file jb hi run hogi jb name ki value main ho
# or agr name2 file me ye name1 file import hogi too file1 ki cheeze name2
# me chlegi to name ho jayega name1 to mtlb main name walli file 
# name1 ki nhi chlegi name2 walli file me


# print(printstr('ye meri string hai'))
# a = addnum(4, 6) 
# print(a)
# print('ye abhi name1 me hai')       
# print('in name1 file', __name__)