import random

random_int = random.randint(0,100)
print(random_int)
random_float = random.random() *3
print(random_float)
love_score = random.randint(1,100)
print(f"Your love score is {love_score}")

#list
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina",
                      "New Hampshire", "Virginia", "New York",
                        "North Carolina", "Rhode Island", "Vermont", 
                        "Kentucky", "Tennessee", "Ohio", "Louisiana",
                          "Indiana", "Mississippi", "Illinois", 
                          "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america)


#dirty_dozen = ["Strawberries", "Spinach", "Kale ", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale","Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

