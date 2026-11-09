# Dashboard de Crescimento Populacional Absoluto & Ritmo Municipal

Dashboard interativo desenvolvido para estudo demográfico da expansão anual de municípios brasileiros, integrando métricas estatísticas rigorosas (**médias**, **medianas** e **desvios padrão**) e sua interpretação territorial.

## 🎯 Foco e Dimensões de Análise

1. **Ritmo de Expansão Anual (% a.a.)**: Taxa geométrica/exponencial anualizada de crescimento populacional dos municípios.
2. **Crescimento Populacional Absoluto (+habitantes/ano)**: Impacto real em volume populacional adicionado a cada ciclo anual.
3. **Média Aritmética ($\mu$)**: Expressa o valor ponderado global, porém é vulnerável a *outliers* (cidades polo, mineração ou frentes agrícolas).
4. **Mediana ($Md$)**: Representa o **município típico** (percentil 50%), insensível a valores extremos.
5. **Desvio Padrão ($\sigma$) & Coeficiente de Variação ($CV$)**: Mensuram a heterogeneidade e a desigualdade do ritmo demográfico intrarregional.

---

## 📊 Estrutura dos Arquivos

- `index.html`: Dashboard interativo completo (HTML5 + Tailwind CSS + Gráficos Vetoriais SVG nativos + Simulador de Projeções).
- `analise_demografica.py`: Script Python puro (sem dependências externas) para processamento, cálculo e sumarização estatística tabular.
- `README.md`: Documentação técnica e guia metodológico.

---

## 🧮 Metodologia e Fórmulas Estatísticas

### 1. Taxa Geométrica Exponencial Anual ($r$)
$$r = \frac{\ln(P_t / P_0)}{t}$$
Onde $P_0$ é a população inicial, $P_t$ a população final e $t$ o intervalo em anos.

### 2. Média Aritmética Regional ($\mu$)
$$\mu = \frac{1}{n} \sum_{i=1}^{n} r_i$$

### 3. Mediana Regional ($Md$)
Valor central do rol ordenado de taxas $r_{(1)} \le r_{(2)} \le \dots \le r_{(n)}$.

### 4. Desvio Padrão Amostral ($\sigma$)
$$\sigma = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (r_i - \mu)^2}$$

### 5. Coeficiente de Variação ($CV$)
$$CV = \left( \frac{\sigma}{|\mu|} \right) \times 100\%$$

---

## 💡 Principais Conclusões e Interpretação

- **Assimetria Positiva**: Na maioria das regiões brasileiras, $\mu > Md$. Isso ocorre porque polos de atração intensa (como Sinop-MT, Sorriso-MT, Canaã dos Carajás-PA e cidades litorâneas de SC) puxam a média para cima, enquanto uma grande proporção de municípios do interior experimenta estagnação demográfica ($r \approx 0$) ou até declínio populacional ($r < 0$).
- **Dispersão Elevada no Centro-Oeste e Sudeste**: Apresentam o maior desvio padrão, refletindo a convivência entre municípios agroindustriais/litorâneos superavitários e municípios interioranos de economia tradicional em encolhimento.
