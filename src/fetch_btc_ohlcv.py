from pathlib import Path

import ccxt
import pandas as pd


def main() -> None:
    exchange = ccxt.binance()
    symbol = "BTC/USDT"
    timeframe = "1h"
    limit = 100

    ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)

    df = pd.DataFrame(
        ohlcv,
        columns=["timestamp", "open", "high", "low", "close", "volume"],
    )
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms", utc=True)

    repo_root = Path(__file__).resolve().parents[1]
    output_path = repo_root / "data" / "raw" / "btc_ohlcv_100h.csv"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(output_path, index=False)
    print(f"Saved {len(df)} rows to {output_path}")


if __name__ == "__main__":
    main()
