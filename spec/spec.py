class Seat:
    """
    Attributes:
    number: seat number
    is_booked: True if booked, else False
    """

    def __init(self, number, is_booked):
        """
        Used to create a new Seat
        :param number: The number of the seat
        :param is_booked: True if booked, else False
        """

    def __str__(self):
        """
        Used to get information about the seat to print
        :return: String with seat number
        """

    def book(self):
        """
        Used to mark the seat as booked
        :return: String confirming the booking
        """

    def unbook(self):
        """
        Used to mark the seat as unbooked
        :return: String confirming the unbooking
        """

    def make_dict(self):
        """
        Used to make the information about the seat into a dictionary to save to json file
        :return: Dictionary of information about seat
        """

class Carriage:
    """
    Attributes:
    id: Id of the carriage
    seats: Dictionary of all seats in the carriage
    """

    def __init__(self, id, seats):
        """
        Used to creates a new carriage
        :param id: Id of the carriage
        :param seats: List of all seats in the carriage
        """

    def __str__(self):
        """
        Used to get information about the carriage to print
        :return: String with information about the carriage
        """

    def show(self):
        """
        Used to get a overview of the carriage with all booked seats marked to print
        :return: String creating a overview of the carriage
        """

    def booked_seats(self):
        """
        Used to display the number of booked seats in the carriage
        :return: String with numbr of booked seats
        """

    def make_dict(self):
        """
        Used to make the information about the carriage into a dictionary to save to json file
        :return: Dictionary of information about the carriage
        """

class Train:
    """
    Attributes:
    id: Id of the train
    carriages: Dictionary of all carriages on the train
    time: Time and date when the train departs
    departure: Name of the departure
    Destination: Name of the destination
    """

    def __init__(self, id, carriages, time, departure, destination):
        """
        Used to create a new train
        :param id: Id of the train
        :param carriages: List of all the carriages the train consists of
        :param time: Time and date the train departs
        :param departure: Name of the departure
        :param destination: Name of the destination
        """

    def __str__(self):
        """
        Used the get information about the train to print
        :return: String with information about the train
        """

    def get_time(self):
        """
        Used to rewrite the time attribute to a printable string
        :return: String with time and date
        """

    def make_dict(self):
        """
        Makes the information about the train into a dictionary to save to json file
        :return: Dictionary of information about the train
        """

#Funktioner

def read_files():
    """
    Used to read all the json-files in the directory "trains" and creates Seat -, Carriage - and Train Objects from the data in the files.
    :return: (nothing)
    """

def write_file(train):
    """
    Used to save the data from a train to a json file in the directory "trains".
    :return: (nothing)
    """

def show_menu():
    """
    Used to print the menu
    :return: (nothing)
    """

def ask_for_choice():
    """
    Used to ask the user for a choice
    :return: Choice as a String
    """

def menu_execute(choice):
    """
    Used to execute the option the user chooses in the menu
    :param choice: a string with the chosen option
    :return: (nothing)
    """

def get_departures():
    """
    Used to get list of all depatures fom all trains to print
    :return: List of all departures
    """

def get_destinations(departure):
    """
    Used to get list of all destinations from the selected departure
    :param departure: Selected departure
    :return: List of destinations
    """

def get_trains(departure, destination):
    """
    Used to get information about all trains connected to the selected departure and destination
    :param departure: Selected departure
    :param destination: Selected destination
    :return:
    """

def book():
    """
    Used to book seats
    :return: String confirming the booking
    """

def unbook():
    """
    Used to unbook a seat
    :return: String confirming the unbooking
    """

def print_ticket():
    """
    Used to print tickets from the booked seats
    :return: String comfirning the printing
    """
