# Kaiming Liu — academic homepage

Public site: https://kming-l.github.io/

A small, responsive academic homepage for GitHub Pages. The warm background, serif headings, restrained blue links, and publication layout are inspired by [Rulin Shao's homepage](https://rulinshao.github.io/). The implementation and text are independently written.

## 修改内容

- 论文：修改 `data/profile.json`。`selected: true` 的论文显示在代表作区域，其他论文显示在可展开列表中。
- 自我介绍、News、经历：修改 `tools/index.template.html`。
- 公开 CV：修改 `tools/cv.template.html`；研究兴趣与论文数据由 `data/profile.json` 提供。
- 配色和排版：修改 `assets/site.css`。
- 照片与论文 logo：位于 `assets/`。

完成修改后，在仓库目录执行：

```sh
python3 tools/build.py
```

将修改提交到 `main` 后，GitHub Pages 会自动更新。生成的 `index.html`、`cv.html` 和 `publications.bib` 需要一起提交。网站运行不依赖 Python、Node.js 或任何框架。

## 本地预览

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

打开 http://127.0.0.1:8000 。CV 页面可以通过“Print / Save PDF”保存为 PDF。

## GitHub Pages 设置

Repository Settings → Pages → Deploy from a branch → `main` → `/ (root)`。

`.nojekyll` 让 GitHub Pages 直接发布这些静态文件。无需额外构建依赖。

## 内容核验与素材

截至 2026-10-14，个人背景依据本人提供的简历，论文依据本人提供的会议状态、Google Scholar、arXiv 及 ACL Anthology。研究兴趣是根据本人说明与公开工作重新组织的表述。没有包含未公开研究计划或原始简历。

- [Google Scholar](https://scholar.google.com/citations?user=X9bm8UMAAAAJ&hl=en)
- [TiGanEval](https://arxiv.org/abs/2610.17757)：前两位作者共同一作。
- [IoA](https://arxiv.org/abs/2608.08210)：作者顺序以 v2 为准。
- [ALIGN](https://arxiv.org/abs/2505.21055)：会议状态为 AACL-IJCNLP 2026 Main。
- [AIGS](https://arxiv.org/abs/2411.11910)：前五位作者共同一作，包含 Zhenhe Zhang。
- [Writing-RL](https://aclanthology.org/2026.acl-long.255/) 和 [EDC²-RAG](https://aclanthology.org/2025.findings-emnlp.522/)：采用正式发表版本的作者列表，可能与最早的 arXiv 版本不同。
- MiMo-V2.6 的作者众多，主页使用团队署名，并明确标出 Kaiming Liu 属于该团队作者列表。
- 头像来自本人的公开 Scholar 资料；TiGanEval、IoA、ALIGN 的 logo 由本人提供；AIGS 缩略图为原创示意图。
- `publications.bib` 为四篇代表作的 arXiv 引文，不伪造尚未核验的会议卷页信息。
- 字体已本地化；各自的 SIL Open Font License 文件保留在 `assets/fonts/`。

网站有键盘可操作的明暗主题切换、BibTeX 展开和复制、其他论文展开；所有正文在关闭 JavaScript 时仍可阅读。无需访问统计或第三方脚本。
