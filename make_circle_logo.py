from PIL import Image, ImageDraw
import sys

if len(sys.argv) < 2:
    print("Usage: python make_circle_logo.py input.png [output.png]")
    sys.exit(1)

inp = sys.argv[1]
outp = sys.argv[2] if len(sys.argv) > 2 else "static/logo_circle.png"

im = Image.open(inp).convert("RGBA")
w,h = im.size

# 1) hapus background putih (threshold adjustable)
threshold = 240
pixels = im.getdata()
new_pixels = []
for r,g,b,a in pixels:
    if r >= threshold and g >= threshold and b >= threshold:
        new_pixels.append((255,255,255,0))
    else:
        new_pixels.append((r,g,b,a))
im.putdata(new_pixels)

# 2) buat mask bundar dan paste
mask = Image.new('L', (w,h), 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0,0,w,h), fill=255)

out = Image.new('RGBA', (w,h), (255,255,255,0))
out.paste(im, (0,0), mask=mask)

out.save(outp)
print("Saved:", outp)
