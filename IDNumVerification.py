# -*- coding: utf-8 -*-
'''
Author: tinsir888
Applying ID number verification(only for 2nd gen)
in the class IDNumVerification
`from IDNumVerification import IDNumVerification` import its function
ID number verification includes several steps:
1. Length verification
2. Birthdate verification
3. Area code verification
4. Checksum verification
1, 2 and 3 will be done with regular expressions.
4 will be done there.
'''
# regular expressions
import re
# area code and id number format
import constant as const

class IDNumVerification(object):
    '''
    for outer class, can be 
    '''
    def __init__(self, str):
        '''
        self.str means the ID number, the type must be string
        '''
        self.id_num = str
        self.area_id = int(self.id_num[0:6])
        self.birth_year = int(self.id_num[6:10])
        self.birth_month = int(self.id_num[10:12])
        self.birth_day = int(self.id_num[12:14])
    def verify_checksum(self):
        W = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2,1]
        tmp = 0
        for idx in range(18):
            if(self.id_num[idx] == 'x' or self.id_num[idx] == 'X'):
                tmp = tmp + 10 * W[idx]
            else:
                tmp = tmp + ((int)(self.id_num[idx])) * W[idx]
            tmp = tmp % 11
        #print(tmp)
        if tmp == 1:
            return True
        else:
            return False
    def verify_brithdate(self):
        return True
    def verify(self):
        if type(self.id_num) != type('aaa'):
            return False
        if re.match(const.ID_NUMBER_15_REGEX, self.id_num):
            return True
        if re.match(const.ID_NUMBER_18_REGEX, self.id_num) == False:
            return False
        if self.verify_checksum() != True:
            return False
        return True
'''
if __name__=='__main__':
    str = input()
    testID = IDNumVerification(str)
    print(testID.verify())
'''