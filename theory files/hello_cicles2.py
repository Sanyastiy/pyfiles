for i in range(1,11):
    print(i)

x=10
while x>0:
    print('{}'.format(x))
    x-=1
print('night king')

night=True
while night:
    print('jesus')
    
    break
#Ctrl+C to interrupt

qs=['whats your name',
    'your favorite colour',
    'what are you doing']
n=0
while True:
    print('Input x for exit')
    a=input(qs[n])
    if a=='x':
        break
    n=(n+1)%3


for i in range(1,6):
    if i==3:
        continue
    print(i)

    
i=1
while i<=5:
    if i==3:
        i+=1
        continue
    print(i)
    i+=1

for i in range(1,3):
    print(i)
    for letter in ['a','b','c']:
        print(letter)

list1=[1,2,3,4]
list2=[5,6,7,8]
added=[]
for i in list1:
    for j in list2:
        added.append(i+j)
print(added)


while input('yes or no')!='no':
    for i in range(1,6):
        print(i)
        
