import collections

c={}
def count(str):
    word = str.split()
    c = collections.Counter(word)
    for i in sorted (c) : 
        print((i,':' ,c[i]),end = " ")
s=count(input("enter the string"))