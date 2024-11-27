 #! Challenge 1: Update the Constructor
class Player:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team

jason = {"name":"Jason Tatum" , "age":24 ,"position":"small forward" , "team":"boston celtics"}
player_jason = Player(jason["name"],jason["age"],jason["position"],jason["team"])

print(player_jason.name)
print(player_jason.age)
print(player_jason.position)
print(player_jason.team)

#! Challenge 2: Create instances using individual player dictionaries.
class Player:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team
    def plyer(self):
        print(self.name)
        print(self.age)
        print(self.position)
        print(self.team)

    
        

k = Player("Kevin Durant",34,"small forward","brooklyn nets")
print(k.plyer())

j = Player("Jason Tatum",24,"small forward","boston celtics")
print(j.plyer())

ky = Player("Kyrie Irving",32,"point guard","brooklyn nets")
print(ky.plyer())

#! Challenge 3: Make a list of Player instances from a list of dictionaries
class Player:
    def __init__(self, players):
        self.name = players.name
        self.age = players.age
        self.position = players.position
        self.team = players.team

players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33, "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32, "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
    	"name": "", 
    	"age":16, 
    	"position": "P", 
    	"team": "en"
    }
]

new_team = []

for i in range (0 , len(players) , 1):
    new_team.append(players[i])

print(new_team)




