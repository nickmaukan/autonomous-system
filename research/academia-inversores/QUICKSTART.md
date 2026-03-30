# Quick Start - Stock Analyzer

## Setup (1 vez)
```bash
cd ~/AutonomousSystem/research/academia-inversores/scripts
pip3 install yfinance pandas numpy
```

## Correr Análisis

### Análisis rápido (1 ticker)
```bash
python3 academia_analyzer.py MSFT
```

### Watchlist completa (academia_picks)
```bash
python3 academia_analyzer.py --watchlist academia_picks
```

### Todas las watchlists
```bash
python3 academia_analyzer.py --all
```

### Tickers específicos
```bash
python3 academia_analyzer.py AAPL MSFT GOOGL AMZN META NVDA
```

## Output
- **JSONs:** `output/*.json` (1 por ticker)
- **Resumen:** `output/summary_analysis.csv`

## Ver resultados
```bash
cat output/summary_analysis.csv
```

## Crontab (Bulletin 9am)
```bash
# Editar crontab
crontab -e

# Agregar línea:
0 9 * * 1-5 cd ~/AutonomousSystem/research/academia-inversores/scripts && python3 academia_analyzer.py --watchlist academia_picks >> ~/logs/analyzer.log 2>&1
```

## Troubleshooting

**Error "Module not found":**
```bash
pip3 install yfinance pandas numpy
```

**Error SSL/Mac Python:**
```bash
# Instalar certificados
/Applications/Python\ 3.9/Install\ Certificates.command
```

**Script lento:**
- Normal en primera ejecución (descarga datos)
- subsequent ejecuciones usan cache

---

Para más details, ver README.md completo.
