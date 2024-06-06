from vpython import *

'''
1. 基礎參數設定
'''
g = -9.8
radius = 0.1
l = 1
t = 0
v = 0
dt = 0.01
b = 1
a = 0

'''
2. 畫面
'''
scene = canvas(center = vec(0,0,0), title = "free falling", width = 1200, height = 800, background = vec(1, 0, 0))
floor = box(pos = vec(0,0,0), size = vec(l, l, 0.1*radius), color = color.blue)
ball = sphere(pos = vec(0,0,40.0), radius = radius, color = vec(0.5,0.5,0.5))
# 這裡的sphere是指「球體」，其中參數「radius」是球的半徑

yplot = graph(title = "y-t plot", xtitle = "t(s)", ytitle = "y(m)", x = 0, y = 800, width = 800, height = 600)
vplot = graph(title = "v-t polt", xtitle = "t(s)", ytitle = "v(m/s)", x = 0, y = 800, width = 800, height = 600)
g1 = gcurve(graph = yplot, color = color.red)
g2 = gcurve(graph = vplot, color = color.red)
#上面的在102_basic motion cm都有提過了

'''
 3. 物體運動部分, 碰撞次數到達20次即停止
'''
while ball.pos.z >= (0.5*floor.size.z + radius):

    rate(100)
    t += dt
    a = g - b*v
    v += a*dt
    ball.pos.z += v*dt
    g1.plot(pos=(t, ball.pos.z))
    g2.plot(pos = (t, v))

print ("t = ", t)
print ("v = ", v)
