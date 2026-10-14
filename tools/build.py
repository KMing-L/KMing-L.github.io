#!/usr/bin/env python3
"""Regenerate the buildless site using only the Python standard library."""
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parents[1]
profile = json.loads((ROOT / 'data/profile.json').read_text())
pubs = profile['publications']

def authors(p):
    return ', '.join(escape(a).replace('Kaiming Liu', '<strong>Kaiming Liu</strong>').replace('*', '<sup>*</sup>') for a in p['authors'])

def paper_url(p):
    return p.get('paper', 'https://arxiv.org/abs/' + p['arxiv'])

def bib(p):
    author = p.get('bib_authors', ' and '.join(a.replace('*', '') for a in p['authors']))
    year = p.get('arxiv_year', p['year'])
    return f"@misc{{{p['id'].replace('-', '')}{year},\n  title = {{{p['title']}}},\n  author = {{{author}}},\n  year = {{{year}}},\n  eprint = {{{p['arxiv']}}},\n  archivePrefix = {{arXiv}},\n  url = {{https://arxiv.org/abs/{p['arxiv']}}}\n}}"

def card(p):
    resources = f'<a href="{paper_url(p)}">Paper <span aria-hidden="true">↗</span></a>'
    if p.get('code'):
        resources += f'<a href="{p["code"]}">Code <span aria-hidden="true">↗</span></a>'
    if p.get('project'):
        resources += f'<a href="{p["project"]}">Project <span aria-hidden="true">↗</span></a>'
    return f'''<article class="paper-card" id="{p['id']}">
      <a class="paper-art" href="{paper_url(p)}" aria-label="Read {escape(p['title'])}">
        <img src="{p['image']}" width="180" height="180" alt="{p['short']}" loading="lazy">
      </a>
      <div class="paper-body">
        <h3><a href="{paper_url(p)}">{escape(p['title'])}</a></h3>
        <p class="authors">{authors(p)}</p>
        <p class="paper-description">{escape(p['description'])}</p>
        <div class="paper-bottom"><span class="venue {p['color']}">{escape(p['venue'])}</span><div class="paper-links">{resources}</div></div>
        <details class="citation"><summary>BibTeX</summary><div class="citation-panel"><button class="copy-citation" type="button">Copy citation</button><pre tabindex="0">{escape(bib(p))}</pre></div></details>
      </div>
    </article>'''

def compact(p):
    return f'''<article class="compact-paper" id="{p['id']}"><h3><a href="{paper_url(p)}">{escape(p['title'])}</a></h3><p class="authors">{authors(p)}</p><p class="compact-venue">{escape(p['venue'])} <span aria-hidden="true">·</span> <a href="{paper_url(p)}">Paper ↗</a></p></article>'''

selected = '\n'.join(card(p) for p in pubs if p.get('selected'))
other = '\n'.join(compact(p) for p in pubs if not p.get('selected'))
# Both pages share the same wording; homepage links only add presentation.
research = escape(profile['research_statement'])
homepage_research = research.replace('human experience (体感)', '<strong>human experience (<span lang="zh-CN">体感</span>)</strong>')
for phrase, target in [('outcome alignment', 'tigan'), ('shared understanding in collaboration', 'ioa'), ('reliable interaction with tools and environments', 'align')]:
    homepage_research = homepage_research.replace(phrase, f'<a href="#{target}">{phrase}</a>')
template = (ROOT / 'tools/index.template.html').read_text()
html = template.replace('{{SELECTED}}', selected).replace('{{OTHER}}', other).replace('{{RESEARCH}}', homepage_research)
html = html.replace('{{SCHOLAR}}', escape(profile['scholar'], quote=True)).replace('{{UPDATED}}', profile['updated'])
(ROOT / 'index.html').write_text(html)
# Only selected entries are exported as arXiv BibTeX; conference author lists
# can differ from the original preprints of other publications.
(ROOT / 'publications.bib').write_text('\n\n'.join(bib(p) for p in pubs if p.get('selected')) + '\n')

# The selected collection contains the four first/co-first-author papers.
cv_papers = [p for p in pubs if p.get('selected')]
cv_pubs = '\n'.join(f'<li><a href="{paper_url(p)}"><strong>{escape(p["title"])}</strong></a><br>{authors(p)}<br><span class="cv-venue">{escape(p["venue"])}</span></li>' for p in cv_papers)
cv = (ROOT / 'tools/cv.template.html').read_text().replace('{{PUBLICATIONS}}', cv_pubs).replace('{{RESEARCH}}', research).replace('{{UPDATED}}', profile['updated'])
(ROOT / 'cv.html').write_text(cv)
print(f'Generated index.html, cv.html, and publications.bib ({len(pubs)} homepage publications; {len(cv_papers)} CV publications).')
