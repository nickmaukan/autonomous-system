#!/usr/bin/env python3
"""
AUTOMATION AGENT - Automatiza tareas repetitivas
"""
import json
from pathlib import Path
from datetime import datetime
import subprocess
import time

BASE = Path.home() / "AutonomousSystem"

class AutomationAgent:
    def __init__(self):
        self.tasks_file = BASE / "data" / "automation_tasks.json"
        self.load_tasks()
    
    def load_tasks(self):
        if self.tasks_file.exists():
            self.tasks = json.loads(self.tasks_file.read_text())
        else:
            self.tasks = []
    
    def save_tasks(self):
        self.tasks_file.write_text(json.dumps(self.tasks, indent=2))
    
    def add_task(self, name, command, interval_minutes=60):
        """Agrega una tarea automatizada"""
        task = {
            "name": name,
            "command": command,
            "interval_minutes": interval_minutes,
            "created_at": datetime.now().isoformat(),
            "last_run": None,
            "run_count": 0
        }
        self.tasks.append(task)
        self.save_tasks()
        return task
    
    def run_task(self, task):
        """Ejecuta una tarea"""
        print(f"⚡ Ejecutando: {task['name']}")
        
        try:
            # Determinar el comando
            cmd = task["command"]
            
            if cmd == "investment_analysis":
                result = subprocess.run(
                    ["python3", str(BASE / "agents" / "investment_agent.py")],
                    capture_output=True,
                    text=True,
                    timeout=60
                )
                output = result.stdout[:500] if result.returncode == 0 else result.stderr[:500]
            
            elif cmd == "growth_analysis":
                result = subprocess.run(
                    ["python3", str(BASE / "agents" / "growth_agent.py")],
                    capture_output=True,
                    text=True,
                    timeout=60
                )
                output = result.stdout[:500] if result.returncode == 0 else result.stderr[:500]
            
            elif cmd == "system_review":
                result = subprocess.run(
                    ["python3", str(BASE / "agents" / "reviewer_agent.py")],
                    capture_output=True,
                    text=True,
                    timeout=60
                )
                output = result.stdout[:500] if result.returncode == 0 else result.stderr[:500]
            
            else:
                output = "Comando desconocido"
            
            task["last_run"] = datetime.now().isoformat()
            task["run_count"] = task.get("run_count", 0) + 1
            
            print(f"   ✅ Completado: {output[:100]}...")
            return True
            
        except Exception as e:
            print(f"   ❌ Error: {str(e)}")
            return False
    
    def run_all(self):
        """Ejecuta todas las tareas"""
        print("🤖 AUTOMATION AGENT - Ejecutando tareas...\n")
        
        for task in self.tasks:
            self.run_task(task)
        
        self.save_tasks()
        
        print(f"\n✅ {len(self.tasks)} tareas ejecutadas")
    
    def setup_daily_tasks(self):
        """Configura tareas diarias"""
        # Limpiar tareas existentes
        self.tasks = []
        
        # Tareas diarias
        self.add_task("Análisis de inversiones", "investment_analysis", 60)  # Cada hora
        self.add_task("Análisis de crecimiento", "growth_analysis", 120)  # Cada 2 horas
        self.add_task("Revisión del sistema", "system_review", 360)  # Cada 6 horas
        
        self.save_tasks()
        
        print("✅ Tareas diarias configuradas:")
        for t in self.tasks:
            print(f"   - {t['name']}: cada {t['interval_minutes']} min")

def main():
    agent = AutomationAgent()
    
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "setup":
            agent.setup_daily_tasks()
        elif sys.argv[1] == "run":
            agent.run_all()
        else:
            print("Uso: python3 automation_agent.py [setup|run]")
    else:
        # Mostrar estado
        print("🤖 AUTOMATION AGENT")
        print(f"   Tareas configuradas: {len(agent.tasks)}")
        
        if agent.tasks:
            print("\n📋 Tareas:")
            for t in agent.tasks:
                print(f"   - {t['name']} (cada {t['interval_minutes']} min)")

if __name__ == "__main__":
    main()
