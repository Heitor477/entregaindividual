"""
Base de Dados Demográfica de Municípios Brasileiros
Crescimento Populacional Absoluto e Ritmo de Expansão Anual
"""

import pandas as pd

def obter_dados_municipios() -> pd.DataFrame:
    dados = [
        # CENTRO-OESTE (Forte expansão agrícola, alta dispersão e assimetria positiva)
        {"nome": "Lucas do Rio Verde", "uf": "MT", "regiao": "Centro-Oeste", "pop": 83798, "taxa": 4.85},
        {"nome": "Sinop", "uf": "MT", "regiao": "Centro-Oeste", "pop": 196094, "taxa": 4.62},
        {"nome": "Sorriso", "uf": "MT", "regiao": "Centro-Oeste", "pop": 110635, "taxa": 4.28},
        {"nome": "Rio Verde", "uf": "GO", "regiao": "Centro-Oeste", "pop": 225696, "taxa": 2.35},
        {"nome": "Senador Canedo", "uf": "GO", "regiao": "Centro-Oeste", "pop": 155635, "taxa": 5.12},
        {"nome": "Goiânia", "uf": "GO", "regiao": "Centro-Oeste", "pop": 1437237, "taxa": 0.98},
        {"nome": "Aparecida de Goiânia", "uf": "GO", "regiao": "Centro-Oeste", "pop": 527550, "taxa": 1.54},
        {"nome": "Brasília", "uf": "DF", "regiao": "Centro-Oeste", "pop": 2817068, "taxa": 0.84},
        {"nome": "Valparaíso de Goiás", "uf": "GO", "regiao": "Centro-Oeste", "pop": 198861, "taxa": 3.65},
        {"nome": "Águas Lindas de Goiás", "uf": "GO", "regiao": "Centro-Oeste", "pop": 225671, "taxa": 3.10},
        {"nome": "Campo Grande", "uf": "MS", "regiao": "Centro-Oeste", "pop": 897938, "taxa": 1.15},
        {"nome": "Dourados", "uf": "MS", "regiao": "Centro-Oeste", "pop": 243368, "taxa": 1.82},
        {"nome": "Três Lagoas", "uf": "MS", "regiao": "Centro-Oeste", "pop": 132152, "taxa": 2.45},
        {"nome": "Cuiabá", "uf": "MT", "regiao": "Centro-Oeste", "pop": 650912, "taxa": 1.45},
        {"nome": "Várzea Grande", "uf": "MT", "regiao": "Centro-Oeste", "pop": 299472, "taxa": 1.62},
        {"nome": "Rondonópolis", "uf": "MT", "regiao": "Centro-Oeste", "pop": 244897, "taxa": 2.15},
        {"nome": "Primavera do Leste", "uf": "MT", "regiao": "Centro-Oeste", "pop": 85146, "taxa": 4.10},
        {"nome": "Nova Mutum", "uf": "MT", "regiao": "Centro-Oeste", "pop": 55648, "taxa": 4.75},
        {"nome": "Corumbá", "uf": "MS", "regiao": "Centro-Oeste", "pop": 96261, "taxa": -0.52},
        {"nome": "Ponta Porã", "uf": "MS", "regiao": "Centro-Oeste", "pop": 92017, "taxa": 1.32},
        {"nome": "Cáceres", "uf": "MT", "regiao": "Centro-Oeste", "pop": 89681, "taxa": 0.15},
        {"nome": "Barra do Garças", "uf": "MT", "regiao": "Centro-Oeste", "pop": 69210, "taxa": 1.20},
        {"nome": "Jataí", "uf": "GO", "regiao": "Centro-Oeste", "pop": 105729, "taxa": 1.78},
        {"nome": "Itumbiara", "uf": "GO", "regiao": "Centro-Oeste", "pop": 107970, "taxa": 1.12},
        {"nome": "Catalão", "uf": "GO", "regiao": "Centro-Oeste", "pop": 114427, "taxa": 2.10},
        {"nome": "Anápolis", "uf": "GO", "regiao": "Centro-Oeste", "pop": 398817, "taxa": 1.58},
        {"nome": "Pirenópolis", "uf": "GO", "regiao": "Centro-Oeste", "pop": 26690, "taxa": 0.85},
        {"nome": "Alto Paraíso de Goiás", "uf": "GO", "regiao": "Centro-Oeste", "pop": 10306, "taxa": 2.70},
        {"nome": "Alcinópolis", "uf": "MS", "regiao": "Centro-Oeste", "pop": 4537, "taxa": -0.25},
        {"nome": "Araguainha", "uf": "MT", "regiao": "Centro-Oeste", "pop": 1010, "taxa": -0.80},

        # NORTE (Fronteira mineral e agro, expansão acelerada em capitais jovens)
        {"nome": "Parauapebas", "uf": "PA", "regiao": "Norte", "pop": 267836, "taxa": 4.15},
        {"nome": "Canaã dos Carajás", "uf": "PA", "regiao": "Norte", "pop": 77079, "taxa": 6.85},
        {"nome": "Boa Vista", "uf": "RR", "regiao": "Norte", "pop": 413486, "taxa": 3.25},
        {"nome": "Palmas", "uf": "TO", "regiao": "Norte", "pop": 302692, "taxa": 2.45},
        {"nome": "Manaus", "uf": "AM", "regiao": "Norte", "pop": 2063547, "taxa": 1.22},
        {"nome": "Porto Velho", "uf": "RO", "regiao": "Norte", "pop": 460413, "taxa": 0.75},
        {"nome": "Macapá", "uf": "AP", "regiao": "Norte", "pop": 442933, "taxa": 0.95},
        {"nome": "Rio Branco", "uf": "AC", "regiao": "Norte", "pop": 364756, "taxa": 0.82},
        {"nome": "Santarém", "uf": "PA", "regiao": "Norte", "pop": 331937, "taxa": 1.15},
        {"nome": "Marabá", "uf": "PA", "regiao": "Norte", "pop": 266536, "taxa": 1.48},
        {"nome": "Ananindeua", "uf": "PA", "regiao": "Norte", "pop": 478778, "taxa": -0.15},
        {"nome": "Belém", "uf": "PA", "regiao": "Norte", "pop": 1303389, "taxa": -0.65},
        {"nome": "Castanhal", "uf": "PA", "regiao": "Norte", "pop": 192262, "taxa": 1.05},
        {"nome": "Araguaína", "uf": "TO", "regiao": "Norte", "pop": 171301, "taxa": 1.35},
        {"nome": "Gurupi", "uf": "TO", "regiao": "Norte", "pop": 85126, "taxa": 1.10},
        {"nome": "Vilhena", "uf": "RO", "regiao": "Norte", "pop": 95832, "taxa": 1.85},
        {"nome": "Cruzeiro do Sul", "uf": "AC", "regiao": "Norte", "pop": 91888, "taxa": 1.15},
        {"nome": "Iranduba", "uf": "AM", "regiao": "Norte", "pop": 60993, "taxa": 3.40},
        {"nome": "Pacaraima", "uf": "RR", "regiao": "Norte", "pop": 19305, "taxa": 4.80},
        {"nome": "Parintins", "uf": "AM", "regiao": "Norte", "pop": 96372, "taxa": -0.45},
        {"nome": "Coari", "uf": "AM", "regiao": "Norte", "pop": 70616, "taxa": -0.85},

        # NORDESTE (Transição demográfica avançada, interiorização dinâmica)
        {"nome": "Salvador", "uf": "BA", "regiao": "Nordeste", "pop": 2418005, "taxa": -0.95},
        {"nome": "Fortaleza", "uf": "CE", "regiao": "Nordeste", "pop": 2428678, "taxa": -0.40},
        {"nome": "Recife", "uf": "PE", "regiao": "Nordeste", "pop": 1488920, "taxa": -0.35},
        {"nome": "Natal", "uf": "RN", "regiao": "Nordeste", "pop": 751300, "taxa": -0.65},
        {"nome": "São Luís", "uf": "MA", "regiao": "Nordeste", "pop": 1037775, "taxa": 0.25},
        {"nome": "Maceió", "uf": "AL", "regiao": "Nordeste", "pop": 957916, "taxa": 0.22},
        {"nome": "Teresina", "uf": "PI", "regiao": "Nordeste", "pop": 866300, "taxa": 0.45},
        {"nome": "João Pessoa", "uf": "PB", "regiao": "Nordeste", "pop": 833932, "taxa": 1.35},
        {"nome": "Aracaju", "uf": "SE", "regiao": "Nordeste", "pop": 602757, "taxa": 0.48},
        {"nome": "Feira de Santana", "uf": "BA", "regiao": "Nordeste", "pop": 616279, "taxa": 0.85},
        {"nome": "Campina Grande", "uf": "PB", "regiao": "Nordeste", "pop": 419379, "taxa": 0.82},
        {"nome": "Caruaru", "uf": "PE", "regiao": "Nordeste", "pop": 378052, "taxa": 1.45},
        {"nome": "Petrolina", "uf": "PE", "regiao": "Nordeste", "pop": 386786, "taxa": 2.15},
        {"nome": "Juazeiro", "uf": "BA", "regiao": "Nordeste", "pop": 235816, "taxa": 1.40},
        {"nome": "Vitória da Conquista", "uf": "BA", "regiao": "Nordeste", "pop": 370868, "taxa": 1.65},
        {"nome": "Juazeiro do Norte", "uf": "CE", "regiao": "Nordeste", "pop": 286120, "taxa": 1.10},
        {"nome": "Sobral", "uf": "CE", "regiao": "Nordeste", "pop": 203062, "taxa": 0.75},
        {"nome": "Mossoró", "uf": "RN", "regiao": "Nordeste", "pop": 264577, "taxa": 0.20},
        {"nome": "Luís Eduardo Magalhães", "uf": "BA", "regiao": "Nordeste", "pop": 107909, "taxa": 4.80},
        {"nome": "Barreiras", "uf": "BA", "regiao": "Nordeste", "pop": 159743, "taxa": 1.55},
        {"nome": "Balsas", "uf": "MA", "regiao": "Nordeste", "pop": 101767, "taxa": 2.10},
        {"nome": "Ilhéus", "uf": "BA", "regiao": "Nordeste", "pop": 178703, "taxa": -1.20},
        {"nome": "Itabuna", "uf": "BA", "regiao": "Nordeste", "pop": 186708, "taxa": -0.90},

        # SUDESTE (Metrópoles consolidadas estáveis/encolhendo, dinamismo no interior)
        {"nome": "São Paulo", "uf": "SP", "regiao": "Sudeste", "pop": 11451245, "taxa": 0.15},
        {"nome": "Rio de Janeiro", "uf": "RJ", "regiao": "Sudeste", "pop": 6211423, "taxa": -0.32},
        {"nome": "Belo Horizonte", "uf": "MG", "regiao": "Sudeste", "pop": 2315560, "taxa": -0.25},
        {"nome": "Vitória", "uf": "ES", "regiao": "Sudeste", "pop": 322869, "taxa": -0.15},
        {"nome": "Campinas", "uf": "SP", "regiao": "Sudeste", "pop": 1138309, "taxa": 0.52},
        {"nome": "São José dos Campos", "uf": "SP", "regiao": "Sudeste", "pop": 697428, "taxa": 0.85},
        {"nome": "Ribeirão Preto", "uf": "SP", "regiao": "Sudeste", "pop": 698259, "taxa": 1.30},
        {"nome": "Sorocaba", "uf": "SP", "regiao": "Sudeste", "pop": 723574, "taxa": 1.65},
        {"nome": "Paulínia", "uf": "SP", "regiao": "Sudeste", "pop": 110537, "taxa": 2.85},
        {"nome": "Indaiatuba", "uf": "SP", "regiao": "Sudeste", "pop": 255729, "taxa": 2.15},
        {"nome": "Itupeva", "uf": "SP", "regiao": "Sudeste", "pop": 70616, "taxa": 3.55},
        {"nome": "Uberlândia", "uf": "MG", "regiao": "Sudeste", "pop": 713232, "taxa": 1.68},
        {"nome": "Uberaba", "uf": "MG", "regiao": "Sudeste", "pop": 337846, "taxa": 1.25},
        {"nome": "Juiz de Fora", "uf": "MG", "regiao": "Sudeste", "pop": 540756, "taxa": 0.45},
        {"nome": "Nova Lima", "uf": "MG", "regiao": "Sudeste", "pop": 111697, "taxa": 3.15},
        {"nome": "Serra", "uf": "ES", "regiao": "Sudeste", "pop": 520653, "taxa": 2.10},
        {"nome": "Maricá", "uf": "RJ", "regiao": "Sudeste", "pop": 197300, "taxa": 3.90},
        {"nome": "Macaé", "uf": "RJ", "regiao": "Sudeste", "pop": 246391, "taxa": 1.75},
        {"nome": "São Gonçalo", "uf": "RJ", "regiao": "Sudeste", "pop": 896744, "taxa": -0.85},
        {"nome": "Duque de Caxias", "uf": "RJ", "regiao": "Sudeste", "pop": 808152, "taxa": -0.45},
        {"nome": "Santos", "uf": "SP", "regiao": "Sudeste", "pop": 418608, "taxa": -0.20},
        {"nome": "Praia Grande", "uf": "SP", "regiao": "Sudeste", "pop": 349935, "taxa": 2.65},

        # SUL (Envelhecimento populacional, atração forte em SC e agro do PR)
        {"nome": "Porto Alegre", "uf": "RS", "regiao": "Sul", "pop": 1332570, "taxa": -0.55},
        {"nome": "Curitiba", "uf": "PR", "regiao": "Sul", "pop": 1773733, "taxa": 0.25},
        {"nome": "Florianópolis", "uf": "SC", "regiao": "Sul", "pop": 537213, "taxa": 2.25},
        {"nome": "Joinville", "uf": "SC", "regiao": "Sul", "pop": 616323, "taxa": 1.78},
        {"nome": "Itajaí", "uf": "SC", "regiao": "Sul", "pop": 264054, "taxa": 3.20},
        {"nome": "Balneário Camboriú", "uf": "SC", "regiao": "Sul", "pop": 139155, "taxa": 2.85},
        {"nome": "Palhoça", "uf": "SC", "regiao": "Sul", "pop": 222598, "taxa": 4.15},
        {"nome": "São José", "uf": "SC", "regiao": "Sul", "pop": 270295, "taxa": 2.30},
        {"nome": "Blumenau", "uf": "SC", "regiao": "Sul", "pop": 361261, "taxa": 1.45},
        {"nome": "Chapecó", "uf": "SC", "regiao": "Sul", "pop": 254781, "taxa": 2.95},
        {"nome": "Londrina", "uf": "PR", "regiao": "Sul", "pop": 555965, "taxa": 0.95},
        {"nome": "Maringá", "uf": "PR", "regiao": "Sul", "pop": 409657, "taxa": 1.35},
        {"nome": "Cascavel", "uf": "PR", "regiao": "Sul", "pop": 348051, "taxa": 1.85},
        {"nome": "Fazenda Rio Grande", "uf": "PR", "regiao": "Sul", "pop": 148873, "taxa": 4.95},
        {"nome": "Pelotas", "uf": "RS", "regiao": "Sul", "pop": 325689, "taxa": -0.15},
        {"nome": "Novo Hamburgo", "uf": "RS", "regiao": "Sul", "pop": 227732, "taxa": -0.30},
        {"nome": "Passo Fundo", "uf": "RS", "regiao": "Sul", "pop": 206224, "taxa": 1.15},
        {"nome": "Rio Grande", "uf": "RS", "regiao": "Sul", "pop": 191900, "taxa": -0.25},
        {"nome": "Toledo", "uf": "PR", "regiao": "Sul", "pop": 150470, "taxa": 2.25}
    ]
    df = pd.DataFrame(dados)
    
    # Crescimento Absoluto Anual (+hab/ano)
    df["ganho_absoluto"] = (df["pop"] * (df["taxa"] / 100)).round().astype(int)

    # Porte Populacional
    def classificar_porte(pop):
        if pop < 20000:
            return "Pequeno (<20k)"
        elif pop < 50000:
            return "Médio-Pequeno (20k-50k)"
        elif pop < 150000:
            return "Médio (50k-150k)"
        elif pop < 500000:
            return "Médio-Grande (150k-500k)"
        else:
            return "Grande / Metrópole (>500k)"

    df["porte"] = df["pop"].apply(classificar_porte)
    return df
