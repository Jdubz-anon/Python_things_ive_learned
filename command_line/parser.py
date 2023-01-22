import csv

class Parser:
    def __init__(self, inputs):
        self.split_input = inputs.split()
        self.location_dict = dict()
        self.category_dict = dict()
        self.dates_dict = dict()
        self.file = None
        self.func_dict = {
            'list': None,
            'connect': None,
            'peek': None
        }
        self.func_list = list(filter(lambda func : func in self.func_dict,
                                     self.split_input))
    def arg_organizer(self):
        self.dates_dict[self.split_input[-1]] = self.split_input[-1].split('-')
        if "&" in self.split_input[-2]:
            self.locations = self.split_input[-2].split('&')
            for loc in self.locations:
                self.location_dict[loc] = loc.replace('-', ' ') if '-' in loc else loc
        else:
            self.location_dict[self.split_input[-2]] = self.split_input[-2].replace('-', ' ') if '-' in self.split_input[-2] else self.split_input[-2]
        self.category_dict[self.split_input[-3]] = self.split_input[-3]

    def function_worker(self, input_):
        filt_func_list = list(filter(lambda item: item in self.func_dict, self.split_input))
        return filt_func_list




    def create_list(self):
        print('hello')




    # def create_list(self):
    #     self.arg_organizer()
    #     file = '/media/jdubzanon/SmallStorage/csv_files/state_crime.csv'
    #     with open(file) as csv_file:
    #         csv_reader = csv.DictReader(csv_file)
    #         line = 0
    #         for row in csv_reader:
    #             for i in range(int(self.dates_dict[self.split_input[-1]][0]),
    #                            int(self.dates_dict[self.split_input[-1]][1]) + 1):
    #                 for vals in self.location_dict.values():
    #                     if vals.title() in row.values() and str(i) in row['Year']:
    #                         for cats in self.category_dict.values():
    #                             print(row[cats])

                    # if self.location_dict.title() in row.values() and str(i) in row['Year']:
                    #     print(row[self.arg_dict['category']] + " " + str(i))






# user = input('> ')
# par = Parser(user)
# par.arg_organizer()
# par.create_list()
# # print(par.category_dict)
# # print(par.location_dict)
# #print(par.dates_dict)