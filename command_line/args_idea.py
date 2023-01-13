def graph(*args):
    if 'total-crime' in args:
        return 'total-crime'
    else:
        return 'this doesnt work'
user = input(' ')
splitted_user = user.split()
func = splitted_user[0]
dktry = {
    'graph': graph
}
print(dktry['graph'](*splitted_user))