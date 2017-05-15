import os
import csv

from FamilyTreeException.FileReaderErr import PartnerDontExistError


class MarriageDataLoader(object):
    def __init__(self, FamilyTree, path):

        script_dir = os.path.dirname(os.path.realpath('__file__'))
        rel_path_marriage = path
        abs_file_path_marriage = os.path.join(script_dir, rel_path_marriage)

        print('Loading data from marriage.csv...')

        # populate marriage data and partner link
        with open(abs_file_path_marriage, 'r') as f:
            index = -1
            reader = csv.reader(f, delimiter=';')
            for row in reader:
                index = index + 1
                try:
                    # create marriage

                    # first check whether both partners is alive or not
                    temp_partner_1 = row[1]
                    temp_partner_2 = row[2]
                    partner1 = FamilyTree.getPerson(temp_partner_1)
                    partner2 = FamilyTree.getPerson(temp_partner_2)
                    if partner1 is None:
                        raise PartnerDontExistError(temp_partner_1)
                    if partner2 is None:
                        raise PartnerDontExistError(temp_partner_2)

                    # if there is no problem at all
                    # temp_marriage = Marriage(row[0], row[1], row[2], row[3], row[4])

                    # link partner - whether the wedding is over or not will be decided in the detail function
                    FamilyTree.recordWedding(row[0], row[1], row[2], row[3], row[4])

                except PartnerDontExistError as e:
                    print("%s" % e.printMsg())
                    print('Gagal baca row' % row, index)