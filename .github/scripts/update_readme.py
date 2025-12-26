import os
import json
import urllib.request

def fetch(url):
    req = urllib.request.Request(url, headers={'Authorization': f'token {os.environ["GITHUB_TOKEN"]}'})
    return json.loads(urllib.request.urlopen(req).read())

activity = ''
for repo in ['Jarv1s0/RouteX', 'Jarv1s0/Proxy_Script']:
    name = repo.split('/')[1]
    try:
        rel = fetch(f'https://api.github.com/repos/{repo}/releases/latest')
        tag, url = rel['tag_name'], rel['html_url']
    except:
        tag, url = 'No release', '#'
    
    commit = fetch(f'https://api.github.com/repos/{repo}/commits?per_page=1')[0]
    msg = commit['commit']['message'].split('\n')[0]
    curl = commit['html_url']
    sha = commit['sha'][:7]
    activity += f'- **{name}** — 🚀 [{tag}]({url}) · 📝 [{msg}]({curl}) (`{sha}`)\n'

try:
    quote_data = json.loads(urllib.request.urlopen('https://v1.hitokoto.cn/?c=i&c=k').read())
    quote = quote_data['hitokoto'] + ' — ' + quote_data['from']
except:
    quote = '保持好奇，持续学习。'

readme = f"""<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=auto&height=200&section=header&text=Hi,%20I'm%20Jarv1s0&fontSize=70&animation=fadeIn" />
</p>

<p align="center">
  <img src="https://img.shields.io/github/followers/Jarv1s0?label=Follow&style=for-the-badge&logo=github&color=24292e" />
  <img src="https://komarev.com/ghpvc/?username=Jarv1s0&color=blue&style=for-the-badge&label=VIEWS" />
</p>

---

## 🛠 技术栈

### 语言
<p align="left">
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Shell_Script-121011?style=for-the-badge&logo=gnu-bash&logoColor=white" />
</p>

### 框架 & 工具
<p align="left">
  <img src="https://img.shields.io/badge/Electron-47848F?style=for-the-badge&logo=electron&logoColor=white" />
  <img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white" />
  <img src="https://img.shields.io/badge/Vue.js-4FC08D?style=for-the-badge&logo=vuedotjs&logoColor=white" />
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" />
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
</p>

---

## 🚀 精选项目

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>RouteX</h3>
      <p>基于 Electron + TypeScript 的桌面客户端，专注于 UI 重构与构建优化。</p>
      <a href="https://github.com/Jarv1s0/RouteX">
        <img src="https://img.shields.io/github/stars/Jarv1s0/RouteX?style=flat-square&logo=github&color=yellow" />
      </a>
      <a href="https://github.com/Jarv1s0/RouteX/releases">
        <img src="https://img.shields.io/github/v/release/Jarv1s0/RouteX?style=flat-square&color=blue" />
      </a>
    </td>
    <td width="50%" valign="top">
      <h3>Proxy_Script</h3>
      <p>精选代理客户端配置 (Clash / QX / Loon) 与自动化脚本集合。</p>
      <a href="https://github.com/Jarv1s0/Proxy_Script">
        <img src="https://img.shields.io/github/stars/Jarv1s0/Proxy_Script?style=flat-square&logo=github&color=yellow" />
      </a>
    </td>
  </tr>
</table>

---

## 📊 GitHub 统计
<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=Jarv1s0&show_icons=true&theme=tokyonight&hide_border=true&count_private=true" width="49%" />
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=Jarv1s0&theme=tokyonight&hide_border=true" width="49%" />
</p>

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Jarv1s0&layout=compact&theme=tokyonight&hide_border=true&langs_count=8" width="49%" />
  <img src="https://github-profile-trophy.vercel.app/?username=Jarv1s0&theme=tokyonight&no-frame=true&column=4&margin-w=15&margin-h=15" width="49%" />
</p>

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=Jarv1s0&theme=tokyo-night&hide_border=true&area=true" width="98%" />
</p>

---

## 🕒 最近动态
{activity}

## 💬 每日一句
> {quote}

<p align="right">
  <i>最后更新时间：自动更新</i>
</p>
"""

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)
