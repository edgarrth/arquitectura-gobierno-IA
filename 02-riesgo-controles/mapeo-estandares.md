# Mapeo de estándares y cumplimiento

# Objetivo

Demostrar que el framework lite mantiene trazabilidad contra los estándares 
definidos para Gobierno de IA, seguridad, riesgo y auditoría, sin replicar 
documentos separados por cada marco.

# Marcos usados

| Marco | Uso en este repositorio |
|---|---|
| NIST AI RMF | Ciclo Govern, Map, Measure, Manage para riesgos de IA. |
| ISO/IEC 42001:2023 | Sistema de gestión de IA: política, roles, evaluación, operación, auditoría y mejora continua. |
| ISO/IEC 23894 | Gestión de riesgos asociados a IA. |
| EU AI Act, Regulation (EU) 2024/1689 | Referencia de clasificación basada en riesgo e impacto. |
| ISO/IEC 27001 | Controles de seguridad, accesos, continuidad, incidentes y gestión de proveedores. |
| ISO/IEC 27701 / privacidad | Uso autorizado, minimización, PII, retención y evidencia. |
| PCI DSS v4.0.1 | Protección de datos de tarjetas cuando aplica. |
| SR 11-7 / Model Risk Management | Validación independiente y monitoreo para modelos de decisión financiera. |
| OWASP Top 10 LLM / GenAI | Riesgos de prompt injection, data leakage, supply chain, excessive agency y output handling. |
| COBIT | Gobierno, accountability, medición y control. |
| TOGAF | Arquitectura, estándares y gobierno de soluciones. |

# Mapeo consolidado

| Control lite | NIST AI RMF | ISO 42001 | EU AI Act | ISO 27001/27701 | PCI DSS | SR 11-7 | OWASP LLM | Evidencia |
|---|---|---|---|---|---|---|---|---|
| GOV-001 Inventario IA | Govern | Contexto y sistema de gestión | Gestión de riesgo | Gobierno de activos | Req. 12 | Inventario de modelos | N/A | AI Portfolio |
| RSK-001 Risk assessment | Map/Manage | Riesgos y oportunidades | Clasificación de riesgo | Risk management | Req. 12 | Model risk | N/A | AI Risk Assessment |
| DAT-001 Uso autorizado de datos | Map | Gestión de datos | Data governance | Privacidad | Req. 3/4 | Data quality | Training data poisoning | Data Review |
| DAT-002 Minimización/masking | Manage | Controles operativos | Protección de datos | Privacy/security | Req. 3 | N/A | Sensitive information disclosure | Privacy Review |
| MOD-001 Model Card Lite | Measure | Evaluación | Documentación técnica | N/A | N/A | Model documentation | N/A | Model Card |
| MOD-002 Validación independiente | Measure | Evaluación | Testing | N/A | Req. 6 | Independent validation | N/A | Validation Report |
| GEN-001 Prompt/RAG registry | Measure/Manage | Control operativo | Transparencia | Registro y logging | Req. 10 | N/A | Prompt injection / output handling | Prompt/RAG Card |
| SEC-001 Threat model IA | Manage | Seguridad | Cybersecurity | Security by design | Req. 1-12 | Operational risk | LLM01-LLM10 | Threat Model |
| OPS-001 Monitoreo IA | Measure/Manage | Monitoreo | Post-market monitoring | Logging/monitoring | Req. 10 | Ongoing monitoring | Model DoS / drift | Dashboard |
| AUD-001 Evidence log | Govern/Manage | Auditoría interna | Obligaciones de registro | Audit evidence | Req. 12 | Audit trail | N/A | AI Release Pack |

# Mapeo por tipo de caso

| Caso | Marcos más relevantes | Evidencia reforzada |
|---|---|---|
| Scoring crediticio | NIST, ISO 42001, SR 11-7, privacidad | validación independiente, explainability, fairness, HITL |
| Fraude transaccional | NIST, ISO 42001, SR 11-7, PCI DSS, ISO 27001 | monitoreo, reason codes, rollback, logs, seguridad |
| Copiloto de reclamos | NIST, ISO 42001, OWASP LLM, privacidad | prompt eval, DLP, RAG sources, human approval |
| RAG normativo | NIST, ISO 42001, OWASP LLM | grounding, source traceability, versioning |
| Agente de conciliaciones | NIST, ISO 42001, OWASP LLM, ISO 27001 | tool registry, policy engine, approval, kill switch |

# Evidencia mínima audit-ready

| Pregunta de auditoría | Evidencia que responde |
|---|---|
| ¿Qué sistemas de IA existen? | AI Portfolio / Use Case Register |
| ¿Quién aprobó el uso? | RACI + approval record |
| ¿Qué riesgo tiene? | Risk Assessment |
| ¿Qué datos usa? | Data Review / Dataset Card |
| ¿Qué versión de modelo o prompt está activa? | Model Registry / Prompt Registry |
| ¿Cómo se probó? | Model Card / Evaluation Report |
| ¿Cómo se monitorea? | Dashboard / Metrics / Alerts |
| ¿Qué incidentes tuvo? | Incident log + RCA |
| ¿Qué excepción sigue abierta? | Exception request + due date |

# Referencias oficiales sugeridas

- NIST AI Risk Management Framework 1.0.
- ISO/IEC 42001:2023 Artificial intelligence management system.
- Regulation (EU) 2024/1689 Artificial Intelligence Act.
- OWASP Top 10 for LLM Applications.
- PCI DSS v4.0.1.
- ISO/IEC 27001 e ISO/IEC 27701.
