# Academic Homepage — Hugo + PaperMod

基于 [Hugo](https://gohugo.io/) + [PaperMod](https://github.com/adityatelange/hugo-PaperMod) 主题的学术个人主页，部署在 GitHub Pages 和 Vercel。

## 项目结构

```
danchunchen.github.io/
├── hugo.toml                    # Hugo 配置（主题、菜单、社交链接等）
├── vercel.json                  # Vercel 部署配置
├── content/
│   ├── _index.md                # 首页 About（含 News）
│   ├── publications.md          # 发表论文
│   ├── archives.md              # 文章归档
│   ├── search.md                # 搜索页
│   └── posts/                   # 博客文章
├── _includes/
│   └── sidebar.html             # 自定义侧边栏组件
├── assets/                      # JS/CSS 资源
├── styles/                      # 自定义 CSS
├── static/
│   ├── images/                  # 头像、论文配图等
│   └── files/                   # CV PDF 等下载文件
├── themes/
│   └── PaperMod/                # Hugo 主题（git submodule）
└── .github/workflows/
    └── deploy.yml               # GitHub Pages 自动部署
```

## 本地预览

```bash
# 需要 Hugo Extended v0.163.1+
hugo server
```

浏览器打开 `http://localhost:1313`。

## 内容修改

| 要改什么 | 对应文件 |
|---|---|
| 个人简介 / News | `content/_index.md` |
| 论文列表 | `content/publications.md` |
| 博客文章 | `content/posts/` 下新建 `.md` 文件 |
| 导航菜单 / 社交链接 | `hugo.toml` |
| 自定义样式 | `styles/` |
| 头像 | `static/images/profile.png` |
| CV | `static/files/CV-CHEN-DANCHUN.pdf` |

## 部署

### GitHub Pages

推送到 `main` 分支后，`.github/workflows/deploy.yml` 自动构建并部署。

### Vercel

连接仓库后 Vercel 自动识别 Hugo 框架，每次推送触发部署。Hugo 版本由 `vercel.json` 中 `HUGO_VERSION` 指定。

## Hugo 安装

```bash
# macOS
brew install hugo

# 或从 GitHub Releases 下载 Extended 版本
# https://github.com/gohugoio/hugo/releases
```

## 许可

MIT License
