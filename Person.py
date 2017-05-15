

class Person(object):
    def __init__(self, person_id, name, gender, birth_date, mother, father):
            self.person_id = person_id
            self.name = name
            self.gender = gender
            self.birth_date = birth_date
            self.father = father
            self.mother = mother
            self.isMotherVar = False
            self.isFatherVar = False
            self.isMarriedVar = False
            self.isDivorcedVar = False
            self.isAdoptedVar = False
            self.currentMarriage = -1

    def __eq__(self, other):
        myId = self.person_id
        othersId = other.person_id
        return myId == othersId

    def __str__(self):
        return "Name: %s, Date of birth: %s, Gender: %s" % (self.name, self.birth_date, self.gender)

    def equals(self, comparedPerson):
        if comparedPerson.person_id == self.person_id:
            return True
        else:
            return False

    def getGender(self):
        return self.gender

    def getPersonId(self):
        return self.person_id

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
        return self.isDivorcedVar

    def setIsDivorced(self, isDivorcedVar):
        self.isDivorcedVar = isDivorcedVar

    def isFather(self):
        return self.isFatherVar

    def setIsFather(self, isFatherVar):
        self.isFatherVar = isFatherVar

    def isMarried(self):
        return self.isMarriedVar

    def setIsMarried(self, isMarriedVar):
        self.isMarriedVar = isMarriedVar

    def isMother(self):
        return self.isMotherVar

    def setIsMother(self, isMotherVar):
        self.isMotherVar = isMotherVar

    def isAdopted(self):
        return self.isAdoptedVar

    def setIsAdopted(self, isAdoptedVar):
        return self.isAdoptedVar

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