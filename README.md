# Online_learning
基于Python的在线学习平台的设计与实现

# 项目介绍

随着人们生活节奏的加快，各种新知识、新技术的不断出现，学习内容丰富，学习门槛逐渐降低，提高学习效率和学习效果尤为重要。疫情当下，更多人选择了网上学习。

针对此问题，本课题拟以Python Web框架为基础，设计并实现一个在线学习平台，提供专业的学习资源、可方便知识交流、知识共享、知识问答，方便学习者找到专业的学习途径和方法，学习内容和资料等，减少学习时间上的浪费，提高学习的质量。

# 环境依赖

Django:
在Django目录下使用命令行

```
pip install -r requirements.txt
```

Vue:

在Vue目录下使用命令行

```
npm install
```





# 目录结构描述

```
├─djangoProject1							Django项目
│  ├─dist									Vue编译文件
│  │  └─static
│  ├─djangoProject1							
│  │  └─__pycache__
│  ├─media									媒体文件
│  │  ├─academy
│  │  ├─course
│  │  │  ├─img
│  │  │  └─resource
│  │  ├─editor
│  │  ├─forum
│  │  │  ├─annex
│  │  │  └─img
│  │  └─head
│  ├─templates								模板
│  ├─web									web应用
│  │  ├─migrations
│  │  │  └─__pycache__
│  │  ├─modelforms
│  │  │  └─__pycache__
│  │  ├─models
│  │  │  └─__pycache__
│  │  ├─utils
│  │  │  └─__pycache__
│  │  ├─views
│  │  │  └─__pycache__
│  │  └─__pycache__
│  └─__pycache__
└─viteproject								Vue项目
    ├─dist									编译文件
    │  └─static
    ├─public
    └─src
        ├─assets
        ├─components						组件
        │  ├─Academy
        │  ├─Course
        │  ├─Forum
        │  └─User
        └─router							路由
```
