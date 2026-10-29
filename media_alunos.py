
alunos = [
    {'nome' : 'Yasmin', 'notas' : [7, 7] , 'idade' : 16, 'faltas' : 11},
    {'nome' : 'Bruno', 'notas' : [8, 7], 'idade' : 16, 'faltas' : 3}

]

def calcular_media(soma, qtde):
    return soma / qtde

def status_aprovacao(nota):
    if nota >=7:
        return 'Aprovado'
    return 'Reprovado'


for aluno in alunos:
    qtde_notas = len(aluno['notas'])
    soma = sum(aluno['notas'])
    nota = calcular_media(soma, qtde_notas)
    faltas = aluno['faltas']
    print(f'Aluno: {aluno['nome']}, Nota: {nota}, Status: {status_aprovacao}(nota, faltas)')


    