# Python 装饰器（decorator）

装饰器的程序定义：装饰器是一个函数，接受另外一个函数作为其参数，扩展输入的函数的功能后返回（并不修改它的功能）。

听起来有点抽象，我们先来举个例子。

我们有个苹果函数，它的主要功能是被吃掉。

```python
def apple():
    print("I'm be eating...")
```

但是，在被吃掉之前，可以先装饰（圣诞包装、水果茶包装...）一下再被吃掉。

```python
def decorate_christmas(func):   #圣诞节装饰
    print("decorate something as christmas")

    def wrap():
        print("use wrap to decorate with christmas")  #装饰到圣诞节
        func()  #原来的函数在这里被调用了。

    return wrap #返回扩展功能（被装饰）后的函数
```


当然，使用水果茶来装饰也是一样的    
```python
def decorate_fruit(func):   #水果茶装饰
    print("decorate something with fruit")

    def wrap():
        print("use wrap to decorate as christmas")  #装饰为水果茶
        func()  #原来的函数在这里被调用了。

    return wrap #返回扩展功能（被装饰）后的函数
```

装饰器定义好了，如何使用呢？

最直观的用法：
```python
decorate_apple = decorate_christmas(apple)
decorate_apple()
```

输出如下：
```
decorate something with christmas
use wrap to decorate with christmas
I'm be eating...
```

当然，上面的写法还是比较麻烦，多了几行、而且引入了新的变量：decorate_apple。

python提供了一种语法：@。只需要在需要装饰的函数（apple）使用@和装饰器函数即可：

```python
@decorate_christmas   #装饰器
def apple():    #被装饰的函数
    print("I'm be eating...")
```


一般来说，函数都是有部分参数的。比如上面的苹果有单价和个数两个参数：

此时的装饰器：
```python
def decorate_christmas(func):   #圣诞节装饰
    print("decorate something as christmas")

    def wrap(price:int, count:int): #单价（price）和个数（count）两个参数
        print("use wrap to decorate with christmas")  #装饰到圣诞节
        return func(price, count)  #原来的函数在这里被调用了。

    return wrap #返回扩展功能（被装饰）后的函数
```

因此，apple函数的定义改为：
```python
@decorate_christmas
def apple(price:int, count:int):
    print(f"I'm be eating..., cost monty : {price * count}")
```


当然，如果参数是不确定的呢？使用python函数的可变参数：function(*args, **kwargs)

因此，以上的装饰器定义为：
```python
def decorate_christmas(func):   #圣诞节装饰
    print("decorate something as christmas")

    def wrap(*args, **kwargs): 
        print("use wrap to decorate with christmas")  #装饰到圣诞节
        return func(*args, **kwargs)  #原来的函数在这里被调用了。

    return wrap #返回扩展功能（被装饰）后的函数
```


所以，装饰器把具有某种功能的函数扩展了，让它具有更加丰富的功能。这样做有什么好处呢？

第一是非常灵活、方便。
当我们需要某种功能的时候，只需要使用 @ 加上另外一个装饰器，就能拥有“特异功能”。而且“拆卸”非常便利。

第二是代码解耦。
各个功能模块独立。我只需要关注自己的业务逻辑，修改任何地方都不会影响到装饰器的功能，彻底解耦。

第二是代码复用。
人人都可以复用一套装饰器的代码，维护起来非常方便。
