# -*- coding: utf-8 -*-
# HCMS-0.0.2;Code by Artesonic
# 适用于python3.8.9;3.11.9
import os
import opencc
import configdeal # 处理config.txt文件的configdeal.py文件

main_work_pyfile_path=os.path.abspath(__file__)  
main_work_path = os.path.dirname(main_work_pyfile_path)  # 返回工作目录
# converter = opencc.OpenCC('s2t.json')
# converter.convert('汉字')  # 漢字
# converter.convert('漢字')  # 汉字
print("欢迎使用繁简字转换程序，本程序的核心功能由opencc(Open Chinese Convert:https://github.com/BYVoid/OpenCC)提供")
print("请选择工作模式（输入字母或数字）：")
print("1. 个别繁简字互转")
print("2. txt文件批量繁简字互转")
print("a. 简转繁")
print("b. 繁转简")
print('c.采用config.txt中的配置文件(打开config.txt,查看配置文件中的使用说明，按照说明选择合适的参数)')
# print("c. 简体>>台体"
# print("d. 繁体>>和制汉字")

key_input = input("请输入模式代码")
def inputchr() :
    global input_file,c1,input_str
    if '1' in key_input:
        input_str = input("请输入要转换的字")
        c1=1
    elif '2' in key_input:
        input_file = input("请拖入转换的txt文件")
        c1=2
    else:
        print("输入错误，请关闭本窗口重新启动程序")
        
def outputchr():
    global input_cmd
    if 'a' in key_input:
        input_cmd= 'opencc.OpenCC("s2t.json").convert(input_str)'
    if 'b' in key_input:
        input_cmd= 'opencc.OpenCC("t2s.json").convert(input_str)'
    if 'c' in key_input:
        file_path=main_work_path+'\config.txt'
        input_cmd_con = configdeal.read_file_ignore_comments(file_path)
        input_cmd= f'opencc.OpenCC("{input_cmd_con}.json").convert(input_str)'
            
    else:
        print("输入错误，请关闭本窗口重新启动程序")

inputchr()
outputchr()
def chr_to_unicode():
    chr_to_unicode_list = []
    for char in input_str:
        chr_to_unicode=f"\\U{ord(char):08X}"
        chr_to_unicode_list.append(chr_to_unicode)
    return chr_to_unicode_list
# utf8_bytes_list = list(utf8_bytes_list)  
if c1==1:
   print("输入的字符为：",input_str)
   output_str=str(eval(input_cmd))
   print(input_cmd)
   print('转换后的字符为：',output_str)
   print('它们的unicode编码为：',chr_to_unicode(),"\n")
if c1==2:
    with open(f'{input_file}','r',encoding='utf-8') as f:
        input_str = f.read()
        output_str=eval(input_cmd)
        f.close()
    main_work_pyfile_path=os.path.abspath(__file__)  
    main_work_path = os.path.dirname(main_work_pyfile_path)  # 返回工作目录
    with open(f'{main_work_path}\output.txt', 'w', encoding='utf-8') as file:  
    # 写入一些内容到文件  
        file.write(f'{output_str}\n')  
        file.close()
        
   



