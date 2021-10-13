# one.py
if __name__ == '__main__': # check whether script is being run directly
    pass

def func():
    print('Func() in one.py')

print('top level in one.py')

if __name__ == '__main__':
    print('one.py is being run directly')
else:
    print('one.py has been imported')