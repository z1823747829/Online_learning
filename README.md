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

# 图片
![网页捕获_2-6-2023_163135_127 0 0 1](https://github.com/z1823747829/Online_learning/assets/88657790/844b59a0-d2f0-4c8d-8dc1-2d19a850470d)
![网页捕获_2-6-2023_163148_127 0 0 1](https://github.com/z1823747829/Online_learning/assets/88657790/ee871e79-30bd-4a6c-917e-35c3d0b12760)
![网页捕获_2-6-2023_163155_127 0 0 1](https://github.com/z1823747829/Online_learning/assets/88657790/293daf5c-bded-4038-b0ce-8bf40d590cc4)
![网页捕获_2-6-2023_163225_127 0 0 1](https://github.com/z1823747829/Online_learning/assets/88657790/0ab7cda3-bfdd-4709-9836-58978ee93cc0)


