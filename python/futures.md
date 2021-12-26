# Python futures模块

futures模块是python3.2版本开始引入的，其官方的介绍是“启动并发任务”。与多进程、多线程不一样，它是基于多进程、多线程来完成“并发任务”的，更贴近应用层面，而无需关心底层并发的控制逻辑（并发锁、数据共享等）。用起来更加便捷，但也牺牲了对进程的部分控制能力。

主要的几个类：
```python
concurrent.futures.Executor，抽象类，提供了异步调用的接口，提供了submit、map、shutdown三个功能接口，通过子类实例化后使用。

concurrent.futures.ProcessPoolExecutor，进程池执行类，继承自Executor，使用进程池异步执行提交的任务。

concurrent.futures.ThreadPoolExecutor，线程池执行类，继承自Executor，使用线程池异步执行提交的任务。

concurrent.futures.Future，封装了异步的计算结果。提供了查看、变更任务执行状态的接口。如：cancel、result、add_done_callback。

concurrent.futures，future模块的功能，包括concurrent.futures.wait（返回futures实例的运行情况）、concurrent.futures.as_completed（futures完成或者取消时会yield该任务）。
```

下面是一个并发求和的demo

```
import concurrent.futures

#求和。如果number有两个数，则计算它们的和；否则返回一个
def sum(numbers:list):
    print(numbers)
    if len(numbers)==2:
        return numbers[0] + numbers[1]
    
    return numbers[0]

#并发求和
def parallel_sum(numbers:list, max_workers:int):

    number_sum = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        fs = []
        for i in range(0, len(numbers), 2): #每两个数字一组
            fs.append(executor.submit(sum, numbers[i:i+2])) #返回创建的future对象

        for future in concurrent.futures.as_completed(fs):
            number_sum = number_sum + future.result()   #把每个并发（future）执行sum完成之后返回的和相加，就得到了最终结果

    return number_sum

if __name__=='__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(parallel_sum(numbers, 4))

```

上面代码并发使用的是线程池（ThreadPoolExecutor）的方式，如果要改成进程池非常简单，只需要把ThreadPoolExecutor，改为ProcessPoolExecutor即可，因为它们都是Executor的子类。我们也能看出这种封装后的优点：代码的复用率非常高。

那什么时候使用线程池（ThreadPoolExecutor），什么时候使用进程池（ProcessPoolExecutor）呢？

这就涉及到并发和并行概念的区别。

并发，是指一个处理器（进程）能同时处理多个任务；并行，指的是多个处理器（进程）同时处理多个不同的任务。

一般可以认为多线程用于并发任务处理，而多进程用于并行任务处理。

因此，当任务是IO型的，适合用线程池的方式，因为一个线程被IO挂起，其他的线程可以继续执行；而如果任务是CPU型的，适合用进程池的方式，此时并未挂起，需要同时执行任务。