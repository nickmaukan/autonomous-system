#!/usr/bin/env python3
"""
BUILDER_AGENT - Generador de proyectos
"""
import json
from pathlib import Path
from datetime import datetime

BASE = Path.home() / "AutonomousSystem"

class BuilderAgent:
    def __init__(self):
        self.state_file = BASE / "data" / "state.json"
        
    def load_state(self):
        if self.state_file.exists():
            return json.loads(self.state_file.read_text())
        return {}
    
    def save_idea(self, idea):
        """Guarda idea en memoria"""
        ideas_file = BASE / "memory" / "ideas.md"
        
        entry = f"""
### {datetime.now().strftime('%Y-%m-%d %H:%M')}
**Proyecto:** {idea['title']}
- Status: {idea.get('status', 'new')}
- Potential: {idea.get('potential', 'medium')}
- Notes: {idea.get('notes', '')}
"""
        
        if ideas_file.exists():
            content = ideas_file.read_text()
            # Add after first header
            if "\n## Ideas" in content:
                content = content.replace("\n## Ideas", f"\n## Ideas{entry}")
            else:
                content += entry
        else:
            content = f"# Ideas\n{entry}"
        
        ideas_file.write_text(content)
    
    def generate_ideas(self):
        """Genera ideas de negocio"""
        ideas = [
            {
                "title": "SaaS Facturación Ecuador",
                "description": "Sistema de facturación electrónica para PYMES",
                "status": "new",
                "potential": "high",
                "execution_time": "2-4 semanas",
                "cost": "$50-100/mes",
                "monetization": "SaaS mensual",
                "notes": "Mercado huge en Ecuador. Integrar con SRI."
            },
            {
                "title": "Dashboard Trading",
                "description": "Visualizador de portfolio de inversiones",
                "status": "new", 
                "potential": "medium",
                "execution_time": "1-2 semanas",
                "cost": "$20/mes",
                "monetization": "Freemium",
                "notes": "Basado en datos públicos de Yahoo Finance"
            },
            {
                "title": "Bot WhatsApp Business",
                "description": "Automación para negocios locales",
                "status": "new",
                "potential": "high",
                "execution_time": "1 semana",
                "cost": "$10/mes",
                "monetization": "Setup + mensual",
                "notes": "Menores costos, alta demanda"
            },
            {
                "title": "Landing Page Generator",
                "description": "Creador de landings sin código",
                "status": "new",
                "potential": "medium",
                "execution_time": "3-4 semanas",
                "cost": "$30/mes",
                "monetization": "Suscripción",
                "notes": "Mercado saturado pero siempre hay espacio para buen producto"
            }
        ]
        
        return ideas
    
    def run(self):
        print("🏗️ BUILDER AGENT - Generando ideas de proyectos...\n")
        
        ideas = self.generate_ideas()
        
        # Guardar en memoria
        for idea in ideas:
            self.save_idea(idea)
        
        # Mostrar ideas
        print("="*60)
        print("💡 IDEAS DE PROYECTOS")
        print("="*60)
        
        for i, idea in enumerate(ideas, 1):
            print(f"\n{i}. {idea['title']}")
            print(f"   📝 {idea['description']}")
            print(f"   ⏱️ {idea['execution_time']}")
            print(f"   💰 Costo: {idea['cost']}")
            print(f"   🎯 Potencial: {idea['potential']}")
            print(f"   💵 Monetización: {idea['monetization']}")
        
        print("\n" + "="*60)
        print("✅ Ideas generadas y guardadas en memoria")
        
        return "\n".join([f"- {i['title']}" for i in ideas])

if __name__ == "__main__":
    BuilderAgent().run()
