name='ted'
for char in name:
    print(char)

shows=['this',
       'is',
       'list']
for smthn in shows:
    print(smthn)

kor=('this',
     'is',
     'tuple')
for jj in kor:
    print(jj)

people_in_dictionary={'jim':
                      'BBT',
                      'brian':
                      'tyler',
                      'some guy':
                      'some film'}
for jj in people_in_dictionary:
    print(jj)

#changing

tv=['lord of castamere',
    'secret materials',
    'fargo']
i=0
for show in tv:
    new=tv[i]
    new=new.upper()
    tv[i]=new
    i+=1

print(tv)

#cheking index!

for i,show in enumerate(tv):
    new=tv[i]
    new=new.lower()
    tv[i]=new

print(tv)

all_shows=[]

for show in tv:
    all_shows.append(show)
for show in kor:
    all_shows.append(show)
print(all_shows)
