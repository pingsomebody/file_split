import os, time, sys

start = time.time()

G = 1073741824  # 一个G的二进制2^30


def file_split(rawfile):  # 反转后分割N+1个G
    filesize = os.path.getsize(rawfile)
    NG = filesize // G + 1
    print(f"{rawfile}文件过大！分割文件ing")
    with open(rawfile, 'rb+') as f:
        bin = f.read()
        for i in range(1, NG + 1):
            with open(str(i) + ".tmp", 'wb+') as tmp:
                if i != NG + 1:
                    tmp.write(bin[(i - 1) * G:i * G])
                else:
                    tmp.write(bin[(i - 1) * G:])
    print("分割完成！")


def del_tmp():  # 删除分割的文件
    print("删除分割的文件ing")
    names = os.listdir()
    [os.remove(i) for i in names if i.split('.')[1] == "tmp"]
    print("删除分割的文件已完成！")


def file_marge(rawfile): # 合并文件
    names = os.listdir()
    os.remove(rawfile)  # 先删掉源文件，再新建一个一样的文件名写入
    print("加密并合并的文件ing")
    tmp = len([i for i in names if i.split('.')[1] == "tmp"])  # 找到所有tmp文件
    with open(rawfile, 'wb+') as f:
        for i in range(1, tmp + 1):  # 合并文件内容给data变量
            with open(str(i) + ".tmp", 'rb+') as t:
                f.write(t.read()[::-1]) # 将其内容取反作为加密算法
    print("加密并合并文件已完成！")
    del_tmp()


def encrypt(rawfile): # 小文件直接加密
    with open(rawfile, "rb+") as f:
        bin = f.read()[::-1]
        f.seek(0)
        f.write(bin)


filenames = os.listdir()  # 获取当前目录所有名字
# curr_filename = os.path.basename(__file__) # 获取程序自己的文件名，
# 打包成exe程序后必面的名字必然是exe,如果有多个exe文件就要求使用者输入当前程序名字，避免连程序自己都被加密了
"""
如果想用python运行，将init到break加注释，把51行的注释去掉
"""
init = 0
for i in filenames:
    if i.split(".")[1] == "exe":
        curr_filename = i
        init += 1
        if init == 2:
            curr_filename = input("检测有其他的exe程序，为避免本程序也被加密，请输入完整的程序名称（带后缀名）：")
            break

for rawfile in filenames:  # 循环文件夹里的文件循环每一个文件进行操作
    if rawfile != curr_filename:  # 判断如果不是程序本身这个文件
        if os.path.getsize(rawfile) > G * 2:  # 如果文件大于2G进行特殊处理
            file_split(rawfile)
            file_marge(rawfile)
        else:
            print(f"{rawfile}文件小于2G直接加密")
            encrypt(rawfile)
print("全部已加密完成！")
print(f"cost time:{time.time() - start}")
input("回车退出")
