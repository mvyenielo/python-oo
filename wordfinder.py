class WordFinder:
    """Word Finder: finds random words from a dictionary."""
def __init__(self, path):
    self.path = path
    self.word_list = read_file()
    #file.close()

def read_file(self):
    file = open(self.path)
    return file.read()

def random():
