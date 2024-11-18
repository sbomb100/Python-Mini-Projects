#basic notes 
var = 0
var1 = 'hello'
typical_convention = 1

input = input('Enter String: ')
print(input)

naming_convention = not(True and False or False)

if True:
    x = 10
else:
    x = 12

arr = [4, True, 'hi'] #len() for length, .append() , .extend() append list, .pop() or .pop(i), 
y = arr[:] #makes a copy not a reference

tup = (1,2,3,4)
#tuples are immutible

for i in range(10): #range has start,stop,step, 1 var means stop
    var += 1
for i, element in enumerate(y):
    print(i, element)

while False:
    x += 1


#slice 
sliced = tup[0:4:2]#[start:stop:step]
print(sliced)
sliced = tup[::-1]
print(sliced)