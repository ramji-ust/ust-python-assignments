class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        return f"({self.x}, {self.y})"

# Testing the class
v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)

v3 = v1 + v2  # Should return Vector2D(4, 6)
v4 = v1 - v2  # Should return Vector2D(2, 2)

print(v3)  # Output: (4, 6)
print(v4)  # Output: (2, 2)
print(v3 == Vector2D(4, 6))  # Output: True