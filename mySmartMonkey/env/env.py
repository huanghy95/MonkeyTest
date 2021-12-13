import numpy as np

device = "127.0.0.1:58526"
'''冲突检测的距离阈值'''
threshold = 10.0
'''epsilon-greedy的阈值参数'''
eps = 0.5
'''测试点数量'''
sample_num = 150
'''关心的区域'''
rect = np.matrix('440, 500, 720, 1000 ; 530, 590, 720, 1000 ; 555, 600, 20, 345 ; 435, 505, 20, 150')

'''是否开启Debug模式'''
DebugFlag = 0

'''是否开启ADB连接'''
adbFlag = 0

'''是否打印结果图像'''
plotFlag = 1

'''测试类型（0：Dummy；1：Digital）'''
testType = 1