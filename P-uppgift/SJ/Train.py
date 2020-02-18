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
        Creates a new train
        :param id: Id of the train
        :param carriages: List of all the carriages the train consists of
        :param time: Time and date the train departs
        :param departure: Name of the departure
        :param destination: Name of the destination
        """
        self.id = id
        self.carriages = {}
        for carriage in carriages:
            self.carriages[carriage.id] = carriage
        self.time = time
        self.departure = departure
        self.destination = destination

    def __str__(self):
        """
        Used the get information about the train to print
        :return: String with information about the train
        """
        return "Tågnummer: " + str(self.id) + " | " + self.departure + " - " + self.destination + " | " + self.get_time()

    def get_time(self):
        """
        Used to rewrite the time attribute to a printable string
        :return: String with time and date
        """
        date_time = self.time.split("T")
        return "Datum: " + date_time[0] + " Tid: " + date_time[1]

    def make_dict(self):
        """
        Makes the information about the train into a dictionary to save to json file
        :return: Dictionary of information about the train
        """
        data = {}
        data['id'] = self.id
        data['carriages'] = []
        for carriage in self.carriages:
            data['carriages'].append(self.carriages[carriage].make_dict())
        data['time'] = self.time
        data['departure'] = self.departure
        data['destination'] = self.destination
        return data