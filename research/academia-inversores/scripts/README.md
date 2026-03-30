# Stock Analyzer - Academia de Inversores Method
## Guía de Uso y Documentación Técnica

**Versión:** 1.0  
**Fecha:** 2026-03-22  
**Autor:** Aurus ⚡  

---

## 📋 Requisitos

### Sistema
- Python 3.9+
- macOS, Linux, o Windows con terminal

### Paquetes Python
```bash
pip3 install yfinance pandas numpy
```

O instalar todos de una vez:
```bash
pip3 install yfinance==1.2.0 pandas==2.3.3 numpy==2.0.2
```

---

## 🚀 Uso Básico

### Analizar tickers específicos
```bash
python3 academia_analyzer.py AAPL MSFT NVDA V
```

### Usar watchlist predefinida
```bash
python3 academia_analyzer.py --watchlist academia_picks
```

### Analizar TODAS las watchlists
```bash
python3 academia_analyzer.py --all
```

---

## 📁 Watchlists Disponibles

| Nombre | Descripción | Tickers |
|--------|-------------|----------|
| `tech_giants` | Las 6 big tech | AAPL, MSFT, GOOGL, AMZN, META, NVDA |
| `fintech` | Procesadores y fintech | V, MA, PYPL, SQ, ADP |
| `semiconductors` | Chips y semicondutores | NVDA, AMD, INTC, TSM, QCOM, ASML |
| `retail_growth` | E-commerce y retail | AMZN, MELI, LULU, NKE, COST |
| `dividend_kings` | Dividend kings clásicos | KO, PG, JNJ, PEP, VZ, T |
| `academia_picks` | Picks del canal Academia | MSFT, V, ADP, LULU, NVDA, META, AMZN, SAP, RACE |
| `europe_tech` | Tech europeas | SAP, ASML, NESN, BHVN, RACE |
| `latam_tech` | Tech latinoamericanas | MELI, NU, VIST, PagSeguro, StoneCo |

---

## 📊 Output

### Archivos Generados

```
output/
├── AAPL_analysis.json    ← Reporte individual (JSON)
├── MSFT_analysis.json
├── ...
├── summary_analysis.csv ← Resumen en CSV
```

### Formato CSV (summary_analysis.csv)
```csv
Ticker,Precio,RSI,52W_Pos,Técnico,Fundamental,Score,Recomendación,Convicción
MSFT,$381.85,33.52,,WEAK_BUY,STRONG_BUY,1.4,📊 COMPRAR CON PRECAUCIÓN,MEDIA
V,$301.62,20.44,,WEAK_BUY,STRONG_BUY,1.4,📊 COMPRAR CON PRERAUCIÓN,MEDIA
```

### Formato JSON (por ticker)
```json
{
  "ticker": "MSFT",
  "generated_at": "2026-03-22T...",
  "technical": {
    "price_current": 381.85,
    "indicators": {
      "rsi": {"value": 33.52, "signal": "neutral"},
      "macd": {"crossover": "BEARISH"},
      "adx": {"value": 23.29}
    },
    "summary": {
      "technical_signal": "📊 COMPRAR CON PRECAUCIÓN",
      "technical_strength": "WEAK_BUY"
    }
  },
  "fundamental": {
    "ratios": {
      "pe": {"value": 23.93, "score": "UP"},
      "roe": {"value": 34.39, "score": "UP"}
    },
    "summary": {
      "fundamental_signal": "✅ FUERTE",
      "fundamental_score": "STRONG_BUY"
    }
  },
  "combined": {
    "recommendation": "📊 COMPRAR CON PRECAUCIÓN",
    "conviction": "MEDIA",
    "scores": {"combined": 1.4}
  }
}
```

---

## 🎯 Sistema de Scoring

### Análisis Técnico (40% del peso)
| Indicador | Signal | Peso |
|-----------|--------|-------|
| RSI < 30 | BUY (STRONG) | +2 |
| RSI > 70 | SELL (STRONG) | -2 |
| RSI 30-70 | Neutral | 0 |
| MACD crossover bullish | BUY | +1 |
| MACD crossover bearish | SELL | -1 |
| Williams %R < -80 | BUY (STRONG) | +2 |
| Bollinger bajo banda | BUY | +1 |

### Análisis Fundamental (60% del peso)
| Ratio | Umbral UP | Umbral DOWN |
|-------|-----------|-------------|
| P/E | < 35 | >= 35 |
| P/B | < 5 | >= 5 |
| ROE | > 10% | <= 10% |
| Current Ratio | 1.0 - 3.0 | fuera de rango |
| Debt/Equity | < 2.0 | >= 2.0 |
| Revenue Growth | > 0% | <= 0% |

**Score Final:** (Technical_Num × 0.4) + (Fundamental_Num × 0.6)

### Recomendaciones
| Score | Recomendación | Convicción |
|-------|--------------|------------|
| >= 1.5 | 📈 COMPRAR | ALTA |
| >= 0.5 | 📊 COMPRAR CON PRECAUCIÓN | MEDIA |
| >= -0.5 | ⚖️ NEUTRAL | BAJA |
| >= -1.5 | ⚠️ VENDER PARCIAL | MEDIA |
| < -1.5 | 📉 VENDER | ALTA |

---

## 🔧 Desarrollo

### Estructura de Archivos (Futuro)
```
scripts/
├── academia_analyzer.py      # Main (MVP actual)
├── technical_analyzer.py     # Módulo técnico (pendiente)
├── fundamental_analyzer.py   # Módulo fundamental (pendiente)
├── scoring_engine.py         # Scoring combinado (pendiente)
├── report_generator.py       # Generador de reportes (pendiente)
├── main_analyzer.py          # Orquestador (pendiente)
└── README.md                 # Este archivo
```

### Correr en Modo Development
```bash
cd ~/AutonomousSystem/research/academia-inversores/scripts
python3 academia_analyzer.py --watchlist academia_picks
```

### Debug
```bash
# Ver todos los outputs
python3 academia_analyzer.py MSFT V 2>&1

# Solo ver errores
python3 academia_analyzer.py MSFT 2>&1 | grep -i error
```

---

## 📝 Issues Conocidos

| Issue | Workaround |
|-------|-----------|
| 52W Range muestra "nan" | Esperar fix en v1.1 |
| Dividend yield > 100% | Es problema de yfinance, no afecta scoring |
| Sin historical tracking | Por ahora solo genera JSON individual |

---

## 📰 Bulletin Generator

El sistema incluye un generador de bulletin que combina el análisis con recomendaciones:

```bash
# Generar bulletin diario
python3 bulletin_generator.py
```

**Output:** `../output/bulletin_YYYY-MM-DD.txt`

El bulletin incluye:
- 📈 Resumen de mercado
- 🎯 Top 5 oportunidades (del analyzer)
- 💡 Insights del análisis
- 👀 Acciones en vigilancia
- 📋 Plan de acción

El cron job del bulletin (9am L-V) ahora usa este generator automáticamente.

---

## 🔗 Referencias

- Plan de desarrollo completo: `../05_PLAN_DESARROLLO.md`
- Metodología: `../02_METODOLOGIA_ANALISIS.md`
- Investigación del canal: `../00_INDICE.md`

---

## 👤 Contacto

Para dudas sobre el código o metodología, revisar la documentación en el folder `../`.

---

_Last updated: 2026-03-22_
