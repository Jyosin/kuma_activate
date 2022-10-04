import matplotlib.pyplot as plt
# impoty matplotlib
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('/home/wang/kuma_activate_analysis/background.png')

x = np.array(np.arange(0,380,0.01))
y = np.zeros(38000)

for i in range(len(x)):
    if x[i] < 87 :
        y[i]= -0.215*x[i] +108.550
    elif x[i] < 99:
        y[i]= -0.0409*x[i]*x[i] + 6.2681*x[i] - 143.56
    elif x[i] < 133:
        y[i]= 0.0067*x[i]*x[i] - 1.80*x[i] + 187.53
    elif x[i] < 148:
        y[i]= -0.0024*x[i]*x[i] + 1.32*x[i] - 65.62
    elif x[i] < 193:
        y[i]= -0.0031*x[i]*x[i] + 1.31*x[i] - 51.42
    elif x[i] < 244:
        y[i]= 0.0017*x[i]*x[i] - 0.589*x[i] + 133.42   
    elif x[i] < 277:
        y[i]= -0.0034*x[i]*x[i] + 1.640*x[i] - 107.69 
    elif x[i] < 302:
        y[i]= 0.53*x[i] - 64.23
    elif x[i] < 335:
        y[i]= -0.0023*x[i]*x[i] + 2.15*x[i] - 343.19 
    elif x[i] <  380:
        y[i]= -0.0054*x[i]*x[i] + 3.904*x[i] - 582.93         
# y = np.array(y_list)

ax = plt.imshow(img)
# ax.plot(x,y)

plt.plot(x,y)

plt.show()
# print(img)