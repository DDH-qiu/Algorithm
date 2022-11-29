# suitable for interpolation in all scenarios
# need to enter the starting point and end coordinates

from pylab import *

xi = int(input("please enter the starting horizontal coordinate "))
yi = int(input("please enter the starting vertical coordinate "))
# enter the starting coordinate

xe = int(input("please enter the end point of the end point "))
ye = int(input("please enter the horizontal and vertical coordinates of the end point "))
# enter the end coordinate

x = xi
y = yi
# initialize coordinates

x_zero = [xi, xe]
y_zero = [yi, ye]
x_label = [x]
y_label = [y]
# define image array

print("xi =", xi, "yi =", yi)
print("xe =", xe, "ye =", ye)
# output starting coordinates and end point coordinates

n = abs(xe-xi)+abs(ye-yi)
# calculation step
F = (xe-xi)*y+(yi-ye)*x+(xi*ye-xe*yi)
# calculating deviation

if (xe-xi) == 0 and (ye-yi) == 0:
    print("the end point is consistent with the starting point")
else:
    # while n > 0:
    #     n = n-1
    #     if xe-xi == 0:
    #         if ye-yi < 0:
    #             y = y-1
    #         else:
    #             y = y+1
    #     elif xe-xi < 0:
    #         if ye-yi < 0:
    #             if F >= 0:
    #                 y = y-1
    #             else:
    #                 x = x-1
    #         elif ye-yi == 0:
    #             x = x-1
    #         else:
    #             if F >= 0:
    #                 y = y+1
    #             else:
    #                 x = x-1
    #     else:
    #         if ye-yi < 0:
    #             if F >= 0:
    #                 x = x+1
    #             else:
    #                 y = y-1
    #         elif ye-yi == 0:
    #             x = x+1
    #         else:
    #             if F >= 0:
    #                 x = x+1
    #             else:
    #                 y = y+1

    while n > 0:
        n -= 1
        if x >= 0 and F >= 0:
            x = x+1
        elif x < 0 and F < 0:
            x = x-1
        elif (y >= 0, F < 0, x > 0) or (y >= 0, F >= 0, x < 0):
            y = y+1
        else:
            y = y-1
        x_label.append(x)
        y_label.append(y)
        F = (xe-xi)*y+(yi-ye)*x+(xi*ye-xe*yi)
        print(x, '\t', y, '\t', F, '\t', n)


# draw image
plt.plot(x_label, y_label, 'ro-')
plt.plot(x_zero, y_zero)
plt.show()
# end



