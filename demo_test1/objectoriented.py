# class of graduates start
class Examgrades:
    # adding extra double underscore to the name of the argument will make it to be strongly encapulated
    __cusname = 'James'
    __creditunit = 0
    __scoreval = 0
    
    def __init__(self):
        pass
    
    def set_scoreval(self, newScoreval):
        self.__scoreval = newScoreval
        return 
    
    def get_scoreval(self):
        self.__hiddenMethod() #now calling the hidden method here
        return self.__scoreval
    
    # creating an encapsulated method start
    
    def __hiddenMethod(self):
        print('Hello world')
    
    # creating an encapsulated method end
    
# class of graduates end

# class encapsulation start
class Animal:
    hungry ='No'
    owner = 'unknown'
    name = 'unknown'
    
    def __init__(self):
        pass
    
    def set_owner(self, newOwner):
        self.owner = newOwner
        return 
    
    def get_owner(self):
        return self.owner

# encapsulation end

class Customer:
    name = 'Joy'
    age = 23
    address = 'Obinze'
    
    def __init__(self):
        pass
    
    # for encapsulation start
    def set_name(self, newName):
        self.name = newName
        return
    
    def get_name(self):
        return self.name
    
    def phone(self):
        print('082734384')
        return
    # encapsulation end
def main():    
    # creating object start  from customer class
    human = Customer()
    human.set_name('Jerry')
    print human.get_name()
    # creating object end 
    
    # creating object from animal class start
    lion = Animal()
    lion.set_owner('Jeremiah')
    print lion.get_owner()
    # print lion.owner
    
    # creating object from animal class end
    
    # creating object from Examgrades class  start
    
    igbo = Examgrades()
    igbo.set_scoreval(34)
    print igbo.get_scoreval()
    # print igbo.scoreval
    
    # creating object from Examgrades class  start

    
if __name__ == '__main__' : main()