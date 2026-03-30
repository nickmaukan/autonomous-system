#!/usr/bin/env python3
"""
Academia de Inversores - Replicación de Metodología de Análisis
================================================================
Script que replica el análisis híbrido (técnico + fundamental) del canal
Academia de Inversores para un conjunto de acciones.

Uso:
    python3 academia_analyzer.py AAPL MSFT NVDA V
    python3 academia_analyzer.py --watchlist tech_giants
    python3 academia_analyzer.py --all

Autor: Aurus ⚡ para Mauri
Fecha: 2026-03-22
"""

import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime
import json
import sys
import os
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# CONFIGURACIÓN
# ============================================================================

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "..", "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

CONFIG = {
    "period_technical": "1y",
    "rsi_oversold": 30,
    "rsi_overbought": 70,
    "williams_oversold": -80,
    "adx_strong_trend": 25,
}

FUNDAMENTAL_THRESHOLDS = {
    "pe_max": 35,
    "current_ratio_min": 1.0,
    "current_ratio_max": 3.0,
    "debt_ratio_max": 0.6,
    "payout_ratio_max": 0.5,
    "roic_min": 0.10,
    "roe_min": 0.10,
}

WATCHLISTS = {
    "tech_giants": ["AAPL", "MSFT", "GOOGL", "AMZN", "META", "NVDA"],
    "fintech": ["V", "MA", "PYPL", "SQ", "ADP"],
    "semiconductors": ["NVDA", "AMD", "INTC", "TSM", "QCOM", "ASML"],
    "retail_growth": ["AMZN", "MELI", "LULU", "NKE", "COST"],
    "dividend_kings": ["KO", "PG", "JNJ", "PEP", "VZ", "T"],
    "academia_picks": ["MSFT", "V", "ADP", "LULU", "NVDA", "META", "AMZN", "SAP", "RACE"],
    "europe_tech": ["SAP", "ASML", "NESN", "BHVN", "RACE"],
    "latam_tech": ["MELI", "NU", "VIST", "PagSeguro", "StoneCo"],
}


# ============================================================================
# MÓDULO 1: ANÁLISIS TÉCNICO
# ============================================================================

def calculate_rsi(prices, period=14):
    delta = prices.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calculate_macd(prices, fast=12, slow=26, signal=9):
    exp1 = prices.ewm(span=fast, adjust=False).mean()
    exp2 = prices.ewm(span=slow, adjust=False).mean()
    macd = exp1 - exp2
    signal_line = macd.ewm(span=signal, adjust=False).mean()
    histogram = macd - signal_line
    return macd, signal_line, histogram

def calculate_bollinger_bands(prices, period=20, std_dev=2):
    sma = prices.rolling(window=period).mean()
    std = prices.rolling(window=period).std()
    upper_band = sma + (std * std_dev)
    lower_band = sma - (std * std_dev)
    return upper_band, sma, lower_band

def calculate_atr(high, low, close, period=14):
    high_low = high - low
    high_close = np.abs(high - close.shift())
    low_close = np.abs(low - close.shift())
    true_range = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
    atr = true_range.rolling(window=period).mean()
    return atr

def calculate_adx(high, low, close, period=14):
    plus_dm = high.diff()
    minus_dm = -low.diff()
    plus_dm[plus_dm < 0] = 0
    minus_dm[minus_dm < 0] = 0
    tr = calculate_atr(high, low, close, period)
    plus_di = 100 * (plus_dm.ewm(alpha=1/period).mean() / tr)
    minus_di = 100 * (minus_dm.ewm(alpha=1/period).mean() / tr)
    dx = 100 * np.abs(plus_di - minus_di) / (plus_di + minus_di)
    adx = dx.ewm(alpha=1/period).mean()
    return adx, plus_di, minus_di

def get_52_week_position(current_price, high_52w, low_52w):
    if high_52w == low_52w:
        return 50
    position = ((current_price - low_52w) / (high_52w - low_52w)) * 100
    return round(position, 1)

def analyze_technical(ticker_symbol):
    result = {
        "ticker": ticker_symbol,
        "timestamp": datetime.now().isoformat(),
        "price_current": None,
        "price_change_pct": None,
        "indicators": {},
        "signals": [],
        "summary": {}
    }
    
    try:
        ticker = yf.Ticker(ticker_symbol)
        data = ticker.history(period=CONFIG["period_technical"])
        
        if data is None or len(data) < 50:
            result["error"] = "Datos insuficientes"
            return result
        
        close = data['Close'].dropna()
        high = data['High'].dropna()
        low = data['Low'].dropna()
        volume = data['Volume'].dropna()
        
        result["price_current"] = round(close.iloc[-1], 2)
        month_start = close.iloc[-21] if len(close) > 21 else close.iloc[0]
        result["price_change_pct"] = round(((close.iloc[-1] - month_start) / month_start) * 100, 2)
        
        # RSI
        rsi = calculate_rsi(close, 14)
        result["indicators"]["rsi"] = {
            "value": round(rsi.iloc[-1], 2),
            "signal": "oversold" if rsi.iloc[-1] < CONFIG["rsi_oversold"] 
                      else "overbought" if rsi.iloc[-1] > CONFIG["rsi_overbought"] 
                      else "neutral"
        }
        
        if rsi.iloc[-1] < 30:
            result["indicators"]["rsi"]["interpretation"] = "⚠️ SOBREVENTA"
            result["signals"].append({"indicator": "RSI", "signal": "BUY", "strength": "STRONG"})
        elif rsi.iloc[-1] > 70:
            result["indicators"]["rsi"]["interpretation"] = "⚠️ SOBRECOMPRA"
            result["signals"].append({"indicator": "RSI", "signal": "SELL", "strength": "STRONG"})
        else:
            result["indicators"]["rsi"]["interpretation"] = "✅ Neutral"
            result["signals"].append({"indicator": "RSI", "signal": "NEUTRAL", "strength": "WEAK"})
        
        # MACD
        macd, signal_line, histogram = calculate_macd(close)
        result["indicators"]["macd"] = {
            "macd_value": round(macd.iloc[-1], 4),
            "signal_value": round(signal_line.iloc[-1], 4),
            "histogram": round(histogram.iloc[-1], 4),
            "crossover": "BULLISH" if macd.iloc[-1] > signal_line.iloc[-1] and macd.iloc[-2] <= signal_line.iloc[-2]
                         else "BEARISH" if macd.iloc[-1] < signal_line.iloc[-1] and macd.iloc[-2] >= signal_line.iloc[-2]
                         else "NEUTRAL"
        }
        
        if result["indicators"]["macd"]["crossover"] == "BULLISH":
            result["signals"].append({"indicator": "MACD", "signal": "BUY", "strength": "MEDIUM"})
        elif result["indicators"]["macd"]["crossover"] == "BEARISH":
            result["signals"].append({"indicator": "MACD", "signal": "SELL", "strength": "MEDIUM"})
        
        # Williams %R
        highest_high = high.rolling(window=14).max()
        lowest_low = low.rolling(window=14).min()
        williams_r = -100 * (highest_high - close) / (highest_high - lowest_low)
        result["indicators"]["williams_r"] = {
            "value": round(williams_r.iloc[-1], 2),
            "signal": "oversold" if williams_r.iloc[-1] < CONFIG["williams_oversold"] else "neutral"
        }
        
        if williams_r.iloc[-1] < -80:
            result["signals"].append({"indicator": "Williams %R", "signal": "BUY", "strength": "STRONG"})
        
        # ADX
        adx, plus_di, minus_di = calculate_adx(high, low, close)
        result["indicators"]["adx"] = {
            "value": round(adx.iloc[-1], 2),
            "plus_di": round(plus_di.iloc[-1], 2),
            "minus_di": round(minus_di.iloc[-1], 2),
            "trend_strength": "STRONG" if adx.iloc[-1] > CONFIG["adx_strong_trend"] else "WEAK"
        }
        
        if adx.iloc[-1] > 25:
            trend_direction = "BULLISH" if plus_di.iloc[-1] > minus_di.iloc[-1] else "BEARISH"
            result["indicators"]["adx"]["interpretation"] = f"📈 Tendencia {trend_direction} FUERTE"
        
        # Medias Móviles
        ma20 = close.rolling(window=20).mean().iloc[-1]
        ma50 = close.rolling(window=50).mean().iloc[-1]
        ma200 = close.rolling(window=200).mean().iloc[-1] if len(close) >= 200 else None
        current_price = close.iloc[-1]
        
        result["indicators"]["moving_averages"] = {
            "MA20": round(ma20, 2),
            "MA50": round(ma50, 2),
            "MA200": round(ma200, 2) if ma200 else None,
            "price_vs_ma20_pct": round(((current_price - ma20) / ma20) * 100, 2),
            "price_vs_ma50_pct": round(((current_price - ma50) / ma50) * 100, 2),
        }
        
        if ma200:
            result["indicators"]["moving_averages"]["price_vs_ma200_pct"] = round(((current_price - ma200) / ma200) * 100, 2)
        
        # 52 semanas
        high_52w = high.rolling(window=252).max().iloc[-1]
        low_52w = low.rolling(window=252).min().iloc[-1]
        result["indicators"]["52_week_range"] = {
            "high_52w": round(high_52w, 2),
            "low_52w": round(low_52w, 2),
            "current_position_pct": get_52_week_position(current_price, high_52w, low_52w),
            "distance_from_high_pct": round(((high_52w - current_price) / high_52w) * 100, 2),
        }
        
        # Bollinger Bands
        upper_bb, middle_bb, lower_bb = calculate_bollinger_bands(close)
        result["indicators"]["bollinger_bands"] = {
            "upper": round(upper_bb.iloc[-1], 2),
            "middle": round(middle_bb.iloc[-1], 2),
            "lower": round(lower_bb.iloc[-1], 2),
        }
        
        if current_price < lower_bb.iloc[-1]:
            result["signals"].append({"indicator": "Bollinger", "signal": "BUY", "strength": "MEDIUM"})
        elif current_price > upper_bb.iloc[-1]:
            result["signals"].append({"indicator": "Bollinger", "signal": "SELL", "strength": "MEDIUM"})
        
        # ATR
        atr = calculate_atr(high, low, close)
        result["indicators"]["atr"] = {
            "value": round(atr.iloc[-1], 2),
            "atr_pct": round((atr.iloc[-1] / current_price) * 100, 2)
        }
        
        # Resumen
        buy_signals = len([s for s in result["signals"] if s["signal"] == "BUY"])
        sell_signals = len([s for s in result["signals"] if s["signal"] == "SELL"])
        
        if buy_signals >= 3:
            result["summary"]["technical_signal"] = "📈 COMPRAR"
            result["summary"]["technical_strength"] = "STRONG_BUY" if buy_signals >= 4 else "BUY"
        elif buy_signals >= 2:
            result["summary"]["technical_signal"] = "📊 COMPRAR CON PRECAUCIÓN"
            result["summary"]["technical_strength"] = "WEAK_BUY"
        elif sell_signals >= 3:
            result["summary"]["technical_signal"] = "📉 VENDER"
            result["summary"]["technical_strength"] = "STRONG_SELL" if sell_signals >= 4 else "SELL"
        elif sell_signals >= 2:
            result["summary"]["technical_signal"] = "⚠️ VENDER CON PRECAUCIÓN"
            result["summary"]["technical_strength"] = "WEAK_SELL"
        else:
            result["summary"]["technical_signal"] = "⚖️ NEUTRAL"
            result["summary"]["technical_strength"] = "NEUTRAL"
        
        result["summary"]["buy_signals"] = buy_signals
        result["summary"]["sell_signals"] = sell_signals
        
    except Exception as e:
        result["error"] = str(e)
    
    return result


# ============================================================================
# MÓDULO 2: ANÁLISIS FUNDAMENTAL
# ============================================================================

def analyze_fundamental(ticker_symbol):
    result = {
        "ticker": ticker_symbol,
        "timestamp": datetime.now().isoformat(),
        "scores": [],
        "ratios": {},
        "growth": {},
        "dividends": {},
        "summary": {}
    }
    
    try:
        ticker = yf.Ticker(ticker_symbol)
        info = ticker.info
        
        if not info or info.get('regularMarketPrice') is None:
            result["error"] = "Sin datos fundamentales"
            return result
        
        # P/E
        pe_ratio = info.get('trailingPE')
        if pe_ratio and pe_ratio > 0:
            result["ratios"]["pe"] = {"value": round(pe_ratio, 2), "score": "UP" if pe_ratio < 35 else "DOWN"}
            result["scores"].append(result["ratios"]["pe"]["score"])
        
        # P/B
        pb_ratio = info.get('priceToBook')
        if pb_ratio and pb_ratio > 0:
            result["ratios"]["pb"] = {"value": round(pb_ratio, 2), "score": "UP" if pb_ratio < 5 else "DOWN"}
            result["scores"].append(result["ratios"]["pb"]["score"])
        
        # P/S
        ps_ratio = info.get('priceToSalesTrailing12Months')
        if ps_ratio and ps_ratio > 0:
            result["ratios"]["ps"] = {"value": round(ps_ratio, 2), "score": "UP" if ps_ratio < 10 else "DOWN"}
            result["scores"].append(result["ratios"]["ps"]["score"])
        
        # Current Ratio
        current_ratio = info.get('currentRatio')
        if current_ratio and current_ratio > 0:
            result["ratios"]["current_ratio"] = {"value": round(current_ratio, 2), "score": "UP" if 1.0 <= current_ratio <= 3.0 else "DOWN"}
            result["scores"].append(result["ratios"]["current_ratio"]["score"])
        
        # Debt/Equity
        debt_equity = info.get('debtToEquity')
        if debt_equity and debt_equity > 0:
            result["ratios"]["debt_equity"] = {"value": round(debt_equity, 2), "score": "UP" if debt_equity < 2.0 else "DOWN"}
            result["scores"].append(result["ratios"]["debt_equity"]["score"])
        
        # ROE
        roe = info.get('returnOnEquity')
        if roe and roe > 0:
            result["ratios"]["roe"] = {"value": round(roe * 100, 2), "score": "UP" if roe > 0.10 else "DOWN"}
            result["scores"].append(result["ratios"]["roe"]["score"])
        
        # ROA
        roa = info.get('returnOnAssets')
        if roa and roa > 0:
            result["ratios"]["roa"] = {"value": round(roa * 100, 2), "score": "UP" if roa > 0.05 else "DOWN"}
            result["scores"].append(result["ratios"]["roa"]["score"])
        
        # Gross Margin
        gross_margin = info.get('grossMargins')
        if gross_margin and gross_margin > 0:
            result["ratios"]["gross_margin"] = {"value": round(gross_margin * 100, 2), "score": "UP" if gross_margin > 0.30 else "DOWN"}
            result["scores"].append(result["ratios"]["gross_margin"]["score"])
        
        # Operating Margin
        op_margin = info.get('operatingMargins')
        if op_margin and op_margin > 0:
            result["ratios"]["operating_margin"] = {"value": round(op_margin * 100, 2), "score": "UP" if op_margin > 0.15 else "DOWN"}
            result["scores"].append(result["ratios"]["operating_margin"]["score"])
        
        # Net Margin
        net_margin = info.get('profitMargins')
        if net_margin and net_margin > 0:
            result["ratios"]["net_margin"] = {"value": round(net_margin * 100, 2), "score": "UP" if net_margin > 0.10 else "DOWN"}
            result["scores"].append(result["ratios"]["net_margin"]["score"])
        
        # Revenue Growth
        revenue_growth = info.get('revenueGrowth')
        if revenue_growth is not None:
            result["growth"]["revenue_growth"] = {"value": round(revenue_growth * 100, 2), "score": "UP" if revenue_growth > 0 else "DOWN"}
            result["scores"].append(result["growth"]["revenue_growth"]["score"])
        
        # Earnings Growth
        earnings_growth = info.get('earningsGrowth')
        if earnings_growth is not None:
            result["growth"]["earnings_growth"] = {"value": round(earnings_growth * 100, 2), "score": "UP" if earnings_growth > 0 else "DOWN"}
            result["scores"].append(result["growth"]["earnings_growth"]["score"])
        
        # Dividend Yield
        dividend_yield = info.get('dividendYield')
        if dividend_yield and dividend_yield > 0:
            result["dividends"]["yield"] = {"value": round(dividend_yield * 100, 2)}
        
        # Payout Ratio
        payout_ratio = info.get('payoutRatio')
        if payout_ratio and payout_ratio > 0:
            result["dividends"]["payout_ratio"] = {"value": round(payout_ratio * 100, 2), "score": "UP" if payout_ratio < 0.5 else "DOWN"}
            result["scores"].append(result["dividends"]["payout_ratio"]["score"])
        
        # Resumen
        if result["scores"]:
            up_count = result["scores"].count("UP")
            total = len(result["scores"])
            up_pct = (up_count / total) * 100
            
            result["summary"]["scores_up"] = up_count
            result["summary"]["scores_total"] = total
            result["summary"]["health_pct"] = round(up_pct, 1)
            
            if up_pct >= 75:
                result["summary"]["fundamental_signal"] = "✅ FUERTE"
                result["summary"]["fundamental_score"] = "STRONG_BUY"
            elif up_pct >= 60:
                result["summary"]["fundamental_signal"] = "✅ BUENO"
                result["summary"]["fundamental_score"] = "BUY"
            elif up_pct >= 40:
                result["summary"]["fundamental_signal"] = "⚠️ MIXTO"
                result["summary"]["fundamental_score"] = "NEUTRAL"
            elif up_pct >= 25:
                result["summary"]["fundamental_signal"] = "❌ DÉBIL"
                result["summary"]["fundamental_score"] = "SELL"
            else:
                result["summary"]["fundamental_signal"] = "❌ MUY DÉBIL"
                result["summary"]["fundamental_score"] = "STRONG_SELL"
    
    except Exception as e:
        result["error"] = str(e)
    
    return result


# ============================================================================
# MÓDULO 3: SCORING COMBINADO
# ============================================================================

def combined_analysis(technical, fundamental):
    result = {
        "ticker": technical.get("ticker"),
        "timestamp": datetime.now().isoformat(),
        "recommendation": None,
        "conviction": None,
        "scores": {},
        "verdict": None,
        "thesis_bull": [],
        "thesis_bear": [],
        "actions": []
    }
    
    tech_score = technical.get("summary", {}).get("technical_strength", "NEUTRAL")
    fund_score = fundamental.get("summary", {}).get("fundamental_score", "NEUTRAL")
    
    result["scores"]["technical"] = tech_score
    result["scores"]["fundamental"] = fund_score
    
    def score_to_num(s):
        return {"STRONG_BUY": 2, "BUY": 1, "WEAK_BUY": 0.5, "NEUTRAL": 0, "WEAK_SELL": -0.5, "SELL": -1, "STRONG_SELL": -2}.get(s, 0)
    
    tech_num = score_to_num(tech_score)
    fund_num = score_to_num(fund_score)
    combined = (tech_num * 0.4) + (fund_num * 0.6)
    
    result["scores"]["combined"] = round(combined, 2)
    
    if combined >= 1.5:
        result["recommendation"] = "📈 COMPRAR"
        result["conviction"] = "ALTA"
    elif combined >= 0.5:
        result["recommendation"] = "📊 COMPRAR CON PRECAUCIÓN"
        result["conviction"] = "MEDIA"
    elif combined >= -0.5:
        result["recommendation"] = "⚖️ MANTENER / NEUTRAL"
        result["conviction"] = "BAJA"
    elif combined >= -1.5:
        result["recommendation"] = "⚠️ VENDER PARCIAL"
        result["conviction"] = "MEDIA"
    else:
        result["recommendation"] = "📉 VENDER"
        result["conviction"] = "ALTA"
    
    price = technical.get("price_current")
    rsi_val = technical.get("indicators", {}).get("rsi", {}).get("value")
    pos_52w = technical.get("indicators", {}).get("52_week_range", {}).get("current_position_pct")
    
    result["verdict"] = f"${price}" if price else "N/A"
    if rsi_val:
        result["verdict"] += f" | RSI: {rsi_val}"
    if pos_52w:
        result["verdict"] += f" | 52W: {pos_52w}%"
    
    if tech_score in ["STRONG_BUY", "BUY"]:
        result["thesis_bull"].append("Señales técnicas alcistas")
    if fund_score in ["STRONG_BUY", "BUY"]:
        result["thesis_bull"].append("Fundamentales sólidos")
    if rsi_val and rsi_val < 35:
        result["thesis_bull"].append("RSI en zona de oportunidad")
    
    if tech_score in ["WEAK_SELL", "SELL", "STRONG_SELL"]:
        result["thesis_bear"].append("Señales técnicas bajistas")
    if fund_score in ["WEAK_SELL", "SELL", "STRONG_SELL"]:
        result["thesis_bear"].append("Fundamentales débiles")
    if rsi_val and rsi_val > 65:
        result["thesis_bear"].append("RSI en zona de sobrecompra")
    
    if combined >= 1.0:
        result["actions"] = ["✅ ZONA DE COMPRA", "💰 Considerar entrada progresiva"]
    elif combined >= 0.3:
        result["actions"] = ["⚠️ MANTENER, no agregar"]
    elif combined >= -0.3:
        result["actions"] = ["⚖️ NEUTRAL - Esperar"]
    elif combined >= -1.0:
        result["actions"] = ["📤 Considerar tomar beneficios"]
    else:
        result["actions"] = ["🚨 ZONA DE VENTA", "❌ Evitar nuevas posiciones"]
    
    return result


# ============================================================================
# REPORTES
# ============================================================================

def print_report(ticker, technical, fundamental, combined):
    print("\n" + "=" * 80)
    print(f"📊 ANÁLISIS: {ticker}")
    print("=" * 80)
    
    print(f"\n🎯 {combined['recommendation']} (Convicción {combined['conviction']})")
    print(f"   {combined['verdict']}")
    print(f"   Técnico: {combined['scores']['technical']} | Fundamental: {combined['scores']['fundamental']}")
    
    if "error" not in technical:
        print("\n📈 TÉCNICO")
        rsi = technical.get("indicators", {}).get("rsi", {})
        print(f"   RSI(14): {rsi.get('value', 'N/A')} - {rsi.get('interpretation', '')}")
        
        macd = technical.get("indicators", {}).get("macd", {})
        print(f"   MACD: {macd.get('crossover', 'N/A')}")
        
        adx = technical.get("indicators", {}).get("adx", {})
        print(f"   ADX: {adx.get('value', 'N/A')} - {adx.get('interpretation', 'N/A')}")
        
        ma = technical.get("indicators", {}).get("moving_averages", {})
        print(f"   MA20: ${ma.get('MA20', 'N/A')} | MA50: ${ma.get('MA50', 'N/A')}")
        
        range_52w = technical.get("indicators", {}).get("52_week_range", {})
        print(f"   52W: ${range_52w.get('low_52w', 'N/A')} - ${range_52w.get('high_52w', 'N/A')}")
        print(f"   Posición 52W: {range_52w.get('current_position_pct', 'N/A')}%")
        
        sigs = technical.get("summary", {})
        print(f"   ➤ {sigs.get('technical_signal', 'N/A')}")
    else:
        print(f"\n   Error técnico: {technical.get('error')}")
    
    if "error" not in fundamental:
        print("\n💼 FUNDAMENTAL")
        ratios = fundamental.get("ratios", {})
        
        if ratios.get("pe"):
            print(f"   P/E: {ratios['pe']['value']} ({ratios['pe']['score']})")
        if ratios.get("roe"):
            print(f"   ROE: {ratios['roe']['value']}% ({ratios['roe']['score']})")
        if ratios.get("debt_equity"):
            print(f"   D/E: {ratios['debt_equity']['value']} ({ratios['debt_equity']['score']})")
        
        growth = fundamental.get("growth", {})
        if growth.get("revenue_growth"):
            print(f"   Crec. Ingresos: {growth['revenue_growth']['value']}%")
        
        dividends = fundamental.get("dividends", {})
        if dividends.get("yield"):
            print(f"   Dividendo: {dividends['yield']['value']}%")
        
        summary = fundamental.get("summary", {})
        print(f"   Score: {summary.get('scores_up', 0)}/{summary.get('scores_total', 0)} UP")
        print(f"   ➤ {summary.get('fundamental_signal', 'N/A')}")
    else:
        print(f"\n   Error fundamental: {fundamental.get('error')}")
    
    if combined.get("thesis_bull"):
        print("\n   ✅ Bulls:")
        for b in combined["thesis_bull"]:
            print(f"      • {b}")
    
    if combined.get("thesis_bear"):
        print("\n   ❌ Bears:")
        for b in combined["thesis_bear"]:
            print(f"      • {b}")
    
    if combined.get("actions"):
        print("\n   💡 ACCIONES:")
        for a in combined["actions"]:
            print(f"      {a}")


def save_json(ticker, technical, fundamental, combined):
    report = {"ticker": ticker, "generated_at": datetime.now().isoformat(), "technical": technical, "fundamental": fundamental, "combined": combined}
    filename = os.path.join(OUTPUT_DIR, f"{ticker}_analysis.json")
    with open(filename, 'w') as f:
        json.dump(report, f, indent=2, default=str)
    return filename


def save_summary_csv(results):
    rows = []
    for r in results:
        t = r["technical"]
        c = r["combined"]
        rows.append({
            "Ticker": r["ticker"],
            "Precio": t.get("price_current", "N/A"),
            "RSI": t.get("indicators", {}).get("rsi", {}).get("value", "N/A"),
            "52W_Pos": t.get("indicators", {}).get("52_week_range", {}).get("current_position_pct", "N/A"),
            "Técnico": c["scores"]["technical"],
            "Fundamental": c["scores"]["fundamental"],
            "Score": c["scores"]["combined"],
            "Recomendación": c["recommendation"],
            "Convicción": c["conviction"],
        })
    
    df = pd.DataFrame(rows)
    filename = os.path.join(OUTPUT_DIR, "summary_analysis.csv")
    df.to_csv(filename, index=False)
    return filename


# ============================================================================
# MAIN
# ============================================================================

def analyze_tickers(tickers):
    print(f"\n🔍 Analizando {len(tickers)} acciones...")
    results = []
    
    for i, ticker in enumerate(tickers, 1):
        print(f"\n[{i}/{len(tickers)}] {ticker}...", end=" ", flush=True)
        
        technical = analyze_technical(ticker)
        fundamental = analyze_fundamental(ticker)
        
        if "error" not in technical:
            print(f"${technical.get('price_current')}", end=" | ", flush=True)
        else:
            print(f"Error técnico", end=" | ", flush=True)
        
        if "error" not in fundamental:
            health = fundamental.get("summary", {}).get("health_pct", "N/A")
            print(f"F={health}%", end="", flush=True)
        else:
            print(f"Error fundamental", end="", flush=True)
        
        combined = combined_analysis(technical, fundamental)
        print(f" => {combined.get('recommendation', 'N/A')}")
        
        save_json(ticker, technical, fundamental, combined)
        print_report(ticker, technical, fundamental, combined)
        
        results.append({"ticker": ticker, "technical": technical, "fundamental": fundamental, "combined": combined})
    
    if results:
        csv_file = save_summary_csv(results)
        print(f"\n\n💾 Resumen CSV: {csv_file}")
    
    print("\n" + "=" * 80)
    print("📊 RANKING DE OPORTUNIDADES")
    print("=" * 80)
    print(f"{'Ticker':<8} {'Precio':>10} {'RSI':>6} {'52W%':>6} {'Score':>6} {'Recomendación':<25}")
    print("-" * 80)
    
    for r in sorted(results, key=lambda x: x["combined"].get("scores", {}).get("combined", 0), reverse=True):
        t = r["technical"]
        c = r["combined"]
        price = f"${t.get('price_current', 'N/A')}" if t.get('price_current') else "N/A"
        rsi = t.get("indicators", {}).get("rsi", {}).get("value", "N/A")
        pos_52w = t.get("indicators", {}).get("52_week_range", {}).get("current_position_pct", "N/A")
        score = c.get("scores", {}).get("combined", 0)
        rec = c.get("recommendation", "N/A")
        print(f"{r['ticker']:<8} {price:>10} {rsi:>6} {pos_52w:>6} {score:>6.1f} {rec:<25}")
    
    return results


def main():
    print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║       ACADEMIA DE INVERSORES - SISTEMA DE ANÁLISIS REPLICADO ⚡           ║
║                                                                              ║
║  Metodología: Técnico (RSI, MACD, ADX, MAs) + Fundamental (ratios)        ║
║  Score combinado: 40% Técnico + 60% Fundamental                             ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """)
    
    if len(sys.argv) < 2:
        print("❌ Uso: python3 academia_analyzer.py AAPL MSFT NVDA V")
        print("\nWatchlists: --watchlist <nombre>")
        for name in WATCHLISTS.keys():
            print(f"  --watchlist {name}")
        print("\nEjemplo: python3 academia_analyzer.py --watchlist academia_picks")
        sys.exit(1)
    
    tickers = []
    
    if sys.argv[1] == "--watchlist" and len(sys.argv) >= 3:
        list_name = sys.argv[2]
        if list_name in WATCHLISTS:
            tickers = WATCHLISTS[list_name]
            print(f"📋 Watchlist: {list_name} => {', '.join(tickers)}")
        else:
            print(f"❌ Watchlist '{list_name}' no encontrada")
            sys.exit(1)
    elif sys.argv[1] == "--all":
        all_tickers = set()
        for wl in WATCHLISTS.values():
            all_tickers.update(wl)
        tickers = sorted(list(all_tickers))
        print(f"📋 Todas las watchlists: {len(tickers)} acciones")
    else:
        tickers = [arg.upper() for arg in sys.argv[1:] if not arg.startswith("--")]
    
    if not tickers:
        print("❌ No se especificaron tickers")
        sys.exit(1)
    
    analyze_tickers(tickers)


if __name__ == "__main__":
    main()
