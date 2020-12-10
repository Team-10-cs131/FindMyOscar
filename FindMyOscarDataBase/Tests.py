import DataMassager
from DataMassager import *
import MyCsv
from MyCsv import *

#Test for tuple_to_dict in DataMassager
if __name__ == '__main__':
    test_tuple = (1, 2, 3)
    field_tuple = ('1', '2', '3')
    test_dict_expected = tuple_to_dict(test_tuple, field_tuple)
    if test_dict_expected == {'1': 1, '2': 2, '3': 3}:
        print("The Value is the expected value")
    else:
        print("The Value is the unexpected value")


#Test for bad read
try:
    read_from_csv("OscarMovieDatabase.csv")
except:
    print("Success, bad read not allowed")








