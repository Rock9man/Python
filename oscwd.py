#!/usr/bin/python
# -*- coding:UTF-8 -*-

import os, sys

# 切换到“/home/wj"目录
os.chdir("/home/wj/Test")

# 打印当前工作目录
print "当前工作目录：%s" % os.getcwd()

# 打开 ”/text.txt"
fd = os.open("../",os.O_RDONLY)

# 使用os.fchdir() 方法修改目录
os.fchdir(fd)

# 打印当前目录
print "当前工作目录：%s" % os.getcwd()

#关闭文件
os.close(fd)

