import math

def calculate_distance(point1, point2):
  """Calculates the Euclidean distance between two points.

  Args:
    point1: A tuple representing the first point (x1, y1).
    point2: A tuple representing the second point (x2, y2).

  Returns:
    The Euclidean distance between the two points.
  """
  x1, y1 = point1
  x2, y2 = point2
  return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def find_closest_pair_distance(points):
  """Finds the distance between the closest pair of points.

  Args:
    points: A list of tuples, where each tuple represents a point (x, y).

  Returns:
    The distance between the closest pair of points.
  """
  min_distance = float('inf')
  for i in range(len(points)):
    for j in range(i + 1, len(points)):
      distance = calculate_distance(points[i], points[j])
      min_distance = min(min_distance, distance)
  return min_distance

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
  # Read the number of points
  n = int(input())

  # Read the points
  points = []
  for _ in range(n):
    x, y = map(float, input().split())
    points.append((x, y))

  # Find and print the closest pair distance
  closest_distance = find_closest_pair_distance(points)
  print(f"{closest_distance:.6f}")
