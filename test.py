#!/usr/bin/python
# -*- coding: UTF-8 -*-

# print("hello 静妃 2")
# print "aa","bb"

# if True:
# 	print "true"
# else:
# 	print "false"

# istrue = 2
# if istrue == 1:
# 	print "true";
# 	print "true2"
# elif istrue == 2: 
# 	print "false"

# print """hah
# hahhh"""

# print '"aa"'

'''
注释
duo hang的
'''

# name = "jingfei"
# print name[2]
# print name[2:5]
# print name[-2:]

# nameList = ['aa','bb','cc','dd','ee']
# print nameList[2]
# print nameList[2:]

# print not 520
# print 2 in [3,4,2,1]
# print 2 not in [3,4,2,1]
# print 0 or 2
# print 2 and 1

# fruits=['apple','banana','strawberry']
# for index in range(len(fruits)):
# 	print fruits[index]
# else:
# 	print "end"

# import math
# print abs(-3)
# print float(3)

# import random
# print random.choice([1,2,3,4,5])

# print "aabbacc".count("a")
# print "aabbeacc".find("e")
# print "abcbdbe".split("b")

# for x in [2,4,1]:
# 	print x

# 元组不能修改，功能跟list类似
# tup=(3,2,5)
# print tup[1]

# dic={"a":22,"b":33}
# print dic["a"]

# import time
# print time.time()
# print time.localtime(time.time())
# print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
# import calendar
# print calendar.month(2019,2)
# import datetime
# print datetime.datetime.now()

# def addnum(a,b):
# 	return a+b

# print addnum(3,5)

# import mymodule
# print mymodule.sum(5,4)
# print dir(mymodule)

# from modules.test1 import sum1
# print sum1(3,2)

# fo = open("./file.txt","r+")
# print fo.name
# print fo.read()
# fo.close()

import re
line = "Cats are smarter than dogs"
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
if matchObj:
   print "matchObj.group() : ", matchObj.group()
   print "matchObj.group(1) : ", matchObj.group(1)
   print "matchObj.group(2) : ", matchObj.group(2)
else:
   print "No match!!"

print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())         # 不在起始位置匹配