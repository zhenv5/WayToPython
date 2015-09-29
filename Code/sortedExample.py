# sort dictionary
phoneBook = {"Linda":"7789", "Bob":"7865", "Carl":"4532"}
sorted_pb = sorted(phoneBook.iteritems(), key = lambda x: x[0])
print sorted_pb

# sort multi-list
gameresult = [["Bob",95,"B"],["Alan",99,"C"],["Mandy",99,"A"]]
sorted_result = sorted(gameresult, key = lambda x: x[1])
print sorted_result

# sort set
from sets import Set
names = Set(['Jack', 'Sam', 'Susan', 'Janice'])
sorted_set = sorted(names)
print sorted_set

# sort list in dictionary
mydict = {"Li":['M',8],"Zhang":['E',3],"Wang":['P',4],"Du":["K",2]}
sorted_mydict = sorted(mydict.iteritems(), key = lambda (k,v): v[1])
print sorted_mydict






