# 🧠 ARQUITECTURA AUTÓNOMA v2.0
## Sistema Persistente de Generación de Valor

---

## 1. 🧠 MEMORIA PERSISTENTE

### Estructura de Base de Datos

```bash
# Crear directorio de datos
mkdir -p ~/AutonomousSystem/{data,logs,scripts,agents,tools}

# Base de datos SQLite para persistencia
```

### Esquema de Memoria

```sql
-- Tablas principales

-- Estado del sistema
CREATE TABLE system_state (
    id PRIMARY KEY,
    last_update TIMESTAMP,
    active_projects TEXT,  -- JSON
    pending_tasks TEXT,    -- JSON
    decisions TEXT,        -- JSON array
    context TEXT           -- JSON con contexto relevante
);

-- Historial de decisiones
CREATE TABLE decision_history (
    id INTEGER PRIMARY KEY,
    timestamp TIMESTAMP,
    decision TEXT,
    context TEXT,
    result TEXT,
    success BOOLEAN
);

-- Conocimiento aprendido
CREATE TABLE knowledge (
    id INTEGER PRIMARY KEY,
    topic TEXT,
    content TEXT,
    source TEXT,
    timestamp TIMESTAMP,
    tags TEXT
);

-- Proyectos activos
CREATE TABLE projects (
    id TEXT PRIMARY KEY,
    name TEXT,
    status TEXT,  -- active, paused, completed
    progress INTEGER,
    notes TEXT,
    last_update TIMESTAMP
);
```

---

## 2. 👑 ORQUESTADOR REAL

### Componente Central: Orchestrator

```python
#!/usr/bin/env python3
"""
Orquestador Central del Sistema Autonomo
"""

import json
import sqlite3
import os
from datetime import datetime
from pathlib import Path

class Orchestrator:
    def __init__(self, db_path="~/AutonomousSystem/data/main.db"):
        self.db_path = os.path.expanduser(db_path)
        self.init_db()
        
    def init_db(self):
        """Inicializa base de datos"""
        # Crear tablas si no existen
        
    def analyze_state(self):
        """Analiza estado actual del sistema"""
        # 1. Revisar proyectos activos
        # 2. Ver tareas pendientes
        # 3. Analizar contexto guardado
        # 4. Evaluar decisiones previas
        
    def decide_action(self):
        """Decide siguiente acción basada en:
        - Prioridad de proyectos
        - Tareas pendientes
        - Decisiones anteriores exitosas
        """
        
    def delegate_to_agent(self, task):
        """Delega tarea a agente apropiado:
        - coding: subagent Python
        - research: web search
        - execution: shell
        - analysis: analysis agent
        """
        
    def execute_loop(self):
        """Ciclo principal - corre continuamente"""
        while True:
            state = self.analyze_state()
            action = self.decide_action()
            result = self.execute(action)
            self.save_result(state, action, result)
            self.sleep(interval)  -- configurable
```

---

## 3. 🔄 CICLO AUTÓNOMO

### Loop Principal

```
┌─────────────────────────────────────────────────┐
│              ANALIZAR ESTADO                    │
│  ┌─────────┐  ┌─────────┐  ┌─────────────┐   │
│  │Proyectos│  │Tareas   │  │Contexto    │   │
│  │Activos  │  │Pendientes│  │Memoria     │   │
│  └────┬────┘  └────┬────┘  └──────┬──────┘   │
└───────┼────────────┼─────────────┼──────────┘
        │            │             │
        ▼            ▼             ▼
┌───────────────────────────────────────────────┐
│              DECIDIR ACCIÓN                    │
│  - Priorizar proyecto activo                  │
│  - Evaluar oportunidades                      │
│  - Considerar aprendizaje previo              │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌───────────────────────────────────────────────┐
│              DELEGAR                           │
│  - Agente Coding: desarrollo                  │
│  - Agente Research: análisis                 │
│  - Agente Execute: operaciones              │
│  - Main Agent: decisiones complejas          │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌───────────────────────────────────────────────┐
│              EJECUTAR Y GUARDAR               │
│  - Ejecutar acción                           │
│  - Guardar resultado en memoria              │
│  - Actualizar estado                        │
│  - Si es importante → notificar usuario    │
└─────────────────────────────────────────────┘
```

---

## 4. 📊 DATA EXTERNA

### APIs Necesarias

| API | Propósito | Costo |
|-----|-----------|-------|
| **Alpha Vantage** | Stocks fundamentals | Gratis (limitado) |
| **Yahoo Finance** | Quotes, history | Gratis |
| **NewsAPI** | Noticias financieras | Gratis |
| **Brave Search** | Web scraping | API key |
| **Twelvedata** | Time series financial | Freemium |

### Módulo de Datos

```python
class DataManager:
    def __init__(self):
        self.alpha_vantage_key = os.environ.get('ALPHA_VANTAGE_KEY')
        
    def get_stock_quote(self, symbol):
        """Obtiene precio actual"""
        
    def get_financial_news(self, symbols):
        """Noticias relevantes"""
        
    def get_technical_indicators(self, symbol):
        """SMA, RSI, MACD, etc."""
        
    def scan_opportunities(self):
        """Busca:
        - Acciones cerca de MA200
        - Sobreventa (RSI < 30)
        - Breaking resistance
        """
```

---

## 5. 🧩 ESTRUCTURA DE ARCHIVOS

### Directorio Raíz: `~/AutonomousSystem/`

```
~/AutonomousSystem/
├── README.md                    # Este archivo
├── config/
│   ├── .env                    # API keys
│   ├── agents.yaml             # Config de agentes
│   └── system.yaml            # Config general
│
├── data/
│   ├── main.db                # SQLite memoria
│   ├── cache/                 # Cache web
│   └── exports/               # Datos exportados
│
├── scripts/
│   ├── orchestrator.py        # Orquestador principal
│   ├── data_manager.py        # Gestión de datos
│   ├── scheduler.py           # Scheduler avanzado
│   └── notifications.py       # Notificaciones
│
├── agents/
│   ├── investment_agent.py     # Agente de inversión
│   ├── research_agent.py      # Agente de research
│   └── automation_agent.py    # Agente de automatización
│
├── logs/
│   ├── decisions/            # Historial decisiones
│   ├── executions/           # Logs de ejecución
│   └── errors/              # Errores
│
└── tools/
    ├── market_data.py        # Herramientas financieras
    ├── scrapers.py           # Web scrapers
    └── utils.py              # Utilidades
```

---

## 6. ⚙️ IMPLEMENTACIÓN EN MAC

### Paso 1: Crear Estructura

```bash
# Crear directorio principal
mkdir -p ~/AutonomousSystem/{data,logs,scripts,agents,tools}

# Inicializar git
cd ~/AutonomousSystem
git init

# Instalar dependencias Python
pip3 install sqlite3 json datetime pathlib
# (La mayoria ya viene con Python)
```

### Paso 2: Configurar Base de Datos

```bash
python3 << 'EOF'
import sqlite3
import os

db_path = os.path.expanduser("~/AutonomousSystem/data/main.db")
os.makedirs(os.path.dirname(db_path), exist_ok=True)

conn = sqlite3.connect(db_path)
c = conn.cursor()

# Crear tablas
c.executescript('''
CREATE TABLE IF NOT EXISTS system_state (
    id TEXT PRIMARY KEY,
    last_update TIMESTAMP,
    active_projects TEXT,
    pending_tasks TEXT,
    decisions TEXT,
    context TEXT
);

CREATE TABLE IF NOT EXISTS decision_history (
    id INTEGER PRIMARY KEY,
    timestamp TIMESTAMP,
    decision TEXT,
    context TEXT,
    result TEXT,
    success BOOLEAN
);

CREATE TABLE IF NOT EXISTS knowledge (
    id INTEGER PRIMARY KEY,
    topic TEXT,
    content TEXT,
    source TEXT,
    timestamp TIMESTAMP,
    tags TEXT
);

CREATE TABLE IF NOT EXISTS projects (
    id TEXT PRIMARY KEY,
    name TEXT,
    status TEXT,
    progress INTEGER,
    notes TEXT,
    last_update TIMESTAMP
);
''')
conn.commit()
conn.close()
print("Base de datos inicializada")
EOF
```

### Paso 3: Crear Orquestador

```bash
cat > ~/AutonomousSystem/scripts/orchestrator.py << 'PYEOF'
#!/usr/bin/env python3
"""
Orquestador Central del Sistema Autonomo v2.0
"""
import sqlite3
import json
import os
from datetime import datetime
from pathlib import Path

class Orchestrator:
    def __init__(self):
        self.db_path = os.path.expanduser("~/AutonomousSystem/data/main.db")
        self.state_file = os.path.expanduser("~/AutonomousSystem/data/state.json")
        
    def get_db(self):
        return sqlite3.connect(self.db_path)
    
    def analyze_state(self):
        """Analiza estado actual"""
        conn = self.get_db()
        c = conn.cursor()
        
        # Obtener proyectos activos
        c.execute("SELECT * FROM projects WHERE status='active'")
        projects = c.fetchall()
        
        # Obtener decisiones recientes
        c.execute("SELECT * FROM decision_history ORDER BY timestamp DESC LIMIT 10")
        decisions = c.fetchall()
        
        conn.close()
        
        return {
            "projects": projects,
            "recent_decisions": decisions,
            "timestamp": datetime.now().isoformat()
        }
    
    def save_decision(self, decision, context, result, success):
        """Guarda decisión en historial"""
        conn = self.get_db()
        c = conn.cursor()
        c.execute("""
            INSERT INTO decision_history (timestamp, decision, context, result, success)
            VALUES (?, ?, ?, ?, ?)
        """, (datetime.now().isoformat(), decision, context, result, success))
        conn.commit()
        conn.close()
    
    def save_state(self, state):
        """Guarda estado actual"""
        with open(self.state_file, 'w') as f:
            json.dump(state, f, indent=2)
    
    def load_state(self):
        """Carga estado"""
        if os.path.exists(self.state_file):
            with open(self.state_file, 'r') as f:
                return json.load(f)
        return {"initialized": False}
    
    def run_cycle(self):
        """Ejecuta un ciclo del loop"""
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Análisis de estado...")
        
        # 1. Analizar
        state = self.analyze_state()
        
        # 2. Decidir (simplificado)
        if state["projects"]:
            print(f"  Proyectos activos: {len(state['projects'])}")
            # Aquí va la lógica de decisión
        
        # 3. Guardar
        self.save_state(state)
        
        return state

if __name__ == "__main__":
    orch = Orchestrator()
    initial_state = orch.load_state()
    
    if not initial_state.get("initialized"):
        print("Inicializando sistema...")
        orch.save_state({"initialized": True, "first_run": datetime.now().isoformat()})
    
    # Ejecutar ciclo
    orch.run_cycle()
    print("Ciclo completado")
PYEOF
chmod +x ~/AutonomousSystem/scripts/orchestrator.py
```

### Paso 4: Configurar como Servicio (LaunchAgent)

```bash
# Crear plist para macOS
cat > ~/Library/LaunchAgents/com.autonomous.system.plist << 'PLISTEOF'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.autonomous.system</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/python3</string>
        <string>/Users/nickmaukan/AutonomousSystem/scripts/orchestrator.py</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/Users/nickmaukan/AutonomousSystem/logs/orchestrator.log</string>
    <key>StandardErrorPath</key>
    <string>/Users/nickmaukan/AutonomousSystem/logs/errors.log</string>
    <key>StartInterval</key>
    <integer>300</integer>  <!-- Cada 5 minutos -->
</dict>
</plist>
PLISTEOF

# Registrar servicio
launchctl load ~/Library/LaunchAgents/com.autonomous.system.plist
```

### Paso 5: Configurar API Keys

```bash
# Crear archivo .env
cat > ~/AutonomousSystem/config/.env << 'ENVEOF'
# APIs
ALPHA_VANTAGE_KEY=tu_alpha_vantage_key
BRAVE_API_KEY=tu_brave_api_key
NEWS_API_KEY=tu_news_api_key

# Configuración
LOG_LEVEL=INFO
CYCLE_INTERVAL=300
NOTIFICATION_ENABLED=true
ENVEOF
```

---

## 7. 🚀 PLAN DE IMPLEMENTACIÓN

### Fase 1: Fundación (Día 1)
- [ ] Crear estructura de directorios
- [ ] Inicializar SQLite
- [ ] Implementar Orchestrator básico
- [ ] Test de persistencia

### Fase 2: Memoria (Día 2)
- [ ] Sistema de decisiones
- [ ] Guardado automático de contexto
- [ ] Sistema de conocimiento

### Fase 3: Datos (Día 3)
- [ ] Integrar API Alpha Vantage
- [ ] Módulo de análisis técnico
- [ ] Scanner de oportunidades

### Fase 4: Automatización (Día 4)
- [ ] Scheduler mejorado
- [ ] Notificaciones
- [ ] Reporte automático

### Fase 5: Óptimo (Día 5+)
- [ ] Machine learning básico
- [ ] Predicciones
- [ ] Optimización continua

---

## 📊 Beneficios Esperados

| Aspecto | Antes | Después |
|---------|-------|----------|
| Memoria | Nula | Completa |
| Autonomía | Manual | 24/7 |
| Decisiones | Ad-hoc | Basadas en datos |
| Análisis | Superficial | Profundo con APIs |
| Valor | Variable | Constante |

---

## 💰 Costo

| Componente | Costo |
|------------|--------|
| Servidor local | $0 (tu Mac) |
| APIs gratuitas | $0 |
| APIs premium | Opcional |
| **Total** | **$0-50/mes** |

---

*Documento generado para implementación.*
