import FamilyTreeNode
from Marriage import Marriage
from Person import Person

tempEv = None
pronoun = None
sibling = None


class FamilyTree(object):
    def __init__(self):
        self.people = []
        self.marriage = []
        self.divorce = []

    def setPeopleList(self, people):
        self.people = people

    def setMarriageList(self, marriage):
        self.marriage = marriage

    def getMarriageList(self):
        return self.marriage

    def setDivorce(self, divorce):
        self.divorce = divorce

    def addPerson(self, person):
        success = False

        if self.personInTree(person) == -1:
            newPerson = FamilyTreeNode(person)
            self.people.append(newPerson)
            success = True

        return success



    def makeLinkToMother(self, child_id, mother_id):
        child = self.getPerson(child_id)
        mother = self.getPerson(mother_id)

        if child is not None and mother is not None:
            if self.hasMother(child.getItem().getMother()) or mother.containsChildLink(child):
                return False
            else:
                mother.getItem().setIsMother(True)
                child.addLinkToParent(mother)
                return True

        return False

    def makeLinkToFather(self, child_id, father_id):
        child = self.getPerson(child_id)
        father = self.getPerson(father_id)

        if child is not None and father is not None:
            if self.hasFather(child.getItem().getMother()) or father.containsChildLink(child):
                return False
            else:
                father.getItem().setIsFather(True)
                child.addLinkToParent(father)
                return True

        return False


    def recordWedding(self, wedding_id, first_person_id, second_person_id, startDate, endDate):
        success = False
        partner1 = self.getPerson(first_person_id)
        partner2 = self.getPerson(second_person_id)

        if partner1 is not None and partner2 is not None:
            # make sure that neither person is currently married at the moment
            if partner1.sideLinksIsEmpty() == True or partner2.sideLinksIsEmpty() == True:
                partner1.getItem().setIsMarried = True
                partner2.getItem().setIsMarried = True
                # adds two way link between the partners
                partner1.addSideLink(partner2)

                # record in marriage object
                if partner1.getItem().getGender().lower() == "male":
                    husbandId = partner1.getItem().getPersonId()
                    wifeId = partner2.getItem().getPersonId()
                else:
                    husbandId = partner2.getItem().getPersonId()
                    wifeId = partner1.getItem().getPersonId()

                # generate a unique id
                #id = len(self.marriage) + len(self.divorce) + 1
                id = wedding_id

                # if the marriage is over
                if str(endDate).lower() != "null":
                    self.recordDivorce(id, first_person_id, second_person_id, startDate, endDate)

                # use id as a unique flag of particular person in marriage
                partner1.getItem().setCurrentMarriage(id)
                partner2.getItem().setCurrentMarriage(id)

                temp_marriage = Marriage(id, husbandId, wifeId, startDate, endDate)
                self.marriage.append(temp_marriage)
                success = True

        return success

    def recordDivorce(self, marriage_id, first_person_id, second_person_id, startDate, endDate):
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
                partner1.removeSideLink(partner2)

                partner1.getItem().setCurrentMarriage(-1)
                partner2.getItem().setCurrentMarriage(-1)

                # remove marriage from list of marriage and append it to divorce list
                temp_marriage = self.getMarriage(marriage_id)
                if temp_marriage is not None:
                    temp_marriage.setStartDate(startDate)
                    temp_marriage.setEndDate(endDate)
                    self.marriage.remove(temp_marriage)
                    self.divorce.append(temp_marriage)
                    success = True

        return success


    def listPersonDetails(self, person_id):
        details = ""
        person_name = ""
        global pronoun
        node = self.getPerson(person_id)
        if node is not None:
            person = node.getItem()
            person_name = person.getName()
            if str(person.getGender()).lower() == 'male':
                pronoun = "He"
            else:
                pronoun = "She"

            details = details + person_name + " has identification number: " + person.getPersonId() + "\n"
            if person.isAdopted():
                details = details + pronoun + " is adopted."
            if person.isMarried():
                details = details + person_name + " currently married to" + node.getSpouse().getName()
            if person.isDivorced():
                details = details + pronoun + "has had divorce(s) in the past."
                spouses_name = None
                former_spouses = node.getFormerSpouses()
                if former_spouses is not None:
                    index = -1
                    for spouse in former_spouses:
                        index = index + 1
                        spouses_name.locals = " " + spouse.getItem().getName()
                        if index < len(former_spouses):
                            spouses_name = ","
                details = details + "Namely," + spouses_name
        else:
            print("%s is not in the database" % person_name)


        return details

    def recordAdoption(self, person_id):
        person = self.getPerson(person_id)
        if person is not None:
            person.getItem().setIsAdopted(True)
            return True

        return False


    def hasMother(self, person_id):
        person = self.getPerson(person_id)
        if person is not None:
            for parent in person.getParentLinks():
                if parent.getItem().isMother():
                    return True

        return False

    def hasFather(self, person_id):
        person = self.getPerson(person_id)
        if person is not None:
            for parent in person.getParentLinks():
                if parent.getItem().isFather():
                    return True

        return False

    def hasPartner(self, person_id):
        person = self.getPerson(person_id)
        if person is not None:
            if person.getItem().isMarried():
                return True

        return False


    def personInTree(self, person_id = None):
        index = -1

        if person_id is not None:
            for node in self.people:
                index = index + 1
                if person_id == node.getItem().getPersonId():
                    return index

        return -1

    def marriageInRecord(self, marriage_id = None):
        index = -1
        if marriage_id is not None:
            for marriage in self.marriage:
                index = index + 1
                if marriage_id == marriage.getMarriageId():
                    return index

        return - 1

    def getPerson(self, person_id):
        index = self.personInTree(person_id)
        #print('ini index' , index)
        person = None
        if index != -1 and index <= len(self.people):
            person = self.people[index]

        return person

    def getMarriage(self, marriage_id):
        marr = None
        for marriage in self.marriage:
            if marriage.getMarriageId() == marriage_id:
                return marriage
        return marr


    def getPeopleList(self):
        return self.people

    def getFormerSpouses(self, person_id):
        node = self.getPerson(person_id)
        former_spouse = node.getFormerSpouses()
        if len(former_spouse) == 0:
            print(node.getItem().getName() + " has no former spouse(s)")
        else:
            return former_spouse

    def getSpouse(self, person_id):
        node = self.getPerson(person_id)
        spouse = node.getSideLinks()
        if len(spouse) == 0:
            print(node.getItem().getName() + " currently has no spouse.")
            list_former_spouses = self.getFormerSpouses(person_id)
            if list_former_spouses is not None:
                if len(list_former_spouses) == 1:
                    print("But there is a former spouse for this particular person: ")
                else:
                    print("But there are some former spouses for this particular person: ")

                for form_spouse in list_former_spouses:
                    print(str(form_spouse))
        else:
            return spouse

    # find blood parent
    def listParents(self, person_id):
        node = self.getPerson(person_id)
        emp = None
        if node is not None:
            person = node.getItem()
            person_name = person.getName()
            local_details = ""
            if node.linksToParentEmpty() is not True:
                parents = node.getParentLinks()
                for parent in parents:
                    if parent.getItem().isMother:
                        local_details = local_details + person_name + "'s Mother: "
                        local_details = local_details + str(parent.getItem()) + "\n"
                    else:
                        local_details = local_details + "Father: "
                        local_details = local_details + str(parent.getItem()) + "\n"

                return local_details
        return emp



    # find step parent
    def listStepParents(self, person_id):
        node = self.getPerson(person_id)
        emp = None
        if node is not None:
            local_details = ""
            if node.linksToParentEmpty() is not True:
                parents = node.getParentLinks()
                for parent in  parents:
                    if parent.sideLinksIsEmpty() is not True and node.containsParentLink(parent.getSideLinks()[0] is not True):
                        local_details = local_details + "StepParent: "
                        local_details += str(parent.getSideLinks()[0].getItem())
                return local_details
        return emp


    def listParentDetails(self, person_id):

        node = self.getPerson(person_id)
        person = node.getItem()
        person_name = person.getName()

        local_details = self.listParents(person_id)
        local_details = self.listStepParents(person_id)

        if local_details is None:
            local_details = local_details + person_name + "Doesn't have any parent listed."

        return local_details



    def listStepSiblings(self, person_id, fullsiblings = None, halfsiblings = None, stepsiblings_temp = None):
        # make sure person exist
        node = self.getPerson(person_id)
        stepsiblings = stepsiblings_temp
        details = ""

        if node is not None:
            # first, we check if person has parents
            person = node.getItem()
            if node.linksToParentIsEmpty() is not True:
                parents = node.getParentLinks()
                for parent in parents:
                    if parent.sideLinksIsEmpty() is not True:
                        partner  = parent.getSideLinks()[0]
                        partner_sibling = partner.getChildLinks()
                        for sibling in partner_sibling:
                            if person != sibling:
                                if sibling not in fullsiblings and sibling not in halfsiblings and sibling not in stepsiblings:
                                    stepsiblings.append(sibling)

        if stepsiblings is not None:
            for sibling in stepsiblings:
                if sibling.getItem().isAdopted():
                    details = details + "Adopted step sibling: "
                else:
                    details = details + "Step sibling: "

                details = details + str(sibling) + "\n"

        return details

    def listSiblings(self, person_id):
        global details
        halfsiblings = []
        fullsiblings = []
        stepsiblings = []
        global sibling
        # make sure person exist
        node = self.getPerson(person_id)
        person_name = node.getItem().getName()

        if node is not None:
            # first, we check if person has parents
            if node.linksToParentIsEmpty() is not True:
                parents = node.getParentLinks()
                for parent in parents:
                    child_links = parent.getChildLinks()

                    for sibling in child_links:
                        # check if we are not looking for ourselves
                        if sibling != node.getItem():
                            temp_sibling_parents = sibling.getParentLinks()
                            for sibling_parents in temp_sibling_parents:
                                if node.containsParentLink(sibling_parents) is not True:
                                    if sibling not in halfsiblings:
                                        halfsiblings.append(sibling)
                                    break


                            # now we search for another half siblings
                            # if sibling only share one parent, then it is called half sibling

                            temp_person_parent = node.getParentLinks()
                            for person_parent in temp_person_parent:
                                if sibling.containsParentLink(person_parent) is not True:
                                    if sibling not in halfsiblings:
                                        halfsiblings.append(sibling)

                                    break

                            # if not half sibling, it must be full siblings

                            if sibling not in halfsiblings and sibling not in fullsiblings:
                                fullsiblings.append(sibling)

                # now we search for step siblings
                step_sibling_details = self.listStepsSiblings(person_id, fullsiblings, halfsiblings, stepsiblings)

            # details
            # full sibling
            if fullsiblings is not None:
                for sibling in fullsiblings:
                    if sibling.getItem().isAdopted():
                        details = details + "Adopted sibling: "
                    else:
                        details = details + "Sibling: "

                    details = details + str(sibling) + "\n"
            # half sibling
            elif halfsiblings is not None:
                for sibling in halfsiblings:
                    if sibling.getItem().isAdopted():
                        details = details + "Adopted half sibling: "
                    else:
                        details = details + "Half Sibling: "

                    details = details + str(sibling) + "\n"
            elif stepsiblings is not None:
                details = step_sibling_details
            else:
                print("There is no siblings listed for %s", person_name)
        else:
            print("There is no %s in database", person_name)





        pass
    def listSteps(self, person_id):
        pass
    def listUnclesAunties(self, person_id):
        pass
    def listGrandParents(self, person_id):
        pass
    def listGrandChildren(self, person_id):
        pass
    def listNephews(self, person_id):
        pass
    def listCousins(self, person_id):
        pass