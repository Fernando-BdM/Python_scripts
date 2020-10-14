#!/usr/bin/env python
# coding: utf-8

# In[19]:


import random

class blackjack:
    
    
    def __init__(self):
        numeros = list(range(2,11))
        numeros.extend(['Valete de','Rainha de','Rei de'])
        numeros.insert(0,'Às')
        naipes = ['Ouro','Paus','Copas','Coração']
        self.cartas = []
        self.vale10 = []
        self.out = []
        self.pontos = 0
        self.pontos_pc = 0
        for x in naipes:
            self.cartas.extend(list(map(lambda b : str(b) + " "+ x,numeros)))
        for x in naipes:
            self.vale10.extend((list(map(lambda b : str(b) + " "+ x,[10,'Valete de','Rainha de','Rei de']))))
        self.jogar()

    def jogar(self):

        print('#################### - BLACKJACK - ###################')
        print('Bem vindo à jogatina, o blackjack (ou 21) é um jogo de cartas em que o objetivo\né ter mais pontos do que o adversário', 
              'mas sem ultrapassar os 21 pontos')
        print('A pontuação se dá conforme segue: \n2 até 10: pontuam o valor da carta\n2 = 2 pontos e 10 = 10 pontos por exemplo')
        print('O Às pode valer 1 ou 11 pontos, você que escolhe!')
        print('J, Q e K valem 10 pontos\n')
        print('Para este jogo seu adversario será o PC, boa sorte!\n')

        self.pontos = 0
        self.pontos_pc = 0
        self.escolher()
        self.escolher_pc()


        while True:
            continua = input("Quer pescar mais uma carta?\n1)Sim\n2)Nao\n")
            print("======================================================")
            if continua in ["1","Sim","sim","S","s"]:
                if self.escolher():
                    break

                if self.escolher_pc():
                    break

            elif continua in ["2","Nao","nao","Não","não","N","n"]:
                while True:
                    if self.pontos_pc > self.pontos:
                        print("O PC conseguiu mais pontos que voce!! Você perdeu!!" )
                        break
                    elif self.escolher_pc():
                        break
                break
                
            else : pass
        

    def escolher(self):

        escolha = random.choice(self.cartas)

        while escolha in self.out:
            escolha = random.choice(self.cartas)

        self.out.append(escolha)
        print("Voce pescou : {}".format(escolha))

        if escolha in self.vale10:
            self.pontos += 10
            print("Você tem {} pontos\n".format(self.pontos))

        elif escolha[0] == "À":

            while True :
                escolha_as = input("Você pode escolher qual valor quer somar: 1 ou 11? ")

                if escolha_as == "1" or escolha_as == "11":
                    break

            self.pontos += int(escolha_as)
            print("Você tem {} pontos\n".format(self.pontos))

        else:
            self.pontos += int(escolha[0])
            print("Você tem {} pontos\n".format(self.pontos))
        return self.testa(self.pontos)

    def escolher_pc(self):


        if self.pontos_pc in [18,19,20]:
            print ("O PC já tem {} pontos e não vai mais pescar!\n".format(self.pontos_pc))
        else:
            escolha = random.choice(self.cartas)
            while escolha in self.out:
                escolha = random.choice(self.cartas)

            self.out.append(escolha)
            print("O PC pescou : {}".format(escolha))

            if escolha in self.vale10:
                self.pontos_pc += 10
                print("O PC tem {} pontos\n".format(self.pontos_pc))

            elif escolha[0] == "À":
                self.pontos_pc += 1
                print("O PC tem {} pontos\n".format(self.pontos_pc))

            else:
                self.pontos_pc += int(escolha[0])
                print("O PC tem {} pontos\n".format(self.pontos_pc))

            return self.testa_pc(self.pontos_pc)

    def testa(self,pontos):

        if pontos == 21:
            print("Você chegou no 21!! Parabéns você Ganhou!")
            print("======================================================")
            return True

        elif pontos >= 22:
            print("Infelizmente você passou de 21 e perdeu!")
            print("======================================================")
            return True

        else: pass

    def testa_pc(self,pontos):

        if pontos == 21:
            print("O PC chegou no 21!! Você Perdeu!")
            print("======================================================")
            return True

        elif pontos >= 22:

            print("O PC passou de 21!!! Parabéns você Ganhou!")
            print("======================================================")
            return True

        else: pass 
    

    


# In[22]:


blackjack()

