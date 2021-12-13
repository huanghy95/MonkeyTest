import subprocess 
from utils.adbUtils import callADB

'''
@brief 获取收集屏幕分辨率
@param devices 设备
@return [x, y] 分辨率
'''
def get_app_pix(device):
    cmd = "-s " + device + " shell wm size"
    callADB(cmd)
    res = subprocess.check_output(cmd).split()[2].decode()
    spix = str(res).split('x')
    return [int(spix[0]), int(spix[1])]