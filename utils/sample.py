class CountCharacter(object):

    def __init__(self, input_words=None):
        """
        Args:
            input_word(str): given words
        """
        self.input_words = input_words
        
    def count(self, character):
        """
        Count the number of character we look for in given words
        
        Args:
            character(str): a character look for

        Return(int): the number of character
        
        Example:
            >>> cc = CountCharacter("Hello World")
            >>> cc.Count('l')
            3
        """
        c_list = [i for i in self.input_words]
        n = sum([True for char in c_list if char == character])
        return n
