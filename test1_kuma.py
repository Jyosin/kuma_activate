# from tkinter import N
# from cv2 import HISTCMP_BHATTACHARYYA
# from turtle import distance
import matplotlib.pyplot as plt
# impoty matplotlib
import matplotlib.image as mpimg
import numpy as np
import math

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
h = 500
r = h/218
n = 6
n_y = 16
# the right = -h/190 * x = y
# thr left = h/190 * x - 2h = y
the_left_x = 218*190/-h
the_right_x  = (218+2*h)*190/h

the_right   = [the_right_x,218]
the_left    = [the_left_x,218 ]
the_h_point = [190,-h]

#for line
the_right_line_x = [the_right[0],the_h_point[0]]
the_right_line_y = [the_right[1],the_h_point[1]]
the_left_line_x = [the_left[0],the_h_point[0]]
the_left_line_y = [the_left[1],the_h_point[1]]

#for middle
step  = (the_right_x - the_left_x)/n
the_middle_x_n = []
the_middle_line_x_n = []
the_middle_line_y_n = []
for i in range(n-1):
    the_middle_x_n.append(the_left_x + (i+1)*step)
    the_middle_line_x_n.append([the_left_x + (i+1)*step,the_h_point[0]])
    the_middle_line_y_n.append([218,the_h_point[1]])


# for yoko
the_distance = math.dist(the_h_point, the_right)
step_y = the_distance/n_y
cos = (h+218)/the_distance
b = [] 
a = []
for yy in range(n_y-1):
    the_distance = the_distance -step_y
    b.append(the_distance)
    a.append(218-b[yy]*cos)



ax = plt.imshow(img)

plt.plot(x,y)
right
plt.plot(the_right_x,218,".")
# left
plt.plot(the_left_x,218,".")
#  hight
plt.plot(190,-h,".") 
# draw line
plt.plot(the_right_line_x , the_right_line_y, 'bo', linestyle="--")
plt.plot(the_left_line_x , the_left_line_y, 'bo', linestyle="--")

for d in range(n-1):
    plt.plot(the_middle_line_x_n[d] , the_middle_line_y_n[d], 'bo', linestyle="--")
for dd in range(n_y-1):
    plt.plot([0,380] , [a[dd],a[dd]], 'bo', linestyle="--")

plt.show()
# print(img)