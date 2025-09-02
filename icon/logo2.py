import math
import io
import os
import sys
from cairosvg import svg2png

borderRadius = 20

def draw_logo(f, cx, cy, n, inner_r, outer_r, drawAperture, stroke, strokeWidth):
  inner = []
  for i in range(0, n):
    rads = (math.pi * 2 / n)
    rad = i * rads
    x1 = cx + inner_r * math.cos(rad)
    y1 = cy + inner_r * math.sin(rad)

    inner.append((x1, y1))

  for i in range(0, n):
    ip = (i + 1) % n

    theta = math.atan2(inner[ip][1] - inner[i][1], inner[ip][0] - inner[i][0])

    length = (inner_r * math.sin(math.pi / n)) + math.sqrt(math.pow(outer_r,2) -  math.pow(inner_r * math.cos(math.pi/n), 2))

    ext_x = inner[i][0] + length * math.cos(theta)
    ext_y = inner[i][1] + length * math.sin(theta)

    if drawAperture:
      f.write(f"<path d=\"M{inner[i][0]} {inner[i][1]} L{ext_x} {ext_y}\" stroke=\"url(#fade)\" stroke-width=\"{strokeWidth}\" fill=\"none\"/>\n")

  if False:
    draw_mail_icon(f, inner_r, cx, cy, stroke, strokeWidth)
  if drawAperture:
    f.write(f"<circle cx=\"{cx}\" cy=\"{cy}\" r=\"{outer_r}\" stroke=\"{stroke}\" stroke-width=\"{strokeWidth}\" fill=\"none\"/>\n")

def draw_mail_icon(f, inner_r, cx, cy, stroke, strokeWidth):
    mail_x = inner_r * 1.2
    mail_y = inner_r * 1
    rect_x = cx - mail_x/2
    rect_y = cy - mail_y/2
    f.write(f"<g transform=\"rotate(20 {cx} {cy})\">")
    f.write(f"""<rect x="{rect_x}" y="{rect_y}" width="{mail_x}" height="{mail_y}" stroke="{stroke}" stroke-width="{strokeWidth}" fill="none" ry="{borderRadius}" rx="{borderRadius}"/>\n""")
    f.write(f"""<path d="
      M{rect_x + borderRadius} {rect_y + borderRadius}
      l{mail_x/2 - borderRadius} {mail_y/2 - borderRadius}
      a{borderRadius},{borderRadius} 0 0 0 {borderRadius},{0}
      L{rect_x + mail_x -borderRadius} {rect_y + borderRadius}"
      stroke="{stroke}" stroke-width="{strokeWidth}" fill="none"
      stroke-linecap="round"
      />\n""")
    f.write("</g>")



def write_logo(f, fill, stroke, strokeWidth):
  f.write(f"<?xml version=\"1.0\"?>\n")
  f.write(f"<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"1000\" height=\"1000\" viewBox=\"0 0 1000 1000\">\n")
  f.write("""<defs>
  <linearGradient id="fade" x1="0%" y1="0%" x2="100%" y2="0%" gradientUnits="userSpaceOnUse">
  <stop offset="0%" style="stop-color:#f55d42;stop-opacity:1" />
  <stop offset="100%" style="stop-color:#f5b641;stop-opacity:1" />
  </linearGradient>
  </defs>
  """)
  f.write(f"""<rect x="0" y="0" width="1000" height="1000" stroke="none" fill="{fill}" ry="{borderRadius}" rx="{borderRadius}"/>\n""")
  f.write(f"""<rect x="150" y="150" width="600" height="600" stroke="{stroke}" stroke-width="{strokeWidth}" fill="none" ry="{borderRadius}" rx="{borderRadius}"/>\n""")
  f.write(f"""<path d="
  M750 200
  l30 0
  a{borderRadius},{borderRadius} 0 0 1 {borderRadius},{borderRadius}
  l0 560
  a{borderRadius},{borderRadius} 0 0 1 {-borderRadius},{borderRadius}
  l-560 0
  a{borderRadius},{borderRadius} 0 0 1 {-borderRadius},{-borderRadius}
  l0 -30\"
  stroke="{stroke}" stroke-width="{strokeWidth}" fill="none"/>\n""")
  f.write(f"""<path d="
  M800 250
  l30 0
  a{borderRadius},{borderRadius} 0 0 1 {borderRadius},{borderRadius}
  l0 560
  a{borderRadius},{borderRadius} 0 0 1 {-borderRadius},{borderRadius}
  l-560 0
  a{borderRadius},{borderRadius} 0 0 1 {-borderRadius},{-borderRadius}
  l0 -30"
  stroke="{stroke}" stroke-width="{strokeWidth}" fill="none" />\n""")

  draw_logo(f, 450, 450, 8, 150, 240, True, stroke, strokeWidth)

  f.write("</svg>\n")


if len(sys.argv) < 3:
  print(f"must specify stroke and fill: {sys.argv[0]} <stroke> <fill>")
  print("specify fade for the fade, and none for transparent background")
  sys.exit(2)

fill = sys.argv[2]
stroke = sys.argv[1]



buf = io.StringIO("")

strokeArg = "url(#fade)" if stroke == "fade" else stroke

write_logo(buf, fill, strokeArg, 30)

fBase = f"./logo-{stroke}-{fill}"
svg = fBase + ".svg"
with open(svg, "w") as f:
  buf.seek(0)
  f.write(buf.read())

svg2png(url=svg, write_to=fBase + ".png")
