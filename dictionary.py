import random

#######################################################
###### def bank for play 2 ############################
def draw_board(spots):
  board = (f"|{spots[1]}|{spots[2]}|{spots[3]}|\n"
            f"|{spots[4]}|{spots[5]}|{spots[6]}|\n"
            f"|{spots[7]}|{spots[8]}|{spots[9]}|")
  print(board)

def check_turn(turn):
  if turn % 2 ==0: return "0"
  else: return "X"

def check_for_win(spots):
  #handles horizontal cases
  if    (spots[1] == spots[2] == spots[3]) \
    or   (spots[4] == spots[5] == spots[6]) \
    or   (spots[7] == spots[8] == spots[9]):
    return True
  #handels vertical
  elif  (spots[1] == spots[4] == spots[7]) \
    or   (spots[2] == spots[5] == spots[8]) \
    or   (spots[3] == spots[6] == spots[9]):
    return True
  elif (spots[1] == spots[5] == spots[9]) \
    or   (spots[3] == spots[5] == spots[7]):
   return True 

  else: return False
################################################################################################################################
fun_nouns = [
    "banana", "unicorn", "pickle", "glitter", "ninja", "disco ball", "bubblegum", "rainbow", 
    "yeti", "zeppelin", "kazoo", "cupcake", "pirate", "robot", "dinosaur", "potato chip",
    "sock monkey", "tumbleweed", "snorkle", "sunglasses", "whimsicle", "firetruck", "spaceship",
    "disco ball", "mustache", "kangaroo", "flamingo", "hedgehog", "cupcake", "gumball machine",
    "waffle", "disco ball", "watermelon", "sombrero", "fire hydrant", "rubber duck", "slinky",
    "hula hoop", "popcorn", "popsicle", "lollipop", "whimsy"
]
fun_adjectives = [
    "sparkly", "giggly", "wobbly", "bouncy", "fuzzy", "zippy", "slimy", "googly-eyed",
    "loopy", "whimsical", "jumpy", "electric", "bumpy", "scrumptious", "silly", "goofy",
    "dorky", "wonky", "squiggly", "jiggly", "ticklish", "crunchy", "cheesy", "spicy",
    "fidgety", "squirrely", "rambunctious", "zany", "wacky", "quirky", "spunky", "groovy",
    "groovy", "funky", "cosmic", "stellar", "jazzy", "swanky", "snazzy", "splendiferous"
]
city_names = [
    "Wackyville", "Giggleopolis", "Loonytown", "Zanyville", "Sillyville", "Goofington", 
    "Chuckleburg", "Whimsyville", "Quirkville", "Kookytown", "Bonkersville", "Nuttytown", 
    "Daffyville", "Dottyville", "Sillytown", "Sillysburg", "Wackytown", "Zanyopolis", 
    "Goofyville", "Giggleton", "Laughington", "Smileville", "Happyville", "Joyville", 
    "Playville", "Funville", "Chuckleville", "Goofball City", "Silly City", "Wacky City"
]
people_names = [
    "Professor Poopypants", "Queen Quirkytoes", "Captain Underpants", "Major Mayhem", 
    "Sir Laughsalot", "Lady Lollipop", "Mr. Giggles", "Ms. Mischief", "Lord Loony", 
    "Baron Von Bonkers", "Duke Dorkypants", "Count Chuckles", "Mayor Mayhem", 
    "Sheriff Sillyboots", "Doctor Dizzy", "Nurse Nonsense", "Coach Crazy", 
    "Principal Prankster", "Miss Goofball", "Mr. Wacky", "Professor Zany", "Ms. Zippy",
    "Sir Silly", "Baron Von Bonkers", "Doctor Dorky", "Miss Giggles", "Professor Prankster",
    "Captain Chuckles", "Mayor Mayhem", "Mr. Sillyboots", "Nurse Nonsense", "Coach Crazy"
]
superhero_names = [
    "Captain Awesome", "The Incredible Bulk", "The Amazing Stretch", "Mega Mind", 
    "Electro-Man", "Lady Lava", "Aqua Girl", "The Green Flash", "Whirlwind Woman", 
    "Super Sniffer", "Captain Cuddles", "The Tickling Tornado", "Giggle Girl", 
    "The Bouncy Bandit", "Captain Fuzzy", "The Amazing Zapper", "Electro-Lass", 
    "The Incredible Noodle", "The Amazing Bubble", "Super Speedster", "Captain Muscles", 
    "Mega Brain", "The Invincible Ironclad", "The Incredible Hulk", "The Amazing Spider-Man",
    "Captain America", "Iron Man", "Thor", "Hulk", "Black Widow", "Hawkeye", "Captain Marvel"
]
fun_verbs = [
    "gobble", "giggle", "wiggle", "bounce", "zoom", "zap", "slither", "gobbledygook", 
    "twirl", "whirl", "prance", "gallop", "somersault", "fidget", "snort", "giggle",
    "chortle", "guffaw", "snicker", "chuckle", "burp", "hiccup", "sneeze", "yawn", 
    "snooze", "daydream", "doodle", "juggle", "cartwheel", "moonwalk", "shimmy",
    "boogie", "jive", "waltz", "tango", "foxtrot", "breakdance", "moonwalk", "shimmy", 
    "boogie", "jive", "waltz", "tango", "foxtrot", "breakdance"
]
historical_leaders = [
    "Abraham Lincoln", "Mahatma Gandhi", "Nelson Mandela", "Martin Luther King Jr.", "Winston Churchill", 
    "Franklin D. Roosevelt", "Julius Caesar", "Queen Elizabeth I", "Alexander the Great", "Napoleon Bonaparte", 
    "Genghis Khan", "Cleopatra VII", "Joan of Arc", "Otto von Bismarck", "Catherine the Great", 
    "Akbar the Great", "Augustus Caesar", "Charlemagne", "Frederick the Great", "Harriet Tubman", 
    "Simon Bolivar", "Vladimir Lenin", "Mao Zedong", "Joseph Stalin", "Ho Chi Minh", 
    "Queen Victoria", "Emperor Meiji", "Theodore Roosevelt", "Woodrow Wilson", "Mustafa Kemal Ataturk", 
    "Golda Meir", "Indira Gandhi", "Margaret Thatcher", "Ronald Reagan", "Mikhail Gorbachev", 
    "Deng Xiaoping", "Nelson Mandela", "Bill Clinton", "Angela Merkel", "Barack Obama", 
    "Vladimir Putin", "Xi Jinping", "Narendra Modi", "Jacinda Ardern", "Joe Biden",
    "Justin Trudeau" 
]
superpowers = [
    "Super Strength",
    "Flight",
    "Invisibility",
    "Telekinesis",
    "Time Manipulation",
    "Telepathy",
    "Regeneration",
    "Shape-Shifting",
    "Super Speed",
    "Energy Manipulation",
    "Teleportation",
    "Intangibility",
    "Elemental Control",
    "Precognition",
    "Invulnerability",
    "Super Intelligence",
    "Animal Communication",
    "Technopathy",
    "Immortality",
    "Super Senses",
    "Illusion Casting",
    "Density Control",
    "Empathy",
    "Astral Projection",
    "Probability Manipulation",
    "Matter Manipulation",
    "Hypnosis",
    "Super Agility",
    "Gravity Control",
    "Sonic Scream",
    "Wall Crawling",
    "Biokinesis",
    "Adaptation",
    "Elasticity",
    "X-Ray Vision",
    "Cyrokinesis",
    "Electrokinesis",
    "Geokinesis",
    "Hydrokinesis",
    "Pyrokinesis",
    "Aerokinesis",
    "Photokinesis",
    "Umbrakinesis",
    "Atmokinesis",
    "Chronokinesis",
    "Magnetokinesis",
    "Thermokinesis"
]


def ran_powers():
  return random.choice(superpowers)

def ran_adj():
  return random.choice(fun_adjectives)

def ran_nou():
  return random.choice(fun_nouns)

def ran_nam():
  return random.choice(people_names)
  
def ran_cit():
  return random.choice(city_names)

def ran_sup():
  return random.choice(superhero_names)

def ran_ver():
  return random.choice(fun_verbs)

def ran_his():
  return random.choice(historical_leaders)

def ran_num ():
  return random.randint(1,15)
