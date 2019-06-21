some_str='''
triple
breackets
'''
print(some_str[4])
sy='onetwo'
print(sy[-1])
konkatenation=some_str+sy
print(konkatenation)
mutliply=sy*3
print(mutliply)
upstr='threefour'.upper()
print(upstr)
downstr=upstr.lower()
print(downstr)
firstletterup='gods'.capitalize()
print(firstletterup)

#format
print('William{}'.format('Falkner'))

print('{} {} is stupid {}'.format('John','Snow','?'))

#spaghetti
'''
print('Some Very Long String {} {} {} {}'
      .format(input('enter first word '),
              input('second word '),
              input('third word '),
              input('forth word ')))
              '''
print(upstr.split('E'))

alphabet='abc'
print('+'.join(alphabet))

words=['red','fox','made','jump','through','the head']

print(''.join(words))
print(' '.join(words))

one='                uno            '
print(one)
print(one.strip())

print('all cops are bastards'.replace('a','*'))

print(one.index('n'))
print('o'in one)
print('u' not in one)

print('careful, \nthere is \'special\' symbols needed')
print('or like "that"')
print('=====')
fict=['garrison','brooks','woody','alpen','jakobs']
print(fict[1:3])
poem='Petr Ivanovich calmed down and with intrest began to ask parts about Ivan Ilyich death'
print(poem[:14])
print(poem[69:])
