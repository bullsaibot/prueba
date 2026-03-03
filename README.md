<div align="center">

# BTC Market Intelligence Pipeline

### Captura y Análisis Estadístico de Datos OHLCV en Tiempo Real

**Desarrollado por [SolutAI SAS](https://solutai.co)** — Inteligencia Artificial Aplicada a Mercados Financieros

[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![ccxt](https://img.shields.io/badge/ccxt-Latest-2ECC71?style=flat-square)](https://github.com/ccxt/ccxt)
[![pandas](https://img.shields.io/badge/pandas-Latest-150458?style=flat-square&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/Licencia-Interno%20SolutAI-red?style=flat-square)](./README.md)

</div>

---

## Propósito y Visión Técnica

Este repositorio implementa un **pipeline de inteligencia de mercados cripto** centrado en Bitcoin (BTC/USDT), diseñado como núcleo modular para análisis cuantitativos, backtesting y futuras capas de modelado predictivo.

**Objetivos estratégicos:**

- **Captura automatizada** de velas horarias (OHLCV) desde Binance vía protocolo unificado `ccxt`, eliminando dependencias de APIs propietarias.
- **Persistencia estructurada** en CSV para interoperabilidad con herramientas de análisis científico (pandas, scipy, statsmodels, sklearn).
- **Análisis estadístico descriptivo** reproducible como línea base para estudios de series temporales financieras.
- **Base escalable** hacia modelos de predicción, alertas en tiempo real y dashboards de monitoreo.

El proyecto refleja la filosofía de SolutAI SAS: **rigor científico + infraestructura liviana + resultados accionables**.

---

## Estructura del Repositorio

```
prueba/
├── src/
│   └── fetch_btc_ohlcv.py          # Script de captura OHLCV (Binance · ccxt)
├── data/
│   └── raw/
│       └── btc_ohlcv_100h.csv      # Dataset crudo — últimas 100 velas horarias
├── analysis/
│   └── btc_statistical_report.md  # Informe estadístico descriptivo
└── README.md
```

---

## Tecnologías Utilizadas

| Componente | Versión | Rol |
|---|---|---|
| **Python** | 3.12+ | Lenguaje base del pipeline |
| **ccxt** | Latest | Abstracción unificada para exchanges cripto (Binance, OKX, Bybit…) |
| **pandas** | Latest | Manipulación, transformación y análisis de DataFrames financieros |
| **Codex 5.3** | — | Asistencia en generación y revisión de código cuantitativo |
| **Claude Code 4.6** | — | Orquestación del flujo de desarrollo y documentación |

---

## Guía de Ejecución

### Requisitos previos

```bash
python --version   # Requiere Python 3.12+
```

### Instalación de dependencias

```bash
# Crear entorno virtual aislado
python -m venv .venv

# Activar entorno (Linux/macOS)
source .venv/bin/activate

# Instalar dependencias
pip install ccxt pandas
```

### Ejecutar captura de datos

```bash
python src/fetch_btc_ohlcv.py
```

**Salida esperada:**

```
Saved 100 rows to /ruta/del/proyecto/data/raw/btc_ohlcv_100h.csv
```

El script conecta con Binance (sin autenticación — datos públicos), descarga las últimas **100 velas horarias** de `BTC/USDT` y persiste el resultado en `data/raw/btc_ohlcv_100h.csv`.

### Estructura del dataset generado

| Columna | Tipo | Descripción |
|---|---|---|
| `timestamp` | `datetime64[UTC]` | Apertura de vela en UTC |
| `open` | `float64` | Precio de apertura (USDT) |
| `high` | `float64` | Precio máximo (USDT) |
| `low` | `float64` | Precio mínimo (USDT) |
| `close` | `float64` | Precio de cierre (USDT) |
| `volume` | `float64` | Volumen negociado (BTC) |

---

## Análisis Estadístico — Últimas 100 Horas de BTC

> **Período analizado:** `2026-02-27 11:00 UTC` → `2026-03-03 14:00 UTC`
> **Fuente:** Binance · par `BTC/USDT` · timeframe `1h` · 100 observaciones

### Estadísticas Descriptivas de Precio (USDT)

| Variable | Media | Mediana | Desv. Estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|---:|
| **Open** | 66,513.46 | 66,360.84 | 1,376.05 | 63,216.01 | 69,440.48 |
| **High** | 66,868.55 | 66,735.46 | 1,366.01 | 63,877.09 | 70,096.00 |
| **Low** | 66,169.14 | 66,052.78 | 1,379.16 | 63,030.00 | 69,136.36 |
| **Close** | 66,519.37 | 66,360.85 | 1,377.72 | 63,216.01 | 69,440.49 |
| **Volume** | 1,042.51 | 908.85 | 744.78 | 136.68 | 5,476.57 |

### Métricas de Actividad y Variación

| Métrica | Valor |
|---|---|
| **Volumen total negociado (100h)** | **104,251.26 BTC** |
| **Open inicial del período** | 66,604.90 USDT |
| **Close final del período** | 67,196.54 USDT |
| **Variación neta acumulada** | **+0.89%** |
| **Volatilidad intraperiodo (σ close)** | ~1,377 USDT |

### Observaciones Analíticas

- **Estacionariedad de corto plazo:** Los niveles medios de `open` y `close` (~66.5k USDT) son prácticamente idénticos, consistente con una serie de retornos centrada en cero durante el período.
- **Volatilidad moderada:** La desviación estándar (~1.37k USDT, ~2.1% del precio medio) indica un régimen de volatilidad controlada — sin eventos de ruptura significativa en las 100h analizadas.
- **Heterogeneidad de volumen:** La alta dispersión del volumen (σ = 744.78 vs μ = 1,042.51; coeficiente de variación ≈ 71%) sugiere actividad episódica con picos puntuales hasta 5,476 BTC en una sola vela — señal de participación institucional intermitente.
- **Sesgo positivo leve:** Variación neta del período de +0.89%, con distribución de retornos por vela centrada en +0.012% (media) y mediana +0.020%.

Ver el informe completo en [`analysis/btc_statistical_report.md`](analysis/btc_statistical_report.md).

---

## Roadmap

- [ ] Parametrización de símbolo, timeframe y límite vía CLI (`argparse`)
- [ ] Módulo de análisis estadístico automatizado (exporta el informe desde Python)
- [ ] Soporte multi-exchange (OKX, Bybit, Kraken)
- [ ] Scheduler para captura periódica (cron / APScheduler)
- [ ] Visualización con `matplotlib` / `plotly`

---

## Acerca de SolutAI SAS

**SolutAI SAS** es una empresa colombiana B2B especializada en inteligencia artificial aplicada. Ofrecemos servicios de agéntica con IA, investigación cuantitativa y desarrollo de soluciones de datos para industrias financieras y tecnológicas.

---

<div align="center">

*Uso interno — SolutAI SAS. Todos los derechos reservados.*

*Generado con asistencia de **Claude Code 4.6** (Anthropic) & **Codex 5.3** via ACP*

</div>
