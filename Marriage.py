class Marriage(object):
    def __init__(self, id, husbandId, wifeId, startDate, endDate):
        self.id = id
        self.husbandId = husbandId
        self.wifeId = wifeId
        self.startDate = startDate
        self.endDate = endDate


    def __eq__(self, other):
        myId = self.id
        othersId = other.id
        return myId == othersId


    def getMarriageId(self):
        return self.id

    def getHusband(self):
        return self.husbandId

    def getWife(self):
        return self.wifeId

    def getMarriageDate(self):
        return self.startDate

    def getDivorceDate(self):
        return self.endDate

    def isEnded(self):
        return self.endDate is None