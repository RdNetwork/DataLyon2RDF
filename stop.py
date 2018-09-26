"""Class module for managing stop occurences."""

class Stop(object):
    """Class describing a stop occurence, i.e. a place where a transportation means stops."""

    def __init__(self, number, latitude, longitude):
        """Validation constructor."""
        self.number = number
        self.latitude = latitude
        self.longitude = longitude
