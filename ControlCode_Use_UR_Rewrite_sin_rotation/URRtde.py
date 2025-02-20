# 主要功能是控制机器人进行运动控制。
# 程序中使用了yaml模块读取配置文件，rtde_control控制机器人的移动和姿态控制，rtde_io控制机器人的数字输入输出，rtde_receive接收来自机器人的实时数据。
# FTReading模块用于读取机器人的力矩传感器数据。
# 该程序中定义了URControl类，其中包含机器人的IP地址、连接控制器、接收器、IO接口和力矩传感器读取接口等。get_robot()函数用于返回机器人本身，方便其他程序调用。
# Created by Jie Yu
import yaml
import rtde_control
import rtde_io
import rtde_receive
# import FTReading



class URControl:
    def __init__(self):
        IP = '192.168.1.10'
        self.control_c = rtde_control.RTDEControlInterface(IP)
        self.receive_r = rtde_receive.RTDEReceiveInterface(IP)
        self.io_control = rtde_io.RTDEIOInterface(IP)
        return

    def get_robot(self):
        return self

# class RobotClient(object):
#     def __init__(self):
#         self.robot = URControl().get_robot()

# if __name__ == "__main__":
#     self = RobotClient()