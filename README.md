# Match Poster Generator

Generate match posters automatically from a schedule CSV using Python and Pillow.

这是一个使用 **Python + Pillow** 的自动化工具，用于根据赛程表（CSV）在固定模板底图上，批量生成比赛海报图片，适用于体育赛事、联赛宣传、社交媒体发布等场景。

---

## ✨ Features

- 🖼 使用固定尺寸的底图（1536 × 864）
- 📅 自动渲染比赛日期
- 🏠⚔️🚗 自动渲染主队 / 客队名称
- 🎨 支持中英文混排（基于思源黑体）
- ✏️ 文字位置固定，适合长期复用模板
- 🖊 白色文字 + 黑色描边，保证在复杂背景下清晰可读
- 📦 批量生成海报图片

---

## 📂 Project Structure
```
match-poster-generator/
├── base.png # 底图模板（可自行替换）
├── generate.py # 主脚本
├── schedule.csv # 赛程表（CSV）
├── fonts/
│ ├── SourceHanSansCN-Regular.otf
│ └── SourceHanSansCN-Medium.otf
└── README.md
```

---

## 📋 Schedule CSV Format

`schedule.csv` 示例：

```csv
date,home,away
2026-01-15,Lakers,Warriors
2026-01-16,Bulls,Celtics
```
字段说明：  

date：比赛日期（字符串）

home：主队名称

away：客队名称

🚀 Quick Start  

1️⃣ 环境要求

Python 3.8+

Pillow

安装依赖：

pip install pillow

2️⃣ 运行生成脚本

在项目目录下执行：

python generate.py


生成的海报图片将输出到当前目录（或脚本中指定的输出目录）。

🎨 Layout Design

图片尺寸：1536 × 864

左侧：联盟 / 品牌 Logo 区（宽约 550px）

右侧内容区：

日期：顶部，字号最大

主队名称：中部

客队名称：主队下方，间距适中

文字均为：

白色填充

黑色描边（增强可读性）

🔤 Fonts & License

本项目示例使用 Source Han Sans CN（思源黑体）：

支持中英文混排

可免费商用

字体版权归原作者所有

👉 如用于商业项目，请自行确认字体授权条款。

🧩 Customization

你可以轻松修改以下内容：

字体大小

文字坐标

描边粗细

输出目录

CSV 字段结构

所有配置均集中在 generate.py 中，便于维护。

📄 License

This project is released under the MIT License.

You are free to use, modify, and distribute it.
