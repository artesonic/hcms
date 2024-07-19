# -*- coding: utf-8 -*-
# Code by Artesonic
# 适用于python3.11.9
# 使用说明：
# 此文件与主程序共存
# 此文件的prestart.py文件名保留，用作特定的变量名前缀或变量名
# 通过调用函数的形式执行相关动作
# 本文件中以main_开头的全局变量，除非声明外，全部为文件所在项目所有子程序的公共变量
# 从其他程序中调用本程序的变量：
# import prestart | print(prestart.MY_VAR) 
# 或 from prestart import MY_VAR | print(MY_VAR)
# 在使用第二种方法时，导入的变量名，必须在新定义的变量前加入prestart的前缀，即：prestart_MY_VAR
import os
import json
main_work_pyfile_path=os.path.abspath(__file__)  
main_work_path = os.path.dirname(main_work_pyfile_path)  # 返回程序所在的工作目录