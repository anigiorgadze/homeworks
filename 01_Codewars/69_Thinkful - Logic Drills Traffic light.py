# You're writing code to control your town's traffic lights. You need a function to handle each change from green, to yellow, to red, and then to green again.

def update_light(current):
    my_dict ={
        "green" : "yellow",
        "yellow" : "red",
        "red" : "green"
    }
    
    return my_dict[current]