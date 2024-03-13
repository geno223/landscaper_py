## updates player 

player_update = {
    'money': 0,
    'tool': 0
}

## tool List

list_of_tools = [
    {'name': 'teeth', 'chargeable': 1, 'price': 0},
    {'name': 'rusty scissors', 'chargeable': 5, 'price': 5},
    {'name': 'old-time push lawnmower', 'chargeable': 50, 'price': 25},
    {'name': 'fancy lawnmower', 'chargeable': 100, 'price': 250},
    {'name': 'student team', 'chargeable': 250, 'price': 500}
]

## a player can give input to cut grass, upgrade a tool, or quit the game

def get_input():
    player_input = input("do you want to cut grass, upgrade a tool, or quit the game?")
    if(player_input == "cut"):
        cut_grass()
        
    elif(player_input == "upgrade"):
        upgrade_tool()
        
    elif(player_input == "quit"):
        quit()
    else:
        print("player needs to type cut, upgrade or quit to proceed!")
    get_input()



## a player can cut the grass and make money dependent on the tool they have. the player_status should update their money only in this case

def cut_grass():
    current_tool_ind = player_update['tool']
    tool_now = list_of_tools[current_tool_ind]
    service_charge = tool_now['chargeable']
    player_update['money'] += service_charge
    print( f"you have ${player_update['money']} and cutting with a {tool_now['name']}")
    win()


## a player can upgrade their cutting method. the player_status should update their tool only in this case

def upgrade_tool():
    player_update['tool'] += 1
    current_tool_ind = player_update['tool']
    tool_now = list_of_tools[current_tool_ind]
    # remove money for the charge of the scissors
    player_update['money'] -= tool_now['price']
    print( f"you upgraded to {tool_now['name']}")
    win()



## a player should be able to quit the game. print "the game ended"

def quit():
    print("better luck next time")

# a player can win the game if money is over 1000 and tool is at index 4 (student_team)
      
## start the game by getting input. run the input function, then runt the win function to double check if it should keep going

def win():
    if(player_update['tool'] == 4 and player_update['money'] > 1000):
        print("you won becasue you have more than 1000 dollars and cutting with a team")

get_input()








    