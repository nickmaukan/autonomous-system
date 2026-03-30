# METODOLOGÍA DE ANÁLISIS: Academia de Inversores

## Visión General

Academia de Inversores combina **análisis técnico** (TradingView) con **análisis fundamental** (The Smart Investor Tool) en una metodología híbrida. No es puramente técnico ni puramente fundamental — es un enfoque de **"análisis completo"** orientado a inversores de swing trading y largo plazo en el mercado estadounidense.

---

## PARTE 1: Análisis Técnico

### Plataforma: TradingView

#### Temporalidades usadas
| Temporalidad | Uso |
|--------------|-----|
| **1D (Diario)** | Análisis principal |
| **1W (Semanal)** | Tendencias de medio/largo plazo |
| **1M (Mensual)** | Soportes/resistencias clave |

#### Indicadores técnicos identificados

**Medias Móviles (Moving Averages)**
- SMA 200 (Simple Moving Average 200) — Señal de tendencia larga
- SMA 50 — Señal de tendencia media
- SMA 20 — Señal de tendencia corta
- SMA 8 — Señal rápida/señales de entrada

**Osciladores**
- RSI (Relative Strength Index) — Sobrecompra/sobreventa
  - Observado en SAP: RSI 25.82 (sobreventa extrema)
  - Niveles referencia: <30 sobreventa, >70 sobrecompra
- Williams %R — Sobreventa extrema
  - Observado en SAP: -90.2% (sobreventa extrema)
- ADX (Average Directional Index) — Fuerza de tendencia
  - Observado en SAP: ADX 41.58 (tendencia MUY fuerte)
- MACD (Moving Average Convergence Divergence) — Momentum
  - Histograma + línea MACD + línea de señal
  - Color: verde momentum alcista, rojo momentum bajista

#### Patrones de precio observados
- **Velas japonesas** en gráfico principal
- **Soportes horizontales** (líneas beige punteadas)
- **Resistencias** identificadas visualmente
- **DCF (Discounted Cash Flow)** como línea de valor intrínseco
  - Observado en SAP: DCF ~180 (precio justo estimado)

#### Eventos en gráfico
- **E (Azul)** = Earnings (reportes de ganancias)
- **D (Azul)** = Dividend payout

#### Tabla de métricas superpuesta
En el video de SAP se observó una tabla con:
```
RSI: [valor]
SMA200: [% vs precio actual]
SMA50: [% vs precio actual]
SMA20: [% vs precio actual]
PER: [valor]
P/S: [valor]
P/CF: [valor]
ADX: [valor]
Williams %R: [%]
Div Yield: [%]
```

---

## PARTE 2: Análisis Fundamental

### Herramienta: The Smart Investor Tool

#### Pestañas de análisis

1. **Summary** — Resumen general de la empresa
2. **Financials** — Estados financieros detallados
3. **Ratios** — Ratios de valoración y crecimiento
4. **Rating** — Rating general de la acción
5. **Dividends** — Análisis de dividendos
6. **Estimates** — Proyecciones de crecimiento
7. **EPS Fair Value** — Valor justo por método EPS
8. **DCF Fair Value** — Valor justo por flujo de caja descontado
9. **Historical Ratios** — Ratios históricos (10 años)
10. **Earnings** — Historial de ganancias
11. **Additional Data** — Datos adicionales
12. **Holders** — Poseedores majoritarios

---

### Sistema de Scoring: Ratios and Growth

**8 métricas con pulgar arriba/abajo:**

#### Columna Izquierda (Valoración y Salud Financiera)

| Métrica | Criterio | Qué mide |
|---------|----------|----------|
| P/E Ratio | < X del sector | Valoración (cuánto pagas por beneficio) |
| Current Ratio | 1 - 3 | Liquidez a corto plazo |
| Debt Ratio | < 0.6 | Nivel de deuda total |
| Payout Ratio | < 50% | Sostenibilidad del dividendo |

#### Columna Derecha (Crecimiento y Eficiencia)

| Métrica | Criterio | Qué mide |
|---------|----------|----------|
| ROIC Avg 10 Yrs | > 10% | Eficiencia del capital invertido |
| Revenue Growth 10 Yrs | Valor en B (billones/millones) | Crecimiento de ingresos |
| Net Income Growth 10 Yrs | Valor en B | Crecimiento de beneficios |
| Free Cash Flow Growth 10 Yrs | Valor en B | Crecimiento del flujo de caja |

---

### Tablas Comparativas

#### Tabla 1: Valoración y Márgenes
Compara la acción contra:
- **Sector Average** — Promedio del sector industrial
- **Diff (Sector)** — Diferencia porcentual vs sector
- **SAP 5Y Avg** — Promedio propio de 5 años
- **Diff (5Y Avg)** — Diferencia vs propio histórico

Métricas incluidas:
- P/E GAAP
- Price/Book (P/VC)
- Price/Sales (P/Ventas)
- Price/Cash Flow
- Net Profit Margin
- Dividend Yield

#### Tabla 2: Liquidez, Deuda y Eficiencia
Compara valores actuales vs 5-year average:
- PEG GAAP (< 1 = infravalorada)
- Quick Ratio (> 1 = buena liquidez)
- Cash Ratio (> 0.5 = efectivo suficiente)
- Debt to Equity (< 2 = deuda manejable)
- Return on Equity (> 0.1 = 10% mínimo)
- Free Cash Flow Per Share

---

### Growth Estimates (Proyecciones)

**Período:** 2021 (histórico) → 2026E-2030E (estimado)

| Métrica | Histórico | Proyectado | CAGR |
|---------|-----------|------------|------|
| Revenues | 26,953 M€ | 67,404 M€ | 12.91% |
| Ebitda | 10,987 M€ | 14,289 M€ | 5.46% |
| Net Income | 2,284 M€ | 16,341 M€ | 18.56% |
| EPS | 4.56€ | 14.03€ | 19.54% |
| Free Cash Flow | 5,522 M€ | 18,090 M€ | 17.99% |
| Dividends | — | 2.64€→5.07€ | — |

**Nota:** "Currency in EUR. All numbers in millions."

**Codificación de colores:**
- Azul = crecimiento positivo YoY
- Rojo = caída YoY

---

## PARTE 3: Metodología de Análisis de Acciones en Mínimos de 52 Semanas

### Video: "📉 10 Acciones en Mínimos de 52 Semanas: ¿Oportunidad o Trampa?"

#### Acciones analizadas en este video:
- ADP (Automatic Data Processing)
- LULU (Lululemon Athletica)
- V (Visa)

#### Proceso observado:

**1. Screening inicial**
- Búsqueda de acciones en mínimos de 52 semanas
- Filtro por sector/industria

**2. Análisis individual por acción**

Para cada acción:
```
a) Presentación empresa
   - Nombre completo
   - Sector/Industry
   - CEO
   - Empleados
   - País
   - Descripción del negocio

b) Métricas de precio
   - Precio actual
   - 52 Week Range (visual)
   - Rendimiento: Last Month, Last Year, YTD

c) Gráfico de precio (TradingView)
   - Vela diaria/semanal
   - Medias móviles
   - Línea de tendencia

d) Indicadores
   - RSI
   - MACD
   - Soportes cercanos

e) Fundamental rápido
   - EPS (TTM)
   - Dividends
   - Volume vs Avg Volume
```

**3. Veredicto**
- ¿Oportunidad o trampa?
- Recomendación de acción (comprar, esperar, evitar)

---

## PARTE 4: Análisis de Earnings/Reportes

### Videos de earnings identificados:
- "📉 Fuertes Caídas Tras los Earnings… ¡y Netflix Se Dispara!"
- "📉 Nvidia, Salesforce y The Trade Desk: Análisis Tras los Reportes… ¿Comprar Ahora?"
- "🚨 Esta Acción Entra en Zona de Compra y Dos Reportes de Ganancias Clave"

#### Proceso de análisis post-earnings:
1. **Lectura del reporte** — Números vs expectativas
2. **Reacción del precio** — Gap up/down
3. **Soporte técnico** — ¿Dónde para?
4. **Thesis** — ¿Es temporal o estructural?
5. **Decisión** — Comprar, vender, hold

---

## PARTE 5: Plan de Trading Semanal

### Video: "Acciones Claves Para la Semana"

Estructura típica observada:
1. **Contexto macro** — Qué hizo el mercado la semana anterior
2. **S&P 500, Nasdaq, Dow** — Resumen semanal
3. **Acciones a vigilar** — 3-5 picks para la semana
4. **Niveles clave** — Soportes y resistencias
5. **Eventos de la semana** — Earnings, datos económicos

---

## PARTE 6: Scoring/Valoración Cualitativa

### Rating del Smart Investor Tool
La herramienta tiene un sistema de **Rating** (observable en las pestañas) que aparentemente combina:
- Análisis técnico
- Análisis fundamental
- Valoración relativa
- Momentum

### Factores de decisión observados

**¿CUÁNDO RECOMIENDA COMPRAR?**
- Precio por debajo de DCF Fair Value
- RSI en sobreventa (< 30)
- Caídas por "miedo" no fundamentañes
- P/E por debajo del promedio del sector
- ROIC creciente
- Zona de soportes técnicos confirmada

**¿CUÁNDO RECOMIENDA ESPERAR/EVITAR?**
- RSI en sobrecompra (> 70)
- P/E muy por encima del sector
- Deuda elevada
- ROIC cayendo
- Tendencia tecnológica rota (SMA200)
- Divergencias MACD bajistas

---

## PARTE 7: Estilo de Presentación

### El presentador
- **Apariencia:** Hombre joven, cabello oscuro ondulado, barba, gafas, gorra de béisbol blanca con logo azul
- **Escenario:** Interior (oficina/casa) con setup de pantalla triple
- **Microfono:** Mic de solapa o headset

### Formato de video
1. **Intro** (0-30s) — Logo del canal + título del video
2. **Contexto** (1-3 min) — Explicación del tema
3. **Análisis** (15-25 min) — Pantalla compartida + voz
4. **Conclusión** (1-2 min) — Resumen + recomendación

### Tono
- Educativo pero directo
- Sin rodeos — dice claramente "compro" o "evito"
- Analiza tanto oportunidades como riesgos
- Usa jerga financiera pero la explica

---

## PARTE 8: Comparación Sectorial

### Sectores mencionados
- Technology (software, chips)
- Industrials (ADP, UPS)
- Consumer/Retail (Nike, Lululemon)
- Financials (Visa, Mastercard)
- Healthcare (ocasional)

### Cómo compara
- **vs Sector Average** — ¿Está mejor o peor que peers?
- **vs 5Y Average** — ¿Está cara o barata vs su historia?
- **vs DCF** — ¿Hay margen de seguridad?

---

_Last updated: 2026-03-22_
