# Academic Homepage with Quarto

基于 Quarto + GitHub Pages 的学术个人主页，设计风格参考 [AcadHomepage](https://github.com/RayeRen/acad-homepage.github.io)。

## 项目结构

```
cdc-acad-homepage/
├── _quarto.yml              # Quarto 配置文件
├── index.qmd                # 首页 (About)
├── news.qmd                 # 最新动态
├── publications.qmd         # 发表论文
├── honors.qmd               # 荣誉奖项
├── education.qmd            # 教育背景
├── talks.qmd                # 邀请讲座
├── experience.qmd           # 工作经历
├── _includes/
│   └── author-profile.html  # 侧边栏个人资料组件
├── styles/
│   ├── custom.scss          # 自定义 SCSS 样式
│   └── main.css             # 主 CSS 样式
├── scripts/
│   └── scholar-stats.html   # Google Scholar 引用数脚本
├── google_scholar_crawler/
│   ├── main.py              # 爬虫脚本
│   └── requirements.txt     # Python 依赖
└── .github/workflows/
    ├── publish.yml          # 网站构建部署
    └── scholar-crawler.yml  # 引用数自动更新
```

## 快速开始

### 1. 安装 Quarto

从 [Quarto 官网](https://quarto.org/docs/get-started/) 下载安装：

```bash
# macOS (使用 Homebrew)
brew install quarto

# 或下载 pkg 安装包
```

### 2. 本地预览

```bash
cd /Users/tegan/Documents/2026/personal-website/cdc-acad-homepage
quarto preview
```

浏览器将自动打开 `http://localhost:4000` 预览网站。

### 3. 个性化配置

1. **修改个人信息**：编辑 `_includes/author-profile.html`
2. **修改网站配置**：编辑 `_quarto.yml` 中的 title、description、site-url
3. **替换头像**：将你的头像放到 `images/profile.jpg`（或 .png）
4. **更新页面内容**：编辑各 `.qmd` 文件

### 4. GitHub 部署

1. 创建 GitHub 仓库
2. 推送代码到 main 分支
3. 在 Repository Settings > Pages 中选择 "GitHub Actions" 作为 Source
4. 添加 Secret `GOOGLE_SCHOLAR_ID`（可选，用于自动更新引用数）

## Google Scholar 集成

1. 获取你的 Google Scholar ID（从个人页面 URL 中获取，如 `citations?user=XXXXXX`）
2. 在 GitHub 仓库 Settings > Secrets > Actions 中添加 `GOOGLE_SCHOLAR_ID`
3. 修改 `scripts/scholar-stats.html` 中的 `repoOwner` 和 `repoName`

## 自定义样式

- `styles/custom.scss` - SCSS 变量和规则
- `styles/main.css` - 主样式文件

颜色变量参考参考项目设计：
- 主链接色：`#224b8d`
- 文本色：`#494e52`
- 边框色：`#e0e0e0`

## 许可

MIT License
# Teganone.githup.io
