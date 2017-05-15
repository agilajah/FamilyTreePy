

class Person(object):
    def __init__(self, person_id, name, gender, birth_date, father, mother):
            self.person_id = person_id
            self.name = name
            self.gender = gender
            self.birth_date = birth_date
            self.father = father
            self.mother = mother
            self.isMother = False
            self.isFather = False
            self.isMarried = False
            self.isDivorced = False
            self.isAdopted = False
            self.currentMarriage = -1

    def __eq__(self, other):
        myId = self.person_id
        othersId = other.person_id
        return myId == othersId

    def equals(self, comparedPerson):
        if comparedPerson.person_id == self.person_id:
            return True
        else:
            return False

    def setDateOfBirth(self, birth_date):
        self.birth_date = birth_date

    def getDateOfBirth(self):
        return self.birth_date

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def getMother(self):
        return self.mother

    def getFather(self):
        return self.father

    def isDivorced(self):
        return self.isDivorced

    def setIsDivorced(self, isDivorced):
        self.isDivorced = isDivorced

    def isFather(self):
        return self.isFather

    def setIsFather(self, isFather):
        self.isFather = isFather

    def isMarried(self):
        return self.isMarried

    def setIsMarried(self, isMarried):
        self.isMarried = isMarried

    def isMother(self):
        return self.isMother

    def setIsMother(self, isMother):
        self.isMother = isMother

    def isAdopted(self):
        return self.isAdopted

    def setIsAdopted(self, isAdopted):
        return self.isAdopted

    def isMale(self):
        return str(self.gender).lower() == "male"

    def isFemale(self):
        return str(self.gender).lower() == "female"

    def setGender(self, gender):
        self.gender = gender

    def getCurrentMarriage(self):
        return self.currentMarriage

    def setCurrentMarriage(self, currMarriage):
        self.currentMarriage = currMarriage