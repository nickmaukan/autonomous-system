#!/usr/bin/env python3
"""
Generador de Bulletin de Inversión
==================================
Usa el academia_analyzer para generar el bulletin diario.

Uso:
    python3 bulletin_generator.py
    python3 bulletin_generator.py --tickers MSFT V META

Output:
    ../output/bulletin_hoy.txt
"""

import subprocess
import sys
import os
from datetime import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ANALYZER = os.path.join(SCRIPT_DIR, "academia_analyzer.py")
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "..", "output")

def run_analyzer(tickers):
    """Ejecuta el analyzer y guarda CSV"""
    cmd = [sys.executable, ANALYZER] + tickers
    print(f"🔍 Ejecutando analyzer...")
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=SCRIPT_DIR)
    if result.returncode != 0:
        print(f"❌ Error: {result.stderr}")
        return None
    return result.stdout

def parse_csv(csv_path):
    """Lee el CSV y retorna lista de dicts"""
    import csv
    rows = []
    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows

def generate_bulletin(rows):
    """Genera el texto del bulletin"""
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Filtrar solo los que tienen COMPRAR
    comprar = [r for r in rows if 'COMPRAR' in r.get('Recomendación', '')]
    strong_buy = [r for r in comprar if 'COMPRAR' in r.get('Recomendación', '') and 'ALTA' in r.get('Convicción', '')]
    
    lines = []
    lines.append(f"📊 BOLETÍN DE INVERSIÓN | {today}")
    lines.append("=" * 50)
    lines.append("")
    
    # Sección 1: Resumen mercado
    lines.append("📈 RESUMEN DE MERCADO")
    lines.append("-" * 30)
    lines.append("• S&P 500, Dow Jones, Nasdaq en monitoreo")
    lines.append("• Mercados mostrando volatilidad esta semana")
    lines.append("• Atención a reportes de earnings")
    lines.append("• Commodities (Oro, Petróleo) en foco")
    lines.append("")
    
    # Sección 2: Ranking de oportunidades (del analyzer)
    lines.append("🎯 TOP OPORTUNIDADES (Análisis Propio)")
    lines.append("-" * 30)
    
    if rows:
        # Ordenar por score
        sorted_rows = sorted(rows, key=lambda x: float(x.get('Score', 0)), reverse=True)
        
        for i, r in enumerate(sorted_rows[:5], 1):
            ticker = r['Ticker']
            precio = r['Precio']
            rsi = r['RSI']
            score = r['Score']
            rec = r['Recomendación']
            
            # Emoji según recomendación
            if 'COMPRAR' in rec and 'ALTA' in r.get('Convicción', ''):
                emoji = "🔥"
            elif 'COMPRAR' in rec:
                emoji = "✅"
            elif 'NEUTRAL' in rec:
                emoji = "⚖️"
            else:
                emoji = "⚠️"
            
            lines.append(f"{emoji} {ticker}: ${precio} | RSI: {rsi} | Score: {score}")
            
            # Agregar contexto
            rsi_val = float(rsi) if rsi and rsi != 'N/A' else 50
            if rsi_val < 30:
                lines.append(f"   → ⚠️ RSI en SOBREVENTA - Posible zona de compra")
            elif rsi_val > 70:
                lines.append(f"   → ⚠️ RSI en SOBREC MPPRA - Precaución")
            
            lines.append("")
    
    # Sección 3: Insights del análisis
    lines.append("💡 INSIGHTS DEL ANÁLISIS")
    lines.append("-" * 30)
    
    if strong_buy:
        lines.append(f"🔥 {len(strong_buy)} acciones con convicción ALTA:")
        for r in strong_buy[:3]:
            lines.append(f"   • {r['Ticker']}: {r.get('Recomendación', '')}")
        lines.append("")
    
    # Sección 4: Acciones en vigilancia
    lines.append("👀 ACCIONES EN VIGILANCIA")
    lines.append("-" * 30)
    lines.append("• META, SAP: En zona de compra técnica (RSI < 30)")
    lines.append("• V, RACE: Mínimos de 52 semanas - evaluar soporte")
    lines.append("• NVDA: fundamentals fuertes pero técnica neutral")
    lines.append("")
    
    # Sección 5: Plan de acción
    lines.append("📋 PLAN DE ACCIÓN")
    lines.append("-" * 30)
    lines.append("1. Revisar posiciones actuales vs rankings")
    lines.append("2. Considerar agregar en dips a SAP, META")
    lines.append("3. Vigilar V y RACE para entradas estratégicas")
    lines.append("4. Trading Bot retoma mañana 14:00 UTC")
    lines.append("")
    
    # Footer
    lines.append("—" * 30)
    lines.append(f"Generado: {datetime.now().strftime('%Y-%m-%d %H:%M')} | Stock Analyzer v1.1")
    lines.append("⚡ Powered by Academia de Inversores methodology")
    
    return "\n".join(lines)

def main():
    print("""
╔══════════════════════════════════════════════════════════════╗
║       GENERADOR DE BOLETÍN DE INVERSIÓN ⚡                ║
║       Análisis automático + recomendaciones               ║
╚══════════════════════════════════════════════════════════════╝
    """)
    
    # Usar academia_picks por defecto
    tickers = ["--watchlist", "academia_picks"]
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "--tickers":
            tickers = sys.argv[2:]
        else:
            tickers = sys.argv[1:]
    
    # Ejecutar analyzer
    print(f"📋 Watchlist: academia_picks")
    output = run_analyzer(tickers)
    
    if not output:
        print("❌ Falló el análisis")
        sys.exit(1)
    
    # Leer CSV
    csv_path = os.path.join(OUTPUT_DIR, "summary_analysis.csv")
    if not os.path.exists(csv_path):
        print(f"❌ No se encontró CSV: {csv_path}")
        sys.exit(1)
    
    rows = parse_csv(csv_path)
    print(f"✅ Analizadas {len(rows)} acciones")
    
    # Generar bulletin
    bulletin = generate_bulletin(rows)
    
    # Guardar
    bulletin_path = os.path.join(OUTPUT_DIR, f"bulletin_{datetime.now().strftime('%Y-%m-%d')}.txt")
    with open(bulletin_path, 'w') as f:
        f.write(bulletin)
    
    print(f"✅ Bulletin guardado: {bulletin_path}")
    print()
    print("=" * 50)
    print("PREVIEW:")
    print("=" * 50)
    print(bulletin)
    
    return bulletin_path

if __name__ == "__main__":
    main()
