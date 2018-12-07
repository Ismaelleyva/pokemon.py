# Names of the special moves for our Pokemon
grass_special = "frenzyplant"
fire_special = "blastburn"
water_special = "hydrocannon"
electric_special = "thunder"
self1 = "pikachu"
self2 = "charmander"
self3 = "squirtle"
self4 = "bulbasaur"


class Pokemon():

    def __init__(self, hp, tackle, quickattack, dodge, special, name):
        self.hp = hp
        self.tackle = tackle
        self.quickattack = quickattack
        self.dodge = dodge
        self.special = special
        self.name = name

# Setting a grass type group with access to the grass special move Frenzy Plant
class grass(Pokemon):
    def __init__(self4,atk3):
        # Mr.James => for the super().__init__add all attributes you want, e.g. hp,atk,atk2,name
        super().__init__(grass_special)
        self.atk3 = 30


#Setting a fire type group with access to the grass special move Blast Burn
class fire(Pokemon):
    def __init__(self2,atk3):
        super()._init_(fire_special)
        self.atk3 = 30
# Setting a water type group with access to the water special move Hydro Cannon
class water(Pokemon):
    def __init__(self3,atk3):
        super()._init_(water_special)
        self.atk3 = 30

class electric(Pokemon):
    def __init__add(self1,atk3):
        super().__init__(electric_special)
        self.atk3 = 30


# Initiating the battle
# Mr.James => Why is this outside the pokemon class?
print("a wild charmander is infront of you")
choice = input("do you want to start a battle?")
if choice == "yes":
    def battle(self, other):
            print(self.name, 'and', other.name, 'are fighting')
            print("pikachu knows 4 attacks: tackle, quickattack, dodge, and thunderbolt")
            move = input("what attack would you like to use?")
            if move == "tackle":
                print("pikachu used tackle")
                other.hp = other.hp - self.tackle
                print(other.name,"has",other.hp,"hp left")
                if other.hp > 0:
                    print("charmander used tackle")
                    self.hp = self.hp - other.tackle
                    print(self.name,"has",self.hp,"hp left")
                    if self.hp > 0:
                        move = input("what attack would you like to use?")
                        if move == "tackle":
                            print("pikachu used tackle")
                            other.hp = other.hp - self.tackle
                            print(other.name,"has",other.hp,"hp left")
                            print("charmander used blastburn!")
                            self.hp = self.hp - other.special
                            print(self.name,"has",self.hp,"hp left")
                            if self.hp > 0:
                                return pikachu.battle(charmander)
                            else:
                                print("pikachu fainted")
                        else:
                            print(other.name,"dodged your attack")
                            return pikachu.battle(charmander)
                    else:
                        print("pikachu fainted")
                else:
                    print("charmander fainted")
            elif move == "dodge":
                print("charmander used takle")
                print("But Pikachu dodged")
                print("you have",self.hp,"hp left","and charmander has",other.hp,"hp left")
                print("charmander used quickattack")
                self.hp = self.hp - other.quickattack
                print("pikachu has",self.hp,"hp left")
                if self.hp > 0:
                    return pikachu.battle(charmander)
                else:
                    print("pikachu fainted")
            elif move == "thunderbolt":
                if other.hp > 0:
                    print("pikachu used thunderbolt")
                    other.hp = other.hp - self.special
                    print(other.name,"has",other.hp,"hp left")
                    print("charmander used blastburn")
                    self.hp = self.hp - other.special
                    print(self.name,"has",self.hp,"hp left")
                    move = input("what attack would you like to use?")
                    if move == "tackle":
                        print("pikachu used tackle")
                        other.hp = other.hp - self.tackle
                        print(other.name,"has",other.hp,"hp left")
                        if other.hp > 0:
                            print("charmander used tackle")
                            self.hp = self.hp - other.tackle
                            print(self.name,"has",self.hp,"hp left")
                            if self.hp > 0:
                                move = input("what attack would you like to use?")
                                if move == "tackle":
                                    print("pikachu used tackle")
                                    other.hp = other.hp - self.tackle
                                    print(other.name,"has",other.hp,"hp left")
                                    print("charmander used blastburn!")
                                    self.hp = self.hp - other.special
                                    print(self.name,"has",self.hp,"hp left")
                                    if self.hp > 0:
                                        return pikachu.battle(charmander)
                                    else:
                                        print("pikachu fainted")
                            else:
                                print("pikachu fainted")
                        else:
                            print("charmander fainted")
                    elif move == "dodge":
                        print("charmander used takle")
                        print("But Pikachu dodged")
                        print("you have",self.hp,"hp left","and charmander has",other.hp,"hp left")
                        print("charmander used quickattack")
                        self.hp = self.hp - other.quickattack
                        print("pikachu has",self.hp,"hp left")
                        if self.hp > 0:
                            return pikachu.battle(charmander)
                        else:
                            print("pikachu fainted")

                    elif move == "quickattack":
                        print("pikachu used quickattack")
                        other.hp = other.hp - self.quickattack
                        print(other.name,"has",other.hp,"hp left")
                        print("charmander used quickattack")
                        self.hp = self.hp - self.quickattack
                        print(self.name,"has",self.hp,"hp left")
                        move = input("what attack do you want to use?")
                        if move == "thunderbolt":
                            print("pikachu used thunderbolt")
                            other.hp = other.hp - self.special
                            print(other.name,"has",other.hp,"hp left")
                            if other.hp > 0:
                                return pikachu.battle(charmander)
                            else:
                                print(other.name,"fainted")
                        else:
                            print("charmander dogded your attack")
                            return pikachu.battle(charmander)

                    else:
                        if self.hp > 0:
                            print("pikachu used thunderbolt")
                            other.hp = other.hp - self.special
                            print(other.name,"has",other.hp,"hp left")
                            if other.hp > 0:
                                print("charmander used tackle")
                                self.hp = self.hp - other.tackle
                                print(self.name,"has",self.hp,"hp left")
                                if self.hp >0:
                                    return pikachu.battle(charmander)
                                else:
                                    print("pikachu fainted")
                            else:
                                print("charmander fainted")
                        else:
                            print("pikachu fainted")
                else:
                    print("charmander fainted")
            elif move == "quickattack":
                print("Pikachu used quickattack")
                other.hp = other.hp - self.quickattack
                print("charmander has",other.hp,"hp left")
                print("charmander uses blastburn")
                self.hp = self.hp - other.special
                print("pikachu has",self.hp,"hp left")
                if self.hp > 0:
                    move = input("what attack would you like to use?")
                    if move == "thunderbolt":
                        print("pikachu used thunderbolt")
                        other.hp = other.hp - self.special
                        print(other.name,"has",other.hp,"hp left")
                        if other.hp > 0:
                            print("charmander needs to recharge")
                            move = input("what attack would you like to use?")
                            if move == "tackle":
                                print("pikachu used tackle")
                                other.hp = other.hp - self.tackle
                                print(other.name,"has",other.hp,"hp left")
                                if other.hp > 0:
                                    print("charmander used tackle")
                                    self.hp = self.hp - other.tackle
                                    print(self.name,"has",self.hp,"hp left")
                                    if self.hp > 0:
                                        move = input("what attack would you like to use?")
                                        if move == "tackle":
                                            print("pikachu used tackle")
                                            other.hp = other.hp - self.tackle
                                            print(other.name,"has",other.hp,"hp left")
                                            print("charmander used blastburn!")
                                            self.hp = self.hp - other.special
                                            print(self.name,"has",self.hp,"hp left")
                                            if self.hp > 0:
                                                return pikachu.battle(charmander)
                                            else:
                                                print("pikachu fainted")
                                    else:
                                        print("pikachu fainted")
                                else:
                                    print("charmander fainted")
                            elif move == "dodge":
                                print("charmander used takle")
                                print("But Pikachu dodged")
                                print("you have",self.hp,"hp left","and charmander has",other.hp,"hp left")
                                print("charmander used quickattack")
                                self.hp = self.hp - other.quickattack
                                print("pikachu has",self.hp,"hp left")
                                if self.hp > 0:
                                    return pikachu.battle(charmander)
                                else:
                                    print("pikachu fainted")
                            elif move == "thunderbolt":
                                if other.hp > 0:
                                    print("pikachu used thunderbolt")
                                    other.hp = other.hp - self.special
                                    print(other.name,"has",other.hp,"hp left")
                                    print("charmander used blastburn")
                                    self.hp = self.hp - other.special
                                    print(self.name,"has",self.hp,"hp left")
                                    move = input("what attack would you like to use?")
                                    if move == "tackle":
                                        print("pikachu used tackle")
                                        other.hp = other.hp - self.tackle
                                        print(other.name,"has",other.hp,"hp left")
                                        if other.hp > 0:
                                            print("charmander used tackle")
                                            self.hp = self.hp - other.tackle
                                            print(self.name,"has",self.hp,"hp left")
                                            if self.hp > 0:
                                                move = input("what attack would you like to use?")
                                                if move == "tackle":
                                                    print("pikachu used tackle")
                                                    other.hp = other.hp - self.tackle
                                                    print(other.name,"has",other.hp,"hp left")
                                                    print("charmander used blastburn!")
                                                    self.hp = self.hp - other.special
                                                    print(self.name,"has",self.hp,"hp left")
                                                    if self.hp > 0:
                                                        return pikachu.battle(charmander)
                                                    else:
                                                        print("pikachu fainted")
                                            else:
                                                print("pikachu fainted")
                                        else:
                                            print("charmander fainted")

                                    elif move == "dodge":
                                        print("charmander used takle")
                                        print("But Pikachu dodged")
                                        print("you have",self.hp,"hp left","and charmander has",other.hp,"hp left")
                                        print("charmander used quickattack")
                                        self.hp = self.hp - other.quickattack
                                        print("pikachu has",self.hp,"hp left")
                                        if self.hp > 0:
                                            return pikachu.battle(charmander)
                                        else:
                                            print("pikachu fainted")

                                    elif move == "quickattack":
                                        print("pikachu used quick attack")
                                        other.hp = other.hp - self.quickattack
                                        print(other.name,"has",other.hp,"hp left")
                                        print("charmander used quick attack")
                                        self.hp = self.hp - self.quickattack
                                        print(self.name,"has",self.hp,"hp left")
                                        move = input("what attack do you want to use?")
                                        if move == "thunderbolt":
                                            if other.hp > 0:
                                                print("pikachu used thunderbolt")
                                                other.hp = other.hp - self.special
                                                print(other.name,"has",other.hp,"hp left")
                                                if other.hp > 0:
                                                    return pikachu.battle(charmander)
                                                else:
                                                    print(other.name,"fainted")
                                            else:
                                                print("charmander dogded your attack")
                                                return pikachu.battle(charmander)




                    else:
                        print("pikachu fainted")
pikachu = Pokemon(100, 25, 45, 0, 49, "pikachu")
charmander = Pokemon(100, 20, 30, 0, 49, "charmander")
pikachu.battle(charmander)


#water class


#grass class
