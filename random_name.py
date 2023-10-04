import random

# Lists of adjectives and animals
adjectives = [
    "Amusing", "Bubbly", "Cheerful", "Dapper", "Eccentric", "Flamboyant",
    "Giddy", "Hilarious", "Jovial", "Kooky", "Lively", "Mirthful",
    "Nonsensical", "Outlandish", "Peculiar", "Quirky", "Rambunctious", "Silly",
    "Ticklish", "Unconventional", "Vivacious", "Whimsical", "Zany",
    "Absurd", "Bizarre", "Crazy", "Droll", "Eccentric", "Funky",
    "Goofy", "Hysterical", "Jolly", "Kaleidoscopic", "Ludicrous", "Merry",
    "Nutty", "Oddball", "Playful", "Quixotic", "Ridiculous", "Surreal",
    "Topsy-turvy", "Unpredictable", "Vibrant", "Wacky", "Zigzagging"
]
animals = [
    "Aardvark", "Badger", "Beaver", "Bison", "Bobcat", "Boar",
    "Cheetah", "Coyote", "Cobra", "Dolphin", "Duck", "Deer",
    "Eagle", "Elephant", "Fox", "Ferret", "Falcon", "Frog",
    "Giraffe", "Gazelle", "Gorilla", "Grizzly", "Hawk", "Hyena",
    "Iguana", "Impala", "Jackal", "Jaguar", "Kangaroo", "Koala",
    "Lemur", "Lion", "Lizard", "Lynx", "Mongoose", "Mule",
    "Narwhal", "Newt", "Nightingale", "Ocelot", "Octopus", "Otter",
    "Panda", "Penguin", "Platypus", "Porcupine", "Python", "Puma",
    "Quokka", "Quail", "Raccoon", "Rattlesnake", "Rhinoceros", "Rabbit",
    "Salamander", "Seagull", "Sloth", "Squirrel", "Stingray", "Skunk",
    "Toucan", "Tapir", "Tiger", "Turtle", "Uakari", "Umbrellabird",
    "Vulture", "Viper", "Walrus", "Wombat", "Wallaby", "Weasel",
    "Yak", "Yellowjacket", "Yaksha", "Yapok", "Yardang", "Yowies",
    "Zebra", "Zonkey", "Zorse"
]

def generate_random_name():
    # Randomly select a letter from the alphabet
    first_letter = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    
    # Filter adjectives that start with the selected letter
    possible_adjectives = [adj for adj in adjectives if adj.startswith(first_letter)]
    
    # Filter animals that start with the selected letter
    possible_animals = [animal for animal in animals if animal.startswith(first_letter)]
    
    if not possible_adjectives or not possible_animals:
        # If there are no adjectives or animals starting with the selected letter, try again
        return generate_random_name()
    
    # Randomly select one adjective and one animal
    selected_adjective = random.choice(possible_adjectives)
    selected_animal = random.choice(possible_animals)
    
    return f"{selected_adjective} {selected_animal}"

if __name__ == "__main__":
    random_name = generate_random_name()
    print(random_name)
