class User:
    username = 'none'
    password = 'none'
    
    
    def __init__(self):
        # how to accept infinit numbers of differnect attributes
        pass
    
    
     
    def password(self):
        pass
    
    

def main():
    users = User()
    users.set_username('Jerryjane')
    print users.get_username()
    
    passw = User()
    passw.set_password('passwordword')
    print passw.get_password()
    

if __name__ == '__main__' : main()