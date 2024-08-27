import math
import random

aluno1 = input('insira o nome do primeiro aluno: ')
aluno2 = input('insira o nome do segundo aluno: ')
aluno3 = input('insira o nome do terceiro aluno: ')
aluno4 = input('insira o nome do quarto aluno: ')

alunos = [aluno1, aluno2, aluno3, aluno4]

random.shuffle(alunos)

print(f'a ordem de apresentação é: {alunos}')
