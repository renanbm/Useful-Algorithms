import random

def NameGenerator():
    list_names_men = ["Aiden", "Jackson", "Ethan", "Liam", "Mason", "Noah", "Lucas", "Jacob", "Jayden", "Jack", "Logan",
                      "Ryan", "Caleb", "Benjamin", "William", "Michael", "Alexander", "Elijah", "Matthew", "Dylan", "James",
                      "Owen", "Connor", "Brayden", "Carter", "Landon", "Joshua", "Luke", "Daniel", "Gabriel", "Nicholas",
                      "Nathan", "Oliver", "Henry", "Andrew", "Gavin", "Cameron", "Eli", "Max", "Isaac", "Evan", "Samuel",
                      "Grayson", "Tyler", "Zachary", "Wyatt", "Joseph", "Charlie", "Hunter", "David", "Anthony",
                      "Christian", "Colton", "Thomas", "Dominic", "Austin", "John", "Sebastian", "Cooper", "Levi", "Parker",
                      "Isaiah", "Chase", "Blake", "Aaron", "Alex", "Adam", "Tristan", "Julian", "Jonathan", "Christopher",
                      "Jace", "Nolan", "Miles", "Jordan", "Carson", "Colin", "Ian", "Riley", "Xavier", "Hudson", "Adrian",
                      "Cole", "Brody", "Leo", "Jake", "Bentley", "Sean", "Jeremiah", "Asher", "Nathaniel", "Micah", "Jason",
                      "Ryder", "Declan", "Hayden", "Brandon", "Easton", "Lincoln", "Harrison"]
    list_names_women = ["Sophia", "Emma", "Olivia", "Isabella", "Ava", "Lily", "Zoe", "Chloe", "Mia", "Madison", "Emily",
                        "Ella", "Madelyn", "Abigail", "Aubrey", "Addison", "Avery", "Layla", "Hailey", "Amelia", "Hannah",
                        "Charlotte", "Kaitlyn", "Harper", "Kaylee", "Sophie", "Mackenzie", "Peyton", "Riley", "Grace",
                        "Brooklyn", "Sarah", "Aaliyah", "Anna", "Arianna", "Ellie", "Natalie", "Isabelle", "Lillian",
                        "Evelyn", "Elizabeth", "Lyla", "Lucy", "Claire", "Makayla", "Kylie", "Audrey", "Maya", "Leah",
                        "Gabriella", "Annabelle", "Savannah", "Nora", "Reagan", "Scarlett", "Samantha", "Alyssa", "llison",
                        "Elena", "Stella", "Alexis", "Victoria", "Aria", "Molly", "Maria", "Bailey", "Sydney", "Bella",
                        "Mila", "Taylor", "Kayla", "Eva", "Jasmine", "Gianna", "Alexandra", "Julia", "Eliana", "Kennedy",
                        "Brianna", "Ruby", "Lauren", "Alice", "Violet", "Kendall", "Morgan", "Caroline", "Piper", "Brooke",
                        "Elise", "Alexa", "Sienna", "Reese", "Clara", "Paige", "Kate", "Nevaeh", "Sadie", "Quinn", "Isla",
                        "Eleanor"]
    surnames = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Rodriguez", "Wilson",
                "Martinez", "Anderson", "Taylor", "Thomas", "Hernandez", "Moore", "Martin", "Jackson", "Thompson", "White",
                "Lopez", "Lee", "Gonzalez", "Harris", "Clark", "Lewis", "Robinson", "Walker", "Perez", "Hall", "Young",
                "Allen", "Sanchez", "Wright", "King", "Scott", "Green", "Baker", "Adams", "Nelson", "Hill", "Ramirez",
                "Campbell", "Mitchell", "Roberts", "Carter", "Phillips", "Evans", "Turner", "Torres", "Parker", "Collins",
                "Edwards", "Stewart", "Flores", "Morris", "Nguyen", "Murphy", "Rivera", "Cook", "Rogers", "Morgan",
                "Peterson", "Cooper", "Reed", "Bailey", "Bell", "Gomez", "Kelly", "Howard", "Ward", "Cox", "Diaz",
                "Richardson", "Wood", "Watson", "Brooks", "Bennett", "Gray", "James", "Reyes", "Cruz", "Hughes", "Price",
                "Myers", "Long", "Foster", "Sanders", "Ross", "Morales", "Powell", "Sulliva1n", "Russell", "Ortiz",
                "Jenkins", "Gutierrez", "Perry", "Butler", "Barnes", "Fisher"]

    number_of_names = random.randint(1, 2)
    gender = random.randint(0, 1)

    chosen_name = ""

    if number_of_names == 1:
        if gender == 0:
            chosen_name += random.choice(list_names_men)
        else:
            chosen_name += random.choice(list_names_women)
    elif number_of_names == 2:
        if gender == 0:
            chosen_name += random.choice(list_names_men) + " " + random.choice(list_names_men)
        else:
            chosen_name += random.choice(list_names_women) + " " + random.choice(list_names_women)

    chosen_surname = random.choice(surnames)

    return (chosen_name + " " + chosen_surname)

print(NameGenerator())