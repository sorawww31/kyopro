
import sys
import math

import numpy as np

def main(lines):
    m = int(lines[0])
    points = []
    
    flag = False

    #. 柱のクラスターを保持
    pillars = []
    i=1
    while i <= m:
        points = []
        theta, r = map(float, lines[i].split())
        while r < 30 :
            # x y座標平面に置き換え
            x, y = r * math.cos(math.radians(theta)), r * math.sin(math.radians(theta))
            points.append((x, y))
            
            i += 1
            if i <= m:
                theta, r = map(float, lines[i].split())
            else:
                break
        if points:
            pillars.append(points)
        
        i+=1
    
    # theta=0にまたがる柱をくっつける
    _, first_r = map(float, lines[1].split())
    _ , last_r = map(float, lines[-1].split())
    flag = (first_r < 30 and last_r < 30)
    if flag == True and len(pillars) > 1:
        first_pillar = pillars.pop(0)
        last_pillar = pillars.pop(-1)
        pillars.append(first_pillar + last_pillar)
    print(len(pillars))
    for pillar in pillars:
        mean_xy = np.mean(np.array(pillar), axis = 0)
        print(f"{mean_xy[0]},{mean_xy[1]}")
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)