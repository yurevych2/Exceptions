import test_character

class Cursor:
 
    def __init__(self, document):
        self.document = document
        self.position = 0

    def forward(self):
        self.position += 1
          
    def back(self):
        self.position -= 1

    def home(self):
        try:
            while self.document.characters[
                self.position-1] != '\n':
                self.position -= 1
                if self.position == 0: 
                    break
        except IndexError:
            raise test_character.IndexOut
             
    def end(self):
        try:
            while self.position < len(self.document.characters) \
                                and self.document.characters[self.position] != '\n':
                self.position += 1
        except IndexError:
            raise test_character.IndexOut
