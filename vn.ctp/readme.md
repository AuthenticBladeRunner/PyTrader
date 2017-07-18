# vn.ctp

### 简介
CTP柜台API接口的Python封装，基于pyscript目录下的脚本自动分析头文件生成封装代码模块，提供原生C++ API中的全部功能。

由于 Python 无法直接调用 C++ dll，因此使用 [Boost.Python](http://www.boost.org/doc/libs/1_63_0/libs/python/doc/html/index.html) 对 C++ 接口进行了封装，使之可以被 Python 调用。

使用 Visual Studio 编译 boost 库（可参考 [vn.py 专栏](https://zhuanlan.zhihu.com/p/20031684) 以及 boost 自带文档）

* [下载](https://sourceforge.net/projects/boost/?source=typ_redirect) boost 源码，解压

* 在开始菜单中找到 VS2015菜单 - Visual Studio Tools - VS2015 开发人员命令提示

* 进入下载解压后的 boost 文件夹，执行 <code>bootstrap</code> 生成 b2.exe

* 执行 <code>b2 --build-type=complete address-model=64</code>编译boost库。“--build-type=complete”选项是指编译所有变体（debug版、release版、单线程、多线程版，等等），“address-model=64”是指编译64位版本的。（如果之前曾经编译过，编译之前可以用 <code>b2 clean</code> 先清理一下。）最终库文件会生成在 boost 文件夹的 stage 目录下。

* 把stage目录下的 boost_python-vc140-mt-1_63.dll 拷贝到 D:\Python35 下。

* 在 VS 2015 IDE 环境中编译链接 boost 库时，需要加入相关路径。头文件路径的设置: 项目-属性-C/C++-常规-附加包含目录，添加 D:\boost_1_63_0；库文件路径设置：项目-属性-链接器-常规-附加库目录，添加  D:\boost_1_63_0\stage\lib

* 安装CMake。使用CMake的意义在于，CMake是一个跨平台的工具，使用同一个CMakeList.txt，可以生成适用于Linux的makefile，也可以生成Visual Studio的工程文件。

* 设置环境变量：BOOST_ROOT = D:\boost_1_63_0，用于让CMake能找到boost相关路径。

* 修改本目录下的 CMakeLists.txt 中所有有关 Python 的目录

* 在本目录下新建文件夹，命名为build, 用于保存编译的临时文件及库文件

* 还是使用「VS2015 开发人员命令提示」，进入到上面的build目录下，执行 <code>cmake -G "Visual Studio 14 Win64" ..</code>生成VS工程文件。如果以后想重新生成，可以把build目录下的东西都删了，再重新执行此命令。

* [下载](http://www.sfit.com.cn/5_2_DocumentDown.htm) 64位的CTP dll。注意下载「个股期权api」那个（不同版本的dll的头文件可能有所不同，可能会造成运行问题）。把压缩包的dll, lib文件拷贝至ctpapi文件夹。

* 打开生成的.sln（VS 解决方案）文件 ~~ ，~~在该解决方案下所有项目的属性中，把字符集改为「使用 Unicode 字符集」~~ ~~ 。生成dll的两个项目的「目标文件扩展名」可以改为「.pyd」。最后点击菜单 生成-生成解决方案 生成可被python调用的库文件。

* 生成的pyd文件在build/lib/Release目录下。把生成的两个pyd文件和原始thostmduserapi.dll、thosttraderapi.dll拷贝至vn.trader\ctpGateway目录下。


有兴趣的人可尝试使用 MinGW-w64 编译 boost 库，但强烈不推荐，非常容易出错。最终我可以编译 boost-python 库，但，无法成功使用该库。（参考 [MinGW-w64 官方指导](https://sourceforge.net/p/mingw-w64/wiki2/Building%20Boost/) 和 [boost 文档](http://www.boost.org/doc/libs/1_63_0/doc/html/bbv2/tasks.html#bbv2.tasks.crosscompile)）：

* [下载](https://sourceforge.net/projects/boost/?source=typ_redirect) boost 源码，解压

* 命令行进入解压后的文件夹，执行 <code>bootstrap.bat gcc</code>

* 编译，并把库放在 <code>--prefix</code> 指定的位置（加入 <code>cxxflags="-D_hypot=hypot"</code> 是为了防止mingw gcc编译Python模块时报错）：

> <code>b2 --prefix=D:\mingw-w64\boost64 toolset=gcc cxxflags="-D_hypot=hypot" address-model=64 variant=debug,release link=static,shared threading=multi install</code>

或者加入 <code>--with-python</code> 仅编译Python相关模块:

> <code>b2 --prefix=D:\mingw-w64\boost64 --with-python toolset=gcc cxxflags="-D_hypot=hypot" address-model=64 variant=debug,release link=static,shared threading=multi install</code>

* 创建/修改环境变量，把 boost 库 和 Python 库 加入到 gcc 的 search path: 

> CPLUS_INCLUDE_PATH=D:\mingw-w64\boost64\include\boost-1_63;D:\Python35\include

> LIBRARY_PATH=D:\mingw-w64\boost64\lib;D:\Python35\libs

* 编译完后，可以看到 D:\mingw-w64\boost64\lib 文件夹下有很多库文件，其中有几个 libboost_python 开头的文件。有一个类似 libboost_python3-mgw63-mt-1_63.dll 的文件，拷贝一个，重命名为 libboost_python.dll，因为 bjam 链接的时候会使用 -lboost_python，如果不改名字会找不到库导致链接失败。

动态链接 boost 库的例子（使用 libxxx.dll)：

> <code>g++ example.cpp -lboost_regex-mgw63-mt-1_63 -o example_dynamic</code>

静态链接 boost 库的例子（使用 libxxx.a)：

> <code>g++ example.cpp -Wl,-Bstatic -lboost_regex-mgw63-mt-1_63 -o example.exe</code>

### 目录说明
* vnctpmd: 行情API
* vnctptd: 交易API
* pyscript: 自动封装脚本
* ctpapi：C++ API文件

### 使用CMake编译

**Windows 7**

环境配置:

* Anaconda和Boost的安装方式请参考www.vnpy.org上的教程，必须使用32位

* cmake:安装最新版本的cmake,用于配置编译环境

* 设置环境变量：BOOST_ROOT = C:\boost_1_57_0

* 编译工具：Visual Studio 2013


编译过程:

* 在vn.ctp目录下新建文件夹，并命名为build, 保存编译的临时文件及库文件

* 打开命令行工具输入：cmake-gui .. 则打开cmake配置界面

* 点击configure。

* 点击generate。如果没有错误则配置成功

* 进入build目录，双击vn_ctp_api.sln打开解决方案

* 点击编译按钮,建议编译release库


**Linux (Debian jessie, Ubuntu 16.04)**

环境配置：

* 参考[这里](http://www.continuum.io/downloads)的教程下载并安装Anaconda的Linux 64位版本

* 使用apt-get安装编译相关的工具，注意某些老的Ubuntu必须指定使用boost 1.58.0版本：

    - apt-get install build-essential

    - apt-get install libboost-all-dev

    - apt-get install python-dev

    - apt-get install cmake

* 如果从官网下载新的ctp api tar包，比如v6.3.5_20150803_tradeapi_linux64.tar，需要重命名ctp api so文件名（否则可以忽略该步骤）：

    - thostmduserapi.so --> libthostmduserapi.so

    - thosttraderapi.so --> libthosttraderapi.so


编译过程：

* 当前目录运行build.sh，完成编译

### API版本
日期：2015-08-04

名称：fsopt_traderapi

描述：个股期权API  

链接：[http://www.sfit.com.cn/5_2_DocumentDown.htm](http://www.sfit.com.cn/5_2_DocumentDown.htm)

说明：ctpapi文件夹下的是Windows的32位版本，其下文件夹x64_linux中的是Linux的64位版本
