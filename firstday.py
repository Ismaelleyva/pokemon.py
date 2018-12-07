
#init is telling the computer ot create it
#and now we are telling the computer basic atributes that they have
class stack():
    def _init_(self):
        self.items = []

    def isEmpty(self):
        #retrun a boolean (boolean is a true or false)
        return self.items == []

    def push(self, items):
        self.items.append(item)

#create an instance of the class
#stacky has all of the power in stack its like if stack is the factory stacky is what is noe thing that is comming out
stacky = stack()
stacky.push('hello')
print(stacky.isEmpty())
