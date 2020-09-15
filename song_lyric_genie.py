import string
import random


# valid categories users can choose for advice
categories = ["work", "life", "love", "quarantine"]

# output if user inputs an invalid category
invalid_category = ["Sorry, I didn't understand your response. Let's try again.",
                    "hhhmm that's not an area I know much about",
                    "Whoops that's not an area I can help out much in",
                    "I only have so much knowledge. Unfortunately, that's not an area I know much about. Let's try that again!"]

# artist, song, and lyric that will be randomly selected for advice if user input category is "life." Organized in a dictionary. Inside the dictionary, an artist name is a key that holds another dictionary that holds two keys: the song and the lyric. The song and lyric values are inside of lists so that multiple songs/lyrics by the same artist can be stored.
life_songs = {"Billy Joel": {"song": ["Vienna"], "lyric": ["Slow down, you're doing fine. You can't be everything you want to be before your time"]},
              "Natasha Bedingfield": {"song": ["Pocket Full of Sunshine", "Unwritten"], "lyric": ["Do what you want, but you're never gonna break me", "The rest is still unwritten"]},
              "Renée Elise Goldsberry": {"song": ["Satisfied"], "lyric": ["You will never be satisfied"]},
              "John Mayer": {"song": ["Say"], "lyric": ["Say what you need to say"]},
              "Taylor Swift": {"song": ["Lover"], "lyric": ["This is our place, we make the rules"]},
              "The Beatles": {"song": ["Hey Jude"], "lyric": ["Anytime you feel the pain, hey Jude, refrain. Don’t carry the world upon your shoulders"]},
              "The Smiths": {"song": ["Ask"], "lyric": ["Shyness can stop you from doing all the things in life you’d like to"]},
              "Led Zeppelin": {"song": ["Stairway To Heaven"], "lyric": ["There’s still time to change the road you’re on"]},
              "The Rolling Stones": {"song": ["You Can't Always Get What You Want"], "lyric": ["You can't always get what you want, but if you try sometime, you find you get what you need"]},
              "Christina Aguilera": {"song": ["Beautiful"], "lyric": ["Words can't bring you down"]},
              "Kenny Rogers": {"song": ["The Gambler"], "lyric": ["You've got to know when to hold 'em, know when to fold 'em, know when to walk away, and know when to run"]},
              "R.E.M": {"song": ["Everybody Hurts"], "lyric": ["Today is where your book begins. The rest is still unwritten"]},
              "Idina Mendel": {"song": ["Let it Go"], "lyric": ["It's funny how some distance makes everything seem small"]},
              "Vampire Weekend": {"song": ["Giving up the Gun"], "lyric" :["Your sword's grown old and rusty, burnt beneath the rising sun"]},
              "Tracy Chapman": {"song": [ "Fast Car"], "lyric": ["You gotta make a decision: leave tonight or live and die this way"]},
              "Lizzo": {"song":["Good as Hell", "Good as Hell"], "lyric": ["Go on dust your shoulders off, keep it moving", "I know that it's hard but you have to try"]},
              "The Jam": {"song": ["Town Called Malice"], "lyric": ["Time is short and life is cruel, but it's up to us to change"]},
              "Coastal and Jackie Mendoza": {"song": ["La Luz"], "lyric": ["Don't be afraid to let go"]},
              "Bob Marley": {"song": ["Three Little Birds"], "lyric": ["Don't worry about a thing. 'Cause every little thing gonna be all right"]}
              }

# artist, song, and lyric that will be randomly selected for advice if user input category is "love." Organized in a dictionary. Inside the dictionary, an artist name is a key that holds another dictionary that holds two keys: the song and the lyric. The song and lyric values are inside of lists so that multiple songs/lyrics by the same artist can be stored.
love_songs = {"Taylor Swift": {"song": ["Love Story", "Blank Space"], "lyric": ["This love is difficult, but it's real", "It's gonna be forever, or it's gonna go down in flames"]},
              "Keri Hilson": {"song": ["Knock You Down"], "lyric": ["Sometimes love comes around and it knocks you down. Just get back up when it knocks you down"]},
              "Carly Rae Jepsen": {"song": ["Call Me Maybe"], "lyric": ["Before you came into my life, I missed you so bad"]},
              "Leonard Cohen" : {"song": ["Hallelujah"], "lyric": ["Love is not a victory march. It’s a cold and it’s a broken hallelujah"]},
              "The Smiths": {"song": ["Ask"], "lyric": ["Shyness can stop you from doing all the things in life you’d like to"]},
              "CSNY": {"song": ["Teach Your Children’"], "lyric": ["And so, become yourself, because the past is just a good bye"]},
              "The Judds": {"song": ["Love Can Build a Bridge"], "lyric": ["Love can build a bridge between your heart and mine"]},
              "Gloria Gaynor": {"song": ["I Will Survive"], "lyric": ["I've got all my life to live and all my love to give and I'll survive"]},
              "Bahamas": {"song": ["All the Time"], "lyric": ["I had all the time in the world; you wanted none of that"]},
              "Tracy Chapman": {"song": ["Fast Car"], "lyric": ["You gotta make a decision: leave tonight or live and die this way"]},
              "Lizzo": {"song":["Good as Hell", "Good as Hell"], "lyric": ["Go on dust your shoulders off, keep it moving", "I know that it's hard but you have to try"]},
              "The Supremes": {"song": ["You Can't Hurry Love", "You Can't Hurry Love"], "lyric": ["Love don't come easy. It's game of give and take", "You can't hurry love. No, you just have to wait. You got to trust, give it time. No matter how long it takes"]},
              "Sam Smith": {"song": ["Palace"], "lyric": ["Sometimes I wish we never built this palace, but real love is never a waste of time"]},
              "Kali Uchis": {"song": ["Tyrant"], "lyric": ["Your lovin' is like a kaleidoscope"]},
              "Coastal and Jackie Mendoza": {"song": ["La Luz"], "lyric": ["Don't be afraid to let go"]},
              "Billy Joel": {"song": ["Just the Way You are"], "lyric": ["Don't go changing to try and please me"]}
              }

# artist, song, and lyric that will be randomly selected for advice if user input category is "quarantine." Organized in a dictionary. Inside the dictionary, an artist name is a key that holds another dictionary that holds two keys: the song and the lyric. The song and lyric values are inside of lists so that multiple songs/lyrics by the same artist can be stored.
quarantine_songs = {"Marc E. Bassy": {"song": ["Only The Poets"], "lyric": ["If it's only for survival, guess you dead on arrival"]},
                    "Rolling Stones": {"song": ["You Can’t Always Get What You Want", "Wild Horses"], "lyric": ["You can’t always get what you want, but if you try sometimes you might just find you get what you need", "Wild, wild horses we'll ride them some day"]},
                    "One Republic": {"song": ["Better Days"], "lyric": ["I know that there'll be better days...Got the past million miles away"]},
                    "Tracy Chapman": {"song": [ "Fast Car"], "lyric": ["You gotta make a decision: leave tonight or live and die this way"]},
                    "Elizabeth and the Catapult": {"song": ["More than Enough"], "lyric": ["I forget what is missing, I kiss fear on the cheek, I feel a light on my back, and though it burns with regret, it's more than enough"]},
                    "Dory": {"song": ["Just Keep Swimming"], "lyric": ["Just keep swimming"]},
                    "Flo Rida": {"song": ["My House"], "lyric": ["Sometimes you gotta stay in"]},
                    "Lizzo": {"song":["Good as Hell", "Good as Hell"], "lyric": ["Go on dust your shoulders off, keep it moving", "I know that it's hard but you have to try"]},
                    "The Jam": {"song": ["Town Called Malice", "Town Called Malice"], "lyric": ["Better stop dreaming of the quiet life, 'cause it's the one we'll never know", "Time is short and life is cruel but it's up to us to change"]},
                    "HAIM": {"song": ["Days are Gone"], "lyric": ["I'm moving on. You can have my past. I'll never get that back. I'm moving on, 'cause those days are gone"]},
                    "Billy Joel": {"song": ["We Didn't Start the Fire"], "lyric": ["We didn't start the fire. It was always burning since the world's been turning. We didn't start the fire. No, we didn't light it, but we tried to fight it"]},
                    "Taylor Swift": {"song": ["Wildest Dreams"], "lyric": ["Nothing last forever"]},
                    "Bob Marley": {"song": ["Don't worry be Happy"], "lyric":["It will soon pass"]},
                    "Eagles": {"song": ["Hotel California"], "lyric": ["We are all just prisoners here of our own device"]}}

# artist, song, and lyric that will be randomly selected for advice if user input category is "work." Organized in a dictionary. Inside the dictionary, an artist name is a key that holds another dictionary that holds two keys: the song and the lyric. The song and lyric values are inside of lists so that multiple songs/lyrics by the same artist can be stored.
work_songs = {"Billy Joel": {"song": ["Vienna"], "lyric": ["Slow down, you're doing fine. You can't be everything you want to be before your time"]},
              "Natasha Bedingfield": {"song": ["Pocket Full of Sunshine", "Unwritten"], "lyric": ["Do what you want, but you're never gonna break me", "The rest is still unwritten"]},
              "Lin Manuel Miranda": {"song": ["Satisfied"], "lyric": ["You will never be satisfied"]},
              "The Beatles" : {"song" : ["Let It Be"], "lyric": ["Let it be. Let it be. There will be an answer. Let it be"]},
              "Notorious B.I.G." : {"song": ["The Notorious B.I.G."], "lyric": [ "The more money we come across, the more problems we see"]},
              "The Smiths": {"song": ["Ask"], "lyric": ["Shyness can stop you from doing all the things in life you’d like to"]},
              "Led Zeppelin": {"song": ["Stairway To Heaven"], "lyric": ["There’s still time to change the road you’re on"]},
              "Yolanda Adams": {"song": ["I Believe I Can Fly"], "lyric": ["If I can see it, then I can do it. If I just believe it, there's nothing to it"]},
              "Aaron Tippin": {"song": ["You've Got To Stand For Something"], "lyric": ["Never compromise what's right...You've got to stand for something or you'll fall for anything"]},
              "Tracy Chapman": {"song": [ "Fast Car"], "lyric": ["You gotta make a decision: leave tonight or live and die this way"]},
              "Lizzo": {"song":["Good as Hell", "Good as Hell"], "lyric": ["Go on dust your shoulders off, keep it moving", "I know that it's hard but you have to try"]},
              "Coastal and Jackie Mendoza": {"song": ["La Luz"], "lyric": ["Don't be afraid to let go"]}
              }

# keeps tracker of advice user finds helpful
helpful_advice_counter = 0

# keeps track of advice user does not find helpful
bad_advice_counter = 0

# counts numbers of questions user asks
questions_asked_counter = 1

# stores questions that the users asks
questions_asked = []

#stores the advice that the program gives
advice_given = []

def welcome():
    # prints welcome and introduction to program
    print("""Hello! I'm here to provide advice.\nAsk me a question and I will give you a song and song lyric that will give you some clarity to your question. 
            """)
    # validates that user would like to play
    while True:
    # strips user input for non-alphabetical characters and makes input lowercase
        need_advice = input("Do you need advice? [Yes] [No] ").lower().translate(str.maketrans(" ", " ", string.punctuation))
        if need_advice == "yes" or need_advice == "y":
            break
        elif need_advice == "no" or need_advice == "n":
            print("\nOkay! I'm here if you change your mind.")
            quit()
        else:
            print("\nSorry, I didn't understand your response. Let's try again.\n")
            continue

# informs the user of valid categories to select and validates user's category selection
def get_category():
    counter = 1
    while True:
# global to update global variable
        global category
# strips user input for non-alphabetical characters and makes input lowercase
        category = input("\nWhat kind of advice do you need? You can say life, love, work, or quarantine: ").lower().translate(str.maketrans(" ", " ", string.punctuation))
        if category in categories:
            print(f"I can definitely give you {category} advice!\n")
            return False
        # reminds the user of valid categories on their first invalid response and every third invalid response
        else:
            if counter == 1 or counter % 3 == 0:
                print("Remember, I can only give life, love, work, and quarantine advice.")
                counter += 1
                continue
        # tells the user that the response was invalid
            elif counter > 1 and counter % 3 != 0:
        # randomly selects response from invalid_category list and puts it into string format to tell user that input was invalid
                response = (random.sample(invalid_category, 1))
                response = ', '.join(response)
                print(response)
                counter += 1
                continue
        return category

# gets question from user and appends it into questions_asked list
def get_question():
    while True:
        question = input("What's your question? ")
        print("\nGood question. Let me think of what song can help you out here...")
        questions_asked.append(question)
        break

def give_advice():
# global to update global variable
    global category
    while True:
# if user inputted "life" as the category, randomly pulls advice from life_songs list
        if category == "life":
            artist = random.sample(life_songs.keys(), 1)[0]
            song = random.sample(life_songs[artist]["song"], 1)
            song = ', '.join(song)
            song_index = life_songs[artist]["song"].index(song)
            lyric = life_songs[artist]["lyric"][song_index]
            advice = (f'''I've got it! It's like {artist} sings in the song "{song}," "{lyric}."\n''')
            print(advice)
# store advice in advice_given list
            advice_given.append(advice)
            break
# if user inputted "love" as the category, randomly pulls advice from love_songs list
        if category == "love":
            artist = random.sample(love_songs.keys(), 1)[0]
            song = random.sample(love_songs[artist]["song"], 1)
            song = ', '.join(song)
            song_index = love_songs[artist]["song"].index(song)
            lyric = love_songs[artist]["lyric"][song_index]
            advice = (f'''I've got it! It's like {artist} sings in the song "{song}," "{lyric}."\n''')
            print(advice)
# store advice in advice_given list
            advice_given.append(advice)
            break
# if user inputted "quarantine" as the category, randomly pulls advice from quarantine_songs list
        if category == "quarantine":
            artist = random.sample(quarantine_songs.keys(), 1)[0]
            song = random.sample(quarantine_songs[artist]["song"], 1)
            song = ', '.join(song)
            song_index = quarantine_songs[artist]["song"].index(song)
            lyric = quarantine_songs[artist]["lyric"][song_index]
            advice = (f'''I've got it! It's like {artist} sings in the song "{song}," "{lyric}."\n''')
            print(advice)
# store advice in advice_given list
            advice_given.append(advice)
            break
# if user inputted "work" as the category, randomly pulls advice from work_songs list
        if category == "work":
            artist = random.sample(work_songs.keys(), 1)[0]
            song = random.sample(work_songs[artist]["song"], 1)
            song = ', '.join(song)
            song_index = work_songs[artist]["song"].index(song)
            lyric = work_songs[artist]["lyric"][song_index]
            advice = (f'''I've got it! It's like {artist} sings in the song "{song}," "{lyric}."\n''')
            print(advice)
# store advice in advice_given list
            advice_given.append(advice)
            break


def advice_quality():
# global to update global variable
    global helpful_advice_counter
    global bad_advice_counter
# asks the user to determine if the advice they received was helpful or not
    while True:
# strips user input for non-alphabetical characters and makes input lowercase
        quality_determination = input("Was this helpful? [Yes] [No] ").lower().translate(str.maketrans(" ", " ", string.punctuation))
# adds one to the helpful_advice_counter if the user found the advice helpful. prints the total helpful advice and bad advice the user has received thus far
        if quality_determination == "yes" or quality_determination == "y":
            helpful_advice_counter += 1
            print(f"\nAwesome!\nHelpful advice: {helpful_advice_counter}\nBad advice: {bad_advice_counter}\n")
            break
# adds one to the bad_advice_counter if the user did not find the advice helpful. prints the total helpful advice and bad advice the user has received thus far
        elif quality_determination == "no" or quality_determination == "n":
            bad_advice_counter += 1
            print(f"\nI can do better!\nHelpful advice: {helpful_advice_counter}\nBad advice: {bad_advice_counter}\n")
            break
# tells user their response was invalid and goes back to the beginning of the loop
        else:
            print("Invalid response. Try again\n")

# prints in a numerical list each question asked and advice given
def recap():
# global to update global variable
    global advice_given
    for item1, item2, item3 in zip(range(questions_asked_counter), questions_asked, advice_given):
        item1 = item1 + 1
        item3 = item3[23:]
        print(f'{item1}. Question: {item2}')
#extra spacing aligns "Question" and "Answer" when printed
        print(f'   Advice: {item3}')

def play():
    get_category()
    get_question()
    give_advice()
    advice_quality()

def play_again():
# global to update global variable
    global questions_asked
    global advice_given
    global questions_asked_counter
    while True:
# asks user is they would like to ask another question. strips user input for non-alphabetical characters and makes input lowercase
        another_question = input("Would you like to ask another question? [Yes] [No] ").lower().translate(str.maketrans(" ", " ", string.punctuation))
        if another_question == "yes" or another_question == "y":
# adds one to the questions_asked_counter if user would like to ask another question
            questions_asked_counter += 1
            play()
# when player say no/n to play again and they received all helpful advice. ends program
        elif another_question == "no" or another_question == "n" and bad_advice_counter == 0:
            print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print(f"\nYou asked {questions_asked_counter} questions and received good advice to every question!")
            print("\nHere's what you asked and the advice you got:\n")
            recap()
            print("See you next time!")
            exit()
# when player say no/n to play again and they received all bad advice. ends program
        elif another_question == "no" or another_question == "n" and helpful_advice_counter == 0:
            print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print(f"\nWell, this is embarrassing. You asked {questions_asked_counter} questions and only received bad advice.")
            print("\nHere's what you asked and the advice you got:\n")
            recap()
            print("Next time I'll do better!")
            exit()
# when player say no/n to play again and they received more helpful advice than bad advice. ends program
        elif another_question == "no" or another_question == "n" and helpful_advice_counter > bad_advice_counter:
            print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print(f"\nYou asked {questions_asked_counter} questions and got more good advice than bad advice!\n")
            print(f"Helpful advice: {helpful_advice_counter}")
            print(f"Bad advice: {bad_advice_counter}")
            print("\nHere's what you asked and the advice you got:\n")
            recap()
            print("See you next time!")
            exit()
# when player say no/n to play again and they received more bad advice than helpful advice. ends program
        elif another_question == "no" or another_question == "n" and helpful_advice_counter < bad_advice_counter:
            print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print(f"\nYou asked {questions_asked_counter} questions and received more bad advice than good advice :(\n")
            print(f"Helpful advice: {helpful_advice_counter}")
            print(f"Bad advice: {bad_advice_counter}")
            print("\nHere's what you asked and the advice you got:\n")
            recap()
            print("See you next time!")
            exit()
# when player say no/n to play again and they received an equal amount of good advice and bad advice. ends program
        elif another_question == "no" or another_question == "n" and bad_advice_counter == helpful_advice_counter:
            print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print(f"\nYou asked {questions_asked_counter} questions!\n")
            print(f"Helpful advice: {helpful_advice_counter}")
            print(f"Bad advice: {bad_advice_counter}")
            print("\nHere's what you asked and the advice you got:\n")
            recap()
            print("See you next time!")
            exit()
# when player input is invalid
        else:
            print("I didn't understand.\n")
            continue

#loops indefinitely until player says no/n to play again
def start():
    welcome()
    play()
    play_again()


start()
