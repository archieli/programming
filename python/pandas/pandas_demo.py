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
        dict_data = {
            "height":np.random.randint(160, 190, ROW_NUM),   #身高数据，从160到190，构造ROW_NUM个
            "weight":np.random.randint(60, 80, ROW_NUM),
            "gender":[gender[x] for x in np.random.randint(0, 2, ROW_NUM)],
            "smoker":[smoker[x] for x in np.random.randint(0, 2, ROW_NUM)],
            "education":[education[x] for x in np.random.randint(0, 3, ROW_NUM)]
        }

        self.demo_df = pd.DataFrame(data=dict_data)
    

    def dataframe_groupby_map(self):
        """测试dataframe某列的map操作"""
        self.demo_df['gender'] = self.demo_df['gender'].map({'男':1, '女':0})
        print(self.demo_df)

    
    def dataframe_groupby_test(self):
        """测试dataframe的groupby操作"""
        print(self.demo_df.groupby('gender').aggregate(np.sum))

        

if __name__=='__main__':

    demo = PandasDemo()
    demo.dataframe_groupby_map()
    #demo.dataframe_groupby_test()

