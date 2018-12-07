

class Pokemon():
    # Contains the arguments used for the Pokemon
    def __init__(self, hp, tackle, quickattack, dodge, special, name):
        self.hp = hp
        self.tackle = tackle
        self.quickattack = quickattack
        self.dodge = dodge
        self.special = special
        self.name = name
        # if self.hp = 100 then every pokemon's hp would be 100
    #Starts the battle
    print("a wild charmander is infront of you")
    choice = input("do you want to start a battle?")
    if choice == "no":
        print("you ran away")
    else:
        #Battle function
        def battle(self, other):
            print(self.name, 'and', other.name, 'are fighting')
            print(self.name,"has",self.hp,"hp","and",other.name,"has",other.hp,"hp")
            if self.hp > 0:
                if other.hp > 0:
                # Gives list of moves that your pokemon knows
                    print("pikachu knows 4 attacks: tackle, quickattack, dodge, and thunderbolt")
                    # Asks for a move
                    move = input("what attack would you like to use?")
                    if move == "tackle":
                        # Pikachu uses tackle and HP is deducted accordingly
                        print("pikachu used tackle")
                        other.hp = other.hp - self.tackle
                        print(other.name,"has",other.hp,"hp left")
                        if other.hp > 0:
                            # Oppposing Charmander attacking and HP is deducted accordingly
                            print("charmander used tackle")
                            self.hp = self.hp - other.tackle
                            print(self.name,"has",self.hp,"hp left")
                                    # Another move as long as neither Pokemon has fained
                            if self.hp > 0:
                                move = input("what attack would you like to use?")
                                if move == "tackle":
                                    print("pikachu used tackle")
                                    other.hp = other.hp - self.tackle
                                    print(other.name,"has",other.hp,"hp left")
                                    if other.hp > 0:
                                            # Charmander now uses his special move
                                        print("charmander used blastburn!")
                                        self.hp = self.hp - other.special
                                        print(self.name,"has",self.hp,"hp left")
                                        if self.hp > 0:
                                            #The whole thing starts over if both Pokemon are standing
                                            return pikachu.battle(charmander)
                                            #The whole things ends if Pikachu has fainted
                                        else:
                                            print(self.name,"fainted")
                                    else:
                                        print(other.name,"fainted")
                            #For other moves other than tackle
                                else:
                                    print(other.name,"dodged your attack")
                                    return pikachu.battle(charmander)
                            else:
                                print(self.name,"fainted")
                        else:
                            print(other.name,"fainted")
                    #If Pikachu decides to dodge
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
                            print(self.name,"fainted")
                    #Pikachu's special move
                    elif move == "thunderbolt":
                        print("pikachu used thunderbolt")
                        other.hp = other.hp - self.special
                        print(other.name,"has",other.hp,"hp left")
                        if other.hp > 0:
                            print("charmander used blastburn")
                            self.hp = self.hp - other.special
                            print(self.name,"has",self.hp,"hp left")
                            if self.hp > 0:
                                move = input("what attack would you like to use?")
                                #Next attack (Tackle)
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
                                                if other.hp > 0:
                                                    print("charmander used blastburn!")
                                                    self.hp = self.hp - other.special
                                                    print(self.name,"has",self.hp,"hp left")
                                                    if self.hp > 0:
                                                        return pikachu.battle(charmander)
                                                    else:
                                                        print(self.name,"fainted")
                                                else:
                                                    print(other.name,"fianted")
                                            else:
                                                print(other.name,"dodged your attack")
                                                print(other.name,"used blastburn")
                                                self.hp - self.hp - other.special
                                                print(self.name,"has",self.hp,"hp left")
                                                if self.hp > 0:
                                                    return pikachu.battle(charmander)
                                                else:
                                                    print(self.name,"fainted")




                                                    #Insert stuff about other moves
                                        else:
                                            print(self.name,"fainted")
                                    else:
                                        print(other.name,"fainted")



                                    #Next attack (dodge)

                                elif move == "dodge":
                                    print("charmander used takle")
                                    print("But Pikachu dodged")
                                    print("you have",self.hp,"hp left","and charmander has",other.hp,"hp left")
                                    print("charmander used quickattack")
                                    self.hp = self.hp - other.quickattack
                                    print("pikachu has",self.hp,"hp left")
                                    #Recursion
                                    if self.hp > 0:
                                        return pikachu.battle(charmander)
                                    else:
                                        print(self.name,"fainted")


                                    #Next attack (Quick Attack)
                                elif move == "quickattack":
                                    print("pikachu used quickattack")
                                    other.hp = other.hp - self.quickattack
                                    print(other.name,"has",other.hp,"hp left")
                                    print("charmander used quickattack")
                                    self.hp = self.hp - self.quickattack
                                    print(self.name,"has",self.hp,"hp left")
                                    if self.hp > 0:
                                        move = input("what attack do you want to use?")
                                        if move == "thunderbolt":
                                            print("pikachu used thunderbolt")
                                            other.hp = other.hp - self.special
                                            print(other.name,"has",other.hp,"hp left")
                                            if other.hp > 0:
                                                print(other.name,"used quickattack")
                                                self.hp = self.hp - other.quickattack
                                                print(self.name,"has",self.hp,"hp left")
                                                if self.hp > 0:
                                                    return pikachu.battle(charmander)
                                                else:
                                                    print(self.name,"fainted")
                                            else:
                                                print(other.name,"fainted")
                                                #Recursion
                                        else:
                                            print("pikachu didn't listen and used tackle")
                                            print("but charmander dogded your attack")
                                            return pikachu.battle(charmander)
                                    else:
                                        print(self.name,"fainted")

                                        #Next move (Thunderbolt)
                                else:
                                    print("pikachu used thunderbolt")
                                    other.hp = other.hp - self.special
                                    print(other.name,"has",other.hp,"hp left")
                                    if other.hp > 0:
                                        print("charmander used tackle")
                                        self.hp = self.hp - other.tackle
                                        print(self.name,"has",self.hp,"hp left")
                                        if self.hp > 0:
                                            return pikachu.battle(charmander)
                                        else:
                                            print(self.name, "fainted")
                                    else:
                                        print(other.name,"fainted")

                            else:
                                print(self.name,"fainted")

                        else:
                            print(other.name,"fainted")

                    #Quick Attack from when the move was asked at the very beginning
                    elif move == "quickattack":
                        print("Pikachu used quickattack")
                        other.hp = other.hp - self.quickattack
                        print("charmander has",other.hp,"hp left")
                        if other.hp > 0:
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
                                                        if other.hp > 0:
                                                            print(other.hp, "used blastburn!")
                                                            self.hp = self.hp - other.special
                                                            print(self.name,"has",self.hp,"hp left")
                                                            if self.hp > 0:
                                                                return pikachu.battle(charmander)
                                                            else:
                                                                print(self.name,"fainted")
                                                        else:
                                                            print(other.name,"fainted")


                                                    elif move == "dodge":
                                                        print("charmander used takle")
                                                        print("But Pikachu dodged")
                                                        print("you have",self.hp,"hp left","and charmander has",other.hp,"hp left")
                                                        if self.hp > 0:
                                                            if other.hp > 0:
                                                                print("charmander used quickattack")
                                                                self.hp = self.hp - other.quickattack
                                                                print(self.name, "has",self.hp,"hp left")
                                                                if self.hp > 0:
                                                                    return pikachu.battle(charmander)
                                                                else:
                                                                    print(self.name,"fainted")
                                                            else:
                                                                print(other.name,"fainted")
                                                        else:
                                                            print(self.name,"fainted")

                                                    else:
                                                        print("pikachu used thunderbolt")
                                                        other.hp = other.hp - self.special
                                                        print(other.name,"has",other.hp,"hp left")
                                                        if other.hp > 0:
                                                            print("charmander used blastburn")
                                                            self.hp = self.hp - other.special
                                                            print(self.name,"has",self.hp,"hp left")
                                                            if self.hp > 0:
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
                                                                                if other.hp > 0:
                                                                                    print("charmander used blastburn!")
                                                                                    self.hp = self.hp - other.special
                                                                                    print(self.name,"has",self.hp,"hp left")
                                                                                    if self.hp > 0:
                                                                                        return pikachu.battle(charmander)
                                                                                    else:
                                                                                        print(self.name,"fainted")
                                                                                else:
                                                                                    print(other.name,"fainted")
                                                                            elif move == "quickattack":
                                                                                print("pikachu used quickattack")
                                                                                other.hp = other.hp - self.quickattack
                                                                                print(other.name,"has",other.hp,'hp left')
                                                                                if other.hp > 0:
                                                                                    print("charmander used blastburn")
                                                                                    self.hp = self.hp - other.special
                                                                                    print(self.name,"has",self.hp,"hp left")
                                                                                    if self.hp > 0:
                                                                                        return pikachu.battle(charmander)
                                                                                    else:
                                                                                        print(self.name,"fainted")
                                                                                else:
                                                                                    print(other.name,"fainted")

                                                                            elif move == "dodge":
                                                                                print(other.name,"used blastburn")
                                                                                print("but",self.name,"used dodge")
                                                                                print(other.name,"has",other.hp,"hp left")
                                                                                if other.hp > 0:
                                                                                    print(self.name,"has",self.hp,"hp left")
                                                                                    if self.hp > 0:
                                                                                        return pikachu.battle(charmander)
                                                                                    else:
                                                                                        print(self.name,"fainted")
                                                                                else:
                                                                                    print(other.name,"fainted")

                                                                            elif move == "thunderbolt":
                                                                                print(self.name,"used thunderbolt")
                                                                                other.hp = other.hp - self.special
                                                                                print(other.name,"has",other.hp,"hp left")
                                                                                if other.hp > 0:
                                                                                    print(other.name,"used tackle")
                                                                                    self.hp = self.hp - other.tackle
                                                                                    if self.hp > 0:
                                                                                        return pikachu.battle(charmander)
                                                                                    else:
                                                                                        print(self.name,"fainted")
                                                                                else:
                                                                                    print(other.name,"fainted")
                                                                        else:
                                                                            print(self.name,"fainted")
                                                                    else:
                                                                        print(other.name,"fainted")
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
                                                                        print(self.name,"fainted")
                                                                elif move == "quickattack":
                                                                    print("pikachu used quick attack")
                                                                    other.hp = other.hp - self.quickattack
                                                                    print(other.name,"has",other.hp,"hp left")
                                                                    if other.hp > 0:
                                                                        print("charmander used quick attack")
                                                                        self.hp = self.hp - self.quickattack
                                                                        print(self.name,"has",self.hp,"hp left")
                                                                        if self.hp > 0:
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
                                                                                print("charmander dodged your attack and used tackle")
                                                                                self.hp = self.hp - other.tackle
                                                                                print(self.name,"has",self.hp,"hp left")
                                                                                if self.hp > 0:
                                                                                    return pikachu.battle(charmander)
                                                                                else:
                                                                                    print(self.name,"fainted")
                                                                        else:
                                                                            print(self.name,"fainted")
                                                                    else:
                                                                        print(other.name,"fainted")
                                                                else:
                                                                    print(self.name,"used thunderbolt")
                                                                    other.hp = other.hp - self.special
                                                                    print(other.name,"has",other.hp,"hp left")
                                                                    if other.hp > 0:
                                                                        return pikachu.battle(charmander)
                                                                    else:
                                                                        print(other.name,"fainted")
                                                            else:
                                                                print(self.name,"fainted")
                                                        else:
                                                            print(other.name,"fainted")
                                                else:
                                                    print(self.name,"fainted")
                                            else:
                                                print(other.name,"fainted")
                                        elif move == "thunderbolt":
                                            print(self.name,"used thunderbolt")
                                            other.hp = other.hp - self.special
                                            print(other.name,"has", other.hp,"hp left")
                                            if other.hp > 0:
                                                print(other.name,"used tackle")
                                                self.hp = self.hp - other.tackle
                                                print(self.name,"has",self.hp,"hp left")
                                                if self.hp > 0:
                                                    return pikachu.battle(charmander)
                                                else:
                                                    print(self.name,"fainted")
                                            else:
                                                print(other.name,"fainted")
                                        else:
                                            print(other.name,"dodged your attack and used blastburn")
                                            self.hp = self.hp - other.special
                                            print(self.name,"has",self.hp,"hp left")
                                            if self.hp > 0:
                                                return pikachu.battle(charmander)
                                            else:
                                                print(self.name,"fainted")

                                    else:
                                        print(other.name,"fainted")
                                elif move == "tackle":
                                    print(self.name,"used tackle")
                                    other.hp = other.hp - self.tackle
                                    print(other.name,"has", other.hp,"hp left")
                                    if other.hp > 0:
                                        print(other.name,"used quickattack")
                                        self.hp = self.hp - other.quickattack
                                        print(self.name,"has",self.hp,"hp left")
                                        if self.hp > 0:
                                            return pikachu.battle(charmander)
                                        else:
                                            print(self.name,"fainted")
                                    else:
                                        print(other.name,"fainted")

                                elif move == "quickattack":
                                    print(self.name,"used quickattack")
                                    other.hp = other.hp - self.quickattack
                                    print(other.name,"has",other.hp,'hp left')
                                    if other.hp > 0:
                                        print(other.name,"used tackle")
                                        self.hp = self.hp - other.tackle
                                        print(self.name,"has",self.hp,"hp left")
                                        if self.hp > 0:
                                            return pikachu.battle(charmander)
                                        else:
                                            print(self.name,"fainted")
                                    else:
                                        print(other.name,"fainted")

                                else:
                                    print(other.name,"dodged also")
                                    print(other.name,"used quickattack")
                                    self.hp = self.hp - other.quickattack
                                    print(self.name,"has",self.hp,"hp left")
                                    if self.hp > 0:
                                        return pikachu.battle(charmnader)
                                    else:
                                        print(self.name,"fainted")
                            else:
                                print(self.name,"fainted")
                        else:
                            print(other.name,"fainted")

                    else:
                        print("that is not an attack")
                        return pikachu.battle(charmander)
                else:
                    print(other.name,"fainted")
            else:
                print(self.name,"fainted")

pikachu = Pokemon(100, 25, 45, 0, 49, "pikachu")
charmander = Pokemon(100, 20, 30, 0, 49, "charmander")
pikachu.battle(charmander)

    
