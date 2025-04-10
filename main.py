"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Petra Šlahařová
email: petra.slaharova@icloud.com
"""

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

REGISTERED = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

line = "-" * 40

user_name = input("Enter your username: ")
user_password = str(input("Enter your password: "))

if user_name in REGISTERED:
    if user_password == REGISTERED[user_name]:
        print(
            line,
            f"Welcome to the app, {user_name.title()}",
            f"We have {len(TEXTS)} texts to be analyzed.",
            line, sep="\n")
    else: 
        print("Wrong password, terminating the program.")
        quit()
else: 
    print("Unregistered user, terminating the program.")
    quit()

user_choice = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")

if not user_choice.isdigit() or int(user_choice) > len(TEXTS) or int(user_choice) <= 0:
    print("Invalid choice, terminating the program.")
    quit()
else:
    user_choice = int(user_choice)

selected_text = TEXTS[user_choice - 1].split()
cropped_text = []

for word in selected_text:
    cropped_text.append(word.strip(".").strip(","))

count_word = len(cropped_text)
count_titlecase = 0
count_uppercase = 0
count_lowercase = 0
count_numeric = 0
numeric_sum = 0
lenghts_words = []

for word in cropped_text:
    if word.istitle():
        count_titlecase += 1
    elif word.isupper():
        count_uppercase += 1
    elif word.islower():
        count_lowercase += 1
    elif word.isnumeric():
        count_numeric += 1
        numeric_sum += int(word)
    lenghts_words.append(len(word))

print(
    line,
    f"There are {count_word} words in the selected text.",
    f"There are {count_titlecase} titlecase words.",
    f"There are {count_uppercase} uppercase words.",
    f"There are {count_lowercase} lowercase words.",
    f"There are {count_numeric} numeric strings.",
    f"The sum of all the numbers {numeric_sum}",
    line,
    f"{'LEN':<3} | {'OCCURRENCES':<17} | NR.", line, sep="\n")

count_of_lenghts = {}

for number in lenghts_words:
    if number in count_of_lenghts:
        count_of_lenghts[number] += 1
    else:
        count_of_lenghts[number] = 1

count_of_lenghts_sorted = sorted(list(count_of_lenghts.keys()))
    
for number in count_of_lenghts_sorted:
    occurrences = "*" * count_of_lenghts[number]
    print(f"{number:<3} | {occurrences:<17} | {count_of_lenghts[number]}")

