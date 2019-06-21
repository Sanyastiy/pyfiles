
#wow
class Rectangle():
    recs=[]
    def __init__(self,w,l):
        self.width=w
        self.len=l
        self.recs.append((self.width,self.len))
    def print_size(self):
        print('''{} on {}
'''.format(self.width,self.len))

my_rect=Rectangle(10,20)
my_rect.print_size()
r1=Rectangle(10,24)
r2=Rectangle(20,40)
r3=Rectangle(100,200)
print(Rectangle.recs)


#magical methods
class Lion:
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return self.name

lion=Lion('Dilbert')
print(lion)


class AlwaysPositive:
    def __init__(self,n):
        self.number=n
    def __add__(self,other):
        return(abs(self.number+other.number))

x=AlwaysPositive(-20)
y=AlwaysPositive(10)
print(x+y)

class Person:
    def __init__(self):
        self.name='Bob'
bob=Person()
same_bob=bob
another_bob=Person()
print(bob is same_bob,bob is another_bob)

def eqn(x):
    if x is None:
        print('x equals None')
    else:
        print('x not equals None')
    
x=10
eqn(x)
x=None
eqn(x)


class Square:
    square_list=[]
    def __init__(self,w):
        self.width=w
        self.square_list.append((self.width))
        print('{} on {} on {} on {}'.format(self.width,self.width,self.width,self.width))
    pass

print(Square)
s1=Square(43)
s2=Square(543)
print(Square.square_list)

def IsObjEq(ob1,ob2):
    print(ob1 is ob2)
IsObjEq(bob,same_bob)
IsObjEq(s1,s2)
