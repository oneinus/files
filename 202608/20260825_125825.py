#!/usr/bin/env python3
"""할증률 · 할인율 도안. CLAUDE.md 8-6 규격 (캔버스 760 · 배경 #1C1C1C · 3배 래스터화)."""

W, H = 760, 330

BG = "#1C1C1C"
FG = "#ffffff"      # 밝은 글자 17.0:1
DIM = "#898781"     # 흐린 글자 · 축 · 상자 테두리 4.74:1
UP = "#3987e5"      # 미래로 (곱함) 4.68:1
DOWN = "#e66767"    # 현재로 (나눔) 5.28:1

KR = "Apple SD Gothic Neo, Helvetica Neue, sans-serif"
MATH = "STIX Two Math, Apple Symbols, Times New Roman, serif"

CY = 186                       # 상자 세로 중심
BW, BH = 190, 66               # 상자 크기
LX, RX = 72, 498               # 상자 좌측 x
GAP0, GAP1 = LX + BW + 26, RX - 26   # 화살표 구간
AY_UP, AY_DN = CY - 26, CY + 26      # 두 화살표의 y

svg = []
a = svg.append
a(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
a(f'<rect width="{W}" height="{H}" fill="{BG}"/>')
a('<defs>')
for name, col in (("up", UP), ("dn", DOWN)):
    a(f'<marker id="{name}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
      f'orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="{col}"/></marker>')
a('</defs>')

def text(x, y, s, size=15, fill=FG, weight="600", anchor="start", family=KR):
    a(f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" fill="{fill}" '
      f'font-weight="{weight}" text-anchor="{anchor}">{s}</text>')

def box(x, label, value):
    a(f'<rect x="{x}" y="{CY - BH/2}" width="{BW}" height="{BH}" rx="8" fill="none" '
      f'stroke="{DIM}" stroke-width="2"/>')
    text(x + BW/2, CY - BH/2 - 14, label, 15, FG, "600", "middle")
    text(x + BW/2, CY + 9, value, 22, FG, "600", "middle")

# 제목 · 부제
text(24, 34, "할증률과 할인율 : 방향만 다른 같은 값", 20)
text(24, 58, "원금 100원, 이자율 10%, 1년 기준", 14, DIM, "400")

# 두 시점
box(LX, "현재", "100원")
box(RX, "미래 1년", "110원")

# 미래로 (곱함)
a(f'<line x1="{GAP0}" y1="{AY_UP}" x2="{GAP1}" y2="{AY_UP}" stroke="{UP}" stroke-width="2" '
  f'marker-end="url(#up)"/>')
text((GAP0 + GAP1) / 2, AY_UP - 14, '× (1 + 0.1)', 16, FG, "600", "middle", MATH)
text((GAP0 + GAP1) / 2, AY_UP - 38, '할증 · 미래로 보낼 때는 곱함', 14, UP, "600", "middle")

# 현재로 (나눔)
a(f'<line x1="{GAP1}" y1="{AY_DN}" x2="{GAP0}" y2="{AY_DN}" stroke="{DOWN}" stroke-width="2" '
  f'marker-end="url(#dn)"/>')
text((GAP0 + GAP1) / 2, AY_DN + 26, '÷ (1 + 0.1)', 16, FG, "600", "middle", MATH)
text((GAP0 + GAP1) / 2, AY_DN + 50, '할인 · 현재로 당길 때는 나눔', 14, DOWN, "600", "middle")

# 하단 정리
a(f'<line x1="24" y1="{H-58}" x2="{W-24}" y2="{H-58}" stroke="{DIM}" stroke-width="1"/>')
text(24, H - 28, '이자율 · 할증률 · 할인율은 모두 같은 10%. 어느 방향으로 옮기느냐에 따라 이름만 달라짐',
     15, FG, "600")

a('</svg>')
open("/tmp/rv/rate.svg", "w").write("\n".join(svg))
print("written")
