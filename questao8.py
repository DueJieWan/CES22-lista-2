
class Trap():
    n_traits = 5
    
    def __init__(self, size, thiccness, age, personality, race, affectionLevel=0):
        self.size = size
        self.thiccness = thiccness
        self.age = age
        self.personality = personality
        self.race = race
        self.affectionLevel = affectionLevel

    @staticmethod
    def is_ready(affectionLevel):
        return affectionLevel > 80
    
    @staticmethod
    def mean(x, y):
        return (x + y)/2
    
    def fuse_traps(self, trap2):
        self.size = self.mean(self.size, trap2.size)
        self.age = self.mean(self.age, trap2.age)
        self.thiccness = self.mean(self.thiccness, trap2.thiccness)
        self.affectionLevel = 0

    @classmethod
    def get_n_traits(cls):
        return cls.n_traits


    def interfcourse(self):
        raise NotImplementedError

class TheAct(Trap):
    def __init__(self, duration, satisfaction):
        self.duration = duration
        self.satisfaction

    
        

    