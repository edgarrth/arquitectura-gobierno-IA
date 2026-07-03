# AI Evidence Requirements

> Nota de datos: los ejemplos usan datos realistas de industria financiera regulada y patrones operativos típicos de banca, tarjetas, seguros y fintech. No contienen datos productivos, PII real, PAN real ni información confidencial de ninguna empresa.

# Objetivo

Definir la evidencia mínima para demostrar control, trazabilidad y cumplimiento en IA.

# Repositorios recomendados

| Tipo | Repositorio |
|---|---|
| Código | GitHub Enterprise / GitLab |
| Modelos | MLflow / SageMaker / Vertex AI |
| Prompts | Prompt Registry |
| Datasets | Data Catalog |
| Logs | SIEM / Loki / OpenSearch |
| Métricas | Grafana / Datadog |
| Aprobaciones | Jira / ServiceNow / GRC |

# Evidencia por fase

## Intake

| Evidencia | Obligatorio |
|---|---|
| AI Use Case Form | Todos |
| Business Case | Tier 1 y 2 |
| Risk Pre-Screening | Todos |
| Privacy Pre-Screening | Todos |

## Diseño

| Evidencia | Obligatorio |
|---|---|
| AI Risk Assessment | Todos |
| DPIA | Cuando usa PII |
| Threat Model | Tier 1, 2 y GenAI |
| Human Oversight Design | Tier 1 y 2 |

## Desarrollo

| Evidencia | Obligatorio |
|---|---|
| Dataset Card | Todos |
| Data Quality Report | Todos |
| Experiment Tracking | ML |
| Prompt Evaluation | GenAI |
| RAG Evaluation | RAG |

## Validación

| Evidencia | Obligatorio |
|---|---|
| Model Validation Report | Tier 1 y 2 |
| Fairness Report | Tier 1 y 2 |
| Robustness Test | Tier 1 y 2 |
| Red Team Report | GenAI y agentes |

## Operación

| Evidencia | Obligatorio |
|---|---|
| Monitoring Dashboard | Todos |
| Drift Report | ML Tier 1 y 2 |
| Incident Log | Todos |
| Retraining Record | ML |
| Prompt Change History | GenAI |
| Access Logs | Todos |

# Ejemplo de evidencia para fraude

| Evidencia | Valor |
|---|---|
| Model ID | FRD-XGB-3.2 |
| Dataset | CARD-TRX-2024-2025-v17 |
| Feature Store | fs-card-risk-v5 |
| AUC | 0.971 |
| Recall fraude | 0.892 |
| FPR | 1.7% |
| Drift PSI monto | 0.08 |
| Aprobación | AI Council 2026-06-15 |

# Retención

| Evidencia | Retención |
|---|---|
| Model Cards | Vida del modelo + 7 años |
| Logs de inferencia Tier 1 | 7 años |
| Prompts productivos | 5 años |
| Auditorías | 10 años |
| Incidentes críticos | 10 años |
