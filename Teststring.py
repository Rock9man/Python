# -*- coding: utf-8 -*-
#@Author:	wangjun
#@Date:	

import os
import sys
import getpass
import shutil
import time


Sudo_Passwd=" "
TOP_Space=os.getcwd();
WorkSpace=os.path.join(TOP_Space,"WorkSpace")

def Check_Runing_Args(input_args):
	Version=""
	lcd=""
	sdsize=""
	if len(input_args) != 2:
		print "Bad input Args~!"
		Print_Help_Info()
		sys.exit(ERROR_INPUT_ARGS)

	package_name=input_args[1]
	tem=package_name[:4]
	ret=os.system('echo "%s"' % (tem))
	if ret != 0 :
		print "Umount error ,please check~!"
		sys.exit(ERROR_UMOUNT_ERROR)
	tem=package_name[4:12]
	ret=os.system('echo "%s"' % (tem))
	if ret != 0 :
		print "Umount error ,please check~!"
		sys.exit(ERROR_UMOUNT_ERROR)
	lcd=package_name[21:22]
	ret=os.system('echo "%s"' % (lcd))
	if ret != 0 :
		print "Umount error ,please check~!"
		sys.exit(ERROR_UMOUNT_ERROR)
	sdsize=package_name[23:25]
	ret=os.system('echo "%s"' % (sdsize))
	if ret != 0 :
		print "Umount error ,please check~!"
		sys.exit(ERROR_UMOUNT_ERROR)
	



if __name__ == '__main__':
	if os.path.isdir(WorkSpace):
		shutil.rmtree(WorkSpace)
		os.mkdir(WorkSpace)
	else:
		os.mkdir(WorkSpace)

	Check_Runing_Args(sys.argv)

#	Check_Runing_Args(sys.argv)

#	Check_Runing_Args(sys.argv)
	print " %s " % sys.argv[1]

	for i in range(1,5):
		print " %s " % i

