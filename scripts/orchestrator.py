#!/usr/bin/env python3
"""
ORCHESTRATOR v2.0 - CEO del Sistema
Interpretar intención -> Leer estado -> Priorizar -> Delegar -> Registrar
"""
import json
import sys
from pathlib import Path
from datetime import datetime

BASE = Path.home() / "AutonomousSystem"

# Intents mapping
INTENTS = {
    "INVERSION": ["analiza", "inversion", "mercado", "acciones", "bolsa", "trading", "oportunidad", "nvda", "aapl", "msft", "googl"],
    "PROYECTO": ["crea", "idea", "negocio", "saas", "landing", "app", "desarrolla", "proyecto"],
    "DISEÑO": ["diseña", "ui", "ux", "interfaz", "mejora", "visual", "diseño"],
    "LEGAL": ["contrato", "legal", "acuerdo", "terminos", "privacidad", "aviso"],
    "REVISION": ["revisa", "valida", "revisar", "calidad", "auditoria"],
    "CRECIMIENTO": ["crece", "crecimiento", "marketing", "用户增长", "monetiza", "vende"],
    "AUTONOMO": ["trabaja", "autonomo", "solo", "continua", "ejecuta"]
}

AGENTS = {
    "investment": "agents/investment_agent.py",
    "builder": "agents/builder_agent.py",
    "design": "agents/design_agent.py",
    "legal": "agents/legal_agent.py",
    "reviewer": "agents/reviewer_agent.py",
    "growth": "agents/growth_agent.py"
}

class Orchestrator:
    def __init__(self):
        self.state_file = BASE / "data" / "state.json"
        self.state = self.load_state()
        
    def load_state(self):
        if self.state_file.exists():
            with open(self.state_file) as f:
                return json.load(f)
        return {"goals": [], "tasks": [], "ideas": [], "last_actions": []}
    
    def save_state(self):
        self.state["last_update"] = datetime.now().isoformat()
        with open(self.state_file, 'w') as f:
            json.dump(self.state, f, indent=2)
    
    def log_action(self, action, result):
        """Registra acción en memoria"""
        # Guardar en last_actions
        if "last_actions" not in self.state:
            self.state["last_actions"] = []
        
        self.state["last_actions"].insert(0, {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "result": result
        })
        self.state["last_actions"] = self.state["last_actions"][:20]
        
        # Guardar en decisions.md
        decisions_file = BASE / "memory" / "decisions.md"
        entry = f"\n### {datetime.now().strftime('%Y-%m-%d %H:%M')}\n**{action}**: {result}\n"
        
        if decisions_file.exists():
            content = decisions_file.read_text()
            # Find last --- marker
            if "---" in content:
                pos = content.rfind("---")
                content = content[:pos+3] + entry + content[pos+3:]
            else:
                content = entry + "\n" + content
        else:
            content = f"# Decisiones\n{entry}"
        
        decisions_file.write_text(content)
        
        self.save_state()
    
    def detect_intent(self, message):
        """Detecta intención del usuario"""
        msg = message.lower()
        
        for intent, keywords in INTENTS.items():
            for kw in keywords:
                if kw in msg:
                    return intent
        
        return "UNKNOWN"
    
    def decide_agent(self, intent):
        """Decide qué agente usar"""
        mapping = {
            "INVERSION": "investment",
            "PROYECTO": "builder",
            "DISEÑO": "design",
            "LEGAL": "legal",
            "REVISION": "reviewer",
            "CRECIMIENTO": "growth",
            "AUTONOMO": "autonomous"
        }
        return mapping.get(intent, "general")
    
    def run_agent(self, agent_name, task):
        """Ejecuta un agente"""
        import subprocess
        
        agent_file = BASE / AGENTS.get(agent_name, "agents/general_agent.py")
        
        if not agent_file.exists():
            return f"Agente {agent_name} no encontrado"
        
        try:
            result = subprocess.run(
                ["python3", str(agent_file)],
                capture_output=True,
                text=True,
                timeout=120
            )
            return result.stdout if result.returncode == 0 else result.stderr
        except Exception as e:
            return f"Error: {str(e)}"
    
    def execute(self, message):
        """Ejecuta el ciclo completo"""
        print(f"📥 Mensaje: {message[:50]}...")
        
        # 1. Detectar intención
        intent = self.detect_intent(message)
        print(f"🎯 Intención detectada: {intent}")
        
        # 2. Decidir agente
        agent = self.decide_agent(intent)
        print(f"🤖 Agente seleccionado: {agent}")
        
        # 3. Ejecutar
        result = self.run_agent(agent, message)
        
        # 4. Registrar
        self.log_action(f"Intent: {intent} -> Agent: {agent}", result[:200] if result else "OK")
        
        return result
    
    def autonomous_cycle(self):
        """Ciclo autónomo cuando no hay input"""
        print("🔄 Modo autónomo - buscando oportunidades...")
        
        # Usar growth agent
        result = self.run_agent("growth", "analiza_oportunidades")
        
        # Registrar
        self.log_action("autonomous_cycle", result[:100] if result else "Sin oportunidades")
        
        return result

def main():
    orch = Orchestrator()
    
    if len(sys.argv) > 1:
        # Modo: mensaje directo
        message = " ".join(sys.argv[1:])
        result = orch.execute(message)
        print(result)
    else:
        # Modo autónomo
        print("🔄 Iniciando ciclo autónomo...")
        result = orch.autonomous_cycle()
        print(result)
        orch.save_state()

if __name__ == "__main__":
    main()
