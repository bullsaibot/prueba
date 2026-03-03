# Informe Estadístico BTC OHLCV (Últimas 100 Horas)

## Resumen del dataset
- **Archivo fuente:** `data/raw/btc_ohlcv_100h.csv`
- **Número de observaciones:** 100 velas horarias
- **Rango temporal (UTC):** 2026-02-27 11:00:00+00:00 a 2026-03-03 14:00:00+00:00

## Estadísticas descriptivas

| Variable | Media | Mediana | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|---:|
| Open | 66,513.46 | 66,360.84 | 1,376.05 | 63,216.01 | 69,440.48 |
| High | 66,868.55 | 66,735.46 | 1,366.01 | 63,877.09 | 70,096.00 |
| Low | 66,169.14 | 66,052.78 | 1,379.16 | 63,030.00 | 69,136.36 |
| Close | 66,519.37 | 66,360.85 | 1,377.72 | 63,216.01 | 69,440.49 |
| Volume | 1,042.51 | 908.85 | 744.78 | 136.68 | 5,476.57 |

## Volumen acumulado
- **Volumen total negociado (100h):** **104,251.25653 BTC**

## Variación porcentual del precio (Open -> Close)

### Distribución por vela (100 observaciones)
- **Media:** 0.0118%
- **Mediana:** 0.0199%
- **Desv. estándar:** 0.7695%
- **Mínimo:** -3.6210%
- **Máximo:** 2.9075%

### Variación neta del periodo completo
- **Open inicial:** 66,604.90
- **Close final:** 67,196.54
- **Variación neta (100h):** **+0.8883%**

## Observaciones rápidas
- Los precios `open` y `close` presentan un nivel medio muy similar (~66.5k), consistente con una serie relativamente estacionaria en el corto plazo.
- La dispersión de precios (desviación estándar ~1.37k) indica volatilidad intraperiodo moderada.
- El volumen presenta alta heterogeneidad (desv. estándar 744.78 vs media 1,042.51), con picos puntuales de actividad.
