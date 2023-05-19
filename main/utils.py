def calculate_closest_points(points: str):
    points_list = [point.split(',') for point in points.split(';')]
    points_list = [(int(x), int(y)) for x, y in points_list]

    min_distance = float('inf')
    closest_points = []

    for i in range(len(points_list)):
        for j in range(i + 1, len(points_list)):
            distance = calculate_distance(points_list[i], points_list[j])

            if distance < min_distance:
                min_distance = distance
                closest_points = [points_list[i], points_list[j]]

    closest_points_str = ';'.join([','.join(map(str, point)) for point in closest_points])
    return closest_points_str


def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distance
