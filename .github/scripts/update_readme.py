import os
import json
import urllib.request

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

## 📊 GitHub 统计

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=Jarv1s0&theme=tokyo-night&hide_border=true&area=true" width="98%" />
</p>

---

## 💬 每日一句
> {quote}

<p align="right">
  <i>最后更新时间：自动更新</i>
</p>
"""

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)
