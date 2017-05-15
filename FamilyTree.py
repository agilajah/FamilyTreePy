import FamilyTreeNode
from Marriage import Marriage
from Person import Person

tempEv = None
pronoun = None
sibling = None
node = None
details = None


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
            if self.hasMother(child.getItem().getMother()) or mother.containsLinkToChild(child):
                return False
            else:
                mother.getItem().setIsMother(True)
                child.addLinkToParent(mother)
                #mother.addLinkToChild(child)
                return True

        return False

    def makeLinkToFather(self, child_id, father_id):
        child = self.getPerson(child_id)
        father = self.getPerson(father_id)

        if child is not None and father is not None:
            if self.hasFather(child.getItem().getMother()) or father.containsLinkToChild(child):
                return False
            else:
                father.getItem().setIsFather(True)
                child.addLinkToParent(father)
                #father.addLinkToChild(child)
                return True

        return False


    def recordWedding(self, wedding_id, first_person_id, second_person_id, startDate, endDate):
        success = False
        partner1 = self.getPerson(first_person_id)
        partner2 = self.getPerson(second_person_id)

        if partner1 is not None and partner2 is not None:
            # make sure that neither person is currently married at the moment
            if partner1.sideLinksIsEmpty() == True or partner2.sideLinksIsEmpty() == True:
                partner1.getItem().setIsMarried(True)
                partner2.getItem().setIsMarried(True)
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
            if partner1.sideLinksIsEmpty() is False or partner2.sideLinksIsEmpty() is False:
                partner1.getItem().setIsMarried(False)
                partner2.getItem().setIsMarried(False)
                partner1.getItem().setIsDivorced(True)
                partner2.getItem().setIsDivorced(True)
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
                details = details + person_name + " currently married to " + str(self.getSpouse(person.person_id)[0])
            if person.isDivorced():
                details = details + pronoun + " has had a/some divorce(s) in the past."
                former_spouses = self.getFormerSpouses(person_id)
                if len(former_spouses) > 0:
                    index = 0
                    spouses_name = ""
                    while index < len(former_spouses):

                        spouses_name += " " + former_spouses[index].getItem().getName()
                        if index < len(former_spouses):
                            spouses_name += ","
                        index = index + 1

                    details = details + " Namely," + spouses_name

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
        person_name = ""
        node = self.getPerson(person_id)

        emp = None
        if node is not None:
            person = node.getItem()
            person_name = person.getName()
            local_details = ""
            if node.linksToParentIsEmpty() is False:
                parents = node.getParentLinks()
                for parent in parents:
                    if parent.getItem().isMother():
                        local_details = local_details + person_name + "'s Mother: "
                        local_details = local_details + str(parent.getItem()) + "\n"
                    else:
                        local_details = local_details + "Father: "
                        local_details = local_details + str(parent.getItem()) + "\n"

                return local_details
            else:
                print("%s has no parents on record." % person_name)
        else:
            print("There is no %s in database" % person_name)
        return emp



    # find step parent
    def listStepParents(self, person_id):
        person_name = ""
        node = self.getPerson(person_id)

        emp = None
        if node is not None:
            person = node.getItem()
            person_name = person.getName()
            local_details = ""
            if node.linksToParentIsEmpty() is False:
                parents = node.getParentLinks()
                for parent in  parents:
                    if parent.sideLinksIsEmpty() is False and node.containsLinkToParent(parent.getSideLinks()[0]) is False:
                        local_details = local_details + "StepParent: "
                        local_details += str(parent.getSideLinks()[0].getItem())
                return local_details
            else:
                print("%s has no step parents on record." % person_name)
        else:
            print("There is no %s in database" % person_name)

        return emp


    def listParentDetails(self, person_id):
        details = ""
        person_name = ""
        node = self.getPerson(person_id)

        if node is not None:
            person = node.getItem()
            person_name = person.getName()
            temp = self.listParents(person_id)
            if temp is not None:
                details = details + temp

            temp = self.listStepParents(person_id)
            if temp is not None:
                details = details + temp

        if details is None:
            details = person_name + " doesn't have any parent listed."

        return details



    def listStepSiblings(self, person_id, fullsiblings = None, halfsiblings = None, stepsiblings_temp = None):
        # make sure person exist
        node = self.getPerson(person_id)
        stepsiblings = stepsiblings_temp
        details = ""

        if node is not None:
            # first, we check if person has parents
            person = node.getItem()
            if node.linksToParentIsEmpty() is False:
                parents = node.getParentLinks()
                for parent in parents:
                    if parent.sideLinksIsEmpty() is False:
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

                details = details + str(sibling.getItem()) + "\n"

        return details

    def listSiblings(self, person_id):
        global details
        halfsiblings = []
        fullsiblings = []
        stepsiblings = []
        global sibling
        # make sure person exist
        node = self.getPerson(person_id)
        person_name = ""


        if node is not None:
            person_name = node.getItem().getName()
            # first, we check if person has parents
            if node.linksToParentIsEmpty() is False:
                parents = node.getParentLinks()
                for parent in parents:
                    child_links = parent.getChildLinks()

                    for sibling in child_links:
                        # check if we are not looking for ourselves
                        if sibling != node.getItem():
                            temp_sibling_parents = sibling.getParentLinks()
                            for sibling_parents in temp_sibling_parents:
                                if node.containsParentLink(sibling_parents) is False:
                                    if sibling not in halfsiblings:
                                        halfsiblings.append(sibling)
                                    break


                            # now we search for another half siblings
                            # if sibling only share one parent, then it is called half sibling

                            temp_person_parent = node.getParentLinks()
                            for person_parent in temp_person_parent:
                                if sibling.containsParentLink(person_parent) is False:
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

                    details = details + str(sibling.getItem()) + "\n"
            # half sibling
            elif halfsiblings is not None:
                for sibling in halfsiblings:
                    if sibling.getItem().isAdopted():
                        details = details + "Adopted half sibling: "
                    else:
                        details = details + "Half Sibling: "

                    details = details + str(sibling.getItem()) + "\n"
            elif stepsiblings is not None:
                details = step_sibling_details
            else:
                print("There is no siblings listed for %s", person_name)
        else:
            print("There is no %s in database", person_name)

    def getStepChildren(self, person_id):
        global details
        global node
        person_name = ""
        node = self.getPerson(person_id)

        if node is not None:
            person_name = node.getItem().getName()
            temp = node.getSideLinks()
            partner = None
            if len(temp) > 0:
                partner = temp[0]
            if partner is not None:
                child_list = partner.getChildLinks()
                if child_list is not None:
                    for child in child_list:
                        if node.containsLinkToChild(child) is False:
                            print ("Stepchild: " + str(child.getItem()) + "\n")
            else:
                print("There is no step child for %s in database." % person_name)

        else:
            print("There is particular person in database.")



    def listChildren(self, person_id):
        person_name = ""
        node = self.getPerson(person_id)

        if node is not None:
            person_name = node.getItem().getName()
            if node.linksToChildIsEmpty() is False:
                details = person_name + "'s children: \n"
                child_list = node.getChildLinks()
                for child in child_list:
                    if child.getItem().isAdopted():
                        details += "Adopted child: "
                    else:
                        details += "Child "

                    details +=  str(child.getItem()) + "\n"

                # now check if partner have step children
                tempstep = self.getStepChildren(person_id)
                if tempstep is not None:
                    details += tempstep

                if details is None:
                    print("%s has no child on record." % person_name)

                return details
            else:
                print("There is no child for %s in database." % person_name)

        else:
            print("There is particular person in database.")

    def listSteps(self, person_id):
        global details
        print("Step Children: \n")
        details = self.getStepChildren(person_id)
        self.listStepSiblings(person_id)

    def listGrandParents(self, person_id):
        details = ""
        person_name = ""
        node = self.getPerson(person_id)
        if node is not None:
            person_name = node.getItem().getName()
            parent_list = node.getParentLinks()
            for parent in parent_list:
                grand_parent_list = parent.getParentLinks()
                for grand_parent in grand_parent_list:
                    if len(details) == 0:
                        if node.getItem().isAdopted():
                            details += person_name + "'s adoptive grandparents:\n"
                        else:
                            details += person_name + "'s grandparents:\n"
                    if(grand_parent.getItem().isMother()):
                        details += "GrandMother: "
                    else:
                        details += "GrandFather: "

                    details += str(grand_parent.getItem()) + "\n"

            if len(details) == 0:
                details += person_name + "'s doesnt have any grandparents."
        else:
            details += "There is no person with that id."

        return details



    def listGrandChildren(self, person_id):
        details = ""
        person_name = ""
        node = self.getPerson(person_id)
        if node is not None:
            person_name = node.getItem().getName()
            if node.linksToChildIsEmpty() is False:
                child_list = node.getChildLinks()
                for child in child_list:
                    grand_child_list = child.getChildLinks()
                    for grand_child in grand_child_list:
                        if len(details) == 0:
                            details += person_name + "'s grandchildren: \n"

                        if node.getItem().isAdopted():
                            details += "'s adopted grandchild:\n"
                        else:
                            details += " grandchild:\n"


                        details += str(grand_child.getItem()) + "\n"

                if len(details) == 0:
                    details += person_name + "'s doesnt have any grandchildren."


        else:
            details += "There is no person with id: %s in database" % person_id

        return details


    def listNephews(self, person_id):
        pass


    def listUnclesAunties(self, person_id):
        details = ""
        person_name = ""
        node = self.getPerson(person_id)

        # find parents
        if node is not None:
            person_name = node.getItem().getName()
            parent_list = node.getParentLinks()
            for parent in parent_list:
                # find grandparents
                grand_parent_list = parent.getParentLinks()
                for grand_parent in grand_parent_list:
                    # find uncle and aunts
                    parent_sibling_list = grand_parent.getChildLinks()
                    for parent_sibling in parent_sibling_list:
                        # find cousins
                        if parent_sibling != parent:
                            cousin_list = parent_sibling.getChildLinks()
                            for cousin in cousin_list:
                                if len(details) == 0:
                                    if cousin.getItem().isAdopted():
                                        details += person_name + "'s adoptive cousins:\n"
                                    else:
                                        details += person_name + "'s cousins:\n"
                                    # if not listed yet
                                    if details.find(str(cousin.getItem())) == -1:
                                        if (cousin.getItem().isAdopted()):
                                            details += "Adopted cousin: "
                                        else:
                                            details += "Cousin: "

                                        details += str(cousin.getItem()) + "\n"

                if len(details) == 0:
                    details += person_name + " has no cousins"
            else:
                details += " has no parent listed. "

        else:
            details += "There is no record of person with id: %s" % person_id

        return details

    def listCousins(self, person_id):
        details = ""
        person_name = ""
        node = self.getPerson(person_id)

        # find parents
        if node is not None:
            person_name = node.getItem().getName()
            parent_list = node.getParentLinks()
            for parent in parent_list:
                # find grandparents
                grand_parent_list = parent.getParentLinks()
                for grand_parent in grand_parent_list:
                    # find uncle and aunts
                    parent_sibling_list = grand_parent.getChildLinks()
                    for parent_sibling in parent_sibling_list:
                        # find cousins
                        if parent_sibling != parent:
                            cousin_list = parent_sibling.getChildLinks()
                            for cousin in cousin_list:
                                if len(details) == 0:
                                    if cousin.getItem().isAdopted():
                                        details += person_name + "'s adoptive cousins:\n"
                                    else:
                                        details += person_name + "'s cousins:\n"
                                    # if not listed yet
                                    if details.find(str(cousin.getItem())) == -1:
                                        if (cousin.getItem().isAdopted()):
                                            details += "Adopted cousin: "
                                        else:
                                            details += "Cousin: "

                                        details += str(cousin.getItem()) + "\n"

                if len(details) == 0:
                    details += person_name + " has no cousins"
            else:
                details += " has no parent listed. "

        else:
            details += "There is no record of person with id: %s" % person_id

        return details

    def isParent(self, parent_id, child_id):
        parent = self.getPerson(parent_id)
        child = self.getPerson(child_id)
        if parent is not None and child is not None:
            return parent.containsLinkToChild(child)
        else:
            print("Parent or child is not on record.")
            return False

    def isStepParent(self, parent_id, child_id):
        # not blood related
        if self.isParent(parent_id, child_id) is False:
            node = self.getPerson(parent_id)
            child_asked = self.getPerson(child_id).getItem()
            partner = node.getSideLinks()[0]
            child_list = partner.getChildLinks()
            if child_list is not None:
                for child in child_list:
                    if node.containsLinkToChild(child) is False:
                        return child == child_asked

        return False