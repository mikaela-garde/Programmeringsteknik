class Seat:
    """
    Attributes:
    number: seat number
    is_booked: True if booked, else False
    is_printed: True if ticket for seat is printed, else False
    """

    def __init__ (self, number, is_booked, is_printed):
        """
        Creates a new Seat
        :param number: The number of the seat
        :param is_booked: True if booked, else False
        :param is_printed: True if ticket for seat is printed, else False
        """
        self.number = number
        self.is_booked = is_booked
        self.is_printed = is_printed

    def __str__(self):
        """
        Used to get information about the seat to print
        :return: String with seat number
        """
        if self.is_booked:
            return "*"+str(self.number)+"*"
        else:
            return str(self.number)

    def book(self):
        """
        Used to mark the seat as booked
        :return: String confirming the booking
        """
        if not self.is_booked:
            self.is_booked = True
            return "Du har bokat plats " + str(self.number) + "."
        else:
            return "Platsen är redan bokad"

    def unbook(self):
        """
        Used to mark the seat as unbooked
        :return: String confirming the unbooking
        """
        if self.is_booked:
            self.is_booked = False
            return "Plats " + str(self.number) + " är avbokad."
        else:
            return "Platsen är inte bokad."

    def print_ticket(self):
        """
        Used to mark the seat as printed
        :return: Nothing
        """
        self.is_printed = True

    def make_dict(self):
        """
        Used to make the information about the seat into a dictionary to save to json file
        :return: Dictionary of information about seat
        """
        data = {}
        data['number'] = self.number
        data['is_booked'] = self.is_booked
        data['is_printed'] = self.is_printed
        return data

