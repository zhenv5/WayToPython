teststr = "I am a pytlon string"
import array
a = array.array('c',teststr)
a[10] = 'h'
print a.tostring()


