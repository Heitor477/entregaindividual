"""
Análise Estatística de Crescimento Populacional Municipal (Python + Pandas)
Foco no Ritmo de Expansão Anual, Médias, Medianas e Desvio Padrão por Região
"""

import sys
import pandas as pd
import numpy as np
from dados import obter_dados_municipios

# Garante compatibilidade UTF-8 no terminal Windows
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def carregar_e_analisar():
    df = obter_dados_municipios()

    print("=" * 90)
    print(" ANÁLISE DEMOGRÁFICA REGIONAL: MÉDIAS, MEDIANAS E DESVIOS PADRÃO DAS TAXAS DE EXPANSÃO")
    print("=" * 90)

    # 1. Agrupamento e Métricas por Região
    resumo_regional = df.groupby("regiao").agg(
        Num_Municipios=("taxa", "count"),
        Media_Taxa=("taxa", "mean"),
        Mediana_Taxa=("taxa", "median"),
        Desvio_Padrao=("taxa", lambda x: x.std(ddof=1)),
        Minimo=("taxa", "min"),
        Maximo=("taxa", "max"),
        Ganho_Total_Hab_Ano=("ganho_absoluto", "sum")
    ).reset_index()

    # Coeficiente de Variação (CV% = DP / Media * 100)
    resumo_regional["CV_Pct"] = (resumo_regional["Desvio_Padrao"] / resumo_regional["Media_Taxa"].abs() * 100).round(1)
    resumo_regional["Delta_Media_Mediana"] = (resumo_regional["Media_Taxa"] - resumo_regional["Mediana_Taxa"]).round(2)

    # Formatação de exibição
    print(f"\n{'Regiao':<15} | {'N':<4} | {'Media (%)':<10} | {'Mediana (%)':<11} | {'Desvio Padrao':<13} | {'CV (%)':<7} | {'Delta(Med-Md)':<13} | {'+Hab/Ano':<12}")
    print("-" * 95)

    for _, row in resumo_regional.iterrows():
        print(f"{row['regiao']:<15} | {int(row['Num_Municipios']):<4} | "
              f"{row['Media_Taxa']:>9.2f}% | "
              f"{row['Mediana_Taxa']:>10.2f}% | "
              f"{row['Desvio_Padrao']:>12.2f}% | "
              f"{row['CV_Pct']:>6.1f}% | "
              f"{row['Delta_Media_Mediana']:>+12.2f}% | "
              f"{int(row['Ganho_Total_Hab_Ano']):>+12,d}".replace(",", "."))

    # Total Brasil
    media_br = df["taxa"].mean()
    mediana_br = df["taxa"].median()
    desvio_br = df["taxa"].std(ddof=1)
    cv_br = (desvio_br / abs(media_br) * 100)
    ganho_br = df["ganho_absoluto"].sum()
    delta_br = media_br - mediana_br

    print("-" * 95)
    print(f"{'BRASIL (Total)':<15} | {len(df):<4} | "
          f"{media_br:>9.2f}% | "
          f"{mediana_br:>10.2f}% | "
          f"{desvio_br:>12.2f}% | "
          f"{cv_br:>6.1f}% | "
          f"{delta_br:>+12.2f}% | "
          f"{ganho_br:>+12,d}".replace(",", "."))
    print("=" * 95)

    # 2. Diagnóstico Interpretativo
    print("\nINTERPRETAÇÃO ESTATÍSTICA E TERRITORIAL:")
    print("1. ASSIMETRIA POSITIVA (μ > Md):")
    print("   - Observa-se Delta positivo generalizado. Municípios do agronegócio (MT/GO), polos minerais (PA)")
    print("     e hubs litorâneos (SC/RJ) têm taxas entre 3% e 6.8% a.a., puxando a média para cima.")
    print("   - Conclusão: Em políticas públicas, usar a MÉDIA sobre-estima a demanda da maioria das cidades.")
    print("     A MEDIANA é o estimador correto do comportamento típico.")

    print("\n2. INTERPRETAÇÃO DO DESVIO PADRÃO (σ):")
    print("   - Mede a dispersão intrarregional. No Norte e Centro-Oeste, o desvio padrão elevado (2.0% - 2.5%)")
    print("     revela extrema heterogeneidade: cidades crescendo vertiginosamente ao lado de municípios em esvaziamento.")

    print("\n3. RITMO ABSOLUTO (HABITANTES/ANO):")
    print("   - Cidades de porte intermediário com taxa elevada geram forte pressão relativa.")
    print("   - Metrópoles com ritmo moderado (+0.5% a.a.) concentram a maior pressão em volume absoluto.")

    # Exporta tabela consolidada
    caminho_csv = "C:/Users/12400165/.gemini/antigravity/scratch/crescimento_populacional/resumo_estatistico_regional.csv"
    resumo_regional.to_csv(caminho_csv, index=False, sep=";", decimal=",")
    print(f"\n[OK] Tabela estatística consolidada exportada com sucesso.")

if __name__ == "__main__":
    carregar_e_analisar()
