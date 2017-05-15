# class Error is derived from super class Exception
class FileReaderErr(Exception):
    # Error is derived class for Exception, but
    # Base class for exceptions in this module
    pass

class PeopleDontExistError(FileReaderErr):
    # Raised when an operation attempts a state
    # transition that's not allowed.
    pass

class FatherDontExistError(PeopleDontExistError):
    # Raised when an operation attempts a state
    # transition that's not allowed.
    def __init__(self, msg=None, id=-1):
        # Error message thrown is saved in msg
        if msg is not None:
            self.msg = msg
        else:
            self.msg = "Father with %d doesn\'t exist" % (id)

class MotherDontExistError(PeopleDontExistError):
    # Raised when an operation attempts a state
    # transition that's not allowed.
    def __init__(self, msg=None, id=-1):
        # Error message thrown is saved in msg
        if msg is not None:
            self.msg = msg
        else:
            self.msg = "Mother %d doesn\'t exist" % (id)

class SpouseDontExistError(PeopleDontExistError):
    # Raised when an operation attempts a state
    # transition that's not allowed.
    def __init__(self, msg=None, id=-1):
        # Error message thrown is saved in msg
        if msg is not None:
            self.msg = msg
        else:
            self.msg = "Spouse %d doesn\'t exist" % (id)