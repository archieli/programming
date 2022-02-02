from operator import index
import pandas as pd
import numpy as np


class PandasDemo():

    """练习pandas的类"""

    def __init__(self) -> None:
        """构造初始数据"""

        ROW_NUM = 20
        gender = ["男", "女"]
        smoker = [True, False]
        education = ["本科", "硕士", "博士"]
        dict_random_data = {   #随机生成的数据
            "height":np.random.randint(160, 190, ROW_NUM),   #身高数据，从160到190，构造ROW_NUM个
            "weight":np.random.randint(60, 80, ROW_NUM),
            "gender":[gender[x] for x in np.random.randint(0, 2, ROW_NUM)],
            "smoker":[smoker[x] for x in np.random.randint(0, 2, ROW_NUM)],
            "education":[education[x] for x in np.random.randint(0, 3, ROW_NUM)]
        }

        dict_fixed_data = {  #固定的数据，便于观测结果
            "height":[160,  170,    170,    170,    172,    180,    170,    172,    180,    181],
            "weight":[60,   65,     70,     66,     65,     70,     80,     70,     73,     75],
            "gender":['男', '女',   '女',   '女',   '男',   '女',   '男',   '女',   '男',   '女'],
            "smoker":[True, False,  False,  True,   True,   False,  True,   False,  False,  False],
            "education":["本科", "本科", "硕士", "硕士", "博士", "博士", "博士", "硕士", "本科", "本科"],
        }

        self.demo_df = pd.DataFrame(data=dict_fixed_data)
    

    def dataframe_groupby_map(self):
        """测试dataframe某列的map操作"""
        self.demo_df['gender'] = self.demo_df['gender'].map({'男':1, '女':0})
        print(self.demo_df)

    
    def dataframe_groupby_test(self):
        """测试dataframe的groupby操作"""
        print(self.demo_df.groupby('gender').aggregate(np.sum))

        
    def apply_sum(self, group_df:pd.DataFrame, *args, **kwargs):
        """每个group的dataframe作为输入，计算这一组group的结果"""
        
        sum = 0
        for item in args:
            sum = sum + item

        sum = sum + kwargs['base1']
        sum = sum + kwargs['base2']
        
        for row in group_df.itertuples():
            sum = sum + row[1]

        return sum, group_df.shape[0], group_df.shape[1]

    
    def dataframe_groupby_apply_test(self):
        """测试dataframe的groupby的apply操作。"""

        print(self.demo_df.groupby('education').apply(self.apply_sum, 1, 2, 3, base1=1, base2=2))


    def dataframe_at_loc_test(self):
        """dataframe查找/修改 指定位置的元素"""

        self.demo_df.at[0, 'height'] = 1000 #at，使用行标签名和列标签名查找/修改某一个元素
        print(self.demo_df.at[0, 'height'])

        self.demo_df.iat[0, 0] = 2000   #iat，使用行列的整形值查找/修改某一个元素
        print(self.demo_df.iat[0, 0])

        #loc，查找/设置 多组行或者列
        print(self.demo_df.loc[1], type(self.demo_df.loc[1]))  #返回第二行数据，类型为Series
        print(self.demo_df.loc[[0, 3]], type(self.demo_df.loc[[0, 3]]))    #返回第一和第四行数据，类型为dataframe
        print(self.demo_df.loc[0, 'height'])    #使用行标签名和列标签名查找/修改某一个元素，类似at

        self.demo_df.loc[:, 'height'] = 180 #设置整列
        print(self.demo_df)

        self.demo_df.loc[self.demo_df['gender']=='男'] = 0  #设置满足条件的整行为0
        print(self.demo_df)


if __name__=='__main__':

    demo = PandasDemo()
    #demo.dataframe_groupby_map()
    #demo.dataframe_groupby_test()
    #demo.dataframe_groupby_apply_test()
    demo.dataframe_at_loc_test()

