"""Create self-contained decorative *illustrations*, not actual shop product photographs."""
from pathlib import Path
import random,math
A=Path(__file__).parent/'assets'; A.mkdir(exist_ok=True)
sets=[
 ('rose-dream',['#b96c80','#eea7b4','#f4d6cb','#fff0dc'], '#eee1df','#cfaaae',4),
 ('powder-blush',['#cf9d98','#eec3bc','#f7e5dc','#b87f8b'], '#f1e7e2','#d0aba6',5),
 ('soft-white',['#f4eadd','#fff9ed','#d7ddd2','#e5c5b7'], '#eceddf','#bbbda5',4),
 ('sunset-peach',['#efab87','#dc8a87','#f4c4a6','#f7e3c0'], '#f6e7e0','#d59b91',5),
 ('berry-mood',['#a3546c','#cc819d','#e6b2ba','#f5d2c5'], '#e9dfeb','#a98ba3',5),
 ('lilac-letter',['#b6a0d0','#c7b1d7','#f2d2d9','#f2e7da'], '#e7e5ed','#aba0be',5),
]
for idx,(name,colors,bg,wrapping,nrows) in enumerate(sets):
 rnd=random.Random(23+idx)
 centers=[]
 for row in range(nrows):
  maxc=2+int(3*math.sin((row+1)/nrows*math.pi))
  for k in range(maxc):
   x=445 + (k-(maxc-1)/2)*rnd.randrange(90,122)+rnd.randrange(-22,23)
   y=258+row*79+rnd.randrange(-28,29)
   r=rnd.randrange(40,68)
   centers.append((x,y,r,rnd.choice(colors)))
 lines=[];leaves=[]
 for (x,y,r,c) in centers:
  lines.append(f'<path d="M{x:.0f} {y:.0f} Q{(x+470)/2:.0f} {((y+825)/2):.0f} 461 826" stroke="#7e9474" stroke-width="6" fill="none" opacity=".82"/>')
  if rnd.random()>.32:
   u=x+(460-x)*.32;v=y+(825-y)*.52
   side=rnd.choice([-1,1]);leaves.append(f'<ellipse cx="{u+side*28:.0f}" cy="{v-12:.0f}" rx="37" ry="14" fill="#{rnd.choice(["879b79","9ab09b","7d9a84","afb99b"])}" transform="rotate({side*38},{u+side*28:.0f},{v-12:.0f})" opacity=".86"/>')
 petals=[]
 for x,y,r,c in centers:
  shadow=r*.2
  petals.append(f'<circle cx="{x+4}" cy="{y+6}" r="{r*.83}" fill="#664653" opacity=".085"/>')
  n=7
  for p in range(n):
   a=2*math.pi*p/n+rnd.uniform(-.08,.08);px=x+math.cos(a)*r*.52;py=y+math.sin(a)*r*.52
   petals.append(f'<ellipse cx="{px:.0f}" cy="{py:.0f}" rx="{r*.47:.0f}" ry="{r*.35:.0f}" fill="{c}" opacity=".90" transform="rotate({p*360/n:.0f} {px:.0f} {py:.0f})"/>')
  petals.append(f'<circle cx="{x}" cy="{y}" r="{r*.29:.0f}" fill="{c}" opacity=".83"/>')
  petals.append(f'<circle cx="{x}" cy="{y}" r="{r*.15:.0f}" fill="#f9e8bf" opacity=".72"/>')
 art=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 1100" role="img" aria-label="Декоративная иллюстрация букета">
 <defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop stop-color="{bg}"/><stop offset="1" stop-color="#fdf7ef"/></linearGradient><linearGradient id="paper" x1="0" y1="0" x2=".9" y2="1"><stop stop-color="#fffdf8"/><stop offset=".55" stop-color="{wrapping}"/><stop offset="1" stop-color="#dbc5bc"/></linearGradient><radialGradient id="glow"><stop stop-color="#fffdf9" stop-opacity=".7"/><stop offset="1" stop-color="#fffdf9" stop-opacity="0"/></radialGradient></defs>
 <rect width="900" height="1100" fill="url(#bg)"/><circle cx="510" cy="310" r="480" fill="url(#glow)"/>
 <path d="M80 835 Q450 790 820 835" stroke="#b8a8a2" stroke-opacity=".30" stroke-width="3" fill="none"/>
 <ellipse cx="465" cy="962" rx="300" ry="34" fill="#605151" opacity=".08"/>
 <g>{''.join(lines)}{''.join(leaves)}</g>
 <g><path d="M175 575 Q452 645 760 560 L555 977 Q457 1007 361 971 Z" fill="url(#paper)" opacity=".96"/>
 <path d="M175 575 L420 684 L364 969 Z" fill="#fffdf8" opacity=".70"/><path d="M760 560 L493 690 L555 978 Z" fill="{wrapping}" opacity=".85"/>
 <path d="M195 585 Q453 750 738 572" stroke="#fff8f2" stroke-width="4" opacity=".65" fill="none"/>
 </g>
 <g>{''.join(petals)}</g>
 <path d="M387 836 Q459 882 525 840" stroke="#a77d83" stroke-width="15" fill="none" opacity=".65"/>
 <path d="M452 861 Q419 842 367 867 Q396 903 448 873 Q494 895 546 861 Q500 844 459 865 Z" fill="#e4c2bb" opacity=".93"/>
 <text x="450" y="1057" font-family="Georgia,serif" font-size="17" letter-spacing="5" fill="#8a7775" text-anchor="middle" opacity=".70">AINALAIYN · КОНЦЕПТ</text>
 </svg>'''
 (A/f'{name}.svg').write_text(art,encoding='utf-8')
print('Generated',len(sets),'SVG bouquet illustrations')
