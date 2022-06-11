import os,time,sys
start = time.time()

def del_tmp(): # 删除分割的文件
    print("删除分割的文件ing")
    names = os.listdir()
    [os.remove(i) for i in names if i.split('.')[1] == "tmp"]
    print("删除分割的文件已完成！")

def file_marge(rawfile):
    names = os.listdir()
    if rawfile in names:
        print("已存在相同名字的文件！无法创建！")
        input("回车退出")
        sys.exit()
    print("合并文件ing")
    tmp = len([i for i in names if i.split('.')[1] == "tmp"]) # 找到所有tmp文件
    with open(rawfile,'wb+') as f:
        for i in range(1,tmp+1):
            with open(str(i)+".tmp",'rb+') as t:
                f.write(t.read()[::-1])
    print("合并文件已完成！")
    del_tmp()

print("程序和文件要放在同一目录")
file_marge(input("合并后的文件名称（带后缀名）："))
print(f"cost time:{time.time-start}")
input("回车退出")