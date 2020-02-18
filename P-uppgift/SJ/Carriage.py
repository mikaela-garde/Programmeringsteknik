class Carriage:
    """
    Attributes:
    id: Id of the carriage
    seats: Dictionary of all seats in the carriage
    """

    def __init__(self, id, seats):
        """
        Creates a new carriage
        :param id: Id of the carriage
        :param seats: List of all seats in the carriage
        """
        self.id = id
        self.seats = {}
        for seat in seats:
            self.seats[seat.number] = seat

    def __str__(self):
        """
        Used to get a overview of the carriage with all booked seats marked to print
        :return: String creating a overview of the carriage
        """
        text = "{:^24}".format("Vagn " + str(self.id))
        line = "\n--------------------------"
        text += line
        for row in range(int(len(self.seats)/4)):
            text += "\n"
            for seatnr in range(1,5):
                if seatnr == 3:
                    text += "|\t\t"
                text += "|"
                if row%2 == 0:
                     text += "{:^4}".format(str(self.seats[row*4 + seatnr]))
                else:
                    text += "{:^4}".format(str(self.seats[(row+1) * 4 - (seatnr-1)]))
            text += "|"
        text += line
        text += "\n*nr* = Upptagen plats\n"
        return text

    def number_of_booked_seats(self):
        """
        Used to get the number of booked seats in the carriage
        :return: Number of booked
        """
        booked = 0
        for i in self.seats:
            if self.seats[i].is_booked:
                booked +=1
        return booked

    def find_seats_together(self, number_of_seats):
        """
        Used to find available seats that are next to each other
        :param number_of_seats: number of seats wanted
        :return: Dictionary of seats found
        """
        possible_seats = {}
        for key in self.seats:
            seat = self.seats[key]
            if not seat.is_booked:
                possible_seats[key] = seat
            else:
                possible_seats.clear()
            if len(possible_seats) == number_of_seats:
                break
        return possible_seats

    def find_seats_separate(self, number_of_seats):
        """
        Used to find available seats that does not have to be next to each other
        :param number_of_seats: number of seats wanted
        :return: Dictionary of seats found
        """
        possible_seats = {}
        for key in self.seats:
            seat = self.seats[key]
            if not seat.is_booked:
                possible_seats[key] = seat
            if len(possible_seats) == number_of_seats:
                return possible_seats

    def is_full(self):
        """
        Checks if all the seats in the carriage are booked
        :return: True if all seats are booked, else false
        """
        if len(self.seats) == self.number_of_booked_seats():
            return True
        else:
            return False

    def make_dict(self):
        """
        Used to make the information about the seat into a dictionary to save to json file
        :return: Dictionary of information about seat
        """
        data = {}
        data['id'] = self.id
        data['seats'] = []
        for seat in self.seats:
            data['seats'].append(self.seats[seat].make_dict())
        return data