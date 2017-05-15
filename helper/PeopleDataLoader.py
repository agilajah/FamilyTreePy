import os
import csv

import FamilyTree
from FamilyTreeException.FileReaderErr import MotherDontExistError, FatherDontExistError
from FamilyTreeNode import FamilyTreeNode
from Person import Person

class PeopleDataLoader(object):
    def __init__(self, FamilyTree, path):

        script_dir = os.path.dirname(os.path.realpath('__file__'))
        rel_path_people = path
        abs_file_path_people = os.path.join(script_dir, rel_path_people)

        print('Loading data from people.csv...')

        # populate peope data and parent-children links
        with open(abs_file_path_people, 'r') as f:
            index = -1
            reader = csv.reader(f, delimiter = ';')
            for row in reader:
                index = index + 1
                try:
                    # create person
                    # first check parent - whether it is actually
                    temp_mother_id = row[4]
                    temp_father_id = row[5]
                    # check if mother and father is actually exist
                    if str(temp_mother_id).lower() != 'null' or str(temp_father_id).lower() != 'null':
                        mother = FamilyTree.getPerson(temp_mother_id)
                        father = FamilyTree.getPerson(temp_father_id)
                        if mother is None:
                            raise MotherDontExistError(temp_mother_id)
                        if father is None:
                            raise FatherDontExistError(temp_father_id)



                    # if there is no problem whatsoever
                    temp_person = Person(row[0], row[1], row[2], row[3], row[4], row[5])
                    familyTreeNode = FamilyTreeNode(temp_person)

                    FamilyTree.people.append(familyTreeNode)

                    if str(temp_mother_id).lower() != 'null' or str(temp_father_id).lower() != 'null':
                        # link to father and mother
                        FamilyTree.makeLinkToMother(row[0], temp_mother_id)
                        FamilyTree.makeLinkToFather(row[0], temp_father_id)
                    # print(row[0])
                    # print(row[1])
                    # print(row[2])


                except FatherDontExistError as e:
                    print ("%s" % e.printMsg())
                    print ('Gagal baca row %d' % (index))
                except MotherDontExistError as e:
                    print ("%s" % e.printMsg())
                    print ('Gagal baca row %d' % (index))
