from pathlib import Path
import re

p = Path('index.html')
text = p.read_text(encoding='utf-8')

css_anchor = '.map-help{padding:10px 16px;border-top:1px solid var(--line);font-size:12px;color:var(--muted);background:#fff}'
if '.overview-legend{' not in text and css_anchor in text:
    extra_css = '''
.overview-legend{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;margin-top:14px}
.overview-legend-item{display:flex;gap:10px;align-items:flex-start;padding:10px 12px;border:1px solid var(--line);border-radius:14px;background:#fff}
.overview-legend-num{flex:0 0 auto;width:26px;height:26px;border-radius:999px;background:var(--ink);color:#fff;display:inline-flex;align-items:center;justify-content:center;font-size:12px;font-weight:800}
.overview-legend-text{font-size:13px;line-height:1.35}
.overview-legend-text strong{display:block;font-size:13px}
.overview-legend-text span{display:block;color:var(--muted);font-size:12px;margin-top:2px}
.map-node{fill:#fff;stroke:var(--ink);stroke-width:2.4}.map-node-text{font-size:11px;font-weight:800;fill:var(--ink);text-anchor:middle;dominant-baseline:middle}
@media(max-width:700px){.overview-legend{grid-template-columns:1fr}.overview-legend-item{padding:9px 10px}}
'''
    text = text.replace(css_anchor, css_anchor + extra_css, 1)

new_section = '''<section class="overview">
<div class="map-toolbar"><button class="map-zoom-btn" type="button" id="openOverviewMap">🔍 放大地图</button></div>
<svg id="overviewMapSvg" aria-label="美国西部自驾总览详细路线图" class="map-svg" role="img" viewbox="0 0 980 690">
  <rect x="18" y="18" width="944" height="654" rx="20" fill="#fbfcfd" stroke="var(--line)"></rect>
  <text x="52" y="70" font-size="26" font-family="Georgia, serif" fill="var(--ink)">美国西部 14 天路线总览</text>
  <text x="52" y="96" font-size="12" fill="var(--muted)">地图仅显示路线与编号；详细地点请看下方列表。</text>
  <path d="M135 560 Q365 420 610 270 Q665 152 702 118 Q718 102 736 126 Q720 150 688 192 Q760 264 812 356 Q786 382 752 416 Q700 412 650 434 Q618 452 586 470 Q538 432 488 421 Q396 428 320 470 Q284 517 242 564 Q188 548 144 560" fill="none" stroke="#d8e0e8" stroke-width="18" stroke-linecap="round" stroke-linejoin="round"></path>
  <path d="M135 560 Q365 420 610 270" fill="none" stroke="#ef6c57" stroke-width="6" stroke-linecap="round"></path>
  <path d="M610 270 Q665 152 702 118" fill="none" stroke="#f4a340" stroke-width="6" stroke-linecap="round"></path>
  <path d="M702 118 Q718 102 736 126" fill="none" stroke="#c79a32" stroke-width="6" stroke-linecap="round"></path>
  <path d="M736 126 Q720 150 688 192" fill="none" stroke="#3d8d92" stroke-width="6" stroke-linecap="round"></path>
  <path d="M688 192 Q760 264 812 356" fill="none" stroke="#4a77b3" stroke-width="6" stroke-linecap="round"></path>
  <path d="M812 356 Q786 382 752 416 Q700 412 650 434" fill="none" stroke="#8d5ca6" stroke-width="6" stroke-linecap="round"></path>
  <path d="M650 434 Q618 452 586 470" fill="none" stroke="#b65b85" stroke-width="6" stroke-linecap="round"></path>
  <path d="M586 470 Q538 432 488 421" fill="none" stroke="#dd6c4d" stroke-width="6" stroke-linecap="round"></path>
  <path d="M488 421 Q396 428 320 470" fill="none" stroke="#da8a3a" stroke-width="6" stroke-linecap="round"></path>
  <path d="M320 470 Q284 517 242 564" fill="none" stroke="#b7a13a" stroke-width="6" stroke-linecap="round"></path>
  <path d="M242 564 Q188 548 144 560" fill="none" stroke="#738f59" stroke-width="6" stroke-linecap="round"></path>
  <g>
    <circle class="map-node" cx="135" cy="560" r="12"></circle><text class="map-node-text" x="135" y="560">1</text>
    <circle class="map-node" cx="610" cy="270" r="12"></circle><text class="map-node-text" x="610" y="270">2</text>
    <circle class="map-node" cx="702" cy="118" r="12"></circle><text class="map-node-text" x="702" y="118">3</text>
    <circle class="map-node" cx="718" cy="102" r="12"></circle><text class="map-node-text" x="718" y="102">4</text>
    <circle class="map-node" cx="736" cy="126" r="12"></circle><text class="map-node-text" x="736" y="126">5</text>
    <circle class="map-node" cx="688" cy="192" r="12"></circle><text class="map-node-text" x="688" y="192">6</text>
    <circle class="map-node" cx="760" cy="264" r="12"></circle><text class="map-node-text" x="760" y="264">7</text>
    <circle class="map-node" cx="812" cy="356" r="12"></circle><text class="map-node-text" x="812" y="356">8</text>
    <circle class="map-node" cx="650" cy="434" r="12"></circle><text class="map-node-text" x="650" y="434">9</text>
    <circle class="map-node" cx="586" cy="470" r="12"></circle><text class="map-node-text" x="586" y="470">10</text>
    <circle class="map-node" cx="488" cy="421" r="12"></circle><text class="map-node-text" x="488" y="421">11</text>
    <circle class="map-node" cx="320" cy="470" r="12"></circle><text class="map-node-text" x="320" y="470">12</text>
    <circle class="map-node" cx="242" cy="564" r="12"></circle><text class="map-node-text" x="242" y="564">13</text>
    <circle class="map-node" cx="144" cy="560" r="12"></circle><text class="map-node-text" x="144" y="560">14</text>
  </g>
</svg>
<div class="overview-legend">
  <div class="overview-legend-item"><div class="overview-legend-num">1</div><div class="overview-legend-text"><strong>洛杉矶 / LAX</strong><span>D1 抵达；D15 回到洛杉矶</span></div></div>
  <div class="overview-legend-item"><div class="overview-legend-num">2</div><div class="overview-legend-text"><strong>盐湖城</strong><span>D2 取车并过夜</span></div></div>
  <div class="overview-legend-item"><div class="overview-legend-num">3</div><div class="overview-legend-text"><strong>West Yellowstone</strong><span>D3 夜宿</span></div></div>
  <div class="overview-legend-item"><div class="overview-legend-num">4</div><div class="overview-legend-text"><strong>Gardiner</strong><span>D4 夜宿</span></div></div>
  <div class="overview-legend-item"><div class="overview-legend-num">5</div><div class="overview-legend-text"><strong>Yellowstone Lake</strong><span>D5 夜宿园内</span></div></div>
  <div class="overview-legend-item"><div class="overview-legend-num">6</div><div class="overview-legend-text"><strong>Thayne</strong><span>D6 夜宿</span></div></div>
  <div class="overview-legend-item"><div class="overview-legend-num">7</div><div class="overview-legend-text"><strong>Moab / Arches</strong><span>D7–D8</span></div></div>
  <div class="overview-legend-item"><div class="overview-legend-num">8</div><div class="overview-legend-text"><strong>Monument Valley</strong><span>D8 观景</span></div></div>
  <div class="overview-legend-item"><div class="overview-legend-num">9</div><div class="overview-legend-text"><strong>Page / Antelope Canyon</strong><span>D8–D10</span></div></div>
  <div class="overview-legend-item"><div class="overview-legend-num">10</div><div class="overview-legend-text"><strong>Grand Canyon South Rim</strong><span>D9 往返</span></div></div>
  <div class="overview-legend-item"><div class="overview-legend-num">11</div><div class="overview-legend-text"><strong>Springdale / Zion</strong><span>D11–D12</span></div></div>
  <div class="overview-legend-item"><div class="overview-legend-num">12</div><div class="overview-legend-text"><strong>Las Vegas</strong><span>D13 夜宿</span></div></div>
  <div class="overview-legend-item"><div class="overview-legend-num">13</div><div class="overview-legend-text"><strong>Joshua Tree / Banning</strong><span>D14</span></div></div>
  <div class="overview-legend-item"><div class="overview-legend-num">14</div><div class="overview-legend-text"><strong>Santa Monica</strong><span>D15 海边停留后去 LAX</span></div></div>
</div>
<div class="smallprint" style="margin:8px 4px 0">地图内只保留编号，避免地点文字与路线重叠；详细地点与日期请看编号列表。</div>
</section>'''

text, count = re.subn(r'<section class="overview">.*?</section>', new_section, text, count=1, flags=re.S)
if count == 0:
    raise SystemExit('overview section not found')

p.write_text(text, encoding='utf-8')
Path('public').mkdir(exist_ok=True)
Path('public/index.html').write_text(text, encoding='utf-8')
