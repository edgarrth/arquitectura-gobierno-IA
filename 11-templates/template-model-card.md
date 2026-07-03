# Template — Model Card

> Nota de datos: los ejemplos usan datos realistas de industria financiera regulada y patrones operativos típicos de banca, tarjetas, seguros y fintech. No contienen datos productivos, PII real, PAN real ni información confidencial de ninguna empresa.

# Información general

| Campo | Valor |
|---|---|
| Model ID | AI-FRD-001-FRD-XGB-3.2 |
| Nombre | Motor de fraude transaccional |
| Tipo | ML supervisado |
| Algoritmo | XGBoost |
| Owner negocio | Fraude |
| Owner técnico | Data Science |
| Tier | Tier 1 |
| Estado | Productivo |

# Propósito

Detectar transacciones potencialmente fraudulentas en POS, ecommerce y card-not-present.

# Uso permitido

- Scoring transaccional
- Priorización de revisión manual
- Bloqueo temporal con reglas aprobadas
- Alertas de fraude

# Uso no permitido

- Decisiones irrevocables sin apelación
- Uso para scoring crediticio
- Uso con datos no aprobados
- Uso fuera de jurisdicciones aprobadas

# Datos de entrenamiento

| Campo | Valor |
|---|---|
| Dataset ID | DS-CARD-TRX-2024-2025-v17 |
| Periodo | 2024-01 a 2025-12 |
| Registros | 86,000,000 |
| Positivos fraude | 248,400 |
| Ratio fraude | 0.288% |
| PII | Tokenizada |
| PAN | No usado |

# Variables

| Feature | Tipo | Descripción | Sensibilidad |
|---|---|---|---|
| amount_pen | numérica | Monto | Baja |
| mcc | categórica | Merchant Category Code | Media |
| merchant_risk_score | numérica | Riesgo comercio | Media |
| device_risk_score | numérica | Riesgo dispositivo | Alta |
| velocity_5m | numérica | Conteo 5 minutos | Media |
| geo_distance_km | numérica | Distancia anómala | Media |

# Performance

| Métrica | Valor |
|---|---:|
| AUC | 0.971 |
| Precision | 0.947 |
| Recall | 0.892 |
| F1 | 0.918 |
| FPR | 1.7% |
| Latency P95 | 28ms |

# Fairness

| Segmento | Recall | FPR |
|---|---:|---:|
| Lima | 0.895 | 1.6% |
| Provincias | 0.846 | 2.1% |
| Tarjeta premium | 0.921 | 1.3% |
| Tarjeta clásica | 0.884 | 1.9% |
| Cliente nuevo | 0.836 | 2.4% |

# Explainability

```json
{
  "trx_id": "TRX-9382821",
  "score": 0.91,
  "top_reasons": [
    "Monto 4.3x superior al promedio del cliente",
    "Comercio con riesgo histórico alto",
    "Dispositivo no usado previamente",
    "Alta velocidad en 5 minutos"
  ]
}
```

# Monitoreo

| Métrica | Umbral |
|---|---|
| PSI feature crítica | >0.25 |
| Recall drop | >5 pp |
| FPR increase | >1 pp |
| Latency P95 | >50ms |
| Missing features | >1% |
