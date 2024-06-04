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
# 這裡的sphere是指「球體」，其中參數「radius」是球的半徑

yplot = graph(title = "y-t plot", xtitle = "t(s)", ytitle = "y(m)", x = 0, y = 800, width = 800, height = 600)
vplot = graph(title = "v-t polt", xtitle = "t(s)", ytitle = "v(m/s)", x = 0, y = 800, width = 800, height = 600)
g1 = gcurve(graph = yplot, color = color.red)
g2 = gcurve(graph = vplot, color = color.red)
#上面的在102_basic motion cm都有提過了

'''
 3. 物體運動部分, 碰撞次數到達20次即停止
'''
while collapse <= 20:
#這裡的條件是：當「碰撞次數」<=20次之後，即停止迴圈
    rate(100)
    t += dt
    v += g*dt
    ball.pos.z += v*dt
    g1.plot(pos=(t, ball.pos.z))
    g2.plot(pos = (t, v))

    if ball.pos.z <= 0.5*floor.size.z+radius:
        ball.pos.z = 0.5*floor.size.z+radius
        #由於v*dt可能會使球體的z<0.5*floor.size.z+radius
        #因此我們會需要在每一次碰撞後把再出發點校正回 y=0
        #可以參考103_free falling em1，看看球落地後的情況；或是103_free falling em2，看看不加這一行的下場
        v = -v
        #這裡我們假設完全彈性碰撞
        collapse += 1

print ("t = ", t)
print ("v = ", v)
