class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __add__(self, other):
        if isinstance(other, Time):
            total_seconds = self.to_seconds() + other.to_seconds()
            return Time.from_seconds(total_seconds)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Time):
            return self.to_seconds() > other.to_seconds()
        return NotImplemented

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    @classmethod
    def from_seconds(cls, total_seconds):
        hours = total_seconds // 3600
        total_seconds %= 3600
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return cls(hours, minutes, seconds)

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

# Testing the class
if __name__ == "__main__":
    t1 = Time(1, 45, 50)
    t2 = Time(0, 30, 20)
    t3 = t1 + t2  # Should be (2, 16, 10)

    print("t1:", t1)  # 01:45:50
    print("t2:", t2)  # 00:30:20
    print("t3:", t3)  # 02:16:10
    print(t1 > t2)    # True
    print(t2 > t1)    # False
