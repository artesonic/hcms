# -*- coding: utf-8 -*-
# HCMS-0.0.2;Code by Artesonic
# confiigdeal.py-0.1.0;Code by Artesonic
# 适用于python3.8.9;3.11.9
# 使用说明：
# 读取文件并忽略所有以#开头的行（包括只包含#的行和空行）
# 
# 函数参数：file_path为要读取的文件的绝对路径
# 函数返回值：读取到的有效行，去除行尾的换行符；以字符串的类型返回。
# 所有不带‘#’的行为有效行，以‘#’开头的行为注释行。
# 空行和只带有制表符、换行符的行也视为无效行。
#
# ##########################################
# config.txt的格式：
# 带有‘#’的为注释行，不被读取
# 从不带有‘#’的行开始，直到文件结束为止均为有效文件
# 
# #
def read_file_ignore_comments(file_path):  # 读取文件并忽略所有以#开头的行（包括只包含#的行和空行）
    """  
    读取文件并忽略所有以#开头的行（包括只包含#的行和空行）  
      
    :param file_path: 要读取的文件的路径  
    """  
    try:  
        with open(file_path, 'r', encoding='utf-8') as file:  
            for line in file:  
                # 使用strip()去除行首和行尾的空白字符（包括空格、制表符、换行符等）  
                # 然后检查去除空白后的行是否以#开头或是否为空  
                if not line.strip().startswith('#') and line.strip():  # line.strip()判断是否为空行，后面的.startswith('#')是判断条件，符合的话返回True.not不对and后面的表达式产生作用
                    return line.strip()  # 返回有效行，去除行尾的换行符
            file.close()  
                    # print(line.strip())  # 打印有效行，去除行尾的换行符  
    except FileNotFoundError:  
        print(f"文件 {file_path} 未找到。")  
    except Exception as e:  
        print(f"读取文件时发生错误：{e}")  
  
