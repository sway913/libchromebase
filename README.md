# 剪切chromium的基础库

这份源码都来自于chromium项目，这个伟大的项目提供了chrome浏览器、chrome OS并且在安卓8.0以上的系统中的组件：
libchrome。该项目是跨平台的：因为chrome浏览器本身就是跨平台的。那么其中的base库也就是跨平台的了。这里剪切了
其中的base库，并且作为基础组件供大家使用。使用需要遵守google的chromium的许可。提供的组件有（仅列出部分）：
线程池、任务调度、定时器、文件系统、文件操作、日志、base64、OS系统信息、时间库、调试库、json、进程通信等等。

# 如何使用

1. 下载源码，使用CMake生成工程，注意因为chromium包含build目录，所以cmake工程不能指定为build目录
2. 使用IDE编辑器打开
3. 编译simpleStackTrace
4. 运行示例程序simpleStackTrace

# 关于更新到chromium最新版

改库的原始代码地址(libchrome)[https://android.googlesource.com/platform/external/libchrome]  有需要自己自己合并更新
