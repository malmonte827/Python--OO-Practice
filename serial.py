"""Python serial number generator."""

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
        """Make new generator , beggining at start"""
        self.start = start
        self.increment = self.start
    
    def generate(self):
        """Returns next incrementing number"""
        self.increment += 1
        return self.increment - 1
        
    def reset(self):
        """Resets number to start"""
        self.increment = self.start

