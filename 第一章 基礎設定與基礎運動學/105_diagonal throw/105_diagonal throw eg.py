from vpython import *

l = 100
radius = 1
g = -0.98
v = vec(10, 10, 0)
a = vec(0, g, 0)
t = 0
dt = 0.001
b = 0.1
m = 1

back = canvas(center = vec(0,0,0), background = vec(0.3,0.3,0.7), width =  800, height = 600, title = "ideal horizontal throw")
floor = box(pos = vec(0,0,0), size = vec(l,0.1*radius,0.1*l), color = vec (0.5, 0.6,0.3))
ball = sphere(radius = radius, pos = vec(-floor.size.x*0.5,floor.pos.y*0.5+radius,0), color = color.red, make_trail=True, trail_color = color.white, v = v, a = a)

x = arrow(axis = vec(1,0,0), length= 5, pos = vec(0,2,20))
z = arrow(axis = vec(0,1,0), length = 5, pos = vec(0,2,20))

xyplot = graph(title = "x-y plot", xtitle = "x(m)", ytitle = "y(m)", height = 400, width = 600)
vtplot = graph(title = "vx-t plot", xtitle = "t(s)", ytitle = "vx(m/s)", height = 400, width = 600)
vytplot = graph(title = "vy-t plot", xtitle = "t(s)", ytitle = "vy(m/s)", height = 400, width = 600)

xy = gcurve(graph = xyplot, color = color.red)
vxt = gcurve(graph = vtplot, color = color.black)
vyt = gcurve(graph = vytplot, color = color.blue)

for i in range(20):
    t += dt
    a = vec(0,g,0) - b*v
    v += a*dt
    ball.pos += v*dt

    xy.plot(ball.pos.x, ball.pos.y)
    vxt.plot(pos = (t,v.x))
    vyt.plot(pos = (t, abs(v.y)))

while ball.pos.y >= (floor.size.y*0.5 + ball.radius):
    rate(1000)
    t += dt
    a = vec(0,g,0) - b*v
    v += a*dt
    ball.pos += v*dt

    xy.plot(ball.pos.x, ball.pos.y)
    vxt.plot(pos = (t,v.x))
    vyt.plot(pos = (t, v.y))
