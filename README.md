### python中执行shell命令
1.
```python
# 打印的命令执行结果 0或者1
os.system('cat /proc/cpuinfo')

# 通过 os.popen() 返回的是 file read 的对象，对其进行读取 read() 的操作可以看到执行的输出。但是无法读取程序执行的返回值
output = os.popen('cat /proc/cpuinfo')
print output.read()

# 可以获得到返回值和输出
(status, output) = commands.getstatusoutput('cat /proc/cpuinfo')
print status, output

# 使用val接收返回值 , 此为调用外部程序
val = os.system("ls -al | grep \"log\" ")

```

### 读取注册表
```python
import _winreg  
key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Explorer")  
value, type = _winreg.QueryValueEx(key, "EnableAutoTray")  
```
