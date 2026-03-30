# PLAN DE DESARROLLO: Sistema de Análisis type Academia de Inversores
## Para Equipo de Desarrollo

**Proyecto:** Replication of Academia de Inversores Analysis System  
**Autor (spec):** Aurus ⚡  
**Fecha:** 2026-03-22  
**Versión:** 1.0  
**Prioridad:** MEDIA-ALTA  

---

## 1. CONTEXTO Y OBJETIVO

Academia de Inversores es un canal de YouTube (111K suscriptores) que analiza acciones usando una combinación de:
- **Análisis técnico** (TradingView): RSI, MACD, ADX, Medias Móviles, Bollinger Bands
- **Análisis fundamental** (Smart Investor Tool): 8 ratios con scoring visual (pulgar arriba/abajo)
- **Decisión clara**: COMPRAR / ESPERAR / EVITAR

### Objetivo del proyecto
Crear un sistema automatizado que replique esta metodología para:
1. Analizar un conjunto de acciones (watchlist)
2. Generar reportes detallados (técnico + fundamental)
3. Dar recomendaciones claras con convicción
4. Integrarse con el bulletin diario de inversión (9am)

---

## 2. ARQUITECTURA DEL SISTEMA

```
┌─────────────────────────────────────────────────────────────────┐
│                    SISTEMA DE ANÁLISIS                           │
│                  Academia de Inversores                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐   │
│  │   INPUT      │    │   PROCESS    │    │   OUTPUT     │   │
│  │              │───▶│              │───▶│              │   │
│  │  Watchlist   │    │  Analisis    │    │  Reportes    │   │
│  │  tickers.txt │    │  Tecnico +   │    │  JSON        │   │
│  │              │    │  Fundamental │    │  CSV         │   │
│  │              │    │  + Scoring   │    │  Dashboard   │   │
│  └──────────────┘    └──────────────┘    └──────────────┘   │
│                              │                    │            │
│                              ▼                    ▼            │
│                    ┌──────────────────┐  ┌──────────────┐  │
│                    │  MODULOS         │  │  INTEGRAC.   │  │
│                    │  • technical.py   │  │  • Bulletin  │  │
│                    │  • fundamental.py │  │  • TradingBot│  │
│                    │  • scoring.py     │  │  • Telegram  │  │
│                    │  • reporting.py   │  │              │  │
│                    └──────────────────┘  └──────────────┘  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 3. MÓDULOS (FASE 1 - MVP)

### 3.1 `technical_analyzer.py`
**Propósito:** Análisis técnico completo

**Indicadores a implementar:**
- [x] RSI (Relative Strength Index) — 14 períodos
- [x] MACD (Moving Average Convergence Divergence) — 12/26/9
- [x] Williams %R — 14 períodos
- [x] ADX (Average Directional Index) — 14 períodos
- [x] Medias Móviles — SMA 20, 50, 200
- [x] Bollinger Bands — 20 períodos, 2 desviaciones
- [x] ATR (Average True Range) — 14 períodos
- [x] 52-week High/Low + posición relativa
- [ ] Soportes y resistencias (algoritmo automático)
- [ ] Patrones de velas (doji, hammer, engulfing)

**Data source:** yfinance

**Output:** Diccionario con señales BUY/SELL/NEUTRAL

### 3.2 `fundamental_analyzer.py`
**Propósito:** Análisis fundamental tipo Smart Investor Tool

**Métricas a calcular:**
- [x] P/E Ratio (vs umbral sector)
- [x] P/B Ratio
- [x] P/S Ratio
- [x] Current Ratio
- [x] Debt/Equity
- [x] ROE, ROA
- [ ] ROIC (requiere cálculo desde financials)
- [x] Gross Margin, Operating Margin, Net Margin
- [x] Revenue Growth, Earnings Growth
- [x] Dividend Yield, Payout Ratio

**Sistema de Scoring:**
```
Para cada métrica: UP (✓) o DOWN (✗)

Umbrales:
- P/E < 35 → UP
- Current Ratio 1-3 → UP
- Debt Ratio < 0.6 → UP
- Payout Ratio < 50% → UP
- ROIC > 10% → UP
- Revenue Growth > 0 → UP
```

**Output:** Score de salud (X/Y UP) + señal

### 3.3 `scoring_engine.py`
**Propósito:** Combinar análisis técnico y fundamental

**Fórmula:**
```
Score = (Technical_Score * 0.4) + (Fundamental_Score * 0.6)

Technical_Score: STRONG_BUY=2, BUY=1, WEAK_BUY=0.5, NEUTRAL=0, ...
Fundamental_Score: STRONG_BUY=2, BUY=1, NEUTRAL=0, SELL=-1, STRONG_SELL=-2

Decisión:
>= 1.5 → 📈 COMPRAR (ALTA convicción)
>= 0.5 → 📊 COMPRAR CON PRECAUCIÓN (MEDIA)
>= -0.5 → ⚖️ NEUTRAL (BAJA)
>= -1.5 → ⚠️ VENDER PARCIAL (MEDIA)
< -1.5 → 📉 VENDER (ALTA)
```

### 3.4 `report_generator.py`
**Propósito:** Generar reportes输出

**Formatos:**
- [x] JSON (individual por ticker)
- [x] CSV (resumen de watchlist)
- [ ] PDF (reportes detallados)
- [ ] HTML Dashboard (visualización web)
- [ ] Telegram (envío automático)

### 3.5 `main_analyzer.py`
**Propósito:** Orquestar todo el sistema

**Función:**
1. Leer watchlist
2. Para cada ticker:
   - Ejecutar análisis técnico
   - Ejecutar análisis fundamental
   - Calcular score combinado
   - Generar reporte individual
3. Generar resumen CSV
4. Ranking de oportunidades
5. Guardar resultados

---

## 4. WATCHLISTS PREDEFINIDAS

```
tech_giants:      AAPL, MSFT, GOOGL, AMZN, META, NVDA
fintech:           V, MA, PYPL, SQ, ADP
semiconductors:    NVDA, AMD, INTC, TSM, QCOM, ASML
retail_growth:     AMZN, MELI, LULU, NKE, COST
dividend_kings:    KO, PG, JNJ, PEP, VZ, T
academia_picks:    MSFT, V, ADP, LULU, NVDA, META, AMZN, SAP, RACE
europe_tech:       SAP, ASML, NESN, BHVN, RACE
latam_tech:        MELI, NU, VIST, PagSeguro, StoneCo
```

---

## 5. INTEGRACIONES (FASE 2)

### 5.1 Integration con Bulletin Diario (9am)
```
Bulletin Agent → llama a → Stock Analyzer
                          ↓
                    Analiza Academy Picks
                          ↓
                    Genera "RESUMEN VIDEO ACADEMIA"
                    + Análisis propio de acciones vigiladas
                          ↓
                    Bulletin incluye → Sección "Acciones"
```

### 5.2 Integration con Trading Bot
```
Trading Bot (cuando reanude)
  ↓
Para cada acción en portfolio:
  → Análisis semanal
  → ¿Mantener? ¿Vender? ¿Agregar?
  → Alerts si RSI < 30 o > 70
```

### 5.3 Integration con Telegram
```
Usuario → /analizar AAPL MSFT NVDA
          ↓
    Bot → Análisis en background
          ↓
    Envía reportes por Telegram
```

---

## 6. ROADMAP DE DESARROLLO

### Fase 1: MVP (1-2 semanas)
**Goal:** Script funcional que analice watchlists y genere reportes

```
Semana 1:
□ Hacer `technical_analyzer.py` más robusto
□ Hacer `fundamental_analyzer.py` más robusto  
□ Crear `scoring_engine.py`
□ Crear `report_generator.py`
□ Crear `main_analyzer.py` integrador
□ Testing con academia_picks (9 tickers)
□ Fix bugs

Semana 2:
□ Generar reportes JSON + CSV
□ Crear dashboard HTML básico
□ Integrar con Trading Bot
□ Integrar con Bulletin Agent
□ Documentar para el equipo
```

### Fase 2: Enhancements (2-3 semanas)
**Goal:** Sistema completo con visualizaciones

```
□ Dashboard web con Charts.js o similar
□ Gráficos de velas (TradingView embed?)
□ Alerts por Telegram
□ Screener automático (RSI < 30, P/E bajo, etc.)
□ Comparativa sectorial
□ Historical tracking (guardar análisis previos)
□ Backtesting de señales
```

### Fase 3: Avanzado (1 mes+)
**Goal:** Sistema profesional

```
□ DCF Fair Value calculation
□ Integración con datos de Bloomberg/Refinitiv
□ AI-powered thesis generation
□ Portfolio optimization
□ Risk analysis (VaR, Sharpe ratio)
□ Integración con broker API (alpaca, interactive brokers)
□ Trading automático (si es deseado)
```

---

## 7. TECHNICAL STACK

### Current (Python scripts)
- yfinance — data de mercado
- pandas — manipulation de datos
- numpy — cálculos
- json — output

### Recommended para dashboard
- FastAPI — API del servicio
- Chart.js / Plotly — visualizaciones
- SQLite — guardar histórico
- Docker — deployment

### Para producción
- PostgreSQL — datos
- Redis — caching
- Celery — background jobs
- Docker Compose — deployment

---

## 8. ARCHIVOS ACTUALES

```
~/AutonomousSystem/research/academia-inversores/
├── scripts/
│   └── academia_analyzer.py    ← MVP actual (funcionando)
├── output/                       ← Donde se guardan los reportes
├── 01_CANAL_OVERVIEW.md
├── 02_METODOLOGIA_ANALISIS.md
├── 03_RESUMEN_EJECUTIVO.md
├── 04_VIDEOS_ANALIZADOS.md
├── 05_PLAN_DESARROLLO.md        ← Este archivo
└── 00_INDICE.md
```

---

## 9. ISSUES CONOCIDOS (del script actual)

| Issue | Prioridad | Status |
|-------|-----------|--------|
| 52-week range muestra "nan" | MEDIA | Bug en cálculo |
| Dividend yield incorrecto (95% vs 0.95%) | BAJA | yfinance inconsistency |
| No hay historical tracking | MEDIA | Pendiente |
| No hay comparativa sectorial | ALTA | Pendiente |
| No hay DCF fair value | ALTA | Pendiente |

---

## 10. PRÓXIMOS PASOS PARA EL EQUIPO

1. **Revisar** `academia_analyzer.py` actual
2. **Separar** en módulos (technical.py, fundamental.py, etc.)
3. **Fix** bugs conocidos
4. **Agregar** datos de comparativa sectorial
5. **Crear** dashboard web
6. **Integrar** con el bulletin de 9am

---

## 11. METRICAS DE ÉXITO

```
□ Script analiza 20+ tickers en < 60 segundos
□ Accuracy de señales vs mercado (backtest)
□ Engagement del bulletin (¿la gente lee la sección de acciones?)
□ Reducción de tiempo de análisis manual
□ Tomas de decisiones basadas en datos vs intuición
```

---

## 12. CONTACTO / QUESTIONS

Para dudas sobre la metodología, revisar:
- `02_METODOLOGIA_ANALISIS.md` — metodología completa
- `03_RESUMEN_EJECUTIVO.md` — overview del canal

Para bugs o features, crear issue en el repo.

---

_Last updated: 2026-03-22_
_Autor: Aurus ⚡ para Mauri_
