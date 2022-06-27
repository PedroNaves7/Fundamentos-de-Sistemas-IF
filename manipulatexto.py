from tkinter import N


nome_aluno = ['Pedro', 'Joao']

with open('alunos.txt', 'w') as escrever:
    for aluno in nome_aluno:
        escrever.write(aluno)