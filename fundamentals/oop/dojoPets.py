class Ninja:
    def __init__(self,first_name,last_name,pet,treats,pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
        #self.animal = Pet("chiwawa","caniche", "trick1" , 17 , 22)

    def walk(self):
        self.pet.play()
        return self


    def feed(self):
        if len(self.pet_food) > 0:
            food = self.pet_food
            print(food)
            self.pet.eat(self)

        print("you need food")
        return self


    def bathe(self):
        self.pet.noise()
        
        return self


class Pet:
    def __init__(self,name,type,tricks, noise):
        self.name = name 
        self.type = type 
        self.tricks = tricks
        self.energy = 17
        self.health = 22
        self.noise = noise
        

    def sleep(self):
        self.energy += 25
        return self
    
    def eat(self):
        self.energy += 5
        self.health += 10
        print(my_petfood)
        #print(self.energy)

        return self

    def play(self):
        self.health += 5
        self.energy -= 8
        return self
    
    def noise(self):
        print(self.noise)
        

my_petfood = ["salami", "cheese", "egg"]

tom = Pet("tom", "dog", ["trick1", "trick2"], "hop hop")
ninjaA = Ninja("gabriel" , "silva" , "dog" , "treat1" , my_petfood)
ninjaA.feed().walk().bathe()

