import text_encryption_function
import random
import json

""""
-----------UPPGIFT 1-------------------
Kopierar texten från in_file och skriver ut den kopierade texten i out_file
"""
def copy_text_file(in_file, out_file):
    file = open(in_file, "r")
    text = file.read()
    file.close()
    file_copy = open(out_file, "w")
    file_copy.write(text)
    file_copy.close()

copy_text_file("namn.csv", "my_copy.csv")

"""
-----------UPPGIFT 2-------------------
Läser en fil och krypterar den och skriver sedan ut den krypterade filen i ut-filen
"""
def encrypt_file(in_file, out_file):
    file = open(in_file, "r")
    text = file.read()
    file.close()
    encrypted_text = text_encryption_function.encrypt(text)
    file_encrypted = open(out_file, "w")
    file_encrypted.write(encrypted_text)
    file_encrypted.close()

encrypt_file("namn.csv", "secret_names.csv")

"""
-----------UPPGIFT 3-------------------
Frågar användaren om en fil för att sedan göra en ny ryterad version av filen.
Funtionen körs till dess att användaren anger att filnamn som är giltigt.
"""
def user_dialogue():
    while True:
        try:
            in_file = input("Vilken fil vill du kryptera?")
            out_file = input("Vad ska den nya krypterade filen heta?")
            encrypt_file(in_file, out_file)
        except FileNotFoundError as error:
            print("Filen kunde inte hittas. Fel: "+ str(error))
        except Exception as error:
            print("Fel: " + str(error))
        else:
            print("Krypteringen är klar!")
            break

#user_dialogue()

"""
-----------UPPGIFT 4-------------------
"""
def get_int_input(prompt_string):
    while True:
        try:
            tal = int(input(prompt_string))
        except ValueError:
            print("Du måste ange ett heltal!")
        else:
            return tal

#get_int_input("Ange ett heltal:")

"""
-----------UPPGIFT 5-------------------
"""
def run_quiz(quiz_list_of_lists):
    print("----------------------------------------")
    print("Hello and welcome to the quiz!")
    for question in quiz_list_of_lists:
        print("----------------------------------------")
        print(question[0])
        alternatives = question[1:4]
        random.shuffle(alternatives)
        print("Alternativ 1: " + str(alternatives[0]) + ", Alternativ 2: " + str(alternatives[1]) + ", Alternativ 3: " + str(alternatives[2]))

        while True:
            try:
                answer = get_int_input("Vilket är ditt svar? (1,2,3):")
                if answer <= 0:
                    raise IndexError
                if alternatives[answer-1] is question[1]:
                   print("Rätt, det är: " + question[1])
                else:
                    print("Fel, det rätta svaret är: " + question[1])
            except IndexError:
                print("Svara 1,2 eller 3")
            else:
                break

#short_quiz_list_of_lists = [['Vad heter Norges huvudstad?', 'Oslo', 'Bergen', 'Köpenhamn'],['Vad står ABBA för?', 'Agneta Björn Benny Annefrid', 'Kalle och Lisa', 'Smarrig Sill']]
#run_quiz(short_quiz_list_of_lists)

"""
-----------UPPGIFT 6-------------------
"""
def get_quiz_list_handle_exceptions():
    quiz_list = []

    while True:
        try:
            filename = input("Namn på quiz-filen: ")
            file = open(filename, "r")
            while True:
                line = file.readline()
                if not line:
                    file.close()
                    break
                question = line.strip().split(";")
                if len(question) != 4:
                    raise Exception("The file is not on the proper format. There needs to be four strings, separated by ; in each line of the file.")
                quiz_list.append(question)
        except FileNotFoundError:
            print("That resulted in an input/output error, please try again!")
        except Exception as error:
            print(error)
        else:
            break
    return quiz_list

"""
-----------UPPGIFT 7-------------------
"""
#run_quiz(get_quiz_list_handle_exceptions())


"""
-----------UPPGIFT 8-------------------
Koden skriver om lista till en lista på json format och skriver det 
till en jsonfil. Formatet på hur man skriver ut listor är annorlunda
mellan csv och json. Det verkar som att json har metoder för att 
få ut värde från listorna vilket är lättare än att behöva använda split.
Json har funktioner så att man kan göra så att listorna visas mer lättlästa.
"""
def uppgift8():
    ql = get_quiz_list_handle_exceptions()
    json_string = json.dumps(ql, indent=2)
    fo = open("quiz.json", "w")
    fo.write(json_string)
    fo.close()

#uppgift8()


