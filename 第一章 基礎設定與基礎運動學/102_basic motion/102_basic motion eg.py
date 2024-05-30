from vpython import *
#上面那一行的目的是「引入」vpython 這個函式庫，就是一個標準用法，把他背起來就好

'''
1. 基礎參數設定
'''
size = 0.1
L = 1
v = 0.03
t = 0
dt = 0.01
#以上為吾人自行設定的參數，我習慣一開始就把參數寫在上面，給他一個專屬區域。
#其中size 是箱子的大小，L 是地板長度，其他你們應看的懂

'''
2. 畫面
'''

scene = canvas(title = "1D same velocity motion", width = 800, height = 600, x = 0, y = 0, center = vec(0,0,0), background = vec(0.2, 0.4, 0.8))
# 這裡的scene 指的是背景。而canvas則是vpython程式庫裡面定義的一個「物件」。你在設定一個vpyhton的模擬時，一定要加入這個canva，不然世界將會一片空虛

floor = box(pos=vec(0,0,0), size = vec(L, 0.1*size, L))
# floor 和上述的scene有點類似，都是屬於vpyhton內建的場景部分。而box則是另一個物件，在 「some object function」都有詳提

cube = box(pos = vec(-0.5*L+0.5*size, 0.55*size, 0), size = vec(size, size, size), color = color.blue)

gd = graph(title = 'x-t plot', width = 600, height = 450, x = 0, y = 600, xtitle= "t(s)", ytitle='v(m/s)')
gd2 = graph(title="v-t plot", width=600, height=450, x=0, y=1050, xtitle="t(s)", ytitle="v(m/s)")
# 這裡的graph 指的是「圖表」，在「some useful function」中有詳提

xt = gcurve(graph=gd, color=color.red)
vt = gcurve(graph=gd2, color=color.red)
# 這裡的gcurve 指的是「會出現在圖表裡面的線」，在「some useful function」中有詳提

'''
這裡補一個小細節，我在剛學的時候超級無敵搞不懂的地方：請問scene, cube這些名字我可以亂改嗎？
答案是可以的，因為這些名字都是那個物體的「名稱」。也可以把他們想成儲存「圖形資料」的變數
而物體今天真正出現在畫面上的原因是因為：你今天只要建立了一個儲存圖形的變數，那麼圖形就會同時出現在畫面之中，無需額外的函數等等
'''

'''
 3. 物體運動部分, 木塊到達地板邊緣時停止執行
'''
while cube.pos.x <= 0.5*L - 0.5*size:
    rate(1000)
    # 這裡的rate 指的是「一秒會跑幾次迴圈」，1000算是相當夠了。但太快的話就很就跑完了。如果你想要現實生活中的一秒=模擬器裡的一秒，可以令rate = 1/dt

    cube.pos.x += v*dt
    xt.plot(pos=(t, cube.pos.x))
    vt.plot(pos=(t, v))
    #這裡的plot指的是gcurve這個物體執行「畫線」的這個動作

    t += dt


print("t = ", t)