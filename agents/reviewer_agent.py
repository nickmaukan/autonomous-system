#!/usr/bin/env python3
"""
REVIEWER_AGENT - Control de calidad
"""
import json
from pathlib import Path

BASE = Path.home() / "AutonomousSystem"

class ReviewerAgent:
    def review_system(self):
        """Revisa el estado del sistema"""
        issues = []
        
        # Check state.json
        state_file = BASE / "data" / "state.json"
        if not state_file.exists():
            issues.append("CRÍTICO: state.json no existe")
        else:
            state = json.loads(state_file.read_text())
            
            # Verificar estructura
            if "goals" not in state:
                issues.append("FALTA: goals en state.json")
            if "last_actions" not in state:
                issues.append("FALTA: last_actions en state.json")
            if "last_update" not in state:
                issues.append("FALTA: last_update en state.json")
        
        # Check memory files
        for f in ["decisions.md", "ideas.md", "watchlist.md"]:
            fpath = BASE / "memory" / f
            if not fpath.exists():
                issues.append(f"FALTA: {f}")
        
        # Check agents
        agents_dir = BASE / "agents"
        if agents_dir.exists():
            agents = list(agents_dir.glob("*.py"))
            print(f"Agentes encontrados: {len(agents)}")
        
        return issues
    
    def run(self):
        print("🔍 REVIEWER AGENT - Revisando sistema...\n")
        
        issues = self.review_system()
        
        print("="*60)
        print("🔍 REVISIÓN DEL SISTEMA")
        print("="*60)
        
        if issues:
            print("\n⚠️ PROBLEMAS ENCONTRADOS:")
            for issue in issues:
                print(f"  - {issue}")
        else:
            print("\n✅ Sistema OK - No se encontraron problemas")
        
        # Sugerencias
        print("\n💡 SUGERENCIAS:")
        print("  - Agregar más métricas al análisis")
        print("  - Configurar API keys para datos reales")
        print("  - Automatizar tareas repetitivas")
        
        # Guardar reporte
        report = {
            "timestamp": "2026-03-20T16:20:00Z",
            "issues": issues,
            "suggestions": [
                "Agregar métricas",
                "Configurar APIs",
                "Automatizar tareas"
            ]
        }
        
        output = BASE / "data" / "review_report.json"
        output.write_text(json.dumps(report, indent=2))
        
        print(f"\n✅ Reporte guardado en {output}")
        
        return "Revisión completada"

if __name__ == "__main__":
    ReviewerAgent().run()
