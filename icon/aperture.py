import math

def draw_logo(f, cx, cy, n, inner_r, outer_r):
  f.write(f"<circle cx=\"{cx}\" cy=\"{cy}\" r=\"{outer_r}\" stroke=\"black\" stroke-width=\"1\" fill=\"none\"/>\n")
  inner = []
  for i in range(0, n):
    rads = (math.pi * 2 / n)
    rad = i * rads
    x1 = cx + inner_r * math.cos(rad)
    y1 = cy + inner_r * math.sin(rad)
    #print(f"x{i} = 60 * cos({i} * pi * 2 / n), y{i}= 60 * sin({i} * pi * 2 / n),")
    inner.append((x1, y1))

  for i in range(0, n):
    ip = (i + 1) % n

    theta = math.atan2(inner[ip][1] - inner[i][1], inner[ip][0] - inner[i][0])

    length = (inner_r * math.sin(math.pi / n)) + math.sqrt(math.pow(outer_r,2) -  math.pow(inner_r * math.cos(math.pi/n), 2))

    ext_x = inner[i][0] + length * math.cos(theta)
    ext_y = inner[i][1] + length * math.sin(theta)

    #print(f"u = arctan2(y{ip}- y{i}, x{ip} - x{i}),")
    #print(f"o{i} = x{i} + l * cos(u),")
    #print(f"v{i} = y{i} + l * sin(u)")
    #print(f"(o{i})^2 + (v{i})^2 = 100^2")
    f.write(f"<path d=\"M{inner[i][0]} {inner[i][1]} L{ext_x} {ext_y}\" stroke=\"black\" stroke-width=\"1\" fill=\"none\"/>\n")

    f.write(f"<path d=\"M{cx - 25} {cy - 20} l50 0 l0 40l-50 0 z l25 25 l25 -25\" stroke=\"black\" stroke-width=\"1\" fill=\"none\"/>\n")


with open("./aperture.svg", "w") as f:
  f.write(f"<?xml version=\"1.0\"?>\n")
  f.write(f"<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"2000\" height=\"2000\" viewBox=\"0 0 2000 2000\">\n")
  for i in [0, 1, 2, 3, 4]:
    draw_logo(f, 120 + i*240, 120, 3+i, 60, 100)
  for i in [0, 1, 2, 3, 4]:
    draw_logo(f, 120 + i*240, 360, 8+i, 70, 120)
    #f.write(f"<text text-anchor=\"center\" x=\"{midx}\" y=\"{midy}\" fill=\"blue\">{i}={theta}</text>")

  f.write("</svg>\n")
