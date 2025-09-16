"""
Dojo 068 - A Revolução Constitucionalista de 9 de julho

Exercício 3: Planejamento de Suprimentos

CONTEXTO HISTÓRICO:
A Revolução Constitucionalista foi o maior conflito armado da história do Brasil.
São Paulo lutava em completa desvantagem:

Tropas Federais (Governo):
- 18.000 homens no setor Sul
- 20.000 homens no setor Norte
- 15.000 homens na fronteira com Minas
- 1 arma automática para cada 3 soldados
- Mais de 200 canhões no total

Tropas Paulistas:
- Apenas 46.500 combatentes no total
- 1 arma automática para cada 50 soldados
- Menos de 40 canhões no total
- Indústrias improvisadas produzindo munição
- Porto de Santos bloqueado pela Marinha

REGRAS DE CONSUMO:
Por Voluntário:
- 3 unidades de comida por dia
- 1 remédio por dia

Por Telegrama Enviado (do Ex2):
- 2 unidades de munição (para proteger mensageiros)
- 1 arma (para defesa do mensageiro)

REGRA ESPECIAL:
Se a meta de 250+ voluntários foi atingida em algum dia (Ex1), o moral está alto
e o consumo aumenta! Aplique +50% em todos os suprimentos.

FORMATO DOS DADOS:
1. Relatório de Voluntários (do Ex1):
   {"total": 300, "dias_acima_media": 2, "meta_atingida": True}

2. Lista de Telegramas (do Ex2):
   ["JEJMOX", "JEJMOX"]  # Cada string é um telegrama codificado

3. Dados das Cidades:
   [
     {
       "cidade": "Campinas",
       "suprimentos": {"comida": 100, "armas": 50, "remedios": 30, "municao": 20}
     }
   ]

4. Dicionário de Retorno:
   {
     "demanda_total": {  # Quanto precisamos de cada item
       "comida": 900,    # 3 por voluntário
       "remedios": 300,  # 1 por voluntário
       "municao": 4,     # 2 por telegrama
       "armas": 2        # 1 por telegrama
     },
     "suprimentos_disponiveis": {  # Soma do que as cidades oferecem
       "comida": 1000,
       "remedios": 500,
       "municao": 50,
       "armas": 10
     },
     "situacao": "SUFICIENTE",  # ou "INSUFICIENTE"
     "faltam": {},  # Itens e quantidades que faltam
     "cidades_fornecedoras": ["Santos"]  # Nomes das cidades que ajudam
   }

OBJETIVO FINAL:
Seu relatório determinará se São Paulo tem condições de sustentar a revolução
ou se precisa buscar apoio de mais cidades. A história mostra que este foi um
dos fatores cruciais: o isolamento de São Paulo contribuiu para o fim do
movimento em outubro de 1932.

Implemente as funções seguindo TDD:

>>> calcular_demanda_comida(300)
900  # 300 voluntários × 3 unidades cada
>>> calcular_demanda_comida(0)
0

>>> calcular_demanda_remedios(300)
300  # 300 voluntários × 1 remédio cada
>>> calcular_demanda_remedios(600)
600

>>> calcular_demanda_municao(["TEL1", "TEL2"])
4  # 2 telegramas × 2 munições cada
>>> calcular_demanda_municao([])
0

>>> aplicar_bonus_meta(1000, True)
1500  # +50% pois meta foi atingida
>>> aplicar_bonus_meta(1000, False)
1000  # Sem bônus pois meta não foi atingida

>>> somar_suprimentos_disponiveis([{"cidade": "Campinas", "suprimentos": {"comida": 100, "armas": 50}}])
{'comida': 100, 'armas': 50}

>>> verificar_suficiencia({"comida": 1000}, {"comida": 800})
('INSUFICIENTE', {'comida': 200})  # Faltam 200 de comida
>>> verificar_suficiencia({"comida": 800}, {"comida": 1000})
('SUFICIENTE', {})  # Nada falta

>>> calcular_suprimentos({"total": 300, "dias_acima_media": 0, "meta_atingida": False}, [], [{"cidade": "Santos", "suprimentos": {"armas": 10, "comida": 1000, "remedios": 500, "municao": 50}}])
{'demanda_total': {'comida': 900, 'remedios': 300, 'municao': 0, 'armas': 0}, 'suprimentos_disponiveis': {'armas': 10, 'comida': 1000, 'remedios': 500, 'municao': 50}, 'situacao': 'SUFICIENTE', 'faltam': {}, 'cidades_fornecedoras': ['Santos']}
"""

def calcular_demanda_comida(total_voluntarios):
    """Calcula demanda de comida (3 por voluntário)"""
    pass

def calcular_demanda_remedios(total_voluntarios):
    """Calcula demanda de remédios (1 por voluntário)"""
    pass

def calcular_demanda_municao(lista_telegramas):
    """Calcula demanda de munição (2 por telegrama)"""
    pass

def aplicar_bonus_meta(valor, meta_atingida):
    """Aplica bônus de +50% se meta foi atingida"""
    pass

def somar_suprimentos_disponiveis(dados_cidades):
    """Soma todos os suprimentos disponíveis das cidades"""
    pass

def verificar_suficiencia(demanda_total, suprimentos_disponiveis):
    """Verifica se suprimentos são suficientes. Retorna (situacao, faltam)"""
    pass

def calcular_suprimentos(relatorio_voluntarios, telegramas, dados_cidades):
    """Calcula demanda total, soma suprimentos disponíveis e verifica suficiência"""
    pass 