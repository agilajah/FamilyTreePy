from FamilyTree import *
from helper.MarriageDataLoader import MarriageDataLoader
from helper.PeopleDataLoader import PeopleDataLoader


def Menu():
    print("\nFAMILY TREE MENU\n")
    print("1.\tPerson details")
    print("2.\tSpouse")
    print("3.\tParents details")
    print("4.\tList children")
    print("5.\tList siblings (including half-siblings)")
    print("6.\tList steps(parents, brothers, sisters, children")
    print("7.\tList uncles, aunties(only biological)")
    print("8.\tList all grandparents")
    print("9.\tList all grandchildren")
    print("10.\tList nephews")
    print("11.\tList all cousins")
    # print("12.\tList paternal lineage (male line back to oldest man in the tree)")
    # print("13.\tList maternal lineage (female line back to oldest woman in the tree)")
    # print("14.\tList all great great… (repeated N times) grandparents")
    # print("15.\tList all great great… (repeated N times) grandchildren\n")
    print("12. Want to make your own query?")


    print("X\tEXIT\n")

    choice = input("Enter menu choice 1-12, X: ")

    return choice


def input_id():
    id = input("Input person's ID: ")
    print("\n")
    return id



def first_case():
    id = input_id()
    print (FamilyTree.listPersonDetails(id))

def second_case():
    id = input_id()
    result =  FamilyTree.getSpouse(id)
    if result is not None:
        print(str(FamilyTree.getSpouse(id)))


def third_case():
    id = input_id()
    result =  FamilyTree.getFormerSpouses(id)
    if result is not None:
        print(str(FamilyTree.getFormerSpouses(id)))

def fourth_case():
    id = input_id()
    print(FamilyTree.listParentDetails(id))

def fifth_case():
    id = input_id()
    print(FamilyTree.listChildren(id))

def sixth_case():
    id = input_id()
    print(FamilyTree.listSiblings(id))

def seventh_case():
    id = input_id()
    print(FamilyTree.listSteps(id))

def eighth_case():
    id = input_id()
    print(FamilyTree.listUnclesAunties(id))

def ninth_case():
    id = input_id()
    print(FamilyTree.listGrandParents(id))

def tenth_case():
    id = input_id()
    print(FamilyTree.listGrandChildren(id))

def eleventh_case():
    id = input_id()
    print(FamilyTree.listNephews(id))

def twelvth_case():
    id = input_id()
    print(FamilyTree.listCousins(id))


mycase = {
    '1': first_case,
    '2': second_case,
    '3': third_case,
    '4': fourth_case,
    '5': fifth_case,
    '6': sixth_case,
    '7': seventh_case,
    '8': eighth_case,
    '9': ninth_case,
    '10': tenth_case,
    '11': eleventh_case,
    '12': twelvth_case,
}

# initialization
choice = None
FamilyTree = FamilyTree()
PeopleDataLoader(FamilyTree, "data/people.csv")
MarriageDataLoader(FamilyTree, "data/marriage.csv")
print('Data loaded..')

# while not exit
while str(choice).lower() != 'x':
    choice = Menu()
    myfunc = mycase[choice]
    print("Result: ")
    myfunc()

# index = -1
# peoplelist = FamilyTree.getPeopleList()
# for person in peoplelist:
#     print(FamilyTree.listPersonDetails(person.getItem().getPersonId()))
#
# print('success')

