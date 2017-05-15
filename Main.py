import csv
import FamilyTree
from FamilyTreeException.FileReaderErr import MotherDontExistError, FatherDontExistError
from Marriage import Marriage
from Person import Person

# create initial data
people_data = []
marriage_data = []
FamilyTree = FamilyTree()

# populate peope data and parent-children links
with open('/data/people.csv', 'r') as f:
    index = -1
    reader = csv.reader(f)
    for row in reader:
        index = index + 1
        try:
            # create person
            # first check parent - whether it is actually
            temp_mother_id = row[4]
            temp_father_id = row[5]
            mother = FamilyTree.getPerson(temp_mother_id)
            father = FamilyTree.getPerson(temp_father_id)
            if mother is not None:
                raise MotherDontExistError(temp_mother_id)
            if mother is not None:
                raise FatherDontExistError(temp_father_id)

            # if there is no problem whatsoever
            temp_person = Person(row[0], row[1], row[2], row[3], row[4], row[5])

            # link to father and mother
            FamilyTree.makeLinkToMother(row[0], temp_mother_id)
            FamilyTree.makeLinkToFather(row[0], temp_father_id)

            people_data.append(temp_person)
        except FatherDontExistError:
            print ("%s" % (FatherDontExistError.msg))
            print ('Gagal baca row %d' % (index))
        except MotherDontExistError:
            print ("%s" % (MotherDontExistError.msg))
            print ('Gagal baca row %d' % (index))


# populate marriage data and partner link
with open('/data/marriage.csv', 'r') as f:
    index = -1
    reader = csv.reader(f)
    for row in reader:
        index = index + 1
        try:
            # create marriage
            temp_marriage = Marriage(row[0], row[2], row[3], row[4])
            marriage_data.append(temp_person)
        except:
            print ('Gagal baca row' % row, index)