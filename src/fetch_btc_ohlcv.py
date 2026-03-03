import ccxt
import pandas as pd
import os
from datetime import datetime, timedelta

def fetch_data():
    exchange = ccxt.binance()
    symbol = 'BTC/USDT'
    timeframe = '1h'
    limit = 100
    
    print(f"Bullsy ♉: Conectando a Binance para extraer {limit} horas de {symbol}...")
    
    try:
        # Fetch OHLCV
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
        
        # Convert to DataFrame
        df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        
        # Save path
        output_dir = 'data/raw'
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, 'btc_ohlcv_100h.csv')
        
        df.to_csv(output_file, index=False)
        print(f"✅ Bullsy ♉: Datos guardados con éxito en {output_file}")
        print(df.tail())
        
    except Exception as e:
        print(f"❌ Error en la captura de datos: {e}")

if __name__ == "__main__":
    fetch_data()
