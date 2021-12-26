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
