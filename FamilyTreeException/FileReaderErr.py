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
    def __init__(self, id=-1, msg=None):
        # Error message thrown is saved in msg
        self.msg = ''
        if msg is not None:
            self.msg = msg
        else:
            self.msg = "Father with id %d doesn\'t exist" % int(id)

    def printMsg(self):
        return self.msg

class MotherDontExistError(PeopleDontExistError):
    # Raised when an operation attempts a state
    # transition that's not allowed.
    def __init__(self, id=-1, msg=None):
        # Error message thrown is saved in msg
        self.msg = ''
        if msg is not None:
            self.msg = msg
        else:
            self.msg = "Mother id  %d doesn\'t exist" % int(id)

    def printMsg(self):
        return self.msg


class PartnerDontExistError(PeopleDontExistError):
    # Raised when an operation attempts a state
    # transition that's not allowed.
    def __init__(self, msg=None, id=-1):
        # Error message thrown is saved in msg
        self.msg = ''
        if msg is not None:
            self.msg = msg
        else:
            self.msg = "Partner with id %d doesn\'t exist" % int(id)

    def printMsg(self):
        return self.msg

class SpouseDontExistError(PeopleDontExistError):
    # Raised when an operation attempts a state
    # transition that's not allowed.
    def __init__(self, msg=None, id=-1):
        # Error message thrown is saved in msg
        self.msg = ''
        if msg is not None:
            self.msg = msg
        else:
            self.msg = "Spouse with id %d doesn\'t exist" % int(id)

    def printMsg(self):
        return self.msg