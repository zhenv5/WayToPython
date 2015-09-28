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

page 86










