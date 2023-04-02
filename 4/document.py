import test_character

class Document:    

    def __init__(self):        
        self.characters = []        
        self.cursor = 0        
        self.filename = ''    
        
    def insert(self, character):        
        self.characters.insert(self.cursor, character)        
        self.cursor += 1    
    
    def delete(self):  
        try:      
            del self.characters[self.cursor]  
        except IndexError:
            raise test_character.IndexOut()
              
    
    def save(self):
        try:
            with open(self.filename, 'w') as f:            
                f.write(''.join(self.characters))    
        except FileNotFoundError:
            raise test_character.NotFound
    
    def forward(self):        
        self.cursor += 1    
    
    def back(self):        
        self.cursor -= 1
