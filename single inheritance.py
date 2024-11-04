#parent cls single inheritance

class parent_dog():
    def __init__(self,breed):
        self.breed=breed

    def display(self):
        print(self.breed)

#child cls single inheritance

class child_dog(parent_dog):
    def __init__(self,breed,name,age):
        super().__init__(breed)
        self.name=name
        self.age=age

    def show(self):
        print( self.breed,self.name,self.age)

s=child_dog('Generic','puppy',4)
s.display()
s.show()   

class Grand:
    def __init__(self, house, land):
        self.house = house
        self.land = land

class Father(Grand):
    def __init__(self, house, land, bike):
        super().__init__(house, land)
        self.bike = bike

    def show(self):
        print(self.house, self.land, self.bike)

class Son(Father):
    def __init__(self, house, land, bike):
        super().__init__(house, land, bike)
        print("Son is a student")

s = Son('villa', 4, 'yamaha')
s.display()





































    
