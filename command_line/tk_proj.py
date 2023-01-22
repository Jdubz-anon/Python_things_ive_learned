import tkinter as tk
from tkinter import ttk
import subprocess
from Python.command_line.parser import Parser
import csv
import pandas

class Shell(ttk.Frame):
    def add_frame(self, label, row=None, col=None):
        frame = ttk.LabelFrame(self, text=label)
        frame.grid(row=row, column=col)
        return frame

    def __init__(self):
        super().__init__()

                        #####entry widget/command execution window####
        entry_frame = self.add_frame('Enter Commands Here',row=0)
        self.entry_var = tk.StringVar()
        self.ent_widget = tk.Entry(entry_frame , textvariable=self.entry_var, width=80)
        self.ent_widget.grid()

                    #####command history window#####
        command_history_frame = self.add_frame('Command History',row=1)
        self.history_var = tk.StringVar()
        self.command_history_list = []
        self.command_history = ttk.Combobox(command_history_frame ,values=self.command_history_list, width=80,
                                            postcommand=lambda: self.command_history.configure(values=self.command_history_list,
                                                                                               takefocus=1))
        self.command_history.grid()

                        ###textbox widget/output window#####
        textbox_frame = self.add_frame('Output Window',row=2)
        self.big_box = tk.Text(textbox_frame, height=30,width=100, background='black', foreground='white',
                               takefocus=0, wrap='none')
        self.big_box.grid()
                        ###widget binding###
        self.command_history.bind('<Return>', self.cmd_history_bind_func)
        self.big_box.bind('<FocusIn>', lambda event: self.ent_widget.focus_set())

    def cmd_history_bind_func(self, event):
        self.command_history.focus_set()
        self.entry_var.set(self.command_history_list[self.command_history.current()])
        self.command_history_list.pop(self.command_history.current())
        self.ent_widget.focus_set()
        self.ent_widget.icursor(tk.END)
        self.command_history.set('')

    # def bind_ent_widget_func(self, event):
    #     if self.entry_var.get():
    #         self.big_box.delete('1.0', tk.END)
    #         command = self.entry_var.get()
    #         self.command_history_list.append(command)
    #         #sp = subprocess.check_output(self.entry_var.get(), shell=True)
    #         self.big_box.insert('1.0', self.entry_var.get())
    #         self.entry_var.set('')


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.par = None
        self.title('Database Shell')
        self.sh = Shell()
        self.sh.grid()
        self.sh.ent_widget.bind('<Return>', self.bind_ent_widget_func)
        self.file = None
        self.function_dict = {
            'graph': self.graph,
            'showme': "showme()",
            'list': self.create_list,
            'peek': self.peek,
            'connect' : self.change_file
                }


    def bind_ent_widget_func(self, event):
        if self.sh.entry_var.get():

            self.sh.big_box.delete('1.0', tk.END)
            #command history list
            command = self.sh.entry_var.get()
            self.sh.command_history_list.append(command)
            # sp = subprocess.check_output(self.entry_var.get(), shell=True)

                #calling functions from entrybox widget
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
        #subprocess.run(f'gedit {self.file}', shell=True)




    def create_list(self):
        self.par.arg_organizer()
        file = f'/media/jdubzanon/SmallStorage/csv_files/{self.file}'
        with open(file) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                for i in range(int(self.par.dates_dict[self.par.split_input[-1]][0]),
                               int(self.par.dates_dict[self.par.split_input[-1]][1]) + 1):
                    for vals in self.par.location_dict.values():
                        if vals.title() in row.values() and str(i) in row['Year']:
                            for cats in self.par.category_dict.values():
                                self.sh.big_box.insert('1.0', str(cats) + ' ' +str(vals).title() +"\n" 'Year'+ ' ' + str(i) + ":" + "Total" + ' ' +
                                                       row[cats] + ";\n")

                                #print(row[cats])


        # file = '/media/jdubzanon/SmallStorage/csv_files/state_crime.csv'
        # with open(file) as csv_file:
        #     csv_reader = csv.DictReader(csv_file)
        #     line = 0
        #     for row in csv_reader:
        #         for i in range(2000, 2010 + 1):
        #             if 'alabama'.title() in row.values() and str(i) in row['Year']:
        #                 print(row['Data.Rates.Property.Burglary'] + " " + str(i))


    def graph(self,arg):
        print(arg)




if __name__ == "__main__":

    app = App()
    app.mainloop()