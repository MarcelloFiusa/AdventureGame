#Jogo de Aventura

#Chegando a finais diferentes, dependendo de suas respostas

#Cenário: Estou numa guerra entre duas nações, Água e Fogo. Para a nação da água vencer, derrotando os malignos da nação do Fogo
#devo tomar as decisões corretas para que isso aconteça!
import random


class JogoDeAventura:
    def __init__(self):
        self.pergunta1 = 'Você é da nação da água ou do fogo? (agua/fogo)'
        self.pergunta2 = 'Você prefere equilibrio ou controle? (E/C)'
        self.pergunta3 = 'Você prefere força bruta ou determinação? (FB/D)'
        self.inimigo = ['Combustão',
                        'Raio']
        self.finalDaHistoria1 = 'Ele é muito forte pra você! Quebrou suas defesas de gelo e conseguiu te atingir! Recue!!!'
        self.finalDaHistoria2 = 'Os raios do inimigo são ineficazes contra sua especialidade! Você venceu sem derramar uma gota de suor! (Talvez pela temperatura negativa haha)'
        self.finalDaHistoria3 = 'Com muita agilidade e treino, você conseguiu chegar no alcance de sua habilidade e dominou completamente seu oponente. Mais uma marionete para sua coleção >:D'
        self.finalDaHistoria4 = 'Os raios do inimigo te deixam completamente paralizado(a), a derrota é certa..'
        self.finalDaHistoria5 = 'Então você é o inimigo?!?! Achei que podia confiar em você!!!'
        self.finalDaHistoria6 = 'Você ainda pode se redimir pelos maus de sua nação! Paralize-o e corrija os erros do passado!'
        self.finalDaHistoria7 = 'Você ainda pode se redimir pelos maus de sua nação! Faça-o recuar e corrija os erros do passado!'



    def Iniciar(self):
        resposta1 = input(self.pergunta1)
        try:
            if resposta1 == 'agua':
                resposta1B = input(self.pergunta2)
                if resposta1B.lower() == 'e':
                    print('sua especialidade de dobra é Gelo!')
                    especialidadeDoOponente = self.GerarInimigo()
                    if especialidadeDoOponente == 'Combustão':
                        print(self.finalDaHistoria1)
                    elif especialidadeDoOponente == 'Raio':
                        print(self.finalDaHistoria2)
                    else:
                        print('algo errado')
                if resposta1B.lower() == 'c':
                    print('sua especialidade de dobra é Sangue!')
                    especialidadeDoOponente = self.GerarInimigo()
                    if especialidadeDoOponente == 'Combustão':
                        print(self.finalDaHistoria3)
                    elif especialidadeDoOponente == 'Raio':
                        print(self.finalDaHistoria4)
            if resposta1 == 'fogo':
                resposta1A = input(self.pergunta3)
                if resposta1A.lower() == 'fb':
                    print('sua especialidade de dobra é Combustão!')
                    especialidadeDoOponente = self.GerarInimigo()
                    if especialidadeDoOponente == 'Combustão':
                        print(self.finalDaHistoria5)
                    elif especialidadeDoOponente == 'Raio':
                        print(self.finalDaHistoria6)
                if resposta1A.lower() == 'd':
                    print('sua especialidade de dobra é Raio!')
                    especialidadeDoOponente = self.GerarInimigo()
                    if especialidadeDoOponente == 'Combustão':
                        print(self.finalDaHistoria7)
                    elif especialidadeDoOponente == 'Raio':
                        print(self.finalDaHistoria5)
        except:
            print('Por favor, digitar da forma que está em parênteses >()<!')
            self.Iniciar()

    def GerarInimigo(self):
        inimigo = random.choice(self.inimigo)
        print(f'Seu inimigo é especialista em: {inimigo}')
        return inimigo


jogar = JogoDeAventura()
jogar.Iniciar()