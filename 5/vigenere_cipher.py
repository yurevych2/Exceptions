'''
Module.
'''

class VigenereCipher:
    '''Class docstring.'''
    def init(self, keyword) -> None:
        self.keyword = keyword

    def extend_keyword(self, number):
        '''Method that extend.'''
        repeats = number // len(self.keyword) + 1
        return (self.keyword * repeats)[:number]

    def _code(self, text, combine_func):
        '''One more method.'''
        text = text.replace(' ', '').upper()
        combined = []
        keyword = self.extend_keyword(len(text))
        for p,k in zip(text, keyword):
            combined.append(combine_func(p,k))  
        return ''.join(combined)

    def encode(self, plaintext):
        '''Encoding.'''
        return self._code(plaintext, combine_character)

    def decode(self, ciphertext):
        '''Decoding.'''
        return self._code(ciphertext, separate_character)

def combine_character(plain, keyword):
    '''Function for combing two items.'''
    plain = plain.upper()
    keyword = keyword.upper()
    plain_num = ord(plain) - ord('A')
    keyword_num = ord(keyword) - ord('A')
    return chr(ord('A') + (plain_num + keyword_num) % 26)

def separate_character(cypher, keyword):
    '''Function separate_character.'''
    cypher = cypher.upper()
    keyword = keyword.upper()
    cypher_num = ord(cypher) - ord('A')
    keyword_num = ord(keyword) - ord('A')
    return chr(ord('A') + (cypher_num - keyword_num) % 26)
