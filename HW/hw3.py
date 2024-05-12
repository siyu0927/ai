# 用爬山改的,有借助chatGPT的力量
from random import uniform  #取隨機浮點數的

def objective_function(x, y, z):  #要找的目標
    return 3*x + 2*y + 5*z

def is_feasible(x, y, z):  #判斷有沒有合規則 :  x+y<=10, 2x+z<=9, y+2z<=11, x>=0, y>=0, z>=0
    return x >= 0 and y >= 0 and z >= 0 and x + y <= 10 and 2*x + z <= 9 and y + 2*z <= 11

def neighbor(x, y, z):  #取0-10之間隨機,是因為包含了限制下的所有浮點數
    new_x = max(0, min(x + uniform(-1, 1), 10)) 
    new_y = max(0, min(y + uniform(-1, 1), 10)) 
    new_z = max(0, min(z + uniform(-1, 1), 10)) 
    return new_x, new_y, new_z

def height(x, y, z):
    if is_feasible(x, y, z):
        return objective_function(x, y, z)
    else:
        return float('-inf')  #不符合的話就設成負無限大

def hill_climbing(x, y, z, height, neighbor, max_iter):
    for i in range(max_iter):
        new_x, new_y, new_z = neighbor(x, y, z)
        if height(new_x, new_y, new_z) > height(x, y, z):
            x, y, z = new_x, new_y, new_z
    return x, y, z

initial_x, initial_y, initial_z = 0, 0, 0

final_x, final_y, final_z = hill_climbing(initial_x, initial_y, initial_z, height, neighbor, max_iter=10000)

print("x =", final_x)
print("y =", final_y)
print("z =", final_z)
print("Objective Value:", objective_function(final_x, final_y, final_z))
