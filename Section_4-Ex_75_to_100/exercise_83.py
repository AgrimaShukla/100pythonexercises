# Monitor Size Detector
from screeninfo import get_monitors


for m in get_monitors():
    print(str(m))

width = get_monitors()[0].width
height = get_monitors()[0].height
print(f"Width: {width} and Height: {height}")