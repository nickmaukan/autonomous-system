#!/usr/bin/env python3
"""
RESEARCH AGENT - Investiga temas y genera insights
"""
import json
from pathlib import Path
from datetime import datetime
import subprocess

BASE = Path.home() / "AutonomousSystem"

class ResearchAgent:
    def __init__(self):
        self.state_file = BASE / "data" / "state.json"
    
    def search_web(self, query):
        """Busca en la web usando Brave API o simple curl"""
        # Intentar con Brave Search si está configurado
        try:
            result = subprocess.run(
                ["curl", "-s", f"https://api.search.brave.com/res/v1/web/search?q={query}&count=5"],
                capture_output=True,
                text=True,
                timeout=10
            )
            if result.returncode == 0:
                data = json.loads(result.stdout)
                results = []
                if "web" in data and "results" in data["web"]:
                    for r in data["web"]["results"][:5]:
                        results.append({
                            "title": r.get("title", ""),
                            "url": r.get("url", ""),
                            "description": r.get("description", "")[:150]
                        })
                return results
        except:
            pass
        
        # Fallback: búsqueda simple
        return [{"title": f"Resultado para: {query}", "url": "", "description": "Brave API no configurada"}]
    
    def research_topics(self):
        """Investiga temas de interés"""
        topics = [
            "SaaS Ecuador 2024 oportunidades",
            "inversión técnicas Monte Carlo finanzas",
            "facturación electrónica Ecuador SRI",
            "AI automation small business 2024"
        ]
        
        all_results = []
        
        for topic in topics:
            print(f"🔍 Investigando: {topic}")
            results = self.search_web(topic)
            all_results.append({
                "topic": topic,
                "results": results
            })
        
        return all_results
    
    def run(self, topic=None):
        if topic:
            print(f"🔍 Investigando: {topic}")
            results = self.search_web(topic)
            
            print("\n" + "="*60)
            print(f"📚 RESULTADOS: {topic}")
            print("="*60)
            
            for i, r in enumerate(results, 1):
                print(f"\n{i}. {r['title']}")
                print(f"   📝 {r['description']}")
                if r['url']:
                    print(f"   🔗 {r['url']}")
            
            # Guardar
            output = BASE / "data" / "research.json"
            output.write_text(json.dumps({"topic": topic, "results": results, "timestamp": datetime.now().isoformat()}, indent=2))
            print(f"\n✅ Guardado en {output}")
        else:
            # Investigación general
            print("🔍 RESEARCH AGENT - Investigando temas de interés...\n")
            results = self.research_topics()
            
            print("\n" + "="*60)
            print("📚 RESUMEN DE INVESTIGACIÓN")
            print("="*60)
            
            for r in results:
                print(f"\n📌 {r['topic']}")
                print(f"   Resultados: {len(r['results'])}")
            
            # Guardar
            output = BASE / "data" / "research.json"
            output.write_text(json.dumps(results, indent=2))
            print(f"\n✅ Investigación guardada en {output}")

if __name__ == "__main__":
    import sys
    topic = sys.argv[1] if len(sys.argv) > 1 else None
    ResearchAgent().run(topic)
