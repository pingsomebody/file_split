# file_split
Solve wechat sending file size

  今天不知道怎么了，突然想到某盘会和谐资源，然后就想到了加密文件，想自己简单的实现一下加密文件，结果发现只能加密的文件大小，最多就是可支配内存的一半，我无法接受，就萌生了另一种想法，使用了分割的办法，实现了可以加密可支配内存少1G。
  
  分割的时候想到微信只能传输1G的文件传不了大文件，就顺便简单的做了两个，一个用于分割，一个用于合并，这样就可以传输了，发现刚好1G还是没法用微信传输，就设置了1023M，成功传输，虽然现在应该早就有很多软件可以实现文件分割，不过就当作是学习了吧！
  
  encrypt使用方法：创建一个新的文件夹，把要加密的文件和encrypt.exe程序放在同一个目录里，直接运行，需要变回来就再运行一次。里面不要有文件夹（有的话打包成压缩包再加密），有要加密exe文件会提示你输入本程序的名称（encrypt.exe）按回车继续。
  
  分割程序，用于微信传不了大文件，将其进行分割。
  
  拆合文件程序用法：将大文件和分割程序.exe放在同一个目录里，运行程序，输入大文件的名称（大文件至少要大于1G），回车继续，将会自动分割成若干个tmp文件。
  
  合并文件程序用法：运行程序，输入合并之后文件的名字，就会自动将若干个tmp文件合成并且顺便删掉tmp文件。
  
  如果非要想用python运行的看encrypt的51-55行代码，代码写的不好，有更好的改进意见或其他可以邮箱联系2909303574@qq.com
  
  声明：这项目已被王多鱼投了！！！
