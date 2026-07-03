# Política de Reentrenamiento

# Propósito

Definir cuándo, cómo y bajo qué aprobaciones se reentrenan modelos productivos.

# Disparadores de reentrenamiento

| Trigger | Acción |
|---|---|
| PSI crítico | evaluar reentrenamiento |
| caída de KPI crítico | reentrenamiento prioritario |
| cambio regulatorio | revisión obligatoria |
| nuevo patrón de fraude | entrenamiento extraordinario |
| cambio de producto | recalibración |

# Frecuencia recomendada

| Modelo | Frecuencia mínima |
|---|---|
| fraude transaccional | mensual o por evento |
| scoring crédito | trimestral/semestral |
| collections ranking | mensual |
| LLM prompt/RAG | por cambio de fuente o métrica |

# Reglas

- El modelo reentrenado no reemplaza producción sin validación.
- Todo reentrenamiento debe generar nueva versión.
- Se debe comparar contra champion actual.
- El rollback debe estar disponible.

# Ejemplo realista

```yaml
retraining_event: RETRAIN-FRD-2025-011
model_current: FRD-XGB-TRANSACTION-v3.2
candidate: FRD-XGB-TRANSACTION-v3.3
reason: concept_drift_new_ecommerce_fraud_pattern
baseline_recall: 0.887
candidate_recall: 0.912
baseline_fpr: 0.016
candidate_fpr: 0.018
approval_required: Model Risk + Fraud Owner
```
