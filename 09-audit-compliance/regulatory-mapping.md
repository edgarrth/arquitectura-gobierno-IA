# AI Regulatory Mapping

> Nota de datos: los ejemplos usan datos realistas de industria financiera regulada y patrones operativos típicos de banca, tarjetas, seguros y fintech. No contienen datos productivos, PII real, PAN real ni información confidencial de ninguna empresa.

# Objetivo

Mapear controles de gobierno de IA contra marcos regulatorios, estándares y prácticas aplicables a empresas reguladas.

# Marcos considerados

## AI Governance

- NIST AI RMF 1.0
- ISO/IEC 42001:2023
- ISO/IEC 23894
- EU AI Act, Regulation (EU) 2024/1689

## Gobierno, seguridad y riesgo

- COBIT
- ISO/IEC 27001
- ISO/IEC 27701
- PCI DSS v4.0.1
- SR 11-7 Model Risk Management

# Matriz resumen

| Dominio | NIST AI RMF | ISO 42001 | EU AI Act | SR 11-7 | PCI DSS | Artefacto |
|---|---|---|---|---|---|---|
| Gobierno | Govern | AIMS governance | Obligaciones de gobernanza | Gobierno MRM | Req. 12 | AI Council |
| Riesgo | Map, Manage | Risk process | Risk-based approach | Model risk | Req. 12 | AI Risk Assessment |
| Datos | Map, Measure | Data management | Data governance | Data quality | Req. 3, 4 | Dataset Card |
| Transparencia | Measure | Transparency | Transparency | Explainability | N/A | Model Card |
| Validación | Measure | Evaluation | Testing | Independent validation | Req. 6 | Validation Report |
| Seguridad | Manage | Security | Cybersecurity | Operational risk | Req. 1-12 | Threat Model |
| Monitoreo | Manage | Monitoring | Post-market monitoring | Ongoing monitoring | Req. 10 | ModelOps |
| Incidentes | Manage | Incident response | Serious incidents | Issue management | Req. 12 | Incident Runbook |

# Clasificación de riesgo adaptada

| Categoría | Adaptación empresarial |
|---|---|
| Prohibido | Casos bloqueados por política interna |
| Alto riesgo | Tier 1 |
| Riesgo limitado | Tier 2 o Tier 3 |
| Riesgo mínimo | Tier 4 |

# Mapeo por caso

| Caso | NIST | ISO 42001 | EU AI Act | SR 11-7 | PCI DSS |
|---|---|---|---|---|---|
| Credit Scoring | Alto | Alto | Alto | Alto | Medio |
| Fraud Detection | Alto | Alto | Medio | Alto | Alto |
| Collections Prioritization | Alto | Alto | Alto | Alto | Medio |
| Call Center Copilot | Alto | Alto | Limitado | Bajo | Medio |
| RAG interno | Medio | Alto | Limitado | Bajo | Bajo |

# Gaps comunes

| Gap | Riesgo | Control |
|---|---|---|
| Modelos sin inventario | Shadow AI | AI Use Case Register |
| Prompts sin versionado | No reproducibilidad | Prompt Registry |
| Features sin lineage | Auditoría incompleta | Feature Store |
| Métricas sin segmentos | Bias no detectado | Fairness Dashboard |
| Vendor sin evaluación | Third-party risk | Vendor Assessment |
