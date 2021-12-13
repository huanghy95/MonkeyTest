import os

def PATH(p): return os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


adb_port = "58526"

'''
@brief 初始化ADB，连接到adb_port端口
'''
def initADB():
    os.system(PATH('./kill5037.bat'))
    os.popen("adb kill-server adb")
    os.popen("adb start-server")
    os.popen("adb connect 127.0.0.1:" + adb_port)

'''
@brief 调用ADB命令
@param command 命令内容
@return 调用返回结果
'''
def callADB(command):
    command_result = ''
    command_text = 'adb %s' % command
    print(command_text)
    results = os.popen(command_text, "r")
    while 1:
        line = results.readline()
        if not line:
            break
        command_result += line
    results.close()
    return command_result
