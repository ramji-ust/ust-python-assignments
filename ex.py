from functools import total_ordering

@total_ordering
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __eq__(self, other):
        return self.pages == other.pages

    def __lt__(self, other):
        return self.pages < other.pages

# Now __le__, __gt__, __ge__ are auto-created!

b1 = Book("Python 101", 300)
b2 = Book("AI Basics", 400)

print(b1 < b2)   # True
print(b1 == b2)  # False
print(b1 >= b2)  # False (auto-generated)
