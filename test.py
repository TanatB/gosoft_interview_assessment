try:
    print('hello')
    raise Exception('im')
except Exception as e:
    print(e)
else:
    print('oh')
    
finally:
    print('bye')
    
class First(object):
    speed = 5
    def hi(self):
        print('1')

class Second(object):
    speed = 4
    def hi(self):
        print('2')
        
class Third(First, Second):
    pass

if __name__ == '__main__':
    Third().hi()
    print(Third().speed)

    