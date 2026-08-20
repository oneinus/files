#!/usr/bin/env python3
"""확률변수 도안 생성. CLAUDE.md 8-6 규격 (캔버스 760 · 배경 #1C1C1C · 3배 래스터화)."""

W, H = 760, 330

BG = "#1C1C1C"
FG = "#ffffff"       # 밝은 글자 17.0:1
DIM = "#898781"      # 흐린 글자 · 축 · 기준선 4.74:1
LINE = "#c3c2b7"     # 의미를 가진 선 9.5:1
ACC = "#3987e5"      # 주 계열 파랑 4.68:1

KR = "Apple SD Gothic Neo, Helvetica Neue, sans-serif"
MATH = "STIX Two Math, Apple Symbols, Times New Roman, serif"

# 좌표
CY = 205                     # 도해의 기준선
BX, BY, BRX, BRY = 145, CY, 112, 80   # 표본공간 blob
PRX, PRY = 155, CY - 4       # 역상 영역 중심
OMX, OMY = 128, CY - 4       # 표본점 ω
LX0, LX1 = 470, 730          # 실수 직선
IMX = 512                    # x(ω)
IB0, IB1 = 572, 686          # 구간 B

svg = []
a = svg.append

a(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
a(f'<rect width="{W}" height="{H}" fill="{BG}"/>')
a('<defs>')
a(f'<marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
  f'<path d="M 0 0 L 10 5 L 0 10 z" fill="{LINE}"/></marker>')
a(f'<marker id="ard" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
  f'<path d="M 0 0 L 10 5 L 0 10 z" fill="{DIM}"/></marker>')
a(f'<marker id="arx" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
  f'<path d="M 0 0 L 10 5 L 0 10 z" fill="{DIM}"/></marker>')
a('</defs>')

def text(x, y, s, size=15, fill=FG, weight="600", anchor="start", family=KR, style="normal"):
    a(f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" fill="{fill}" '
      f'font-weight="{weight}" font-style="{style}" text-anchor="{anchor}">{s}</text>')

# 제목 · 부제
text(24, 34, "확률변수 : 두 무대를 잇는 함수", 20)
text(24, 58, '표본공간 위의 확률 P 를 실수 위의 분포 <tspan font-style="italic">P</tspan>'
     '<tspan font-size="11" dy="4">x</tspan><tspan dy="-4"> 로 옮김</tspan>', 14, DIM, "400")

# 표본공간
a(f'<ellipse cx="{BX}" cy="{BY}" rx="{BRX}" ry="{BRY}" fill="none" stroke="{DIM}" stroke-width="2"/>')
text(BX, BY - BRY - 14, '(𝒳, P)', 15, FG, "600", "middle", MATH)

# 역상 영역
a(f'<ellipse cx="{PRX}" cy="{PRY}" rx="56" ry="42" fill="none" stroke="{LINE}" '
  f'stroke-width="2" stroke-dasharray="5 5"/>')
text(PRX + 6, PRY + 66, '{ ω : x(ω) ∈ B }', 14, LINE, "400", "middle", MATH)

# 표본점
a(f'<circle cx="{OMX}" cy="{OMY}" r="7" fill="{ACC}" stroke="{BG}" stroke-width="2"/>')
text(OMX - 14, OMY + 5, 'ω', 15, FG, "600", "end", MATH)

# 확률변수 화살표
a(f'<line x1="{BX+BRX+14}" y1="{CY}" x2="{IMX-22}" y2="{CY}" stroke="{LINE}" '
  f'stroke-width="2" marker-end="url(#ar)"/>')
text((BX + BRX + IMX) / 2, CY - 14, 'x', 16, FG, "600", "middle", MATH, "italic")
text((BX + BRX + IMX) / 2, CY + 26, '확률변수', 14, DIM, "400", "middle")

# 실수 직선
a(f'<line x1="{LX0}" y1="{CY}" x2="{LX1}" y2="{CY}" stroke="{DIM}" stroke-width="2" '
  f'marker-end="url(#arx)"/>')
text(LX1 - 4, CY - 22, 'ℝ', 15, FG, "600", "end", MATH)

# 구간 B
a(f'<line x1="{IB0}" y1="{CY}" x2="{IB1}" y2="{CY}" stroke="{ACC}" stroke-width="9" '
  f'stroke-linecap="butt"/>')
text((IB0 + IB1) / 2, CY - 22, 'B', 15, FG, "600", "middle", MATH, "italic")

# 상 x(ω)
a(f'<circle cx="{IMX}" cy="{CY}" r="7" fill="{ACC}" stroke="{BG}" stroke-width="2"/>')
text(IMX, CY - 22, 'x(ω)', 15, FG, "600", "middle", MATH)

# 역상 점선 (B → 표본공간)
a(f'<path d="M {(IB0+IB1)/2} {CY-34} C 540 116, 320 106, {PRX+42} {PRY-31}" fill="none" '
  f'stroke="{DIM}" stroke-width="2" stroke-dasharray="2 7" stroke-linecap="round" '
  f'marker-end="url(#ard)"/>')
text(392, 104, '역상으로 되돌아가 P 로 계산', 14, DIM, "400", "middle")

# 하단 캡션
text(W / 2, H - 26, '<tspan font-style="italic">P</tspan><tspan font-size="12" dy="4">x</tspan>'
     '<tspan dy="-4">(B) = P( x ∈ B ) = P( { ω : x(ω) ∈ B } )</tspan>', 16, FG, "600", "middle", MATH)

a('</svg>')

open("/tmp/rv/random_variable.svg", "w").write("\n".join(svg))
print("written")
