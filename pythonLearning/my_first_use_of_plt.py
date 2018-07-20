import numpy as np
import matplotlib.pyplot as plt

# 从[-1,1]中等距去50个数作为x的取值
x = np.linspace(-1, 1, 50)
print(x)
y = 2 * x + 1
# 第一个是横坐标的值，第二个是纵坐标的值
plt.plot(x, y)
# 必要方法，用于将设置好的figure对象显示出来

'''
plt.ion()    # 打开交互模式
# 同时打开两个窗口显示图片
plt.figure()
plt.imshow()
plt.figure()
plt.imshow(i2)
# 显示前关掉交互模式
plt.ioff()
'''
plt.show()

