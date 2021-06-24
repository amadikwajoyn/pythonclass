age = int(raw_input('Enter your age '))
if age >= 0 and age <=120 :
    print 'Welcome, you are is', age
elif age < 0 :
    print ' You age cannot be below 0'
else:
    print 'Say your real age'
    
while age <=120 :
    print age,
    age += 2

a,b = 2 , 3
c = 'a is less than b'  if (a<b)  else 'a is greater than b '
print c

namecus = ['Joy', 'Jerry', 'Charles']
agecus = [23, 45, 72]
cusnum = [0, 1, 2]

for i in cusnum :
    print '%s is %d years old' % (namecus[i], agecus[i])

rangedigi = range(3,20)
for m in  rangedigi :
    print m, 

print '\n'
# to print only the odd numbers
rangeval = range(1,30)
for n in rangeval:
    if (n%2) ==0:
        continue
    elif n== 21:
        break
    else:
        print n,

