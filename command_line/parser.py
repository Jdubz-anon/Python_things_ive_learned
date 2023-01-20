import csv

class Parser:
    def __init__(self, input_):
        self.split_input = input_.split()
        self.arg_dict = {
            'location': None,
            'category': None,
            'dates': None
            }
        self.func_dict = {
            'list': self.create_list
        }
        self.func_list = list(filter(lambda func : func in self.func_dict,
                                     self.split_input))
    def _arg_organizer(self):
        self.arg_dict['dates'] = self.split_input[-1].split('-')
        self.arg_dict['location'] = self.split_input[-2]
        self.arg_dict['category'] = self.split_input[-3]

    def create_list(self):
        self._arg_organizer()
        file = '/media/jdubzanon/SmallStorage/csv_files/state_crime.csv'
        with open(file) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line = 0
            for row in csv_reader:
                for i in range(int(self.arg_dict['dates'][0]), int(self.arg_dict['dates'][1]) + 1):
                    if self.arg_dict['location'].title() in row.values() and str(i) in row['Year']:
                        print(row[self.arg_dict['category']] + " " + str(i))






input_ = input("> ")
par = Parser(input_)
for items in par.func_list:
    par.func_dict[items]()
