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
collapse = 0
#其中g 是重力加速度，l 是地板寬＋長度，collapse 是碰撞次數，其他你們應看的懂

'''
2. 畫面
'''
scene = canvas(center = vec(0,0,0), title = "free falling", width = 1200, height = 800, background = vec(1, 0, 0))
floor = box(pos = vec(0,0,0), size = vec(l, l, 0.1*radius), color = color.blue)
ball = sphere(pos = vec(0,0,10.0), radius = radius, color = vec(0.5,0.5,0.5))


yplot = graph(title = "y-t plot", xtitle = "t", ytitle = "y", x = 0, y = 800, width = 800, height = 600)
vplot = graph(title = "v-t polt", xtitle = "t", ytitle = "v", x = 0, y = 800, width = 800, height = 600)
g1 = gcurve(graph = yplot, color = color.red)
g2 = gcurve(graph = vplot, color = color.red)


'''
 3. 物體運動部分
'''
while ball.pos.z >= 0.5*floor.size.z+radius:
    t += dt
    v += g*dt
    ball.pos.z += v*dt
    g1.plot(pos=(t, ball.pos.z))
    g2.plot(pos = (t, v))

print ("t = ", t)
print ("v = ", v)