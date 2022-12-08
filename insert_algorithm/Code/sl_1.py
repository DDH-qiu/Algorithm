# 全象限的直线插补算法python实现
from pylab import *
xe = int(input("please enter the end point of then end point"))
ye = int(input("please enter the end point coordinate"))
print("xe =", xe, "ye = ", ye)
xi = 0
yi = 0
x_label = [xi]
y_label = [yi]
x_zero = [xi, xe]
y_zero = [yi, ye]
n = abs(xe-xi)+abs(ye-yi)
F = xe * yi - ye * xi
print("---------------------------------")
print(xi, '\t', yi, '\t', F, '\t', n)
while n > 0:
    n = n - 1
    if xe > 0 and ye == 0:
        xi = xi + 1
        print(xi, '\t', yi, '\t', F, '\t', n)
    if xe < 0 and ye == 0:
        yi = yi - 1
        print(xi, '\t', yi, '\t', F, '\t', n)
    if xe == 0 and ye > 0:
        yi = yi + 1
        print(xi, '\t', yi, '\t', F, '\t', n)
    if xe == 0 and ye < 0:
        xi = xi - 1
        print(xi, '\t', yi, '\t', F, '\t', n)
    # 第一象限
    if xe > 0 and ye > 0:
        if F < 0:
            yi = yi + 1
            print(xi, '\t', yi, '\t', F, '\t', n)
        if F >= 0:
            xi = xi + 1
            print(xi, '\t', yi, '\t', F, '\t', n)
    # 第二象限
    if xe < 0 and ye > 0:
        if F < 0:
            xi = xi - 1            
            print(xi, '\t', yi, '\t', F, '\t', n)
        if F >= 0:
            yi = yi + 1
            print(xi, '\t', yi, '\t', F, '\t', n)
    # 第三象限
    if xe < 0 and ye < 0:
        if F < 0:
            yi = yi - 1
            print(xi, '\t', yi, '\t', F, '\t', n)
        if F >= 0:
            xi = xi - 1
            print(xi, '\t', yi, '\t', F, '\t', n)
    # 第四象限
    if xe > 0 and ye < 0:
        if F < 0:
            xi = xi + 1
            print(xi, '\t', yi, '\t', F, '\t', n)
        if F >= 0:
            yi = yi - 1
            print(xi, '\t', yi, '\t', F, '\t', n)
    x_label.append(xi)
    y_label.append(yi)
    F = xe * yi - ye * xi

plt.plot(x_label, y_label, 'ro-')
plt.plot(x_zero, y_zero)
plt.show()