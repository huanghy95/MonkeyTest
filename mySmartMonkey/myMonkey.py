import cv2
import numpy as np
import math

from utils.adbUtils import initADB, callADB
from utils.phoneUtils import get_app_pix
from env.env import *


'''
@brief 计算两点间直线距离
@param point_a 点坐标
@param point_b 点坐标
@return distance 距离值
'''
def straight_distance(point_a, point_b):
    distance = math.sqrt((point_a[0] - point_b[0])**2 + (point_a[1] - point_b[1])**2)
    return distance

'''
@brief 点冲突检测，防止反复点击
@param p 待检查点
@param vertex 已检测点数组
@param 是否冲突
'''
def check_point(p, vertex):
    vertex_tuple = tuple(map(tuple, vertex))  # 将数组转化为元组
    for point in vertex_tuple:
        if straight_distance(point, p) <= threshold:
            return False
    return True

'''
@brief 进行epsilon-greedy随机生成测试点
@return [y, x] 生成的测试点
'''
def epsilon_greedy():
    r = np.random.rand()
    if r < eps:
        sz = rect.shape[0]
        choice = np.random.randint(0, sz, 1)[0]
        x = np.random.randint(rect[choice, 0], rect[choice, 1], 1)
        y = np.random.randint(rect[choice, 2], rect[choice, 3], 1)
    else :
        x = np.random.randint(0, size[0] - 1, 1)
        y = np.random.randint(0, size[1] - 1, 1)
    return [y[0], x[0]]

'''
@brief Digital-MonkeyTest主体逻辑
'''
def startDigitalMonkey(size):
    print(str(size))
    p_strat = np.array([0, 0])
    p_goal = np.array([size[1] - 1, size[0] - 1])
    vertex = np.vstack((p_strat, p_goal))
    '''采样并添加顶点'''
    while vertex.shape[0] < (sample_num + 2):
        p = np.array(epsilon_greedy())
        '''点碰撞检测，将合理点添加到顶点集'''
        while check_point(p, vertex) == False:
            p = np.array(epsilon_greedy())
        vertex = np.vstack((vertex, p))
        if adbFlag:
            cmdline = "-s " + device + " input tap " + str(p[0]) + " " + str(p[1])
            callADB(cmdline)
    return vertex

'''
@brief Digital-MonkeyTest主体逻辑
'''
def startDummyMonkey(size):
    print(str(size))
    p_strat = np.array([0, 0])
    p_goal = np.array([size[1] - 1, size[0] - 1])
    vertex = np.vstack((p_strat, p_goal))
    '''采样并添加顶点'''
    while vertex.shape[0] < (sample_num + 2):
        x = np.random.randint(0, size[0] - 1, 1)
        y = np.random.randint(0, size[1] - 1, 1)
        vertex = np.vstack((vertex, [y[0], x[0]]))
        if adbFlag:
            cmdline = "-s " + device + " input tap " + str(y[0]) + " " + str(x[0])
            callADB(cmdline)
    return vertex

'''
@brief 打印测试点集
'''
def plotResult(img, vertex):
    point_size = 5
    point_color = (0, 127, 0)  # BGR
    thickness = 4
    vertex_tuple = tuple(map(tuple, vertex))  # 将数组转化为元组
    for point in vertex_tuple:
        cv2.circle(img, point, point_size, point_color, thickness)
    cv2.imwrite("./result.png", img)
    cv2.imshow("map", img)  # 转为RGB显示
    cv2.waitKey()

if __name__ == '__main__':
    if adbFlag == True:
        initADB()
    if adbFlag == True:
        if testType == 0:
            vertex = startDummyMonkey(get_app_pix(device))
        if testType == 1:
            vertex = startDigitalMonkey(get_app_pix(device))
    else:
        image_path = "./1.png"
        img = cv2.imread(image_path)
        size = img.shape
        if testType == 0:
            vertex = startDummyMonkey(size)
        if testType == 1:
            vertex = startDigitalMonkey(size)
    if adbFlag == False and plotFlag == True:
        plotResult(img, vertex)
