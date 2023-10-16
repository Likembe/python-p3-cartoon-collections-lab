def roll_call_dwarves(dwarves):
    for i, dwarf in enumerate(dwarves,start=1):
        print(f"{i}. {dwarf}")

#Example usage
dwarves = ["Dopey", "Grumpy", "Bashful"]
roll_call_dwarves(dwarves)


def summon_captain_planet(captains):
    result = []
    for call in captains:
        #Modify the call and append it to the result list
        modified_call=call.capitalize() + "!"
        result.append(modified_call)
    return result

#Example usage
captains = ['carrot', 'cucumber', 'pepper']
captain_planet_calls = summon_captain_planet(captains)

print(captain_planet_calls)
    
def long_planeteer_calls(planeteer_calls):
    for call in planeteer_calls:
        if len(call) > 4:
            return True
    return False

#Example usage
planeteer_calls = ['axe', 'fire', 'water', 'heart']
result = long_planeteer_calls(planeteer_calls)
print(result)

def find_the_cheese(arr):
    for element in arr:
        if element == "cheddar":
            return element
    return None  # Return None if no cheese is found

# Example usage:
my_list = ["banana", "cheddar", "sock"]
cheese = find_the_cheese(my_list)
print(cheese)
