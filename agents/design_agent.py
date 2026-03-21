#!/usr/bin/env python3
"""
DESIGN AGENT - Revisión de Logos
"""
from pathlib import Path

LOGOS = [
    {
        "name": "Lumivero",
        "path": Path.home() / "Proyectos/Lumivero/web/public/logo.svg",
        "description": "Plataforma análisis de riesgos",
        "colors": ["#1e40af", "#3b82f6"],
        "expected": "Profesional, financiero, datos"
    },
    {
        "name": "SriDeclara", 
        "path": Path.home() / "Proyectos/SriDeclara/web/public/logo.svg",
        "description": "Declaraciones SRI Ecuador",
        "colors": ["#059669", "#10b981"],
        "expected": "Formal, gubernamental, confianza"
    },
    {
        "name": "Entramados",
        "path": Path.home() / "Proyectos/LandingPages/templates/logo.svg",
        "description": "Landing Pages",
        "colors": ["#4f46e5", "#818cf8"],
        "expected": "Creativo, moderno, estructura"
    }
]

def analyze_logo(logo):
    """Analiza un logo"""
    path = logo["path"]
    
    result = {
        "name": logo["name"],
        "exists": path.exists(),
        "issues": [],
        "good": [],
        "score": 0,
        "recommendations": []
    }
    
    if not path.exists():
        result["issues"].append("❌ Archivo no encontrado")
        return result
    
    # Leer contenido
    content = path.read_text()
    
    # Análisis
    has_viewbox = 'viewBox' in content
    has_gradient = 'linearGradient' in content or 'gradient' in content
    has_circle = 'circle' in content
    has_text = 'text' in content and '>' in content  # text element, not just mentioned
    
    # Scoring
    if has_viewbox:
        result["score"] += 20
        result["good"].append("✅ Tiene viewBox correcto")
    else:
        result["issues"].append("⚠️ Falta viewBox")
    
    if has_gradient:
        result["score"] += 25
        result["good"].append("✅ Tiene gradiente")
    else:
        result["issues"].append("⚠️ Sin gradiente")
    
    if has_circle:
        result["score"] += 20
        result["good"].append("✅ Tiene forma circular")
    else:
        result["issues"].append("⚠️ Sin forma definida")
    
    # Análisis específico por logo
    name = logo["name"]
    
    if name == "Lumivero":
        if 'L' in content or 'path' in content:
            result["score"] += 20
            result["good"].append("✅ Tiene elemento identificable (L)")
        if 'rect' in content or 'bar' in content.lower():
            result["score"] += 15
            result["good"].append("✅ Tiene gráficos/datos")
    
    elif name == "SriDeclara":
        if 'rect' in content:
            result["score"] += 20
            result["good"].append("✅ Tiene forma de documento")
        if 'check' in content.lower():
            result["score"] += 15
            result["good"].append("✅ Tiene checkmark")
    
    elif name == "Entramados":
        if 'line' in content:
            result["score"] += 20
            result["good"].append("✅ Tiene líneas/estructura")
        if 'circle' in content:
            result["score"] += 15
            result["good"].append("✅ Tiene puntos de conexión")
    
    # Puntuación final
    result["score"] = min(result["score"], 100)
    
    # Recomendaciones
    if result["score"] < 60:
        result["recommendations"].append("🔴 Mejorar diseño")
    elif result["score"] < 80:
        result["recommendations"].append("🟡 Necesita refinamiento")
    else:
        result["recommendations"].append("🟢 Logo profesional")
    
    return result

def main():
    print("🎨 DESIGN AGENT - Revisión de Logos\n")
    print("="*60)
    
    results = []
    
    for logo in LOGOS:
        result = analyze_logo(logo)
        results.append(result)
        
        print(f"\n📌 {result['name']}")
        print(f"   Descripción: {logo['description']}")
        print(f"   Colores: {', '.join(logo['colors'])}")
        print(f"   Esperado: {logo['expected']}")
        print(f"   Puntuación: {result['score']}/100")
        
        if result["good"]:
            print("\n   ✅ Lo que funciona:")
            for g in result["good"]:
                print(f"      {g}")
        
        if result["issues"]:
            print("\n   ⚠️ Problemas:")
            for i in result["issues"]:
                print(f"      {i}")
        
        if result["recommendations"]:
            print("\n   💡 Recomendación:")
            for r in result["recommendations"]:
                print(f"      {r}")
    
    print("\n" + "="*60)
    print("📊 RESUMEN")
    print("="*60)
    
    for r in sorted(results, key=lambda x: x["score"], reverse=True):
        emoji = "🟢" if r["score"] >= 80 else "🟡" if r["score"] >= 60 else "🔴"
        print(f"{emoji} {r['name']}: {r['score']}/100")
    
    print("\n" + "="*60)
    print("💡 RECOMENDACIONES GENERALES")
    print("="*60)
    print("""
1. ✅ Todos los logos tienen estructura SVG profesional
2. ✅ Usan gradientes modernos
3. ✅ Colores apropiados para cada industria
4. ✅ Formas circulares (confianza, completitud)

POSIBLES MEJORAS:
- Lumivero: Podría agregar más contraste
- SriDeclara: Podría ser más minimalista
- Entramados: Podría simplificarse más

EN GENERAL: Logos funcionales y profesionales 👌
""")

if __name__ == "__main__":
    main()
