class user :
    def __init__(self,first_name,last_name,email,age,is_rewarded_member,gold_card_points):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewarded_member = is_rewarded_member
        self.gold_card_points = gold_card_points
    
    def display_info(self):
        print(f"First Name :{self.first_name} ")
        print(f"Last Name :{self.last_name} ")
        print(f"Email :{self.email} ")
        print(f"Age :{self.age} ")
        print(f"Is he a rewarded member ? :{self.is_rewarded_member} ")
        print(f"Number of gold card points :{self.gold_card_points} ")

    def enroll(self):
        self.is_rewarded_member = reward
        self.gold_card_points = nbPoints

        print(f"rewarded member status : {reward}")
        print(f"New number of gold cards points : {nbPoints}")

    def spend_points(self,amount):
        if amount < nbPoints :
            print(f"Newest number of gold cards points : {amount}")
        else:
            print(f"New number of gold cards points : {nbPoints}")





info = user("John" , "DOE" , "johndoe@gmail.com" , 33 , False , 0 )

info.display_info()
reward = True
nbPoints = 200
info.enroll()
info.spend_points(100)

