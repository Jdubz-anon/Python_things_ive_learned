

file = open('/home/jdubzanon/PycharmProjects/pythonProject/Python/command_line/testing_exec','rb')
test = file.read()
exec(compile(test, 'testing_exec', 'exec'))

