class Love:

    def __init__(self, first_love, last_love):
        self.first_love = first_love
        self.last_love = last_love

    @property
    def email_of_love(self):
        return '{}.{}@it.is.love'.format(self.first_love, self.last_love)

    @property
    def fulllove(self):
        return '{} {}'.format(self.first_love, self.last_love)
    
    @fulllove.setter
    def fulllove(self, name):
        first_love, last_love = name.split(' ')
        self.first_love = first_love
        self.last_love = last_love
    
    @fulllove.deleter
    def fulllove(self):
        print('Delete Name_of_love!')
        self.first_love = None
        self.last_love = None


lov_1 = Love('Fairy', 'Fly')
lov_1.fulllove = "Marmeid Water"

print(lov_1.first_love)#Marmeid
print(lov_1.email_of_love)#Marmeid.Water@it.is.love
print(lov_1.fulllove)#Marmeid Water

del lov_1.fulllove #Delete Name_of_love