def roll_call_dwarves(dwarves):
    for index, dwarf in enumerate(dwarves, start=1):
        print(f"{index}. {dwarf}")

def summon_captain_planet(planeteer_calls):
    capitalized_calls = [call.capitalize() + "!" for call in planeteer_calls]
    return capitalized_calls

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(strings):
    cheeses = ["cheddar", "gouda", "camembert"]
    for item in strings:
        if item in cheeses:
            return item
    return None