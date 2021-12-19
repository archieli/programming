#圣诞节装饰器，装饰一个函数，返回具有更多功能的函数
def decorate_christmas(func):
    print("decorate something with christmas")

    def wrap():
        print("use wrap to decorate with christmas")  #装饰到圣诞节
        return func()  #原来的函数在这里被调用了。

    return wrap #返回扩展功能（被装饰）后的函数


#水果茶装饰器，装饰一个函数，返回具有更多功能的函数
def decorate_fruit(func):   #水果茶装饰
    print("decorate something with fruit")

    def wrap():
        print("use wrap to decorate as christmas")  #装饰为水果茶
        return func()  #原来的函数在这里被调用了。

    return wrap #返回扩展功能（被装饰）后的函数    

#苹果函数-使用christmas装饰器
@decorate_christmas
def apple_christmas():
    print("I'm be eating...")

#苹果函数-使用水果茶装饰器
@decorate_fruit
def apple_fruit():
    print("I'm be eating...")





#有变量参数的圣诞节装饰器，装饰一个函数，返回具有更多功能的函数
def decorate_christmas_args(func):
    print("decorate something with christmas")

    def wrap(*args, **kwargs):
        print("use wrap to decorate with christmas")  #装饰到圣诞节
        return func(*args, **kwargs)  #原来的函数在这里被调用了。

    return wrap #返回扩展功能（被装饰）后的函数  

@decorate_christmas_args
def apple_with_args(price:int, count:int):
    print(f"I'm be eating..., cost monty : {price * count}")


if __name__=='__main__':

    apple_christmas()

    #apple_fruit()    
    #apple_with_args(6, 6)
