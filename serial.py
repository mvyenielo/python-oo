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
        """ Create serial number and initialize and save start value """

        self.start = start
        self.initial = start


    def __repr__(self):
        return f"<SerialGenerator start={self.start}>"

    def generate(self):
        """ Generate number. If called again, increment current value by 1 """

        if self.start == self.initial:
            self.start += 1
            return self.initial
        else:
            self.start += 1
            return self.start - 1


        # Looked at solutions afterwards to see the difference
        # self.start += 1
        # return self.start - 1


    def reset(self):
        """ Reset current value to its original value """

        self.start = self.initial
