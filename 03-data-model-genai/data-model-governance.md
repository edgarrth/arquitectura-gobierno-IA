# Data governance y model governance lite

# Objetivo

Consolidar en un solo documento los controles mínimos de datos, 
datasets, modelos, validación y model registry.

# Regla central

Todo sistema IA que use datos empresariales debe poder responder:

- qué datos usa;
- para qué propósito;
- quién es el owner;
- qué versión del dataset o feature set alimentó el modelo;
- qué versión de modelo/prompt está en producción;
- qué métricas justifican su uso;
- qué limitaciones y riesgos tiene;
- cómo se monitorea.

# Dataset Card 

| Campo | Ejemplo simulado |
|---|---|
| Dataset ID | DS-CARD-TRX-RISK-2026Q1-v17 |
| Nombre | Transacciones tarjeta tokenizadas para riesgo |
| Owner | Data Owner Tarjetas |
| Propósito autorizado | Detección y prevención de fraude |
| Fuentes | switch transaccional, contracargos, device signals, merchant risk |
| PII | Sí, tokenizada |
| PCI | No se almacena PAN/CVV; solo token y BIN parcial |
| Retención | 5 años según política de riesgo y auditoría |
| Calidad mínima | completitud > 98%, duplicados < 0.5%, labels conciliados mensualmente |
| Sesgos conocidos | subrepresentación de comercios nuevos y tickets internacionales |
| Restricciones | No usar para campañas comerciales sin nuevo propósito aprobado |

# Model Card

| Campo | Ejemplo simulado |
|---|---|
| Model ID | FRD-XGB-TRANSACTION-v3.2 |
| Caso asociado | AI-UC-2026-001 Motor de fraude CNP |
| Tipo | XGBoost supervisado |
| Owner | Lead Data Science Fraude |
| Decisión | score de riesgo y reason codes |
| Versión productiva | v3.2.1 |
| Fecha de aprobación | 2026-06-12 |
| Dataset entrenamiento | DS-CARD-TRX-RISK-2026Q1-v17 |
| Métrica principal | Recall fraude = 0.887 |
| Métricas secundarias | Precision 0.941, AUC 0.973, FPR 1.6% |
| Explainability | SHAP global + reason codes por transacción |
| Limitaciones | menor señal en comercios nuevos y transacciones cross-border |
| Human oversight | revisión operaciones para casos desafiados o reclamos |
| Rollback | FRD-RULES-v2 como fallback |

# Criterios mínimos de validación

| Criterio | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|---|---:|---:|---:|---:|
| Train/test split documentado | Sí | Sí | Sí | No |
| Métricas por segmento | Sí | Sí | Recomendado | No |
| Fairness/bias review | Sí | Si impacta cliente | Recomendado | No |
| Explainability | Sí | Si impacta cliente | Recomendado | No |
| Stress/robustness test | Sí | Sí | Recomendado | No |
| Validación independiente | Sí | Según impacto | No | No |
| Reproducibilidad | Sí | Sí | Sí | Básico |

# Model Registry mínimo

| Campo | Descripción |
|---|---|
| model_id | identificador único |
| use_case_id | caso asociado |
| owner | responsable |
| version | versión activa |
| tier | nivel de riesgo |
| status | candidate, approved, production, retired |
| training_dataset | dataset/version |
| approval_date | fecha de aprobación |
| monitoring_dashboard | link o referencia |
| rollback_model | fallback |

# Ejemplo de modelos registrados

| model_id | use_case_id | tier | status | métrica principal | estado |
|---|---|---|---|---|---|
| FRD-XGB-TRANSACTION-v3.2 | AI-UC-2026-001 | Tier 1 | production | Recall 0.887 | OK |
| CRD-LGBM-WALLET-v1.1 | AI-UC-2026-002 | Tier 1 | candidate | KS 0.421 | pending validation |
| MKT-PROP-XSELL-v2.4 | AI-UC-2026-006 | Tier 3 | production | uplift 7.8% | OK |
| COL-PRD-EARLY-v0.8 | AI-UC-2026-008 | Tier 2 | discovery | AUC 0.842 | draft |

# Reglas para datos personales

- Usar solo datos con propósito autorizado.
- Evitar atributos protegidos salvo justificación legal y control de sesgo.
- Tokenizar identificadores de cliente.
- No almacenar PAN completo ni CVV.
- Evitar que prompts o logs incluyan PII no necesaria.
- Mantener lineage de origen, transformación y consumo.
- Definir retención y eliminación.

# Evidencia requerida en el AI Release Pack

| Evidencia | Descripción |
|---|---|
| Dataset Card Lite | fuentes, owner, propósito, calidad, PII/PCI, retención |
| Model Card Lite | versión, métricas, limitaciones, explainability, rollback |
| Validation Summary | resultados, segmentos, sesgos, aprobación |
| Monitoring Plan | métricas, umbrales, frecuencia, owner |
| Change Log | historial de cambios de modelo, features o parámetros |
