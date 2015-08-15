# template-engine
Generate, import and export templates.

# pyinstaller
pyinstaller -F -w -n template-engine -p ./ template-engine/main_window.py

# Manual

## 整体介绍
共分为4个部分：

1、菜单栏&工具栏

2、左窗口

3、主窗口

4、右窗口

###菜单栏&工具栏

文件：打开，保存，新建，退出

动作：各种需要添加的动作（下面将详细介绍）

上传：打包文件、上传到测试&生产服务器

设置：配置一些文件

关于：啥都没写

###左窗口

左窗口的默认路径由`设置`里的路径来定义

双击选中.plist文件可以直接读入到`主窗口`

##主窗口
用于显示整个树状结构

双击某一层，相应的内容将显示在右窗口，可以在右窗口进行修改

回车某一层，将隐藏&打开该层

### 右窗口
用于显示&修改数据

### 动作
1、`Add`添加一个普通节点，每个节点有三个值`Key,Type,Value`，有一些添加规则：

1)`Type=integer`会检查`Value`是否是正确的`integer`

2)`Type=bool`会有选项选择`True&False`

3)如果该节点的父节点`Type=array`,则该节点没有`Key`这一属性,`array`下无法再加`array`

2、`Delete`删除这个节点和对应的子树

3、`AddLayer`添加一个`layer`

4、`AddSubtitle`添加一个`subtitle`,其父节点只能是`subtitles`

5、`AddTrack`添加一个`track`,其父节点只能是`segment`

6、`AddCuttoLayer`添加一个`cutto_Layers`,其父节点只能是`root`

7、`AddCutto`添加一个`cutto`,其父节点只能是`cutto_layers`

8、`AddSegments`添加一个`segments`,其父节点只能是`root`

9、`AddHead`添加一个`segment`，其父节点只能是`segments`，对应`segment`中的`head`

10、`AddNormal`添加一个`segment`,其父节点只能是`segments`,对应`segment`中的普通节点

11、`AddFoot`添加一个`segment`,其父节点只能是`segments`，对应`segment`中的`foot`

12、`addStill`添加一个`animation`，其父节点只能是`adnimations`,对应`still`

13、`addScale`添加一个`animation`，其父节点只能是`adnimations`,对应`scale`

14、`addRotate`添加一个`animation`，其父节点只能是`adnimations`,对应`rotate`

15、`addOpacity`添加一个`animation`，其父节点只能是`adnimations`,对应`opacity`

16、`addStraightline`添加一个`animation`，其父节点只能是`adnimations`,对应`straightline`

### 一些联动操作

1、修改`segment`层的`starttime&duration`整个`segment`下的`starttime&duration`都会改变

2、修改`straightline中values`的最后一个值，则上一层的`position`发生改变

3、修改`scale中values`的最后一个值，则上一层的`scale`发生改变

4、修改`opacity中values`的最后一个值，则上一层的`opacity`发生改变

5、`animation`里的`times`的默认值，默认读入4个，前3个的默认值是本层的`starttime`最后一个的默认值是本层的`starttime+duration`

6、添加`segment`或者`cutto`时，比如添加`segment3`，则`segment3`的`starttime`默认值为`segment2`的`starttime+duration`

7、修改`animations`层的`starttime&duration`整个`animation`下的`starttime&duration`都会改变
