#def reg(name,action='Credit'):
#     print(f'Hello,{name} your task {action} is being processed.')
# reg('Nikita')
# reg('Nikita','Vklad')

def f(*args):
    print(args)
f(5,10,20,7.5,True)


def f(**kwargs):
    print(kwargs)


f(name='Nikita', age=15, is_student=True)
