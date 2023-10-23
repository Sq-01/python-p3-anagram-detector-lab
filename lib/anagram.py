# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        anagrams = []
        normalized_word = self.normalize(self.word)
        for word in word_list:
            if normalized_word == self.normalize(word) and self.word.lower() != word.lower():
                anagrams.append(word)
        return anagrams

    @staticmethod
    def normalize(word):
        return sorted(word.lower())
