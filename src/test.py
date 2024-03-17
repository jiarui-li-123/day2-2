import streamlit as st
from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt

# 设置页面标题
st.title('Streamlit Example')

# 使用 Streamlit 写副标题
st.subheader('Diabetes Dataset')

# 加载糖尿病数据集
diabetes_data = datasets.load_diabetes()
df = pd.DataFrame(data=diabetes_data.data, columns=diabetes_data.feature_names)

# 展示数据帧
st.dataframe(df)

# 绘制患者年龄的直方图
fig, ax = plt.subplots(figsize=(6, 3))
if len(df['age']) > 0:  # 确保'age'列中至少有一个值
    df['age'].hist(bins=10, ax=ax)
    fig.suptitle('Age Distribution')
    st.pyplot(fig)

