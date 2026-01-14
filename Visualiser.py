import random
import math
import matplotlib.pyplot as plt

SITE_W, SITE_H = 200, 140
PLAZA_SIZE = 40
MIN_BOUNDARY = 10
MIN_BUILDING_DIST = 15
NEIGHBOR_RADIUS = 60

TOWER_A = (30, 20)
TOWER_B = (20, 20)

def rect_distance(a, b):
    ax1, ay1, aw, ah = a
    bx1, by1, bw, bh = b
    ax2, ay2 = ax1 + aw, ay1 + ah
    bx2, by2 = bx1 + bw, by1 + bh

    dx = max(bx1 - ax2, ax1 - bx2, 0)
    dy = max(by1 - ay2, ay1 - by2, 0)
    return math.hypot(dx, dy)

def overlaps(r1, r2):
    x1,y1,w1,h1 = r1
    x2,y2,w2,h2 = r2
    return not (x1+w1 <= x2 or x2+w2 <= x1 or y1+h1 <= y2 or y2+h2 <= y1)

def inside_site(x,y,w,h):
    return (
        x >= MIN_BOUNDARY and
        y >= MIN_BOUNDARY and
        x + w <= SITE_W - MIN_BOUNDARY and
        y + h <= SITE_H - MIN_BOUNDARY
    )

def generate_layout(numA=3, numB=5):
    plaza_x = (SITE_W - PLAZA_SIZE) / 2
    plaza_y = (SITE_H - PLAZA_SIZE) / 2
    plaza = (plaza_x, plaza_y, PLAZA_SIZE, PLAZA_SIZE)

    buildings = []

    def place(w,h):
        for _ in range(500):
            x = random.uniform(0, SITE_W - w)
            y = random.uniform(0, SITE_H - h)
            r = (x,y,w,h)
            if not inside_site(x,y,w,h):
                continue
            if overlaps(r, plaza):
                continue
            if any(rect_distance(r, b) < MIN_BUILDING_DIST for b in buildings):
                continue
            buildings.append(r)
            return True
        return False

    for _ in range(numA):
        place(*TOWER_A)
    for _ in range(numB):
        place(*TOWER_B)

    return buildings, plaza

def check_neighbor_rule(buildings):
    As = buildings[:3]
    Bs = buildings[3:]
    for a in As:
        if not any(rect_distance(a,b) <= NEIGHBOR_RADIUS for b in Bs):
            return False
    return True

def visualize(buildings, plaza, title):
    fig, ax = plt.subplots(figsize=(8,5))
    ax.set_xlim(0, SITE_W)
    ax.set_ylim(0, SITE_H)

    ax.add_patch(plt.Rectangle((0,0), SITE_W, SITE_H, fill=False))
    ax.add_patch(plt.Rectangle(plaza[:2], plaza[2], plaza[3], color='lightgrey'))

    for i,b in enumerate(buildings):
        color = 'red' if i < 3 else 'blue'
        ax.add_patch(plt.Rectangle(b[:2], b[2], b[3], color=color))
    
    ax.set_title(title)
    plt.show()

# Generate multiple layouts
for i in range(3):
    b,p = generate_layout()
    status = "VALID" if check_neighbor_rule(b) else "Neighbor Rule Violated"
    visualize(b,p,f"Layout {i+1} – {status}")
