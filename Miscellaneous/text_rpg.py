from random import randint
from time import sleep

class Player:
    def __init__(self, hp, dano, var_dano, velocidade_projeteis):
        self.hp = hp
        self.dano = dano
        self.var_dano = var_dano
        self.projeteis = []
        self.velocidade_projeteis = velocidade_projeteis

    def disparar(self, distancia):
        self.projeteis.append(Projetil(self.dano, self.var_dano, distancia, self.velocidade_projeteis))


class Projetil:
    def __init__(self, dano_base, var_dano, distancia, velocidade):
        self.dano = randint(dano_base - var_dano, dano_base + var_dano)
        self.distancia = distancia
        self.velocidade = velocidade


class Inimigo:
    def __init__(self, hp, distancia, dano_min, dano_max, chance_crit, espera):
        self.hp = hp
        self.distancia = distancia
        self.dano_min = dano_min
        self.dano_max = dano_max
        self.chance_crit_base = chance_crit
        self.chance_crit = chance_crit
        self.espera = espera
        self.espera_atual = espera

    def atacar(self):
        dano = randint(self.dano_min, self.dano_max)
        if randint(0, 100) < self.chance_crit:
            dano *= 4
        return dano

    def update_crit(self):
        if self.distancia < 100:
            self.chance_crit = self.chance_crit_base + (100 - self.distancia)
        else:
            self.chance_crit = self.chance_crit_base


jogador = Player(300, 20, 7, 50)
inimigo_1 = Inimigo(600, 200, 15, 45, 5, 3)
turno = 1
largura_caixa = 60

print(' RPG em texto '.center(largura_caixa, '='), '\n')

while True:
    print(f' Turno {turno} '.center(largura_caixa, '-'))
    print(f'\nHP: {jogador.hp}    Projeteis: {len(jogador.projeteis)}    HP Inimigo: {inimigo_1.hp}    Distância: {inimigo_1.distancia}')
    
    print('''\nO que fazer:
1 - Disparar;
2 - Aumentar Dano em 5 em troca de 25 de vida
3 - Distância do inimigo
4 - Auto-destruir''')
    sleep(1)

    acao = str(input('>>> '))

    try:
        acao = int(acao)
    except:
        print('Ação inválida;')
        continue
    
    print()

    if acao == 1:
        jogador.disparar(inimigo_1.distancia)
        print('Um projetil foi disparado')
        sleep(1)

    elif acao == 2:
        print(f'HP: {jogador.hp} > {jogador.hp - 25}    Dano: {jogador.dano} > {jogador.dano + 5}')
        jogador.hp -= 25
        jogador.dano += 5
        sleep(1)

    elif acao == 3:
        var_dis = str(input('Variação de distância: '))
        try:
            var_dis = int(var_dis)
        except:
            print('Variação inválida')
        else:
            if inimigo_1.distancia - var_dis > 0:
                inimigo_1.distancia -= var_dis
                inimigo_1.update_crit()
            else:
                print('Não pode ultrapassar o inimigo')
        sleep(1)

    elif acao == 4:
        print('Você se auto-destruiu')
        sleep(2)
        print('Não entendemos o porquê')
        sleep(2)
        print('Você nem tentou')
        sleep(2)
        break

    for projetil in jogador.projeteis:
        projetil.distancia -= projetil.velocidade
        if projetil.distancia <= 0:
            inimigo_1.hp -= projetil.dano
            print(f'Um projetil atingiu o inimigo, causando {projetil.dano} de dano')
            jogador.projeteis.remove(projetil)
            sleep(1)

    if inimigo_1.hp < 0:
        print('\nO inimigo foi derrotado!')
        sleep(2)
        print('O mundo foi salvo!')
        sleep(2)
        print('Obrigado!!')
        sleep(2)
        break
    
    if inimigo_1.espera_atual == 0:
        dano_ini = inimigo_1.atacar()
        jogador.hp -= dano_ini
        inimigo_1.espera_atual = inimigo_1.espera
        print(f'O inimigo atacou aplicando {dano_ini} de dano')
        sleep(1)
    else:
        inimigo_1.espera_atual -= 1

    if jogador.hp < 0:
        print('\nVocê foi derrotado...')
        sleep(2)
        print('O inimigo segue manchando o mundo com o caos...')
        sleep(2)
        print('Mas ainda há esperanças!')
        sleep(2)
        break

    turno += 1
    
print('\n', ' Game Over '.center(largura_caixa, '='), sep='')