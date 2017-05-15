from FamilyTree import *
from helper.MarriageDataLoader import MarriageDataLoader
from helper.PeopleDataLoader import PeopleDataLoader

FamilyTree = FamilyTree()
PeopleDataLoader(FamilyTree, "data/people.csv")
MarriageDataLoader(FamilyTree, "data/marriage.csv")


print('\n')


print('Data loaded..')

index = -1
peoplelist = FamilyTree.getPeopleList()
for person in peoplelist:
    print(FamilyTree.listPersonDetails(person.getItem().getPersonId()))

print('success')