"""
Dojo 068 - A Revolução Constitucionalista de 9 de julho

Exercício 2: Central de Comunicações

Com o relatório de voluntários em mãos (Exercício 1), você agora trabalha na
Central de Comunicações da revolução. A comunicação entre os batalhões é vital
pois São Paulo está isolado:

CONTEXTO HISTÓRICO:
- São Paulo lutava sozinho contra todos os outros estados
- O Rio Grande do Sul e Minas Gerais não aderiram como esperado
- A marinha bloqueava o porto de Santos
- Era crucial coordenar as tropas nas diferentes frentes

REGRA ESPECIAL:
O comando escolheu usar a Cifra de César com deslocamento 9 em homenagem ao
9 de julho. Assim:
- 'A' vira 'J' (avança 9 letras)
- 'B' vira 'K'
- 'Z' volta para 'I' (alfabeto circular)

OBJETIVO FINAL:
Nos dias em que o número de voluntários ficou acima da média, houve necessidade
de enviar telegramas especiais para reorganizar as tropas e redistribuir os
novos recrutas entre os batalhões. Para cada dia que teve um número excepcional
de voluntários (acima da média), é preciso enviar um telegrama codificado com
instruções para os comandantes.

IMPORTANTE:
- Cada telegrama é uma cópia da mesma mensagem base (pois a ordem de reorganização
  é a mesma, só muda o dia)

Por exemplo:
- Se tivemos 3 dias com voluntários acima da média, precisamos enviar 3 telegramas
  (um para cada dia em que foi necessário reorganizar as tropas)
- Se nenhum dia teve voluntários acima da média, não há necessidade de
  reorganização, então não enviamos telegramas
- O campo 'meta_atingida' não afeta a quantidade de telegramas, pois ele indica
  apenas se atingimos o objetivo geral de 250+ voluntários em algum momento

Implemente as funções seguindo TDD:

>>> codificar_letra('A')
'J'

>>> codificar_letra('Z')
'I'

>>> codificar_letra('N')
'W'

>>> codificar_palavra("AVANTE")
'JEJWCN'

>>> codificar_palavra("ZONA")
'IXWJ'

>>> codificar_palavra("viva")
'EREJ'

>>> codificar_palavra("sao")
'BJX'

>>> codificar_palavra("paulo")
'YJDUX'

>>> codificar_palavra("BATALHAO")
'KJCJUQJX'

>>> codificar_mensagem("AVANTE BATALHAO")
'JEJWCN KJCJUQJX'

>>> codificar_mensagem("viva sao paulo")
'EREJ BJX YJDUX'


>>> contar_telegramas_necessarios({"total": 1400, "dias_acima_media": 3, "meta_atingida": True})
3

>>> contar_telegramas_necessarios({"total": 300, "dias_acima_media": 0, "meta_atingida": False})
0



>>> gerar_telegramas({"total": 1400, "dias_acima_media": 3, "meta_atingida": True}, "AVANTE")
['JEJWCN', 'JEJWCN', 'JEJWCN']

>>> gerar_telegramas({"total": 450, "dias_acima_media": 1, "meta_atingida": False}, "RESISTIR")
['ANBRBCRA']

>>> gerar_telegramas({"total": 300, "dias_acima_media": 0, "meta_atingida": False}, "AGUARDAR")
[]
"""

from string import ascii_uppercase
def codificar_letra(letra):
    """Codifica uma letra usando cifra de César com deslocamento 9"""
    alfabeto = ascii_uppercase
    letra_tratada = letra.upper()

    # index = (ord(letra_tratada) - ord('A') + 9) % (len(alfabeto)) + ord('A')
    # return chr(index)
    
    index = (alfabeto.index(letra_tratada) + 9) % len(alfabeto)
    return alfabeto[index]


def codificar_palavra(palavra):
    """Codifica uma palavra (apenas letras)"""
    return "".join(codificar_letra(letra) for letra in palavra)
    
    # palavra_codificada = ""
    # for letra in palavra:
    #   palavra_codificada += codificar_letra(letra)
    # return palavra_codificada


def codificar_mensagem(mensagem):
    """Codifica mensagem completa (letras, espaços, números)"""
    return " ".join(codificar_palavra(palavra) for palavra in mensagem.split())

    # resposta = ''
    # for palavra in mensagem.split():
    #     if len(resposta) > 0:
    #       resposta += ' '
    #     resposta += codificar_palavra(palavra)
    # return resposta

def contar_telegramas_necessarios(relatorio_voluntarios):
    """Conta quantos telegramas são necessários baseado no relatório.
    Um telegrama para cada dia que precisou reorganizar tropas devido
    ao número acima da média de voluntários."""
    return relatorio_voluntarios['dias_acima_media']

def gerar_telegramas(relatorio_voluntarios, mensagem_base):
    """Gera telegramas codificados para cada dia que precisou reorganização.
    Retorna uma lista com a mensagem_base codificada repetida N vezes,
    onde N é o número de dias acima da média."""
    qtd_dia = contar_telegramas_necessarios(relatorio_voluntarios)
    return [codificar_mensagem(mensagem_base)] * qtd_dia

    # retorno = []
    # for index in range(qtd_dia):
    #     retorno.append(codificar_mensagem(mensagem_base))
    # return retorno
