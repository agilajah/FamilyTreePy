import FamilyTreeNode
from Marriage import Marriage
from Person import Person


class FamilyTree(object):
    def __init__(self):
        self.people = []
        self.marriage = []
        self.divorce = []


    def addPerson(self, person):
        success = False

        if self.personInTree(person) == -1:
            newPerson = FamilyTreeNode(person)
            self.people.append(newPerson)
            success = True

        return success



    def makeLinkToMother(self, mother_id):
        child = self.getPerson(self.person_id)
        mother = self.getPerson(mother_id)

        if child is not None and mother is not None:
            if self.hasMother(child.getItem().getMother()) or mother.containsChildLink(child):
                return False
            else:
                mother.getItem().setIsMother(True)
                child.addLinkToParent(mother)
                return True

        return False

    def makeLinkToFather(self, father_id):
        child = self.getPerson(self.person_id)
        father = self.getPerson(father_id)

        if child is not None and father is not None:
            if self.hasFather(child.getItem().getMother()) or father.containsChildLink(child):
                return False
            else:
                father.getItem().setIsFather(True)
                child.addLinkToParent(father)
                return True

        return False


    def recordWedding(self, first_person_id, second_person_id, startDate):
        success = False
        partner1 = self.getPerson(first_person_id)
        partner2 = self.getPerson(second_person_id)

        if partner1 is not None or partner2 is not None:
            # make sure that neither person is already married
            if partner1.sideLinksIsEmpty() == True or partner2.sideLinksIsEmpty() == True:
                partner1.getItem().setIsMarried = True
                partner2.getItem().setIsMarried = True
                # adds two way link between the partners
                partner1.addSideLink(partner2)

                # record in marriage object
                if partner1.getItem().getGender().lower() == "male":
                    husbandId = partner1.getItem().getId()
                    wifeId = partner2.getItem().getId()
                else:
                    husbandId = partner2.getItem().getId()
                    wifeId = partner1.getItem().getId()

                # generate a unique id
                id = len(self.marriage) + len(self.divorce) + 1

                # use id as a unique flag of particular person in marriage
                partner1.getItem().setCurrentMarriage(id)
                partner2.getItem().setCurrentMarriage(id)

                temp_marriage = Marriage(id, husbandId, wifeId, startDate)
                self.marriage.append(temp_marriage)
                success = True

        return success

    def recordDivorce(self, first_person_id, second_person_id, startDate, endDate):
        success = False
        partner1 = self.getPerson(first_person_id)
        partner2 = self.getPerson(second_person_id)

        if partner1 is not None or partner2 is not None:
            # make sure that the couple actually is married
            if partner1.sideLinksIsEmpty() is not True or partner2.sideLinksIsEmpty() is not True:
                partner1.getItem().setIsMarried = False
                partner2.getItem().setIsMarried = False
                partner1.getItem().setIsDivorced = True
                partner2.getItem().setIsDivorced = True
                # removes link between partners
                partner1.addSideLink(partner2)

                # change marriage status in marriage object
                marriageId = partner1.getItem().getCurrentMarriage()

                partner1.getItem.setCurrentMarriage(-1)
                partner2.getItem.setCurrentMarriage(-1)

                # remove marriage from list of marriage and append it to divorce list
                temp_marriage = self.getMarriage(marriageId)
                temp_marriage.setEndDate(endDate)
                self.marriage.remove(temp_marriage)
                self.divorce.append(temp_marriage)
                success = True

        return success



    def recordAdoption(self, person_id):
        person = self.getPerson(person_id)
        if person is not None:
            person.getItem().setIsAdopted(True)
            return True

        return False

    def personInTree(self, person):
        index = -1
        comparedPerson = Person(person.person_id, person.name, person.gender, person.birth_date, person.father, person.mother)
        for node in self.people:
            index = index + 1
            if node.item == comparedPerson:
                return index

        return -1