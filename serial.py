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
    def __init__(self, start=100):
        """ Create serial number and initialize and save start value """

        self.start = self.initial = start


    def __repr__(self):
        return f"<SerialGenerator start={self.start}, initial={self.initial}>"


    def generate(self):
        """ Generate number. If called again, increment current value by 1 """

        self.start += 1
        return self.start - 1


    def reset(self):
        """ Reset current value to its original value """

        self.start = self.initial
