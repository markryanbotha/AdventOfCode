with open("input.txt", "r") as f:
    c = [line.split(",") for line in f]
    coords = [(int(line[0].strip()), int(line[1].strip())) for line in c]

# store edges as line segments for fast iteration
edgeSegments = [(coords[i], coords[(i + 1) % len(coords)])
                for i in range(len(coords))]


def isInPolygon(corner):
    px, py = corner

    # instead of checking if ray crosses each point (slow for large grids),
    # we check if each edge segment crosses the ray (fast - only n segments)
    crosses = 0
    for (x1, y1), (x2, y2) in edgeSegments:
        # check if point is on this edge
        if x1 == x2 == px and min(y1, y2) <= py <= max(y1, y2):
            return True
        if y1 == y2 == py and min(x1, x2) <= px <= max(x1, x2):
            return True
        # only vertical edges can be crossed by horizontal ray
        if x1 == x2 and x1 > px and min(y1, y2) <= py < max(y1, y2):
            crosses += 1

    return crosses % 2 == 1


def edgeCrossesRect(rx1, ry1, rx2, ry2):
    # for concave polygons, all 4 corners can be valid but an edge still cuts through the middle
    # check if any edge passes through the interior (not boundary) of the rectangle
    # if edge x is strictly between left/right AND its y-range overlaps, it cuts through
    left, right = min(rx1, rx2), max(rx1, rx2)
    bottom, top = min(ry1, ry2), max(ry1, ry2)

    for (x1, y1), (x2, y2) in edgeSegments:
        if x1 == x2:  # vertical edge
            if left < x1 < right and not (max(y1, y2) <= bottom or min(y1, y2) >= top):
                return True
        else:  # horizontal edge
            if bottom < y1 < top and not (max(x1, x2) <= left or min(x1, x2) >= right):
                return True
    return False


# Checking all combinations of corners
def checkAllCorners(x1, x2, y1, y2):
    corners = ((x1, y1), (x1, y2), (x2, y1), (x2, y2))
    for corner in corners:
        if not isInPolygon(corner):
            return False
    return True


maximum = 0
for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        x1, x2 = coords[i][0], coords[j][0]
        y1, y2 = coords[i][1],  coords[j][1]
        # For each combination, check the corners of the rectangle
        if checkAllCorners(x1, x2, y1, y2) and not edgeCrossesRect(x1, y1, x2, y2):
            # inclusive of current line with the + 1
            x = abs(x1 - x2) + 1
            y = abs(y1 - y2) + 1
            area = x * y
            maximum = max(maximum, area)

print(maximum)
