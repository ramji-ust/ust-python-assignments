from functools import total_ordering

@total_ordering
class Product:
    def __init__(self, name: str, rating: float):
        self.name = name
        self.rating = rating

    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.rating == other.rating

    def __lt__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.rating < other.rating

    def __repr__(self):
        return f"{self.name}({self.rating})"
    
    

# === SAMPLE TEST CASE ===
if __name__ == "__main__":
    p1 = Product("Laptop", 4.5)
    p2 = Product("Tablet", 4.7)
    p3 = Product("Phone", 4.5)
    p4 = Product("Monitor", 4.2)

    print("Sorted Products:", sorted([p1, p2, p3, p4]))
    print("p1 == p3:", p1 == p3)
    print("p1 < p2:", p1 < p2)
    print("p2 >= p4:", p2 >= p4)
