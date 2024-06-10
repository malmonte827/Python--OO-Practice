"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """
    >>> wf = WordFinder("/Users/student/words.txt")
    3 words read

    >>> wf.random()
    'cat'

    >>> wf.random()
    'cat'

    >>> wf.random()
    'porcupine'

    >>> wf.random()
    'dog'
    """
    def __init__(self, file):
        """opens and reads file and outputs number of items read"""
        path = open(file)

        self.words = self.words(path)

        print(f"{len(self.words)} words read")

    def words(self, path):
        """Loops through path and removes leading and trailing caracters"""
        return [w.strip() for w in path]

    def random(self):
        """returns a random word"""
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):

    def words(self,path):
        """Loops through path and removes leading and trailing caracters. skips over blank lines and comments"""
        return [w.strip() for w in path if w.strip() and not w.startswith('#')]

