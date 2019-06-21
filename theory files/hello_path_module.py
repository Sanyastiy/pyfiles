'''
Some documentation:
This file import a system module
to make a good path for files
then defining TWO or more functions
First, now, opening file and writing there usually
Second analogical First, but using WITH construction
Third is writing to list what file contains
Fourth is creating a .csv file
Fifth is reading .csv file
'''
'''
Strange things in .csv:
local Excel opening all Writerow text in one cell
Google sheets makes parsels this, but both of Excel and GS
inserting one empty row between Writerow rows
'''
import os
import csv

pathobj=os.path.join('path','st.txt')
def first():
    st=open(pathobj,'w+')
    st.write('hello from python')    
    st.close()
    print('first succsessful ^^')
    
def second():
    with open(pathobj,'w+') as st:
        st.write('some dich`')
        print('second succsessful 1/2')
    with open(pathobj,'r') as st:
        print(st.read())
    print('second succsessful 1/2')

def third():
    my_list=list()#or my_list=[]
    with open(pathobj,'r') as st:
        my_list.append(st.read())
    print('third successful ^^')
    print(my_list)

def fourth():
    #using csv
    pathobj=os.path.join('path','st.csv')
    with open(pathobj,'w+') as f:
        newobj=csv.writer(f,delimiter=",")
        newobj.writerow(['one',
                         'two',
                         'three'])
        newobj.writerow(['four',
                         'five',
                         'six'])
    print('fourth successful ^^')

def fifth():
    #using csv
    pathobj=os.path.join('path','st.csv')
    with open(pathobj,'r') as f:
        zig=csv.reader(f, delimiter=',')
        for row in zig:
            print('|'.join(row))    
    print('fifth successful ^^')   

#homework part
def hw1():
    pathobj=os.path.join('R-Undelete','eula.txt')
    with open(pathobj,'r') as file:
        print(file.read())
        
def hw2():
    pathbitch=os.path.join('path','question.otvechaysuka')
    q=input('-I`m tired to write on english... and you?\n-')
    with open(pathbitch,'w') as file:
        file.write(q)
def hw3():
    list_of_lists=[['Star Wars','Terminator','AI'],
                   ['Fool','Matilda','Leviafan'],
                   ['Men in Black','I-Robot','Evolution']]
    p=os.path.join('path','films.csv')
    with open(p,'w') as p:
        w=csv.writer(p, delimiter=',')
        for y in list_of_lists:
            w.writerow(y)
