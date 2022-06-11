import os, time

start = time.time()

G = 2 ** 30 - 2 * 20  # 一个G的二进制2^30，减去1M因为刚好1G微信还是传不了


def file_split(filename):  # 分割文件
    filesize = os.path.getsize(filename)
    NG = filesize // G + 1
    print("分割文件ing")
    with open(filename, 'rb+') as f:
        bin = f.read()
        for i in range(1, NG + 1):
            with open(str(i) + ".tmp", 'wb+') as tmp:
                if i != NG + 1:
                    tmp.write(bin[(i - 1) * G:i * G])
                else:
                    tmp.write(bin[(i - 1) * G:])
    print("分割完成！")


print("程序和文件要放在同一目录")
file_split(input("请输入大于1G的文件名称（带后缀名）："))
print(f"cost time:{time.time - start}")
input("回车退出")
