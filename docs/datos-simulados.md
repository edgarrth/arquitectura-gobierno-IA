# Datos simulados

> Esta página se genera automáticamente desde los CSV de `docs/data-simulada/` durante el pipeline.

Los archivos originales también se publican y pueden descargarse desde cada sección.

## Ai Use Cases

[Descargar `ai_use_cases.csv`](data-simulada/ai_use_cases.csv)

| use_case_id | name | domain | type | tier | status | business_owner | technical_owner | expected_value_pen_year | customer_impact | data_sources | pii | human_oversight |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AI-UC-2026-001 | Motor de fraude CNP tarjetas | Riesgo Transaccional | ML supervisado | Tier 1 | Pilot | Gerencia Riesgo Transaccional | Lead Data Science Fraude | 7800000 | Retención o desafío de transacción | transacciones tokenizadas; chargebacks; device signals; merchant risk | Sí tokenizada | Operaciones revisa desafíos y reclamos |
| AI-UC-2026-002 | Scoring alternativo microcrédito wallet | Crédito Digital | ML supervisado | Tier 1 | Discovery | Gerencia Crédito Digital | Lead Data Science Crédito | 5400000 | Recomendación de límite y pricing | wallet behavior; pagos; ingresos declarados; buro score | Sí | Analista aprueba reglas de excepción |
| AI-UC-2026-003 | Copiloto reclamos de tarjeta | Operaciones Cliente | RAG/GenAI | Tier 2 | Build | Gerencia Operaciones Cliente | Tech Lead Canales | 1600000 | Sugerencia de respuesta a reclamo | tickets; manual reclamos; política chargeback; matriz SLA | Sí minimizada | Agente humano aprueba respuesta |
| AI-UC-2026-004 | RAG normativo compliance | Compliance | RAG | Tier 3 | Production | Gerencia Compliance | Tech Lead Plataforma IA | 800000 | No directo; consultas internas | políticas internas; normas públicas; procedimientos PLAFT | No | Usuario valida respuesta con fuente |
| AI-UC-2026-005 | Agente conciliaciones backoffice | Operaciones Backoffice | Agente A2 | Tier 2 | Pilot | Gerencia Operaciones Backoffice | Lead Platform Automation | 2100000 | Indirecto por conciliación de pagos | lotes de conciliación; estados de pago; ledger operativo | Sí tokenizada | Supervisor aprueba ajustes |
| AI-UC-2026-006 | Propensión cross-sell préstamos | Marketing Analytics | ML supervisado | Tier 3 | Production | Gerencia Crecimiento | Lead Analytics Marketing | 3200000 | Oferta personalizada no vinculante | perfil transaccional; comportamiento app; campañas previas | Sí minimizada | Reglas de exclusión y consentimiento |
| AI-UC-2026-007 | OCR KYC documento de identidad | Onboarding Digital | Computer Vision/OCR | Tier 2 | Build | Gerencia Onboarding | Tech Lead Identidad | 1900000 | Validación de onboarding | imagen documento; selfie liveness; formulario onboarding | Sí sensible | Revisión manual si baja confianza |
| AI-UC-2026-008 | Predicción mora temprana | Cobranzas Preventivas | ML supervisado | Tier 2 | Discovery | Gerencia Cobranzas | Lead Data Science Riesgo | 4300000 | Priorización de gestión preventiva | pagos; saldo; comportamiento app; promesas de pago | Sí | Gestor decide acción final |

## Controls Evidence

[Descargar `controls_evidence.csv`](data-simulada/controls_evidence.csv)

| control_id | control | coverage | status | evidence_ref | owner |
| --- | --- | --- | --- | --- | --- |
| GOV-001 | Caso registrado en AI Portfolio | 8/8 | OK | data-simulada/ai_use_cases.csv | AI Lead |
| RSK-001 | Risk assessment vigente | 8/8 | OK | data-simulada/risk_assessments.csv | Risk Owner |
| DAT-001 | Data owner y propósito autorizado | 5/5 PII cases | OK | Data Catalog synthetic refs | Data Governance |
| MOD-001 | Model/GenAI Card Lite | 6/6 systems | OK | templates/model-card-lite.md + registry | Model Owners |
| MOD-002 | Validación independiente Tier 1 | 1/2 | Warning | CRD-LGBM-WALLET pending validation | Model Risk |
| SEC-002 | DLP/secrets/logging seguro | 5/5 high impact | OK | SIEM-DLP synthetic logs | Security Owner |
| GEN-002 | Guardrails y pruebas de alucinación | 3/3 GenAI/RAG/Agent | OK | data-simulada/rag_evaluation.csv | AI Platform |
| OPS-001 | Monitoreo activo | 3/3 productive systems | OK | data-simulada/model_metrics.csv | AI Ops |
| AUD-001 | Evidence log | 8/8 | OK | AI Release Pack links | AI Lead |

## Incidents

[Descargar `incidents.csv`](data-simulada/incidents.csv)

| incident_id | system_id | severity | date_opened | date_closed | summary | root_cause | action | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AI-INC-2026-0012 | CSC-RAG-CLAIMS-v1.4 | Sev3 | 2026-06-10 | 2026-06-12 | Respuesta sin fuente en consulta de SLA minoritaria durante piloto | documento de SLA no indexado en KB v2026.05 | actualizar KB y agregar eval case | Closed |
| AI-INC-2026-0013 | FRD-XGB-TRANSACTION-v3.2 | Sev3 | 2026-06-24 |  | PSI warning en feature amount para comercios travel | campaña estacional elevó ticket promedio | monitoreo extendido 7 días y revisión de threshold | Monitoring |

## Model Metrics

[Descargar `model_metrics.csv`](data-simulada/model_metrics.csv)

| system_id | metric_date | metric | value | threshold | status |
| --- | --- | --- | --- | --- | --- |
| FRD-XGB-TRANSACTION-v3.2 | 2026-06-30 | recall_fraud | 0.887 | 0.85 | OK |
| FRD-XGB-TRANSACTION-v3.2 | 2026-06-30 | precision | 0.941 | 0.9 | OK |
| FRD-XGB-TRANSACTION-v3.2 | 2026-06-30 | false_positive_rate | 0.016 | 0.02 | OK |
| FRD-XGB-TRANSACTION-v3.2 | 2026-06-30 | psi_amount | 0.18 | 0.25 | Warning |
| MKT-PROP-XSELL-v2.4 | 2026-06-30 | uplift | 0.078 | 0.05 | OK |
| AGT-OPS-RECON-v0.9 | 2026-06-30 | human_override_rate | 0.124 | 0.15 | OK |

## Model Registry

[Descargar `model_registry.csv`](data-simulada/model_registry.csv)

| system_id | use_case_id | type | tier | version | status | owner | training_dataset | approval_date | primary_metric | primary_metric_value | rollback |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FRD-XGB-TRANSACTION-v3.2 | AI-UC-2026-001 | XGBoost | Tier 1 | 3.2.1 | production | Lead Data Science Fraude | DS-CARD-TRX-RISK-2026Q1-v17 | 2026-06-12 | recall_fraud | 0.887 | FRD-RULES-v2 |
| CRD-LGBM-WALLET-v1.1 | AI-UC-2026-002 | LightGBM | Tier 1 | 1.1.0-rc2 | candidate | Lead Data Science Crédito | DS-WALLET-CREDIT-2026Q1-v08 |  | ks_statistic | 0.421 | manual_credit_policy_v2026.02 |
| CSC-RAG-CLAIMS-v1.4 | AI-UC-2026-003 | RAG/LLM | Tier 2 | 1.4.3 | pilot | Tech Lead Canales | KB-CLAIMS-2026.05 | 2026-06-25 | groundedness | 0.958 | human_only_response_workflow |
| CMP-RAG-NORM-v2.0 | AI-UC-2026-004 | RAG | Tier 3 | 2.0.2 | production | Tech Lead Plataforma IA | KB-COMPLIANCE-2026.06 | 2026-05-30 | answer_relevance | 0.932 | search_portal |
| AGT-OPS-RECON-v0.9 | AI-UC-2026-005 | Agent A2 | Tier 2 | 0.9.7 | pilot | Lead Platform Automation | KB-RECON-OPS-2026.04 | 2026-06-18 | human_override_rate | 0.124 | manual_reconciliation_queue |
| MKT-PROP-XSELL-v2.4 | AI-UC-2026-006 | Gradient Boosting | Tier 3 | 2.4.0 | production | Lead Analytics Marketing | DS-MKT-XSELL-2026Q1-v11 | 2026-04-14 | uplift | 0.078 | rules_based_segmentation |

## Rag Evaluation

[Descargar `rag_evaluation.csv`](data-simulada/rag_evaluation.csv)

| system_id | eval_date | groundedness | hallucination_rate | prompt_injection_blocked | pii_leakage_events | status |
| --- | --- | --- | --- | --- | --- | --- |
| CSC-RAG-CLAIMS-v1.4 | 2026-06-28 | 0.958 | 0.021 | 0.996 | 0 | OK |
| CMP-RAG-NORM-v2.0 | 2026-06-28 | 0.943 | 0.026 | 0.991 | 0 | OK |
| AGT-OPS-RECON-v0.9 | 2026-06-28 | 0.971 | 0.012 | 1.0 | 0 | OK |

## Risk Assessments

[Descargar `risk_assessments.csv`](data-simulada/risk_assessments.csv)

| use_case_id | impact_customer | autonomy | sensitive_data | regulation | explainability | robustness | security | third_party | weighted_score | tier | residual_risk | approval |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AI-UC-2026-001 | 5 | 4 | 5 | 5 | 3 | 4 | 4 | 2 | 4.35 | Tier 1 | Medio | AI Council |
| AI-UC-2026-002 | 5 | 3 | 5 | 5 | 4 | 4 | 3 | 2 | 4.25 | Tier 1 | Alto pendiente mitigación | AI Council |
| AI-UC-2026-003 | 4 | 2 | 4 | 4 | 3 | 3 | 4 | 3 | 3.45 | Tier 2 | Medio | AI Office + Risk |
| AI-UC-2026-004 | 2 | 1 | 2 | 3 | 3 | 2 | 3 | 2 | 2.2 | Tier 3 | Bajo | Fast Track |
| AI-UC-2026-005 | 3 | 3 | 4 | 3 | 3 | 4 | 4 | 2 | 3.35 | Tier 2 | Medio | AI Office + Security |
| AI-UC-2026-006 | 3 | 2 | 3 | 3 | 3 | 3 | 2 | 1 | 2.65 | Tier 3 | Bajo | Fast Track |
| AI-UC-2026-007 | 4 | 2 | 5 | 4 | 3 | 3 | 4 | 3 | 3.65 | Tier 2 | Medio | AI Office + Risk |
| AI-UC-2026-008 | 4 | 2 | 4 | 4 | 3 | 3 | 3 | 1 | 3.3 | Tier 2 | Medio | AI Office + Risk |
