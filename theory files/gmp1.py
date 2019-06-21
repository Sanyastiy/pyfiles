import math
def hw():
    print('hello world')#yeah, thats my hello world
    for i in range(10):
        print('decade')
    l=4
    w=10
    d=math.sqrt(l**2+w**2)#1 is a number l is a litera 0_0
    print(d,'''\nsome
long
string
i guess''')

def ho():
    str='''//integer division
%module division
**exponent'''
    f=int(input('some elifs, input number: '))
    if((f>0)and(f%2==0)):
        print('natural, even')
    elif((f<0)and(f%2==0)):
        print('negative, even')
    elif((f>0)and(f%2!=0)):
        print('natural, odd')
    elif((f<0)and(f%2!=0)):
        print('negative, odd')
    print('length of str: ',len(str))
    def func_in_func():
        x=2
        y=6
        print('this is func in func, got it? some nymbers: ',x**y)
    func_in_func()

x='jesus'#only here
def hsov():
    y='christ'
    z='god'
    def f(x=x):
        y='omg'
        z='fukn'
        print(x,y)
        x='gghl'
    def f2():
        global x
        print(x)
    f()
    f2()

def he():
    while(True):
        try:
            print(int(input('a= '))/int(input('b= ')))
            break
        except ValueError:
            print('yeap, value error, smart')
        except ZeroDivisionError:
            print('nope, zero division')
        

def hx(x):
    return print(int(x)**int(x),' ','str: ',str(x))

def hf(i,j,k,m=8,n=6):
    return print(int(i)+j+k+n+m)
def preobr(some):
    b=False
    try:
        x=float(some)
        b=True
        return (print(x/2,x*4,b))
    except ValueError:
        print('intercepted')

def myfactorial(x):
    if x==0:
        return 1
    return x*myfactorial(x-1)
    
def containers():
    fqb=['sound','music','song']
    frb=list('beats')
    fqb.append('mic')
    fqb.append(1321)

    tup=(1,2,3,4)
    tups=('zapyataya',)

    dictionary=dict()
    dictionary={1:'op',2:'gop',3:'stop',4:'hop',5:'top'}
    
    dictionary[6]='opa'
    
    del dictionary[2]
    print(dictionary)
    frb=(dictionary,)
    print(frb,type(frb))

    mnoj=set()
    mnoj.add('some element')
    mnoj.add('sec elem')
    print(mnoj)
