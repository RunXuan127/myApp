import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 设置Streamlit的标题和样式
st.title("sin函数展示")
st.markdown("### 欢迎使用这个程序来查看sin函数!")

# 创建一个滑动条来调节频率
frequency = st.slider("请选择频率", min_value=0.1, max_value=10.0, step=0.1, value=1.0)

# 创建一个滑动条来调节振幅
amplitude = st.slider("请选择振幅", min_value=0.1, max_value=10.0, step=0.1, value=1.0)

# 创建一个滑动条来调节相位
phase = st.slider("请选择相位", min_value=0.0, max_value=2 * np.pi, step=0.1, value=0.0)

# 创建一个文本框来显示频率、振幅和相位
st.write(f"频率: {frequency}")
st.write(f"振幅: {amplitude}")
st.write(f"相位: {phase}")

# 创建一个画布来绘制sin函数
fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 1000)
y = amplitude * np.sin(frequency * x + phase)
ax.plot(x, y)
ax.set_title("sin函数")
ax.set_xlabel("x")
ax.set_ylabel("y")

# 将画布显示在Streamlit应用中
st.pyplot(fig)
