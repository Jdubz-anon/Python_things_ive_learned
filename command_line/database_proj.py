import tkinter as tk
from tkinter import ttk
import subprocess
from Python.command_line.parser import Parser
from Python.command_line.shell import Shell
from Python.command_line.graph_class import MakeGraph
import csv
import pandas

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.par = None
        self.file = None
        self.title('Database Shell')
        self.graph_map = dict()
        self.function_dict = {
            'graph': self.graph,
            'showme': "showme()",
            'list': self.create_list,
            'peek': self.peek,
            'connect': self.change_file
        }

        # shell widget
        self.sh = Shell()
        self.sh.grid()
        self.sh.ent_widget.bind('<Return>', self.bind_ent_widget_func)

    def bind_ent_widget_func(self, event):
        if self.sh.entry_var.get():
            self.sh.big_box.delete('1.0', tk.END)

            # command history list
            command = self.sh.entry_var.get()
            self.sh.command_history_list.append(command)
            # sp = subprocess.check_output(self.entry_var.get(), shell=True)

            # parsing text based commands and calling functions from entrybox widget
            self.par = Parser(self.sh.entry_var.get())
            self.filt_fun_list = self.par.func_list

            for item in self.filt_fun_list:
                if item in self.par.func_dict:
                    self.function_dict[item]()
            self.sh.entry_var.set('')

    def change_file(self):
        self.file = self.par.split_input[-1]
        self.sh.big_box.insert('1.0', f'Connected to {self.file}')

    def peek(self):
        df = pandas.read_csv(f'/media/jdubzanon/SmallStorage/csv_files/{self.file}')
        convert = df.head().to_json
        self.sh.big_box.insert('1.0', df.head())
        # subprocess.run(f'gedit {self.file}', shell=True)

    def create_list(self):
        self.par.arg_organizer()
        file = '/media/jdubzanon/SmallStorage/csv_files/state_crime.csv'
        try:
            with open(file) as csv_file:
                csv_reader = csv.DictReader(csv_file)

                if self.par.category_dict.get('cats'):
                    cat_list = []
                    for fieldname in csv_reader.fieldnames:
                        cat_list.append(fieldname)
                    for names in cat_list:
                        self.sh.big_box.insert('1.0', names + '\n')
                        #self.par.category_dict.clear()


                elif self.par.category_dict.get('locations'):
                    locations_list = []
                    for row in csv_reader:
                        if row['State'] not in locations_list:
                            locations_list.append(row['State'])
                    for location in locations_list:
                        self.sh.big_box.insert('1.0', location + '\n')
                        self.par.category_dict.clear()


                elif self.par.category_dict.get('years'):
                    years_avail = []
                    for row in csv_reader:
                        if row['Year'] not in years_avail:
                            years_avail.append(row['Year'])
                    for year in years_avail:
                        self.sh.big_box.insert('1.0', year + '\n')

                else:
                    try:
                        for row in csv_reader:
                            for i in range(int(self.par.dates_dict[self.par.split_input[-1]][0]),
                                           int(self.par.dates_dict[self.par.split_input[-1]][1]) + 1):
                                for vals in self.par.location_dict.values():
                                    if vals.title() in row.values() and str(i) in row['Year']:
                                        for cats in self.par.category_dict.values():
                                            # self.graph_map[vals] = []
                                            # self.graph_map[vals].append(row[cats])


                                            self.sh.big_box.insert('1.0', str(cats) + ' ' + str(
                                                vals).title() + "\n" 'Year' + ' ' + str(i) + ":" + "Total" + ' ' +
                                                                 row[cats] + ";\n")
                    except KeyError:
                        pass
        except FileNotFoundError:
            self.sh.big_box.insert('1.0',
                                   'You have to connect to a file first \n If you have connected to a file please check that your file name is valid')


    def graph(self):
        self.par.arg_organizer()
        mg = MakeGraph(location_dict=self.par.location_dict,
                       dates_dict=self.par.dates_dict,
                       split_input=self.par.split_input,
                       category_dict=self.par.category_dict)

        mg._make_graph_map()
        try:
            mg._graph_val_mapper()
        except FileNotFoundError:
            self.sh.big_box.insert('1.0',
                          'You have to connect to a file first \n If you have connected to a file please check that your file name is valid')

        mg.create_da_graph()
        # print(mg.years)
        # print(mg.location_dict)
        # print(mg.category_dict)
        # print(mg.split_input)
        # print(mg.dates_dict)
        # print(mg.graph_map.keys())


if __name__ == "__main__":
    app = App()
    app.mainloop()
