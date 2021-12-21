
def closure_demo(arg1, arg2):
    
    env1 = arg1 #环境变量1
    env2 = arg2 #环境变量2
    def show_env(): #输出环境变量
        print(env1, env2)
    
    return show_env


if __name__=='__main__':

    demo_int = closure_demo(1, 2)
    demo_str = closure_demo('str_1', 'str_2')

    demo_int()
    demo_str()