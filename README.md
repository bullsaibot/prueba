# BTC OHLCV — Captura y Análisis Estadístico

**SolutAI SAS** · Proyecto de inteligencia de mercados cripto

---

## Descripción

Pipeline de datos que captura velas horarias de Bitcoin (BTC/USDT) desde Binance a través de la librería `ccxt`, las persiste en formato CSV y genera un informe estadístico descriptivo del período analizado.

El proyecto sirve como base para análisis cuantitativos, backtesting y modelos predictivos sobre precios de activos digitales.

---

## Estructura del repositorio

```
.
├── src/
│   └── fetch_btc_ohlcv.py      # Script de captura de datos OHLCV
├── data/
│   └── raw/
│       └── btc_ohlcv_100h.csv  # Dataset crudo (100 velas horarias)
├── analysis/
│   └── btc_statistical_report.md  # Informe estadístico descriptivo
└── README.md
```

---

## Requisitos

- Python 3.12+
- [ccxt](https://github.com/ccxt/ccxt) — acceso unificado a exchanges cripto
- [pandas](https://pandas.pydata.org/) — manipulación y análisis de datos

Instalar dependencias:

```bash
python -m venv .venv
source .venv/bin/activate
pip install ccxt pandas
```

---

## Uso

```bash
python src/fetch_btc_ohlcv.py
```

El script descarga las últimas **100 velas horarias** de `BTC/USDT` desde Binance y guarda el resultado en `data/raw/btc_ohlcv_100h.csv`.

### Columnas del dataset

| Columna     | Descripción                        |
|-------------|-------------------------------------|
| `timestamp` | Fecha/hora UTC de apertura de vela  |
| `open`      | Precio de apertura (USDT)           |
| `high`      | Precio máximo (USDT)                |
| `low`       | Precio mínimo (USDT)                |
| `close`     | Precio de cierre (USDT)             |
| `volume`    | Volumen negociado (BTC)             |

---

## Resultados del último análisis

> Período: **2026-02-27 11:00 UTC → 2026-03-03 14:00 UTC** (100 velas horarias)

### Estadísticas descriptivas de precio (USDT)

| Variable | Media      | Mediana    | Desv. std  | Mínimo     | Máximo     |
|----------|------------|------------|------------|------------|------------|
| Open     | 66,513.46  | 66,360.84  | 1,376.05   | 63,216.01  | 69,440.48  |
| High     | 66,868.55  | 66,735.46  | 1,366.01   | 63,877.09  | 70,096.00  |
| Low      | 66,169.14  | 66,052.78  | 1,379.16   | 63,030.00  | 69,136.36  |
| Close    | 66,519.37  | 66,360.85  | 1,377.72   | 63,216.01  | 69,440.49  |
| Volume   | 1,042.51   | 908.85     | 744.78     | 136.68     | 5,476.57   |

### Métricas clave

- **Volumen total negociado (100h):** 104,251.26 BTC
- **Variación neta del período:** +0.89% (de 66,604.90 a 67,196.54 USDT)
- **Volatilidad intraperiodo:** moderada (desv. std ~1.37k USDT)

Ver informe completo en [`analysis/btc_statistical_report.md`](analysis/btc_statistical_report.md).

---

## Licencia

Uso interno — SolutAI SAS. Todos los derechos reservados.
