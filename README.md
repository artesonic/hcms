# Chinese Convert Based on OpenCC
中文繁简转换/汉字繁简转换 | Chinese Convert between Traditional Chinese and Simplified Chinese,Based on OpenCC
## 

# 本程序的核心功能依赖于[OpenCC](https://github.com/BYVoid/OpenCC)

<p><br><br></p>

## 已经实现的功能
- 中文简体与繁体之间的互相转换
- 臺灣正體、香港繁體、日文新字體等之间的转换（详细参见config.txt）
- txt文件批量转换

<p><br><br></p>

## 使用说明
- 经测试，本程序可以在Windows10的python3.11.9版本上正常运行。关于其他版本及平台的运行情况，欢迎在issues反馈。
- opencc推荐使用的版本为1.1.7
#### 安装依赖 | Install
- opencc-1.1.7
```python  
pip install opencc
```
### 开始运行
#### 打开命令提示符
输入`python hcms.py`

#### 按照程序提示输入操作码
```
....
请选择工作模式（输入字母或数字）：
1. 个别繁简字互转
2. txt文件批量繁简字互转
a. 简转繁
b. 繁转简
c.采用config.txt中的配置文件....
....
```



### 关于如何使用配置文件

#### 打开```config.txt```，按照提示修改其中的参数
```
....
# s2t.json Simplified Chinese to Traditional Chinese 簡體到繁體
# t2s.json Traditional Chinese to Simplified Chinese 繁體到簡體
# s2tw.json Simplified Chinese to Traditional Chinese (Taiwan Standard) 簡體到臺灣正體
# tw2s.json Traditional Chinese (Taiwan Standard) to Simplified Chinese 臺灣正體到簡體
# s2hk.json Simplified Chinese to Traditional Chinese (Hong Kong variant) 簡體到香港繁體
# hk2s.json Traditional Chinese (Hong Kong variant) to Simplified Chinese 香港繁體到簡體
# s2twp.json Simplified Chinese to Traditional Chinese (Taiwan Standard) with Taiwanese idiom 簡體到繁體（臺灣正體標準）並轉換爲臺灣常用詞彙
# tw2sp.json Traditional Chinese (Taiwan Standard) to Simplified Chinese with Mainland Chinese idiom 繁體（臺灣正體標準）到簡體並轉換爲中國大陸常用詞彙
# t2tw.json Traditional Chinese (OpenCC Standard) to Taiwan Standard 繁體（OpenCC 標準）到臺灣正體
# hk2t.json Traditional Chinese (Hong Kong variant) to Traditional Chinese 香港繁體到繁體（OpenCC 標準）
# t2hk.json Traditional Chinese (OpenCC Standard) to Hong Kong variant 繁體（OpenCC 標準）到香港繁體
# t2jp.json Traditional Chinese Characters (Kyūjitai) to New Japanese Kanji (Shinjitai) 繁體（OpenCC 標準，舊字體）到日文新字體
# jp2t.json New Japanese Kanji (Shinjitai) to Traditional Chinese Characters (Kyūjitai) 日文新字體到繁體（OpenCC 標準，舊字體）
# tw2t.json Traditional Chinese (Taiwan standard) to Traditional Chinese 臺灣正體到繁體（OpenCC 標準）
#
#
#
#
#
#
#
#


t2s
....
```
例如想将简体字转换为繁体字，

注意：在执行以上步骤前，请关闭转换程序.
- (1)查阅`config.txt`的说明得知参数为`s2t`
- (2)然后将原文件中`t2s`改为`s2t`，其他不变.
- (3)最后保存。正常运行程序即可实现你的需求.

如果需求改变，参照以上步骤再次修改配置文件即可.

<p><br></p>


## 许可 
Apache License 2.0

<p><br></p>

#### 
