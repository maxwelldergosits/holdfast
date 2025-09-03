from cairosvg import svg2png

otherContent = """
      <g id="photo" transform="scale({contentScale}) translate(220 80)">
        <!--
        <g id="plant" transform="translate(22 0)">
          <path d="
            M138.54,149.46C106.62,96.25,149.18,43.05,239.63,48.37,245,138.82,191.75,181.38,138.54,149.46Z
            M88.47,160.47c22.8-38-7.6-76-72.21-72.21C12.46,152.87,50.47,183.27,88.47,160.47Z
            M200,88l-61.25,61.25A64,64,0,0,0,120,194.51V224
            M56,128 L120,192
          " fill="none" stroke="{stroke}" stroke-linecap="round" stroke-linejoin="round" stroke-width="{strokeWidth/contentScale}"
          />
        </g>
        -->
        <!--
        <g id="mountain" transform="translate(22 0)">
          <circle cx="164" cy="52" r="20" fill="none" stroke="{stroke}" stroke-linecap="round" stroke-linejoin="round" stroke-width="{strokeWidth/contentScale}"/>
          <path d="M8,200,81.1,75.94a8,8,0,0,1,13.8,0L168,200Z" fill="none" stroke="{stroke}" stroke-linecap="round" stroke-linejoin="round" stroke-width="{strokeWidth/contentScale}"/>
          <line x1="50.35" y1="128" x2="125.65" y2="128" fill="none" stroke="{stroke}" stroke-linecap="round" stroke-linejoin="round" stroke-width="{strokeWidth/contentScale}"/>
          <path d="M146.61,163.71l33.06-55.79a8,8,0,0,1,13.76,0L248,200H168" fill="none" stroke="{stroke}" stroke-linecap="round" stroke-linejoin="round" stroke-width="{strokeWidth/contentScale}"/>
        </g>
        -->
        <!--
        <g id="person" transform="translate(22 -5)">
          <rect width="256" height="256" fill="none"/>
          <circle cx="152" cy="48" r="24" fill="none" stroke="{stroke}" stroke-linecap="round" stroke-linejoin="round" stroke-width="{strokeWidth/contentScale}"/>
          <path d="M48,129s56-52.65,88-24.87C153.94,119.67,168,144,208,144" fill="none" stroke="{stroke}" stroke-linecap="round" stroke-linejoin="round" stroke-width="{strokeWidth/contentScale}"/>
          <polyline points="152 232 152 176 109.54 145.67" fill="none" stroke="{stroke}" stroke-linecap="round" stroke-linejoin="round" stroke-width="{strokeWidth/contentScale}"/>
          <line x1="129.53" y1="99.69" x2="72" y2="232" fill="none" stroke="{stroke}" stroke-linecap="round" stroke-linejoin="round" stroke-width="{strokeWidth/contentScale}"/>
        </g>
        -->
      </g>
      """

strokeWidth = 8
contentScale = .5
stroke = "url(#fade)"
svg = f"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000"
  xmlns:xlink="http://www.w3.org/1999/xlink">
  <defs>
    <linearGradient id="fade" x1="5%" y1="0%" x2="25%" y2="0%" gradientUnits="userSpaceOnUse">
    <stop offset="0%" style="stop-color:#f55d42;stop-opacity:1" />
    <stop offset="100%" style="stop-color:#f5b641;stop-opacity:1" />
    </linearGradient>
  </defs>
  <g transform="scale(3.9)">
      <g id="grab" transform="translate(0 0)">
      <path d="
      M128 96
      m70,20
      h0
      a82.38,82.38,0,0,1,40,70.65
      v41.35
      m-61,0
      l-22.26 -34
      a20,20,0,0,1,34.64 -20
      l6.58 16.31
      v-160
      a8,8,0,0,0-8-8
      h-120
      a8,8,0,0,0,-8,8
      v180
      a8,8,0,0,0,8,8
      h100
      " fill="none" stroke="{stroke}" stroke-linecap="round" stroke-linejoin="round" stroke-width="{strokeWidth}"/>
      </g>
      <g id="photo" fill="{stroke}" fill-rule="nonzero" >
        <path
        d="
        M168,156
        h-80
        a8,8,0,0,1-8-8
        v-56
        a8,8,0,0,1,8,-8
        h16
        l8,-12
        h32
        l8,12
        h16
        a8,8,0,0,1,8,8
        v56
        a8,8,0,0,1,-8,8
        z
        m-65,-36
        a 25 25 0 0 0 50 0
        a 25 25 0 0 0 -50 0
        m9,0
        a 16 16 0 0 0 32 0
        a 16 16 0 0 0 -32 0
        "/>
      </g>
    </g>
</svg>
"""

ugh = """
"""

fBase = f"./logo-hand"
svgPath = fBase + ".svg"

with open(svgPath, "w") as f:
  f.write(svg)


svg2png(url=svgPath, write_to=fBase + ".png")
