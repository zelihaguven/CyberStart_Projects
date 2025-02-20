import math

# Noktaların tanımlanması
points = [(1, 2), (3, 4), (5, 6), (7, 8), (2, 1)]

# Öklid mesafesi için bir fonksiyon
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# Mesafelerin hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafenin bulunması
min_distance = min(distances)

# Sonuçların yazdırılması
print("Hesaplanan mesafeler:", distances)
print("Minimum mesafe:", min_distance)