#procedure
rock=[]
country=[]

def collect_songs():
    song='Write song: '
    ask='Enter r (rock) or c (country). Enter x for exit'

    while True:
        genre=input(ask)
        if genre =='x':
            break
        if genre=='r':
            rock.append(input(song))
        elif genre=='c':
            country.append(input(song))
        else:
            print('error')
    print(rock,'\n',country)
    
#collect_songs()
    
#functional
def increment(a):
    return a+1

#oop
class Orange:
    def __init__(self,w,c):
        self.weight=w
        self.color=c
        self.mold=0
        print('created')
    def rot(self,days,temp):
        self.mold=days*temp

or1=Orange(10,'dark')
print(or1)
print(or1.weight,'\n',or1.color)
or1.weight=100
or2=Orange(11,'light')
or3=Orange(12,'light dark')

or3.rot(10,33)
print(or3.mold)

class Rectangle():
    def __init__(self,w,l):
        self.width=w
        self.len=l

    def area(self):
        return self.width*self.len

    def change_size(self,w,l):
        self.width=w
        self.len=l
rect=Rectangle(10,20)
print(rect.area())
rect.change_size(20,40)
print(rect.area())



#homework
class Apple:
    def __init__(self,c,w,s):
        self.color=c
        self.weght=w
        self.sort=s
        self.mold=0
        print('apple pie!')
import math
class Circle:
    def __init__(self,r):
        self.radius=int(r)
    def area(self):
        print(self.radius*math.pi)
rnd=Circle(4)
rnd.area()
class Triangle:
    def __init__(self,s,h):
        self.side=s
        self.height=h
    def area(self):
        print(self.side*self.height/2)
trg=Triangle(3,7)
trg.area()
class Hexagon:
    def __init__(self,s):
        self.side=s
    def area(self):
        print(3*math.sqrt(3)*math.pow(self.side,2))
              
hxg=Hexagon(6)
hxg.area()
              
