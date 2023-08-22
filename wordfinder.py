import random

class WordFinder:
    """ Word Finder: finds random words from a dictionary. """

    def __init__(self, path):
        """ Generates list of words """

        self.path = path
        self.word_list = self.read_file()


    def read_file(self):
        """ Creates a file out of the path and converts the file into a list """


        file = open(self.path)

        text = file.read()

        return text.split("\n")


    def random(self):
        """ Generates a random word from the word list """

        return random.choice(self.word_list)
