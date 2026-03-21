#!/usr/bin/env python3
"""
Gestor de Datos - Módulo de datos financieros
Integración con APIs de mercado
"""
import os
import json
import requests
from datetime import datetime
from pathlib import Path

class DataManager:
    def __init__(self):
        self.cache_dir = Path.home() / "AutonomousSystem" / "data" / "cache"
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        
        # API Keys (cargar desde config)
        self.alpha_vantage_key = os.environ.get("ALPHA_VANTAGE_KEY", "")
        self.newsapi_key = os.environ.get("NEWS_API_KEY", "")
    
    def cache_get(self, key):
        """Obtiene dato desde cache"""
        cache_file = self.cache_dir / f"{key}.json"
        if cache_file.exists():
            with open(cache_file) as f:
                return json.load(f)
        return None
    
    def cache_set(self, key, data):
        """Guarda dato en cache"""
        cache_file = self.cache_dir / f"{key}.json"
        with open(cache_file, 'w') as f:
            json.dump(data, f)
    
    def get_quote(self, symbol):
        """Obtiene precio actual de acción"""
        # Check cache first
        cache_key = f"quote_{symbol}"
        cached = self.cache_get(cache_key)
        if cached:
            return cached
        
        # Si no hay API key, devolver mock
        if not self.alpha_vantage_key:
            return self._mock_quote(symbol)
        
        # Llamar API
        url = "https://www.alphavantage.co/query"
        params = {
            "function": "GLOBAL_QUOTE",
            "symbol": symbol,
            "apikey": self.alpha_vantage_key
        }
        
        try:
            resp = requests.get(url, params=params, timeout=10)
            data = resp.json()
            
            if "Global Quote" in data and data["Global Quote"]:
                quote = data["Global Quote"]
                result = {
                    "symbol": symbol,
                    "price": float(quote.get("05. price", 0)),
                    "change": float(quote.get("09. change", 0)),
                    "change_percent": quote.get("10. change percent", "0%"),
                    "volume": int(quote.get("06. volume", 0)),
                    "timestamp": datetime.now().isoformat()
                }
                self.cache_set(cache_key, result)
                return result
        except Exception as e:
            print(f"Error getting quote: {e}")
        
        return self._mock_quote(symbol)
    
    def get_technical(self, symbol, indicator="SMA", period=200):
        """Obtiene indicadores técnicos"""
        if not self.alpha_vantage_key:
            return self._mock_technical(symbol)
        
        url = "https://www.alphavantage.co/query"
        params = {
            "function": indicator,
            "symbol": symbol,
            "interval": "daily",
            "time_period": str(period),
            "series_type": "close",
            "apikey": self.alpha_vantage_key
        }
        
        try:
            resp = requests.get(url, params=params, timeout=10)
            data = resp.json()
            return data
        except:
            return self._mock_technical(symbol)
    
    def scan_opportunities(self, watchlist):
        """Escanea oportunidades en watchlist"""
        opportunities = []
        
        for item in watchlist:
            symbol = item.get("symbol")
            if not symbol:
                continue
            
            quote = self.get_quote(symbol)
            
            # Análisis simple
            price = quote.get("price", 0)
            target = item.get("target", 0)
            
            if target and price:
                upside = ((target - price) / price) * 100
                
                opportunities.append({
                    "symbol": symbol,
                    "price": price,
                    "target": target,
                    "upside": upside,
                    "notes": item.get("notes", "")
                })
        
        # Ordenar por upside
        opportunities.sort(key=lambda x: x.get("upside", 0), reverse=True)
        
        return opportunities
    
    def _mock_quote(self, symbol):
        """Mock quote para testing sin API"""
        mocks = {
            "AAPL": {"price": 195.0, "change": -2.5, "change_percent": "-1.27%"},
            "MSFT": {"price": 380.0, "change": 5.0, "change_percent": "1.33%"},
            "NVDA": {"price": 160.0, "change": -8.0, "change_percent": "-4.76%"},
            "GOOGL": {"price": 170.0, "change": 1.5, "change_percent": "0.89%"},
            "AMZN": {"price": 190.0, "change": 3.0, "change_percent": "1.60%"},
        }
        
        data = mocks.get(symbol, {"price": 100.0, "change": 0.0, "change_percent": "0.00%"})
        return {
            "symbol": symbol,
            **data,
            "volume": 0,
            "timestamp": datetime.now().isoformat()
        }
    
    def _mock_technical(self, symbol):
        """Mock technical para testing"""
        return {
            "symbol": symbol,
            "SMA200": 150.0,
            "note": "Mock data - configure API key"
        }

def main():
    dm = DataManager()
    
    # Test
    symbols = ["AAPL", "MSFT", "NVDA"]
    
    print("📊 Datos Financieros - Test\n")
    
    for symbol in symbols:
        quote = dm.get_quote(symbol)
        print(f"{symbol}: ${quote.get('price', 'N/A')} ({quote.get('change_percent', 'N/A')})")

if __name__ == "__main__":
    main()
