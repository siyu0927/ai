#借助劉爵寬同學的作業以及chatGPT以及陳鍾誠老師程式碼的力量
import numpy as np
from numpy.linalg import norm
from micrograd.engine import Value

def gradientDescendent(f, p0, h=0.01, max_loops=100000, dump_period=1000): #要優化的函數,初始點,每次更新的長度,最大次數,輸出的周期
    p = p0.copy() #防止直接修改到p0
    for i in range(max_loops):  #執行到最大次數為止
        fp = f(p) #算出在f函數中p位子的值
        fp.backward() #微分
        gp = [x.grad for x in p] #梯度
        glen = norm(gp)  #梯度的長度
        if i % dump_period == 0: #印出資料
            print('{:05d}:f(p)={:.3f} p={:s} gp={:s} glen={:.5f}'.format(i, fp.data, str([x.data for x in p]), str(gp), glen))
        if glen < 0.00001:  #步伐很小就停止
            break
        gh = np.multiply(gp, -1 * h) #計算梯度的反方向乘以學習率
        p = [x + gh[i] for i, x in enumerate(p)]  #每個變量減去對應的更新向量分量
        for x in p: #重製梯度
            x.grad = 0  
    print('{:05d}:f(p)={:.3f} p={:s} gp={:s} glen={:.5f}'.format(i, fp.data, str([x.data for x in p]), str(gp), glen)) #印出最後結果
    return p  

def f(p): #目標函數
    [x, y, z] = p
    return (x-1)**2+(y-2)**2+(z-3)**2

p = [Value(0), Value(0), Value(0)]
gradientDescendent(f, p)
