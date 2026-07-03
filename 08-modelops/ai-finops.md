# AI FinOps

# Propósito

Controlar costos de inferencia, entrenamiento, embeddings, almacenamiento vectorial, GPUs, APIs externas y observabilidad de IA.

# Categorías de costo

| Categoría | Ejemplo |
|---|---|
| inferencia LLM | tokens input/output |
| embeddings | indexación documental |
| vector store | almacenamiento y consultas |
| entrenamiento | GPU/CPU |
| monitoreo | trazas, logs, evaluaciones |
| red team/evals | pruebas automatizadas |

# Métricas

| Métrica | Fórmula |
|---|---|
| cost_per_case | costo total / casos atendidos |
| cost_per_success | costo / casos útiles |
| token_waste_rate | tokens descartados / tokens totales |
| cache_hit_rate | respuestas cacheadas / solicitudes |

# Ejemplo realista

```json
{
  "service": "claims-copilot",
  "month": "2025-10",
  "input_tokens": 921000000,
  "output_tokens": 184000000,
  "embedding_cost_usd": 860,
  "inference_cost_usd": 14820,
  "vector_store_cost_usd": 1190,
  "cost_per_interaction_usd": 0.014,
  "estimated_agent_time_saved_hours": 4200
}
```

# Controles

- cuotas por aplicación,
- presupuestos por dominio,
- caching semántico,
- modelos pequeños para tareas simples,
- revisión mensual de costo/valor,
- alertas por anomalías de consumo.
