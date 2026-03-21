#!/usr/bin/env python3
"""
Agente de Inversión - Análisis Técnico
Sin APIs externas - Análisis local
"""
import json
import random
from datetime import datetime
from pathlib import Path

class TechnicalAnalysis:
    """Análisis técnico básico"""
    
    @staticmethod
    def calculate_sma(prices, period):
        """Calcula SMA simple"""
        if len(prices) < period:
            return prices[-1] if prices else 0
        return sum(prices[-period:]) / period
    
    @staticmethod
    def detect_pattern(prices, volumes):
        """Detecta patrones básicos"""
        if len(prices) < 20:
            return "INSUFFICIENT_DATA"
        
        # Análisis de tendencia
        ma10 = sum(prices[-10:]) / 10
        ma20 = sum(prices[-20:]) / 20
        
        if prices[-1] > ma10 > ma20:
            return "UPTREND"
        elif prices[-1] < ma10 < ma20:
            return "DOWNTREND"
        else:
            return "CONSOLIDATION"
    
    @staticmethod
    def rsi_estimate(prices, period=14):
        """Estimación simple de RSI"""
        if len(prices) < period + 1:
            return 50
        
        gains = []
        losses = []
        
        for i in range(-period, 0):
            change = prices[i] - prices[i-1]
            if change > 0:
                gains.append(change)
                losses.append(0)
            else:
                gains.append(0)
                losses.append(abs(change))
        
        avg_gain = sum(gains) / period
        avg_loss = sum(losses) / period
        
        if avg_loss == 0:
            return 100
        
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        return rsi
    
    @staticmethod
    def generate_signal(price, ma20, ma50, rsi):
        """Genera señal de trading"""
        if rsi < 30:
            return "STRONG_BUY", "Sobreventa (RSI < 30)"
        elif rsi < 45:
            return "BUY", "Cerca de sobreventa"
        elif rsi > 70:
            return "SELL", "Sobrecompra (RSI > 70)"
        elif rsi > 55:
            return "HOLD", "Zona neutral"
        elif price < ma20 * 0.95:
            return "BUY", "Bajo media móvil"
        elif price > ma20 * 1.10:
            return "SELL", "Sobre media móvil"
        else:
            return "ACCUMULATE", "En rango"

class InvestmentAgent:
    def __init__(self):
        self.base_dir = Path.home() / "AutonomousSystem"
        self.watchlist = self.load_watchlist()
        
    def load_watchlist(self):
        """Carga watchlist"""
        state_file = self.base_dir / "data" / "state.json"
        if state_file.exists():
            with open(state_file) as f:
                state = json.load(f)
                return state.get("watchlist", [])
        return []
    
    def generate_mock_data(self, symbol):
        """Genera datos mock realistas"""
        # Precios base
        base_prices = {
            "AAPL": 195.0, "MSFT": 380.0, "NVDA": 160.0,
            "GOOGL": 170.0, "AMZN": 190.0, "META": 500.0,
            "TSLA": 250.0, "NFLX": 600.0
        }
        
        base = base_prices.get(symbol, 100)
        # Variación aleatoria pequeña
        price = base * (1 + random.uniform(-0.03, 0.03))
        
        # Generar historial
        prices = [price * (1 + random.uniform(-0.05, 0.05)) for _ in range(60)]
        
        return {
            "symbol": symbol,
            "price": round(price, 2),
            "prices": prices,
            "volumes": [random.randint(1000000, 10000000) for _ in range(60)],
            "change": round(random.uniform(-2, 2), 2),
            "change_percent": round(random.uniform(-1.5, 1.5), 2)
        }
    
    def analyze_symbol(self, symbol):
        """Analiza un símbolo"""
        data = self.generate_mock_data(symbol)
        
        prices = data["prices"]
        volumes = data["volumes"]
        
        # Calcular indicadores
        ma20 = TechnicalAnalysis.calculate_sma(prices, 20)
        ma50 = TechnicalAnalysis.calculate_sma(prices, 50)
        rsi = TechnicalAnalysis.rsi_estimate(prices)
        pattern = TechnicalAnalysis.detect_pattern(prices, volumes)
        signal, reason = TechnicalAnalysis.generate_signal(data["price"], ma20, ma50, rsi)
        
        return {
            "symbol": symbol,
            "price": data["price"],
            "change": data["change"],
            "change_percent": data["change_percent"],
            "ma20": round(ma20, 2),
            "ma50": round(ma50, 2),
            "rsi": round(rsi, 1),
            "pattern": pattern,
            "signal": signal,
            "reason": reason,
            "target": self.get_target_price(symbol, data["price"], signal),
            "stop_loss": round(data["price"] * 0.95, 2)
        }
    
    def get_target_price(self, symbol, current, signal):
        """Calcula precio objetivo"""
        targets = {
            "STRONG_BUY": 1.20,
            "BUY": 1.15,
            "ACCUMULATE": 1.10,
            "HOLD": 1.05,
            "SELL": 0.95,
        }
        mult = targets.get(signal, 1.05)
        return round(current * mult, 2)
    
    def generate_report(self):
        """Genera reporte completo"""
        opportunities = []
        
        for item in self.watchlist:
            symbol = item.get("symbol")
            if symbol:
                analysis = self.analyze_symbol(symbol)
                opportunities.append(analysis)
        
        # Ordenar por señal
        opportunities.sort(key=lambda x: (
            0 if x["signal"] in ["STRONG_BUY", "BUY"] else
            1 if x["signal"] == "ACCUMULATE" else 2
        ))
        
        return {
            "timestamp": datetime.now().isoformat(),
            "total_analyzed": len(opportunities),
            "opportunities": opportunities,
            "buy_signals": [o for o in opportunities if "BUY" in o["signal"]],
            "sell_signals": [o for o in opportunities if "SELL" in o["signal"]]
        }
    
    def format_report(self, report):
        """Formatea reporte"""
        lines = [
            "="*60,
            "📈 ANÁLISIS TÉCNICO DE INVERSIÓN",
            "="*60,
            f"Fecha: {report['timestamp'][:19]}",
            f"Analizados: {report['total_analyzed']} símbolos",
            ""
        ]
        
        #Señales de compra
        buys = report.get("buy_signals", [])
        if buys:
            lines.append("🟢 SEÑALES DE COMPRA:")
            for b in buys:
                lines.append(f"  {b['symbol']}: ${b['price']} ({b['change_percent']:+.1f}%)")
                lines.append(f"    RSI: {b['rsi']} | MA20: ${b['ma20']} | MA50: ${b['ma50']}")
                lines.append(f"    Señal: {b['signal']} - {b['reason']}")
                lines.append(f"    Target: ${b['target']} | Stop: ${b['stop_loss']}")
                lines.append("")
        
        #Señales de venta
        sells = report.get("sell_signals", [])
        if sells:
            lines.append("🔴 SEÑALES DE VENTA:")
            for s in sells:
                lines.append(f"  {s['symbol']}: ${s['price']} - {s['signal']}")
                lines.append("")
        
        #Todas las señales
        lines.append("📊 RESUMEN:")
        for o in report["opportunities"]:
            emoji = "🟢" if "BUY" in o["signal"] else "🔴" if "SELL" in o["signal"] else "⚪"
            lines.append(f"{emoji} {o['symbol']}: ${o['price']} | RSI:{o['rsi']} | {o['signal']}")
        
        lines.append("="*60)
        
        return "\n".join(lines)

def main():
    random.seed(42)  # Para reproducibilidad
    agent = InvestmentAgent()
    
    print("🎯 Generando análisis técnico...\n")
    
    report = agent.generate_report()
    print(agent.format_report(report))
    
    # Guardar
    output = agent.base_dir / "data" / "technical_report.json"
    with open(output, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\n✅ Reporte guardado en {output}")

if __name__ == "__main__":
    main()
