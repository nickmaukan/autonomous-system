# Plan de Desarrollo - Desglose de Tareas
## Academia de Inversores Stock Analyzer

**Proyecto:** Sistema de análisis de acciones (réplica metodología Academia de Inversores)  
**Ubicación:** ~/AutonomousSystem/research/academia-inversores/  
**Script actual:** scripts/academia_analyzer.py (MVP funcionando)  
**Prioridad:** MEDIA-ALTA  

---

## FASE 1: MVP Enhancement (Semanas 1-2)

### Tareas de Código

#### T-101: Fix Bugs del Script Actual
**Prioridad:** ALTA  
**Tiempo estimado:** 2-3 horas  
**Responsable:** Dev  
**Status:** ✅ COMPLETADO (2026-03-22 por Aurus)

**Detalles:**
- [x] Fix: 52-week range muestra "nan" → Usar `min_periods=1` en rolling
- [x] Fix: Dividend yield muestra 95% en vez de 0.95% → No multiplicar por 100
- [x] Fix: ADX interpretation muestra "N/A" → Agregar else case

**Criterio de aceptación:** ✅ Script corre sin "nan" ni errores

**Verificado con:** MSFT, V → 52W muestra correctamente, dividendo correcto

---

#### T-102: Agregar Comparativa Sectorial
**Prioridad:** ALTA  
**Tiempo estimado:** 4-6 horas  
**Responsable:** Dev  

**Detalles:**
- [ ] Descargar sector/industria de yfinance (info['sector'], info['industry'])
- [ ] Para cada ratio, comparar vs promedio del sector
- [ ] Mostrar "vs Sector" en el reporte
- [ ] Ajustar scoring para incluir contexto sectorial

**Criterio de aceptación:** Reporte muestra cómo se compara cada acción vs su sector

---

#### T-103: Módulo de Technical Analyzer (Refactoring)
**Prioridad:** MEDIA  
**Tiempo estimado:** 6-8 horas  
**Responsable:** Dev  

**Detalles:**
- [ ] Separar `analyze_technical()` en archivo propio: `technical_analyzer.py`
- [ ] Crear clase `TechnicalAnalyzer` con métodos:
  - `calculate_rsi()`
  - `calculate_macd()`
  - `calculate_adx()`
  - `calculate_bollinger_bands()`
  - `calculate_support_resistance()` (algoritmo simple)
- [ ] Agregar tests unitarios básicos
- [ ] Mantener backwards compatibility con script actual

**Criterio de aceptación:** Script actual sigue funcionando sin cambios

---

#### T-104: Módulo de Fundamental Analyzer (Refactoring)
**Prioridad:** MEDIA  
**Tiempo estimado:** 6-8 horas  
**Responsable:** Dev  

**Detalles:**
- [ ] Separar `analyze_fundamental()` en archivo propio: `fundamental_analyzer.py`
- [ ] Crear clase `FundamentalAnalyzer` con métodos para cada ratio
- [ ] Agregar ROIC calculation desde financials (no disponible en info)
- [ ] Agregar tests unitarios básicos

**Criterio de aceptación:** Script actual sigue funcionando sin cambios

---

#### T-105: Dashboard HTML Básico
**Prioridad:** MEDIA  
**Tiempo estimado:** 8-10 horas  
**Responsable:** Dev/Frontend  

**Detalles:**
- [ ] Crear template HTML con Chart.js
- [ ] Mostrar resumen de watchlist (tabla con score, RSI, recomendación)
- [ ] Embed gráfico de precio para cada ticker (usar Chart.js o similar)
- [ ] Botón para regenerar análisis
- [ ] Diseño responsive (mobile-friendly)

**Criterio de aceptación:** Dashboard carga en navegador y muestra datos del CSV

---

## FASE 2: Integraciones (Semanas 3-4)

#### T-201: Integración con Bulletin Agente
**Prioridad:** ALTA  
**Tiempo estimado:** 4-6 horas  
**Responsable:** Dev  
**Status:** ✅ COMPLETADO (2026-03-22)

**Detalles:**
- [x] Script `bulletin_generator.py` que ejecuta analyzer + genera bulletin formateado
- [x] Cron job actualizado para usar el generator
- [x] Output: `output/bulletin_YYYY-MM-DD.txt` con estructura completa
- [x] Agent now lee el archivo y lo envia por Telegram

**Criterio de aceptación:** ✅ Bulletin automático incluye análisis de acciones

---

#### T-202: Sistema de Alerts (Telegram)
**Prioridad:** MEDIA  
**Tiempo estimado:** 4-6 horas  
**Responsable:** Dev  

**Detalles:**
- [ ] Crear función de alert cuando RSI < 30 o RSI > 70
- [ ] Crear función de alert cuando score cambia de categoría
- [ ] Integrar con sistema de message de OpenClaw
- [ ] Configurable por usuario (qué alerts recibir)

**Criterio de aceptación:** Usuario recibe alert cuando acción entra en zona de sobreventa/sobrecompra

---

#### T-203: Historical Tracking (SQLite)
**Prioridad:** MEDIA  
**Tiempo estimado:** 6-8 horas  
**Responsable:** Dev  

**Detalles:**
- [ ] Crear base de datos SQLite: `data/analysis_history.db`
- [ ] Tabla: `analysis_log (ticker, date, price, rsi, score, recommendation)`
- [ ] Modificar script para guardar cada análisis en DB
- [ ] Crear función para comparar vs análisis anterior
- [ ] Crear script para generar "weekly report" desde DB

**Criterio de aceptación:** Datos persisten entre ejecuciones y se puede ver historial

---

#### T-204: Screening Automático
**Prioridad:** BAJA  
**Tiempo estimado:** 8-10 horas  
**Responsable:** Dev  

**Detalles:**
- [ ] Crear función `screen_stocks(criteria)` que busca acciones matching criteria
- [ ] Criterios: RSI < 30, P/E < 20, ROE > 20%, etc.
- [ ] Buscar en S&P 500 (lista predefinida)
- [ ] Generar lista de "oportunidades" automáticamente
- [ ] Enviar resultado por Telegram

**Criterio de aceptación:** Sistema puede identificar acciones que matchean criterios dados

---

## FASE 3: Avanzado (Mes 2+)

#### T-301: DCF Fair Value Calculation
**Prioridad:** MEDIA  
**Tiempo estimado:** 12-16 horas  
**Responsable:** Dev/Quant  

**Detalles:**
- [ ] Implementar DCF simplificado usando growth estimates
- [ ] Inputs: FCF actual, growth rate, discount rate (WACC), terminal growth
- [ ] Output: Fair value estimado
- [ ] Comparar con precio actual → "X% infravalorado/sobrevalorado"
- [ ] Validar con 5-10 empresas conocidas

**Criterio de aceptación:** DCF da resultado razonable vs precio de mercado

---

#### T-302: Portfolio Optimizer
**Prioridad:** BAJA  
**Tiempo estimado:** 16-20 horas  
**Responsable:** Dev/Quant  

**Detalles:**
- [ ] Implementar mean-variance optimization (Markowitz)
- [ ] Usar histórico de precios para calcular retornos y volatilidades
- [ ] Input: lista de acciones candidatas + constraints (max weight, min weight)
- [ ] Output: pesos óptimos para portfolio
- [ ] Calcular Sharpe ratio esperado

**Criterio de aceptación:** Optimizer devuelve pesos que maximizan Sharpe ratio

---

#### T-303: Integración Broker API
**Prioridad:** BAJA  
**Tiempo estimado:** 20+ horas  
**Responsable:** Dev  

**Detalles:**
- [ ] Evaluar APIs: Alpaca, Interactive Brokers, TD Ameritrade
- [ ] Implementar demo con Alpaca (paper trading)
- [ ] Integrar signals del analyzer con órdenes simuladas
- [ ] Dashboard de portfolio con P&L
- [ ] Documentar limitaciones y risks

**Criterio de aceptación:** Sistema puede hacer trading simulado basado en signals

---

## Tareas Administrativas

#### T-ADMIN-1: Documentación API
**Prioridad:** ALTA  
**Tiempo estimado:** 3-4 horas  
**Responsable:** Dev  

**Detalles:**
- [ ] Documentar todas las funciones públicas
- [ ] Crear docstrings en formato Google
- [ ] Generar API docs con pdoc o similar

---

#### T-ADMIN-2: Testing Suite
**Prioridad:** MEDIA  
**Tiempo estimado:** 6-8 horas  
**Responsable:** Dev  

**Detalles:**
- [ ] Setup pytest
- [ ] Tests para indicadores técnicos (verificar contra valores conocidos)
- [ ] Tests para scoring logic
- [ ] Integration tests para workflow completo

---

#### T-ADMIN-3: Deployment Guide
**Prioridad:** BAJA  
**Tiempo estimado:** 4-6 horas  
**Responsable:** DevOps  

**Detalles:**
- [ ] Crear requirements.txt
- [ ] Dockerizar aplicación
- [ ] Crear docker-compose para DB + app
- [ ] Documentar cómo deployar en servidor

---

## PRIORIZACIÓN SUGERIDA

### Sprint 1 (Semana 1)
| Tarea | Prioridad | Tiempo | Entregable |
|-------|-----------|--------|-------------|
| T-101 Fix Bugs | 🔴 ALTA | 2-3h | Script sin bugs |
| T-102 Comparativa Sectorial | 🔴 ALTA | 4-6h | Reportes mejorados |

### Sprint 2 (Semana 2)
| Tarea | Prioridad | Tiempo | Entregable |
|-------|-----------|--------|-------------|
| T-103 Refactor Technical | 🟡 MEDIA | 6-8h | Módulo separado |
| T-104 Refactor Fundamental | 🟡 MEDIA | 6-8h | Módulo separado |
| ~~T-201 Integración Bulletin~~ | ✅ COMPLETADO | 2h | ✅ Bulletin mejorado |

### Sprint 3 (Semana 3-4)
| Tarea | Prioridad | Tiempo | Entregable |
|-------|-----------|--------|-------------|
| T-105 Dashboard HTML | 🟡 MEDIA | 8-10h | Web UI |
| T-203 Historical Tracking | 🟡 MEDIA | 6-8h | DB + historial |
| T-202 Alerts Telegram | 🟡 MEDIA | 4-6h | Notificaciones |

### Sprint 4+ (Mes 2)
| Tarea | Prioridad | Tiempo | Entregable |
|-------|-----------|--------|-------------|
| T-301 DCF Fair Value | 🟡 MEDIA | 12-16h | Valuación |
| T-302 Portfolio Optimizer | 🟢 BAJA | 16-20h | Optimización |
| T-303 Broker Integration | 🟢 BAJA | 20+h | Trading simulado |

---

## Métricas de Éxito

- [ ] Script analiza 20+ tickers en < 60 segundos
- [ ] Bulletin diario incluye análisis de acciones sin errores
- [ ] Dashboard carga en < 3 segundos
- [ ] Alerts llegan dentro de 1 minuto de detectarse condición
- [ ] 0 bugs críticos en producción después de Sprint 1

---

## Riscos

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| yfinance cambia API | MEDIA | ALTO | Agregar fallback a otra fuente |
| Complejidad DCF | ALTA | MEDIA | Empezar con versión simplificada |
| Overengineering | ALTA | MEDIA | Priorizar features que Mauri usará |

---

## Recursos

- **Repositiorio:** ~/AutonomousSystem/research/academia-inversores/
- **Script actual:** scripts/academia_analyzer.py
- **Plan completo:** 05_PLAN_DESARROLLO.md
- **Investigación canal:** 00_INDICE.md

---

_Last updated: 2026-03-22_
_Autor: Aurus ⚡_
