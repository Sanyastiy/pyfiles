one='Chehov'
for i in one:
    print(i)

print('Yesterday I writed {}. Yesterday I was in {}.'
      .format(input('first word: '),input('second word: ')))

print('oldos Haksley was born in 1894'.capitalize())

words='Where is it? Who is it? When is it?'
print(words.split('?'))

words=['red','fox','jumped','.']
words=' '.join(words)
words.replace('.','')
words.strip()
words+'.'
print(words)

print('child is a mirror of parents decides'.replace('o','0'))
print('m index is:','hemingawey'.index('m'))

dialog=['find a dialog in your favorite book','and make from it','a one string']
print(' '.join(dialog))
t='three'
print(t+t+t,'\n',t*3)

r='Why we need to screem! I heard it in a first time.'
print(r[:r.index('!')])
