# python
python 练习demo

- 安装pip

```
python2.7安装方法

 https://pypi.org/project/pip/#files 下载第二个，解压，然后进入目录执行python setup.py install
 然后就可以用pip安装了，命令为 python -m pip install [package name]
 比如python -m pip install mysql
 但是这样比较麻烦，安装pip后，在python/scripts下可以找到pip
 设置环境D:\Python27\Scripts到环境变量就可以直接在命令行执行pip了。
 pip -V
 pip install mysql


python3.7

安装python3.7自带pip不需要额外安装
使用代理 pip install mysql --proxy=http://ip:port

用清华的源
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pack_name[mysql]
```

=== 注意在linux下不要去卸载python27，很多软件基于python27的，安装python37后直接用python3执行指令，python指令对应是python2。pip3同理对应python3，默认pip是对应python27.必要时可以设置软连接 ln -s old new.

- linux 安装https://www.linuxidc.com/Linux/2018-07/153286.htm

- python 模块 https://blog.csdn.net/xuqi7/article/details/78757548/