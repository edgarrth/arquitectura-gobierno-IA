# SLOs y SLAs de IA

# Propósito

Definir objetivos de servicio para soluciones de IA según criticidad.

# SLOs por tipo

| Tipo | Disponibilidad | Latencia p95 | Error rate |
|---|---:|---:|---:|
| fraude online | 99.95% | < 50 ms | < 0.1% |
| scoring batch | 99.5% | ventana batch | < 1% |
| copiloto interno | 99.0% | < 3 s | < 1% |
| RAG atención | 99.5% | < 5 s | < 1% |

# Error budget

El error budget se revisa mensualmente. Si se consume más del 50%, se congelan despliegues no urgentes del servicio de IA afectado.

# Ejemplo realista

```json
{
  "service": "fraud-realtime-scoring",
  "month": "2025-10",
  "availability": 99.97,
  "p95_latency_ms": 34,
  "error_rate": 0.0007,
  "error_budget_consumed": "31%",
  "status": "within_slo"
}
```
