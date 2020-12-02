import pandas as pd
import numpy as np
import copy
import openpyxl
data = {"grammer":["Python","C","Java","GO","R","SQL","PHP","Python"],"score":[1,2,np.nan,4,5,6,7,10]}

# 1. 将字典创建为dataframe
df = pd.DataFrame(data)
print(df)

# 2.提取含有字符串'python'的行
result = df[df['grammer'].str.contains('Python')]
# print(result)

# 3. 输出df的所有列名
result =df.columns
# print(result)

# 4. 修改第二列列名为'popularity'
df_tmp = copy.copy(df)
df_tmp.rename(columns={'score':'popularity'}, inplace = True)
# print(df_tmp)

# 5. 统计grammer列中每种编程语言出现的次数
result = df['grammer'].value_counts()
# print(result)

# 6. 将空值用上下值的平均值填充
df_tmp = copy.copy(df)
df_tmp['score'] = df_tmp['score'].fillna(df_tmp['score'].interpolate())
# print(df_tmp)

# 7.提取popularity列中值大于3的行
result = df[df['score'] > 3]
# print(result)

# 8. 按照grammer列进行去重
df_tmp = df.drop_duplicates(['grammer'])
# print(df_tmp)

# 9. 计算score列平均值
result = df['score'].mean()
# print(result)  

# 10. 将grammer列转换为list
result = df['score'].to_list()
# print(result)

# 11. 将DataFrame保存为EXCEL
result = df.to_excel('tmp.xlsx')
# print(result)

# 12. 查看数据行列数
result = df.shape
# print(result)

# 13. 提取score列值大于3小于7的行
result = df[(df['score'] > 3) & (df['score'] < 7)]
# print(result)

# 14. 交换两列位置
df_tmp = copy.copy(df)
col_tmp = df['score']
df_tmp.drop(labels = ['score'], axis = 1, inplace = True)
df_tmp.insert(0, 'score', col_tmp)
# print(df_tmp)

# 15. 提取score列最大值所在行
result = df[df['score'] ==  df['score'].max()]
# print(result)

# 16. 查看最后5行数据
result = df.tail(5)
# print(result)

# 17. 删除最后一行数据
df_tmp = copy.copy(df)
result = df_tmp.drop(labels = 0)
# print(result)

# 18. 添加一行数据['Perl',6.6]
df_tmp = copy.copy(df)
row={'grammer':'Perl','score_append':6.6}
result = df_tmp.append(row,ignore_index = True)
# print(result)

# 19. 对数据按照"score"列值的大小进行排序
df_tmp = copy.copy(df)
df_tmp.sort_values('score', inplace = True)
# print(df_tmp)

# 20. 统计grammer列每个字符串的长度
result = list(df['grammer'].map(lambda x: len(x)))
# result = list(map(lambda x: len(x), df['grammer'].to_list()))
print(result)
