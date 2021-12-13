# MonkeyTest
#### 一、简介

本仓库为中山大学2021秋季学期移动互联网编程期末项目`Monkey Test`的代码部分

以下是作业要求：

> 课程中已经介绍了Monkey测试的基本概念，本次作业即进一步调研Monkey测试的实现方案并进行实践操作。
>
> - 进一步学习Monkey测试的基础知识，调研Monkey测试的技术方案
> - 实现Monkey测试的基本过程
> - 常规的Monkey测试存在着若干问题，比如遍历界面有限，路径回环等。请调研基础Monkey测试的具体缺陷以及更智能的Monkey测试的思路与方法。
> - 实现智能Monkey测试
> - 设备平台：安卓、iOS（二选一）
> - 目标应用：游戏、普通移动应用（任选一款）
> - 作业产出：
>   - 实验报告：包括调研的基础知识，实验的环境条件、详细过程和测试效果等。结构自行组织，目的是能让阅读者能轻松获取到你想传递的信息。
>   - 若使用到了一些三方工具，请在报告中说清楚该工具包的基本信息及使用流程等
>   - 若进行了一些二次开发，请附上源代码，并在报告中说清楚使用方法



#### 二、目录树

```c++
├─monkeyTestBasedonLouis // 基于`Louis-monkeyTest`的dummy monkeytest+监控
│  ├─Base
│  │  └─__pycache__
│  ├─info
│  └─log
└─mySmartMonkey // 自己实现的SmartMonkeyTest
    ├─env // 环境变量
    │  └─__pycache__
    ├─myMonkey.py // entry
    └─utils // 工具api
        └─__pycache__
```



#### 三、运行与测试

##### 3.1 monkeyTestBasedonLouis

首先配置`monkey.ini`文件，指定测试程序、测试指令和网络环境

```ini
[DEFAULT]
cmd=monkey -p com.eivaagames.RealChess3D.dbzq.m --throttle 500 --ignore-timeouts --ignore-crashes   --monitor-native-crashes -v -v -v 5 >
package_name=com.eivaagames.RealChess3D.dbzq.m
activity = com.baiji.jianshu.account.SplashScreenActivity
net = wifi
```

要求命令行要有`adb`工具，并连接好安卓设备，可通过执行`adb devices`确认

确保环境正常后，直接运行`monkeyTest.py`：

```bash
python3 monkeyTest.py
```



##### 3.2 mySmartMonkey

首先配置`/env/env.py`中的参数，比较关键的参数为：

```yaml
device = "127.0.0.1:58526"

'''是否开启ADB连接'''
adbFlag = 0

'''是否打印结果图像'''
plotFlag = 1

'''测试类型（0：Dummy；1：Digital）'''
testType = 1
```

若开启`plotFlag`，则要有`cv2`环境

准备好环境后，直接运行入口py即可：

```bash
python3 myMonkey.py
```

