import os
import datetime
import numpy as np
import time
import config

ADB_PATH = config.ADB_PATH
EMULATOR = config.EMULATOR
POINTS = {
    'choosekingofghosts': '300 405,650 425,990 420',
    'enterthenightofghosts': '966 534',
    'exorcism': '300 405,650 425,990 420',
    'victories': '1185 620',
    'yysstreet': '904 175',
    'btchoosegroup':'300 185,300 380,300 550',
    'btchooseperson': '650 190,738 286,1015 185,1060 287',
    'btwin':'648 360',
    'btreward':'648 360',
    'btready':'1166 554'
}
Labels = {
    'choosekingofghosts': '百鬼夜行-选择式神界面',
    'enterthenightofghosts': '百鬼夜行-进入百鬼游行界面',
    'exorcism': '百鬼夜行-百鬼游行界面',
    'victories': '百鬼夜行-获得式神界面',
    'yysstreet': '町中',
    'btchoosegroup': '结界突破-选择阴阳寮',
    'btchooseperson': '结界突然-选择人',
    'btwin': '结界突破-胜利',
    'btreward': '结界突破-奖励',
    'btready': '结界突破-准备',
    'btfighting': '结界突破-战斗'
}
bt_chooseperson_count = 0

def connect_adb():
    os.system('%s %s %s' % (ADB_PATH, 'connect', config.ADB_HOST))


def show_devices():
    os.system('%s %s' % (ADB_PATH, 'devices'))


def tap(point):
    os.system('%s -s %s %s %s' % (ADB_PATH, EMULATOR, 'shell input tap', point))


def click(classes):
    if classes not in POINTS.keys():
        return
    points = POINTS[classes]
    plist = points.split(",")
    if classes == 'choosekingofghosts':# 选择式神
        p = plist[np.random.randint(0,3)]
        tap(p)
        time.sleep(0.1)
        tap('1185 620')
        return
    if classes == 'exorcism': # 百鬼夜行
        tap(plist[0])
        time.sleep(0.1)
        tap(plist[1])
        time.sleep(0.1)
        tap(plist[2])
        time.sleep(0.1)
        return
    if classes == 'victories': # 获得式神界面
        tap(plist[0])
        time.sleep(1)
        return
    if classes == 'btchoosegroup':# 结界突破-选择阴阳寮
        p = plist
        tap(p)
        return
    if classes == 'btchooseperson': #结界突然-选择人
        groupp = POINTS['btchoosegroup'].split(",")[np.random.randint(0,3)]
        tap(groupp)
        ri = np.random.randint(0,2)
        if ri == 0:
            p1 = plist[0]
            p2 = plist[1]
            tap(p1)
            time.sleep(0.2)
            tap(p2)
        else:
            p1 = plist[2]
            p2 = plist[3]
            tap(p1)
            time.sleep(0.2)
            tap(p2)
        return
    for p in plist:
        tap(p)


def cap():
    date = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    os.system('%s -s %s %s /mnt/shared/products/yys/%s.png' % (ADB_PATH, EMULATOR, 'shell screencap -p', date))
    image = '%s/%s.png' %(config.MUMU_SHARED, date)
    return image


def random():
    print()
