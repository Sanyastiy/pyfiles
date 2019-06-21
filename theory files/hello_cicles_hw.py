form=['walking dead','beauties','soprano clan','vampire diares']
for i,show in enumerate(form):
    print('"',i,'"',show)

for i in range(25,51):
    print(i)

seq=[13,432,54,332,6,43,34,1,32,35]
while True:
    n=input('guess the number-')
    if n=='x':
        break
    if int(n) in seq:
        print('you win!')
        break
    else:print('no,again')

spis1=[8,19,148,4]
spis2=[9,1,33,83]
spis3=[]
for i in spis1:
    for j in spis2:
        spis3.append(i*j)
print(spis3)
