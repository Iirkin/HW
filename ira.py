class Nature:
    def __init__(self, classes):
        self.classes = classes
    def __str__(self):
        return f'Class is ({self.classes!r})'
    @classmethod
    def plants(cls):
        return cls(['moss', 'trees', 'flowers', 'water plants'])
    @classmethod
    def fungi(cls):
        return cls(['mushrooms', 'fungus'])
    @staticmethod
    def fungi_s():
        return "Специалисты насчитывают до 100 тыс. видов грибов на нашей планете" 
print(Nature.fungi())
print(Nature.fungi_s())