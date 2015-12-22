'''

string.punctuation

String of ASCII characters which are considered 
punctuation characters in the C locale.

'''
import string
delset = string.punctuation

'''

string.translate(s, table[, deletechars])

Delete all characters from s that are in deletechars (if present), 
and then translate the characters using table, which must be a 256-character 
string giving the translation for each character value, indexed by its ordinal.
 If table is None, then only the character deletion step is performed.
'''

line = "Hello, World. This is Python!!!!!!! :)"

l = line.translate(None,delset)

print line
print l

l = l.lower()

word_list = l.split()

print word_list
