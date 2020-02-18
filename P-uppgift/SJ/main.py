import Train
import Carriage
import Seat
import json
import os
import datetime


def read_all_files(trains):
    """
    Used to read all the json-files in the directory "trains".
    :param trains: Dictionary of all trains
    :return: (nothing)
    """
    train_files = os.listdir("trains")
    for file in train_files:
        read_file(file, trains)


def read_file(file, trains):
    """
    Used to read data from a json-file and create Seat -, Carriage - and Train Objects from the data in the file.
    If the departing-time of the train has passed the file won't be read, but instead remove.
    :param file: name of the file
    :param trains: Dictionary of all trains
    :return: (nothing)
    """
    try:
        file_read = open("trains/" + file, "r", encoding="utf8")
        train = json.load(file_read)
        time_date_for_departure = datetime.datetime.fromisoformat(train['time'])
    except IOError and ValueError:
        print("Fel vid inläsning av data.")
        return
    time_date_now = datetime.datetime.now()
    try:
        if time_date_now > time_date_for_departure:
            file_read.close()
            os.remove("trains/" + file)
    except Exception:
        print("Fel vid bortagning av fil " + file)
    else:
        create_train(trains, train)
        file_read.close()


def create_train(trains, train):
    """
    Used to create a new train with data from file
    :param trains: Dictionary of all trains
    :param train: All data in a train-file
    :return: (nothing)
    """
    id = train['id']
    if not isinstance(train['carriages'], list) or not isinstance(id, int):
        print("Tåg med id " + str(id) + " är felaktigt.")
        return
    carriages = []
    for carriage in train['carriages']:
        if not isinstance(carriage['seats'], list) or not (carriage['id'], int):
            print("Vagn med id " + str(carriage['id']) + "i tåg " + str(id) + " är felaktigt.")
            return
        seats = []
        for seat in carriage['seats']:
            if not isinstance(seat['number'], int) or not isinstance(seat['is_booked'], bool) or not isinstance(seat['is_printed'], bool):
                print("Plats med id " + str(seat['number']) + " i vagn " + str(carriage['id']) + " på tåg " + str(id) + " är felaktigt.")
                return
            seats.append(Seat.Seat(seat['number'], seat['is_booked'], seat['is_printed']))
        carriages.append(Carriage.Carriage(carriage['id'], seats))

    trains[id] = Train.Train(id, carriages, train['time'], train['departure'], train['destination'])


def update_file(train, trains):
    """
    Updates data in file.
    :param train: Train whose file needs to be updated
    :param trains: Dictionary of all trains
    :return: (nothing)
    """
    filename = str(train.id) + ".json"
    dir = "trains/" + filename
    file = open(dir, "w", encoding="utf8")
    json.dump(train.make_dict(), file, indent = 2)
    file.close()
    read_file(filename, trains)


def start_screen():
    """
    Used to print a start screen
    :return: (nothing)
    """
    print("------------------------------------------------------\n\
                SJ-Platsbokning\n\
------------------------------------------------------")


def show_menu():
    """
    Used to print the menu
    :return: (nothing)
    """
    print("""\nVad vill du göra?
    • Boka: skriv 'B'
    • Avboka: skriv 'A'
    • Skriva ut de senast bokade biljetterna: skriv 'S'
    • Avsluta: skriv 'Q'""")


def ask_for_int_choice(allowed_answers):
    """
    Used to ask the user for a choice that is an Integer
    :param allowed_answers: List of answers that are allowed
    :return: Choice as an integer
    """
    while True:
        try:
            choice = int(input("Val: "))
        except ValueError:
            print("Du måste ange ett tal.")
            continue
        print("")
        if choice not in allowed_answers:
            print("Det valda alternativet finns ej.")
        else:
            return choice


def ask_for_string_choice(allowed_answers):
    """
    Used to ask the user for a choice that is a String
    :param allowed_answers: List of answers that are allowed
    :return: Choice as a string
    """
    while True:
        choice = input("Val: ")
        print("")
        if choice.lower() not in allowed_answers:
            print("Det valda alternativet finns ej.")
        else:
            return choice.lower()


def execute(trains, choice):
    """
    Used to execute the option the user chooses in the menu
    :param trains: Dictionary of all trains
    :param choice: Choice from the user
    :return: (nothing)
    """
    if choice == "b":
        book(trains)
    elif choice == "a":
        unbook(trains)
    elif choice == "s":
        print_ticket(trains)
    elif choice == "q":
        quit()


def book(trains):
    """
    Used to book tickets
    :param trains: Dictionary of all trains
    :return: (nothing)
    """
    departure = get_departure(trains)
    destination = get_destination(trains, departure)
    chosen_train = get_train(trains, departure, destination)
    chosen_carriage = chosen_train.carriages[get_carriage(chosen_train)]
    seats = get_seats(chosen_carriage)
    for key in seats:
        print(seats[key].book())
    print(chosen_carriage)
    if seats:
        update_file(chosen_train, trains)


def unbook(trains):
    """
    Used o unbook tickets
    :param trains: Dictionary of all trains
    :return: (nothing)
    """
    print("Vilket tågnr har tåget du vill avboka platsen från?")
    allowed_trains = trains.keys()
    train_id = ask_for_int_choice(allowed_trains)
    allowed_carriages = trains[train_id].carriages.keys()

    print("Vilket vagn är platsen du vill avboka på?")
    carriage_id = ask_for_int_choice(allowed_carriages)

    print("Vilket platsnr har platsen du vill avboka?")
    allowed_seats = trains[train_id].carriages[carriage_id].seats.keys()
    seat_id = ask_for_int_choice(allowed_seats)
    train = trains[train_id]
    print(train.carriages[carriage_id].seats[seat_id].unbook())
    print(train.carriages[carriage_id])
    update_file(train, trains)


def print_ticket(trains):
    """
    Used to print all tickets that have not ben printed yet
    :param trains: Dictionary of all trains
    :return: (nothing)
    """
    print("Vilket tåg vill du skriva ut biljetter för?")
    allowed_answers = trains.keys()
    choice = ask_for_int_choice(allowed_answers)
    train = trains[choice]
    tickets_printed = False
    for i in train.carriages:
        carriage = train.carriages[i]
        for j in train.carriages[i].seats:
            seat = train.carriages[i].seats[j]
            if seat.is_booked and not seat.is_printed:
                tickets_printed = True
                write_ticket(seat, carriage, train)
                print("Biljett för plats " + str(seat.number) + " i vagn " + str(carriage.id) + " på tåg " + str(train.id) + " är utskriven. ")
                seat.print_ticket()
    if not tickets_printed:
        print("Det finns inga bokningar att skriva ut.")
    update_file(train, trains)


def write_ticket(seat, carriage, train):
    """
    Used to write the ticket to the file
    :param seat: Booked seat
    :param carriage: Booked carriage
    :param train: Booked train
    :return: (nothing)
    """
    filename = "tickets/" + str(seat.number) + str(carriage.id) + str(train.id) + ".txt"
    file = open(filename, "w")
    file.write("PLATSBILJETT\n")
    file.write(str(train) + "\n")
    file.write("Vagn: " + str(carriage.id) + " | Plats: " + str(seat.number) + "\n")
    if seat.number % 4 == 2 or seat.number % 4 == 3:
        file.write("Mittgångsplats")
    else:
        file.write("Fönsterplats")
    file.close()


def get_departure(trains):
    """
    Used to ask user where they want to get the train from
    :param trains: Dictionary of all trains
    :return: Chosen departure
    """
    departures = []
    print("Vart ifrån åker du? (1, 2, 3, ...)")
    for id in trains:
        train = trains[id]
        if train.departure not in departures:
            departures.append(train.departure)
    allowed_answers = []
    for i in range(len(departures)):
        print(str(i+1) + ". " + departures[i])
        allowed_answers.append(i+1)
    choice = ask_for_int_choice(allowed_answers)
    return departures[choice-1]


def get_destination(trains, departure):
    """
    Used to ask user for destination
    :param trains: Dictionary of all trains
    :param departure: Chosen departure
    :return: Chosen destination
    """
    destinations = []
    print("Vart vill du åka? (1, 2, 3, ...)")
    for id in trains:
        train = trains[id]
        if train.departure == departure and train.destination not in destinations:
            destinations.append(train.destination)
    allowed_answers = []
    for i in range(len(destinations)):
        print(str(i+1) + ". " + destinations[i])
        allowed_answers.append(i+1)
    choice = ask_for_int_choice(allowed_answers)
    return destinations[choice-1]


def get_train(trains, departure, destination):
    """
    Used to ask user about which train, matching the wanted departure and destination
    :param trains: Dictionary of all trains
    :param departure: Chosen departure
    :param destination: Chosen destination
    :return: Chosen train
    """
    matching_trains_id = []
    print("Välj en avgång (Ange tågnr t.ex. 1, 2, ...)")
    for i in trains:
        train = trains[i]
        if train.departure == departure and train.destination == destination:
            print("Tågnummer: " + str(train.id) + ", " + train.get_time())
            matching_trains_id.append(i)
    choice = ask_for_int_choice(matching_trains_id)
    return trains[choice]


def get_carriage(train):
    """
    Used to ask user about carriage on chosen train
    :param train: Dictionary of all trains
    :return: Chosen carriage
    """
    print("Vilken vagn? (Ange vagnnr)")
    carriages_id = []
    for i in train.carriages:
        carriage = train.carriages[i]
        carriages_id.append(i)
        print("Vagn " + str(train.carriages[i].id) + ": " + str(carriage.number_of_booked_seats()) + " av " + str(len(carriage.seats)) + " bokade.")
    while True:
        choice = ask_for_int_choice(carriages_id)
        if train.carriages[choice].is_full():
            print("Vagnen är fullbokad.")
        else:
            print(train.carriages[choice])
            return choice


def get_number_of_seats():
    """
    Used to ash user about how many seats they want to book.
    :return: Number of seat chosen by the user
    """
    print("Hur många platser vill du boka? (1-8)")
    allowed_answers = list(range(1, 9))
    choice = ask_for_int_choice(allowed_answers)
    return choice


def get_seats(carriage):
    """
    Used to find available seats in the chosen carriage
    :param carriage: Chosen carriage
    :return: Dictionary of booked seats
    """
    number_of_seats = get_number_of_seats()
    while number_of_seats > len(carriage.seats)-carriage.number_of_booked_seats():
        print("Det finns inte så många platser lediga.")
        number_of_seats = get_number_of_seats()

    seats_together = carriage.find_seats_together(number_of_seats)
    if len(seats_together) == number_of_seats:
        message = "Platsen/Platserna "
        for key in seats_together:
            message += str(key) + " "
        message += " är lediga. Vill du ha den/de? (Ja/Nej)"
        return confirm_seats(message, seats_together)
    else:
        message = "Tyvärr går det inte att få alla platser intill varandra. Går det bra med sprida platser? (Ja/Nej)"
        return confirm_seats(message, carriage.find_seats_separate(number_of_seats))


def confirm_seats(message, dict_of_seats):
    """
    Used to confirm booking of seats
    :param message: String to ask user if they want to book seats
    :param dict_of_seats: dictionary of suggested seats
    :return:
    """
    print(message)
    choice = ask_for_string_choice(["ja", "nej"])
    if choice == "ja":
        return dict_of_seats
    elif choice == "nej":
        print("Inga platser bokades.")
        return {}


def main():
    trains = {}
    read_all_files(trains)
    start_screen()
    while True:
        show_menu()
        execute(trains, ask_for_string_choice(["b", "a", "s", "q"]))


if __name__ == "__main__":
    main()