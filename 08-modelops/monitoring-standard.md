# Estándar de Monitoreo de IA

# Propósito

Definir monitoreo operacional, estadístico, ético y de seguridad para modelos ML, LLMs, RAG y agentes.

# Capas de monitoreo

| Capa | Métricas |
|---|---|
| plataforma | latencia, errores, disponibilidad |
| datos | drift, calidad, missing values |
| modelo | precisión, recall, calibración |
| GenAI | groundedness, hallucination, toxicidad |
| seguridad | prompt injection, PII leakage, tool abuse |
| negocio | ahorro, conversión, fraude evitado |

# Ejemplo realista

```json
{
  "model_id": "FRD-XGB-TRANSACTION-v3.2",
  "window": "2025-10-01/2025-10-07",
  "precision": 0.941,
  "recall": 0.887,
  "psi_amount": 0.18,
  "p95_latency_ms": 31,
  "false_positive_rate": 0.016,
  "alerts": ["data_drift_warning"]
}
```

# Umbrales mínimos

| Métrica | Warning | Critical |
|---|---:|---:|
| PSI | > 0.10 | > 0.25 |
| caída de recall | > 3 pp | > 7 pp |
| latencia p95 | > SLA | > 2x SLA |
| hallucination rate | > 3% | > 8% |
| PII leakage | > 0 | > 0 |

# Acciones

- Warning: análisis y plan de remediación.
- Critical: comité operativo, rollback o retraining según impacto.
