### 使用方法
1. 安装mkdocs和主题
   
   `pip install mkdocs`
   
   `pip install mkdocs-material`

2. clone
   
   `git clone https://github.com/FrameMinitrue/FrameMinitrue.github.io.git `
   
   （先安装git）

3. 在`FrameMinitrue.github.io/docs`中编辑文档，按照文件夹分类，markdown文件编写，命名规范为“[条目名].md”

4. 生成yml navigation（这里写了一个脚本来生成）
   
   `python gen_nav.py`

5. 提交`main`分支，推荐在pycharm/vscode下直接编辑后，直接update/commit/push完成，熟悉git的可以用命令行

7. 提交`gh-pages`分支，部署网站
   
   在`FrameMinitrue.github.io`文件夹下：
   
   `mkdocs gh-deploy`