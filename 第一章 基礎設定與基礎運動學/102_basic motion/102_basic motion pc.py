from vpython import *

l = 1
size = 0.1
v = 0
a = 0.1
t = 0
dt = 0.01

scene = canvas (title = 'v=t的等加速度運動', center = vec(0,0,0), width = 800, height = 800, background = vec(0,1,0), x=0, y=0)
floor = box(pos= vec(0,0,0), size = vec(l, 0.1*size, l), color = color.red)
thing = box(pos = vec(size*0.5-l*0.5, 0.55*size, 0), color = color.purple, size = vec(size, size, size))

gy1 = graph (title = 'x-t圖', x=600, y=0, width = 600, height = 400, xtitle = 't(s)', ytitle = 'x(m)')
gy2 = graph (title = 'v-t圖', x=600, y=-400, width = 600, height = 400, xtitle = 't(s)', ytitle = 'v(m/s)')

xline = gcurve(graph = gy1, color = color.red)
vline = gcurve(graph = gy2, color = color.red)


while thing.pos.x <= 0.5*l-0.5*size:
    rate(100)
    v = a*t
    thing.pos.x += v*dt
    t += dt

    xline.plot(thing.pos.x, t)
    vline.plot(v, t)
