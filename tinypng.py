# encoding=utf-8
'''
此脚本用来压缩项目中的图片文件，工具使用tinypng，使用中请注意以下几点：
1. tinify.key 请到 tinypng 官网自行注册并替换，本key不一定可用
2. 本脚本功能很简单，用作个人平时使用，尽量简单使用即可，Bug本人不负责修理。
'''
import tinify
import os
import sys

tinify.key = "GYxI6r3XnvHhmDMgllpjivPrlnYAFIg5"

def compress(path):
  abs_path = os.path.abspath(path)
  # 压缩文件
  if os.path.isfile(abs_path):
    compress_file(abs_path)
    return 

  # 压缩文件夹
  print "\n",">>"*40
  print "当前输入为文件夹:",abs_path
  files = os.listdir(abs_path)
  for (n, f) in enumerate(files):
    print "%s:%s"%(n, f)

  print "\n输入(a) -> 压缩当前文件夹下所有图片文件;\n"\
    "输入(b) -> 回到上一级目录;\n"\
    "输入(q) -> 退出;\n"\
    "输入索引(0,1,2...) -> 继续选择文件夹,或选择要压缩的文件;\n"
  choose = raw_input("请输入:")
  if choose == "a":
    files = os.listdir(abs_path)
    for filename in files:
      compress_file(abs_path+"/"+filename)
    exit()
  elif choose == "b":
    parent_dir = os.path.dirname(abs_path)
    compress(parent_dir)
  elif choose == "q":
    exit()
  else:
    if choose == '':
      exit()
    selected_file = abs_path+"/"+files[int(choose)]
    print "选中:", selected_file
    compress(selected_file)

def compress_dir(abs_dir_path):
  files = os.listdir(dir_path)
  for file_name in files:
    abs_file_path = os.path.abspath(file_name)
    compress_file(abs_file_path)

def compress_file(abs_file_path):
  fileName, fileSuffix = os.path.splitext(abs_file_path)
  dirName  = os.path.dirname(abs_file_path)
  fileBaseName = os.path.basename(abs_file_path)
  if not (fileSuffix==".png" or fileSuffix==".jpg" or fileSuffix == ".jepg"):
    return
  print "开始压缩:", abs_file_path
  os.path.join(dirName, fileBaseName)
  source = tinify.from_file(abs_file_path)
  source.to_file(abs_file_path)
  print "压缩结束，保存到:", abs_file_path


if __name__ == "__main__":
  if len(sys.argv) <= 2:
    input_dir = raw_input("请输入文件夹或文件名(例如：images, joy.png, 支持绝对路径和相对路径)\n:")
  else:
    input_dir = sys.argv[1]
  compress(input_dir)
