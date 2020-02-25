### 环境准备
- tenforflow
- python3.5.x
>tensorflow环境搭建查看[官方文档](https://www.tensorflow.org/install/)， 建议使用gpu版本， 以下所有脚本都以项目根目录为相对目录编写

### 训练数据
- [百度云下载](https://pan.baidu.com/s/17D59O0JGMfWnligBGCHSaA) 密码：`ugh5` 包含[百鬼夜行, 结界突破]两个副本的界面分类图片
- 下载后放到项目根目录的`images`目录下(压缩文件应该自带了images文件夹了)。
- 双击`train.bat` 训练(其实系统的可里直接执行里边的命令)

>已经是2017年的数据了，建议重新截图

### 阴阳师测试环境搭建
- 下载Mumu模拟器[用默认的1280*720的分辨率]
- 安装阴阳师
- 在`config.py`配置ADB的位置
- 在`config.py`配置Mumu模拟器共享文件夹的位置， 在般在`EmulatorShell`下的`products`文件夹下创建一个`yys`的目录，这么做的目的是减少文件在传输上的时间(使用`adb pull file`会有一秒左右的传输时间)， 加快对界面预测效率。

### 测试训练的效果
- 进入阴阳师， 点开`町中` 或 进入探索里边的 `结界突破-阴阳寮`
- 在终端执行`python yys_start.py`(确保python使用的是3.5.x， 与2.7共存时运行`python3 yys_start.py`)
- 观察终端里界面预测的情况， 界面会自动执行一些操作。
