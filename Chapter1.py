'''example 1:
Implement an algorithm to determine if a string has all unique characters
'''
def exp1(s1):
    keyEnt=sorted(list(s1))
    if all(keyEnt[i]!=keyEnt[i+1] for i in range(len(keyEnt)-1)):
        print('Unique')
    else:
        print('Not unique!!')

''' Example 2:
Write code to reverse a C-Style String'''
def exp2(s1):
    s1 = (s1[:-2][::-1]) + '\0'
    print('return String is:',s1)
    return s1
'''Exapmle 3
Design an algorithm and write code to remove the duplicate characters
'''
def exp3(s1):
    s2=''
    charAt=0
    while charAt<len(s1):
        if  not s1[charAt] in list(s2):
            s2+=s1[charAt]
        charAt+=1
    print('return String is:',s2)
    return s2
'''Example 4:
    Write a method to decide if two strings are anagrams or not
'''
def exp4(s1,s2):
    if not len(s1)==len(s2):
        print('not Anagrams!')
        return False
    elif all(sorted(list(s1))[i]==sorted(list(s2))[i] for i in range(len(s1))):
        print('Anagrams!')
        return True
    else:
        print('not Anagrams!')
        return False
'''Example 5:
Write a method to replace all spaces in a string with ‘%20’
'''
def exp5(s1):
    print('return String is:', s1.replace(' ','%20'))
    return s1.replace(' ','%20')


'''Example 6:
Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees
'''

def exp6(intN):
    import random
    matrix=[[random.randint(1,10) for i in range(intN)] for j in range(intN)]
    print(matrix)
    returnMat=[[matrix[j][i] for j in range(intN)] for i in range(intN)]
    print(returnMat)
    return returnMat

'''Example 7:
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column is set to 0.
'''
def exp7(M,N):
    import random
    matrix = [[random.randint(0,10) for i in range(M)] for j in range(N)]
    Cmatrix=matrix[:]
    print(matrix)
    for j in range(N):
        for i in range(M):
             if Cmatrix[j][i]==0:
                 matrix[j]=[0]*M
                 for k in range(N): matrix[k][i]=0
    print(matrix)
'''Example 8
Assume you have a method isSubstring which checks if one word is a substring of
another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using
only one call to isSubstring 
'''
def exp8(s1,s2):
    testStr=s2*2
    if len(s1)==len(s2) and testStr.find(s1):
        print('Rotation!!!')
        return True
    else:
        print('Not Rotation!')
        return False
