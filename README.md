# WayToPython

#### Books

* 编写高质量代码，改善Python程序的91个建议
* Python的Language Reference

#### Pythonic Code

* Google Python Style Guide: [Guideline](https://google-styleguide.googlecode.com/svn/trunk/pyguide.html)

#### 字符串格式化方法

```Python
print '{greet} from {language}.'.format(greet = 'Hello World', language = 'Python')
print '{0} from {1}.'.format('Hello World', 'Python')
```
#### 三元操作符

```C?X:Y``` 在 Python中等价的形式为 ```X if C else Y```

#### 数据交换值的时候不推荐使用中间变量

数据交换更Pythonic的实现方式：

```Python
x,y = y,x
```

比使用临时变量更高效。一般情况下Python表达式的计算顺序是从左到右，但遇到表达式赋值的时候表达式右边的操作数先于左边的操作数计算。因此 _exp3, exp4 = exp1, exp2_ 的计算顺序是 _exp1, exp2 = exp3, exp4_ 。因此对于表达式 _x, y = y, x_ , 其在内存中的执行的顺序如下:

* 先计算右边的表达式 y,x, 因此现在内存中创建元组 (y,x), 其标示符和值分别为y,x对应的值。其中y, x实在初始化时已经存在于内存中的对象。
* 计算表达式左边的值并进行赋值，元组被依次分配给左边的标示符，通过unpacking, 元组第一步标示符为y分配给左边第一个元素（此时为x）,元组第二个标示符(为x)
分配给第二个元素(为y)，从而达到x,y值交换的目的。


#### 使用enumerate()获取序列迭代的索引和值

函数 enumerate()解决了在循环中获取索引以及对应值的问题。具有一定的惰性，每次仅在需要的时候才会产生一个(index,item)对。其函数签名如下:

```Python
enumerate(sequence, start=0)
```

其中sequence可以为序列，如list,set等可以迭代的对象，默认的start为 0.

而要获取字典的key 和 value，应该使用如下的iteritems()方法：

```Python
for k,v in personinfo.iteritems():
	print k,v
```

#### 分清 == 与 is 的适用场景

```Python
a = "Hi"
b = "Hi"
str1 = "string"
str2 = "".join(['s','t','r','i','n','g'])
print str1 == str2
print str1 is str2
```
is 表示的对象标识符(object identity), 用来检查对象的标示符是否一致，也就是比较两个对象在内存中是否拥有同一块内存空间,不适用于判断两个字符串是否一致。而 == 表示的意思是相等 (equal)，用来检验两个对象的值是否相等。

可以用id()函数来看看这些变量在内存中具体的存储空间。上例中id(a) 和 id(b)是一样的。原因是Python中的string interning(字符串驻留机制)决定的: 对于较小的字符串，为了提高系统性能会保留其值的一个副本，当创建新的字符串的时候直接指向该副本即可。

#### 使用else子句简化循环(异常处理)

```Python
def print_prime(n):
    for i in range(2,n):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print '{0} is a prime number'.format(str(i))
print_prime(18)
```

else在循环（for,while）自然终结（循环条件为假）时else从句会被执行一次，而当循环是由break语句中断的时，else子句就不会被执行。

#### 连接字符串应优先使用join而不是+

```
str1, str2, str3 = 's1', 's2', 's3'
str1+str2+str3
''.join([str1,str2,str3])
```

使用join方法连接字符串的效率要高于 + 操作符。应为字符串是不可变对象，每次使用+操作都要申请新的内存空间然后进行复制。


#### 区别对待可变对象和不可变对象

Python中一切皆对象，每一个对象都有一个唯一的标示符(id()),类型(type())以及值。对象根据其值能否修改可分为可变对象和不可变对象。其中数字、字符串、元组属于不可变对象，字典以及列表、字节数组属于可变对象。

```Python
teststr = "I am a pytlon string"
teststr[10] = 'h'
print teststr
```
字符串为不可变对象，任何字符串中某个字符的修改都会抛出异常。修改字符串中某个字符的方式为：

```Python
teststr = "I am a pytlon string"
import array
a = array.array('c',teststr)
a[10] = 'h'
print a.tostring()
```

#### []、()和{}: 一致的容器初始化形式

list comprehension (列表解析)的语法为：

```Python
[expr for iter_item in iterable if cond_expr]
```

它迭代的iterable中的每一个元素，当条件满足的时候根据表达式expr计算的内容生成一个元素放进新的列表中，依次类推，并最终返回整个列表。其中条件表达式不是必需的。

支持多重迭代：

```Python
[(a,b) for a in ["a","1","2"] for b in ["1","3","4"] if a != b]
```

#### 函数传参

Python 中一切皆为对象，函数也是对象。对象分为可变（mutable）和不可变(inmutable)两种类型，元组（tuple）、数值型(number)和字符串(string)均为不可变对象，而字典(dictionary)和列表型(list)的对象是可变对象。

对于Python中函数是传值还是传引用的这个问题，正确的叫法应该是传对象(call by object)或者叫传对象的引用(call-by-object-reference)。函数在传递的过程中将整个对象传入，对可变对象的修改在函数的外部以及内部都可见，调用者和被调用者之间共享这个对象，而对于不可变对象，由于并不能真正地被修改，所以函数外部是看不到不可变对象的变化。对于不可变对象的修改，往往是通过生成一个新对象然后赋值来实现的。

警惕默认参数潜在的问题：如果不想让默认参数所指向的对象在所有的函数对象中共享，而是在函数调用的过程中动态生成，可以在定义的时候使用None对象作为占位符。

#### 字符串的基本用法

* istitle() 用来判定字符串是否每个单词都有且有且只有第一个字母为daxie
* 判定子串是不是在字符串中，推荐使用in 和 not in操作符
* title()是将每一个单词的首字母大写，并将单词中的非首字母转换为小写(英文文章标题格式)

#### 按需选择sort() 和 sorted()

两者的函数形式为：

```Python
sorted(iterable, cmp, key, reverse)
a.sort(cmp, key, reverse)
```
* cmp 为用户定义的任何比较函数，函数的参数为两个可比较的元素，第一个参数小于第二个参数返回为-1，otherwise 返回 0 或者 1
* key 是带一个参数的函数，用来为每个元素提取比较值，默认为None,即直接比较每个元素
* reverse 表示结果是否反转

两者比较:

* sorted可用于任何可迭代的对象，sort一般用于列表
* sorted 会返回一个排序后的列表，原有列表保持不变；sort函数会直接修改原有列表，函数返回为None
* sort函数不需要复制原有列表，消耗的内存较小，效率高
* 传入参数key 比参数cmp效率高。key中可以用匿名函数lambda来定义


#### 二维数组的创建

```Python
my_array = [[0]*3 for _ in range(4)]
```
创建4行3列的二维数组。

#### 类方法

在一个类中，可能回出现三种方法，实例方法，静态方法和类方法。

**实例方法**

实例方法的第一个参数是self, 实例方法只能通过类的实例来调用。这时候self就代表实例本身。通过self可以直接访问实例的属性。

**类方法**

类方法以cls作为第一个参数，cls表示类本身，定义时使用 _@classmethod_ 装饰器。通过cls可以访问类的相关属性。

```Python
class Student(object):
    count = 0
    books = []
    def __init__(self,name,age):
        self.name = name
        self.age = age
    @classmethod
    def printStudent(cls):
        print cls.__name__
        print dir(cls)
    pass
```

类方法可以通过类访问，也可以通过实例访问。

**静态方法**

与实例方法和静态方法不同，静态方法没有参数限制，既不需要实例参数，也不需要类参数，定义的时候使用 _@staticmethod_ 装饰器。

静态方法可以通过类名访问，也可以通过实例访问。

这三种方法区别在于参数，实例方法被绑定到一个实例，只能通过实例进行调用，但是对于静态方法和类方法，可以通过类名和实例两种方式进行调用。

#### 访问控制

Python中没有访问控制的关键字，例如private,protect等，但有一些约定来进行访问控制。

**单下划线"_"**

在Python中，通过单下划线**_**来实现模块级别的私有化，一般约定单下划线开头的变量、函数为模块私有的。使用 “from xx import xx”时将不会引入单下划线开头的变量函数。

**双下划线__**

对于Python中的类属性，可以通过双下划线来实现一定程度的私有化，因为双下划线开头的属性在运行时会被混淆（mangling）.


**单下划线"_"**: 以单下划线开头的表示的是protected的变量，即只能允许本身以及子类进行访问；同时表示弱内部变量标示。

**双下划线__**: 双下划线的表示是私有类型的变量。只能允许这个类本身进行访问，连子类也不可以。在运行时属性名会加上但下划线和类名

参考：

* [Python中的类（上）](http://www.cnblogs.com/wilber2013/p/4677412.html)
* [Python中的类（下）](http://www.cnblogs.com/wilber2013/p/4690681.html)
* [Code Demo](https://github.com/zhenv5/WayToPython/blob/master/Code/classDemo.py)
 

















