#! python3
#HOStudio
#LICENSE MIT
#Version:V0.0.1

import psutil
import uuid
import socket
import os
import platform


#System
print('##########System info##########')

def get_mac_address():
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0,11,2)])

def get_host_ip():
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(('1.1.1.1',80))
        ip=s.getsockname()[0]
    finally:
        s.close()
    return ip

def get_load():
    f = open("/proc/loadavg")
    loadstate=f.read().split()
    return loadstate
load_list = get_load()[0:3]
system_load = ''
for i in load_list:
    if system_load:
        system_load = system_load+','+i
    else:
        system_load = i



myname = socket.getfqdn(socket.gethostname())
print('hostname:',myname)
print('host ip:',get_host_ip())
print('host MAC address:',get_mac_address())
print('system load(1, 5, 15):',system_load)
print('system tasks:',len(psutil.pids()))

devs = psutil.disk_partitions()
for dev in devs:
    statvfs = os.statvfs(dev.mountpoint)
devs = psutil.disk_partitions()
for dev in devs:
    statvfs = os.statvfs(dev.mountpoint)
    total_disk_space = statvfs.f_frsize * statvfs.f_blocks
    free_disk_space = statvfs.f_frsize * statvfs.f_bfree
    disk_usage = int((total_disk_space - free_disk_space) * 100.0 / total_disk_space)
    print('Mounted on equipment：%s，Mount point：%s Disk utilization:%d%%  File system:%s' % (dev.device,dev.mountpoint,disk_usage,dev.fstype))


#cpu
cts = psutil.cpu_times()
cputime = 0
for item in cts:
    if item != 0:
        cputime = cputime + item
print('##########CPU info##########')
print('user：%d%%' % (cts.user/cputime * 100))
print('kernel：%d%%' % (cts.system/cputime * 100))
print('free：%d%%' % (cts.idle/cputime * 100))
print('Number of logical CPUs:',psutil.cpu_count())
print('Number of physical CPUs:',psutil.cpu_count(logical=False))


#内存
print('##########MEM info##########')
mem = psutil.virtual_memory()
print('Memory size: %dM'%(int(mem.total/1024/1024)))
print('Used memory: %dM'%(int(mem.used/1000/1000)))
print('Remaining memory:%dM'%(int(mem.free/1024/1024)))
print('Memory utilization: %d%%'%(int(mem.percent)))

print('##########END of system info##########')
#System END
print()
#Python
print('##########Python info##########')
print('Python version: ' + platform.python_version())
print('##########END of python info##########')