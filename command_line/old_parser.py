# graph line total-crime los-angeles&new-york 2000-2010


class Parser:
    def __init__(self, input_):
        self.input = input_.split()
        self.func_list = []
        self.graph_type = ['line', 'bar', 'pie']
        self.arg_list = []
        self.graph = None
        self.function_dict = {
            'graph': "graph",
            'showme': "showme",
            'list': 'create_list',
            'peek': "peek"
        }

        self.func_arg_dict = {
            "graph": None,
            "showme": None,
            "list": None,
            "peek": None,

        }
        super().__init__()
    def ampsand_remover(self, *args):
        new_input = []
        for item in args:
            if "&" in item:
                new_input.append(item.replace('&', ' '))
            else:
                new_input.append(item)
        return new_input

    def function_worker(self, input_):
        # func_list = []
        filt_func_list = list(filter(lambda item: item in self.function_dict, self.input))
        self.func_list.clear()
        self.func_arg_dict.clear()
        for item in filt_func_list:
            item_location = self.input.index(item)
            self.func_arg_dict[item] = self.ampsand_remover(self.input[item_location + 1])
            self.func_list.append(item)

    # def dash_remover(self, *args):
    #     #remove_ampsands = self.ampsand_remover(args)
    #     func_arg_list = []
    #     for item in remove_ampsands:
    #         if "-" in item and not item.isdigit():
    #             func_arg_list.append(item.replace("-", " "))
    #         else:
    #             func_arg_list.append(item)
    #     return func_arg_list

# testing_input = input('say something: ')
#
# par = Parser(testing_input)
# func = par.function_worker(testing_input)
# # print(par.ampsand_remover(testing_input))
# print(*par.func_arg_dict['graph'])
# print(*par.func_arg_dict['showme'])
# print(*par.func_arg_dict['list'])
# print(*par.func_arg_dict['peek'])


# def word_splitter(self):
# for word in self.input:
# if word not in self.graph_type and self.function_dict.keys():
# self.word_split_dict[word] = word.replace('-', '')


# def location_splitter(self, input):
# pass
