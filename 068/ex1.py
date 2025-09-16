"""
Dojo 068 - A Revolução Constitucionalista de 9 de julho

Exercício 1: Relatório dos Voluntários

Era 9 de julho de 1932. São Paulo se levantava contra o governo provisório de 
Getúlio Vargas. O movimento precisava de amplo apoio popular para ter sucesso.
Você trabalha no Quartel General da revolução e precisa analisar os dados de
alistamento dos voluntários.

CONTEXTO HISTÓRICO:
- O alistamento ultrapassou 200 mil voluntários
- Mas só havia armas para 46.500 combatentes
- O apoio popular era crucial para sustentar a revolução
- A mobilização incluía mulheres, estudantes e trabalhadores
- O fluxo diário de voluntários era um indicador importante:
  * Dias com muitos voluntários exigiam reorganização das tropas
  * A média diária servia como referência do apoio popular
  * Dias acima da média indicavam momentos de forte adesão

OBJETIVO FINAL:
Seu relatório conterá:
- Total de voluntários (soma de todos os dias)
- Média de voluntários por dia (total ÷ número de dias)
- Quantos dias ficaram acima da média (importante para reorganização)
- Se algum dia atingiu 250+ voluntários (meta do alto comando)

Por exemplo, para os dias: [150, 200, 180, 220, 300, 250, 100]
- Total = 1400 voluntários
- Média = 200 voluntários por dia
- 3 dias acima da média (220, 300, 250 > 200)
- Meta atingida (300 e 250 >= 250)

Exemplo de relatório:
{
    "total": 1400,
    "dias_acima_media": 3,
    "meta_atingida": True
}

Implemente as funções seguindo TDD:

>>> contar_total_voluntarios([150, 200, 180])
530

>>> contar_total_voluntarios([])
0

>>> calcular_media_voluntarios([150, 200, 100])
150.0

>>> calcular_media_voluntarios([100])
100.0

>>> calcular_media_voluntarios([])
0

>>> contar_dias_acima_media([100, 200, 150])
1

>>> contar_dias_acima_media([100, 100, 100])
0

>>> verificar_meta_atingida([100, 200, 150])
False

>>> verificar_meta_atingida([100, 250, 150])
True

>>> relatorio_voluntarios([150, 200, 180, 220, 300, 250, 100])
{'total': 1400, 'dias_acima_media': 3, 'meta_atingida': True}

>>> relatorio_voluntarios([100, 200, 150])
{'total': 450, 'dias_acima_media': 1, 'meta_atingida': False}

>>> relatorio_voluntarios([])
{'total': 0, 'dias_acima_media': 0, 'meta_atingida': False}
"""

def contar_total_voluntarios(lista_dias):
    """Soma o total de voluntários"""
    return sum(lista_dias)

def calcular_media_voluntarios(lista_dias):
    """Calcula a média de voluntários por dia (total ÷ número de dias)"""
    if len(lista_dias) == 0:
        return 0
    return sum(lista_dias)/len(lista_dias)

def contar_dias_acima_media(lista_dias):
    """Conta quantos dias tiveram mais voluntários que a média diária"""
    media = calcular_media_voluntarios(lista_dias)
    total = 0
    for dia in lista_dias:
        if dia > media:
            total += 1
    return total

def verificar_meta_atingida(lista_dias):
    """Verifica se algum dia atingiu ou superou 250 voluntários"""
    for dia in lista_dias:
        if dia >= 250:
            return True
    return False

def relatorio_voluntarios(lista_dias):
    total = contar_total_voluntarios(lista_dias)
    media = contar_dias_acima_media(lista_dias)
    meta = verificar_meta_atingida(lista_dias)
    
    return {'total': total, 'dias_acima_media': media, 'meta_atingida': meta}