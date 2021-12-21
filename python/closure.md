# Python闭包

首先来看看闭包在Wiki里的定义。
```
A closure is a record storing a function together with an environment.
```
即：闭包是存储了函数及其环境的记录。

所以，闭包不仅仅是函数，它还包括了函数的上下文环境。

这里有两个关键：函数、环境。

函数好理解，环境是什么呢？

环境可以理解为所有变量的统称。

举个例子：
```python
def closure_demo(arg1, arg2):
    
    env1 = arg1 #环境变量1
    env2 = arg2 #环境变量2
    def show_env(): #函数,输出'环境'
        print(env1, env2)
    
    return show_env
```

上面的代码很清晰地展示了函数和环境，而这个整体就是闭包。

怎么使用呢？

```python
demo_int = closure_demo(1, 2)
demo_str = closure_demo('str_1', 'str_2')
```

输出：
```python
1 2
str_1 str_2
```

上面的demo_int和demo_str，都是通过同一个函数closure_demo创建的，只不过创建的时候环境不一样而已，这也是闭包和函数的核心区别。

所以，在python中创建闭包有三个特点:
- 嵌套函数。在函数中定义函数。
- 嵌套函数使用了该函数外的变量（即：环境）
- 该函数返回内部定义的嵌套函数

这套流程下来，有什么好处呢？

- 可以代替python中的类。上面的demo_int、demo_str就是同一个函数closure_demo创建的，和类创建对象比较像，但是比起类会更加优雅，还能实现数据隐藏。这正是python这种语言所追求的。
- [Python装饰器](https://github.com/archieli/programming/blob/main/python/decorator.md)（decorator）实现的底层技术。装饰器是非常灵活的设计模式，使用非常广泛。