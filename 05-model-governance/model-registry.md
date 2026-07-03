# Model Registry

# Propósito

Mantener inventario único de modelos, versiones, estado, riesgo, owners, aprobaciones y evidencia.

# Estados

| Estado | Descripción |
|---|---|
| proposed | caso registrado |
| development | en construcción |
| validation | en validación |
| approved | aprobado para release |
| production | activo en producción |
| deprecated | reemplazado pero disponible |
| retired | retirado |

# Campos del registro

| Campo | Descripción |
|---|---|
| Model ID | identificador único |
| Nombre | nombre funcional |
| Versión | semantic versioning |
| Tipo | scorecard, ML, DL, LLM, agente |
| Tier | clasificación de riesgo |
| Owner negocio | responsable funcional |
| Owner técnico | responsable técnico |
| Dataset | datasets asociados |
| Endpoint | servicio de inferencia |
| Métricas | principales métricas aprobadas |
| Estado | ciclo de vida |
| Evidencia | links a documentos |

# Registro ejemplo

| Model ID | Nombre | Tipo | Tier | Versión | Estado |
|---|---|---|---|---|---|
| MOD-FRAUD-XGB-003 | Fraud Detection | XGBoost | Tier 1 | 3.2.0 | production |
| MOD-CREDIT-LGBM-001 | Credit Scoring | LightGBM | Tier 1 | 1.4.1 | validation |
| MOD-COLLECT-RANK-002 | Collections Prioritization | Ranking ML | Tier 2 | 2.1.0 | production |
| MOD-CS-COPILOT-001 | Customer Service Copilot | LLM + RAG | Tier 2 | 1.0.0 | approved |

# Semantic versioning

```text
MAJOR.MINOR.PATCH
```

| Cambio | Ejemplo | Requiere aprobación |
|---|---|---|
| MAJOR | nuevo algoritmo o objetivo | Sí |
| MINOR | nuevas features o recalibración | Sí según tier |
| PATCH | fix técnico sin cambio predictivo | revisión técnica |

# Evidencia mínima por modelo

- model card
- risk assessment
- dataset registry
- validation report
- approval checklist
- monitoring dashboard
- runbook
- incident history
