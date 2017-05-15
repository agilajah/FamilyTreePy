import csv
import FamilyTree
from Marriage import Marriage
from Person import Person

# create initial data
people_data = []
marriage_data = []
FamilyTree = FamilyTree()

# populate peope data and parent-children links
with open('/data/people.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        people_data.append(Person(row[0], row[1], row[2], row[3], row[4], row[5]))

    FamilyTree.setPeopleList(people_data)

# populate marriage data and partner link
with open('/data/marriage.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        marriage_data.append(Marriage(row[0], row[2], row[3], row[4]))