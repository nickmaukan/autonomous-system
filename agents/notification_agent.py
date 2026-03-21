#!/usr/bin/env python3
"""
NOTIFICATION AGENT - Envía alertas y notificaciones
"""
import json
from pathlib import Path
from datetime import datetime

BASE = Path.home() / "AutonomousSystem"

class NotificationAgent:
    def __init__(self):
        self.alerts_file = BASE / "data" / "alerts.json"
        self.load_alerts()
    
    def load_alerts(self):
        if self.alerts_file.exists():
            self.alerts = json.loads(self.alerts_file.read_text())
        else:
            self.alerts = []
    
    def save_alerts(self):
        self.alerts_file.write_text(json.dumps(self.alerts, indent=2))
    
    def add_alert(self, title, message, priority="normal"):
        """Agrega una alerta"""
        alert = {
            "id": len(self.alerts) + 1,
            "title": title,
            "message": message,
            "priority": priority,
            "created_at": datetime.now().isoformat(),
            "read": False
        }
        self.alerts.insert(0, alert)
        self.save_alerts()
        return alert
    
    def get_unread(self):
        """Obtiene alertas no leídas"""
        return [a for a in self.alerts if not a.get("read", False)]
    
    def mark_read(self, alert_id):
        """Marca alerta como leída"""
        for a in self.alerts:
            if a["id"] == alert_id:
                a["read"] = True
        self.save_alerts()
    
    def generate_daily_summary(self):
        """Genera resumen diario"""
        # Cargar datos
        state_file = BASE / "data" / "state.json"
        if state_file.exists():
            state = json.loads(state_file.read_text())
        else:
            state = {}
        
        summary = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "total_cycles": len(state.get("last_actions", [])),
            "last_action": state.get("last_actions", [{}])[0].get("action", "N/A") if state.get("last_actions") else "N/A",
            "goals_active": len(state.get("goals", [])),
            "tasks_pending": len(state.get("active_tasks", []))
        }
        
        return summary
    
    def notify_opportunity(self, symbol, signal, price):
        """Notifica oportunidad de inversión"""
        return self.add_alert(
            f"📈 Oportunidad: {symbol}",
            f"Señal {signal} para {symbol} a ${price}",
            priority="high" if signal == "BUY" else "normal"
        )

def main():
    agent = NotificationAgent()
    
    print("🔔 NOTIFICATION AGENT")
    
    # Generar resumen
    summary = agent.generate_daily_summary()
    print(f"\n📊 Resumen del día: {summary['date']}")
    print(f"   Ciclos ejecutados: {summary['total_cycles']}")
    print(f"   Última acción: {summary['last_action']}")
    print(f"   Goals activos: {summary['goals_active']}")
    
    # Agregar alerta de ejemplo
    agent.notify_opportunity("GOOGL", "BUY", 171.08)
    
    # Mostrar alertas
    print(f"\n🔔 Alertas ({len(agent.get_unread())} no leídas):")
    for a in agent.get_unread()[:5]:
        emoji = "🔴" if a["priority"] == "high" else "⚪"
        print(f"   {emoji} {a['title']}: {a['message']}")

if __name__ == "__main__":
    main()
