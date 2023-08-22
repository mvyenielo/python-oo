class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """Create serial number and initialize and save start value"""
        self.start = start
        self.initial = start

    def __repr__(self):
        return f"<SerialGenerator start={self.start}>"

    def generate(self):
        self.start+=1
        return self.start

    def reset(self):
        self.start = self.initial
        return self.start



