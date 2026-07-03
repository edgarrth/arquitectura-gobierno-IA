# AI Audit Checklist

> Nota de datos: los ejemplos usan datos realistas de industria financiera regulada y patrones operativos típicos de banca, tarjetas, seguros y fintech. No contienen datos productivos, PII real, PAN real ni información confidencial de ninguna empresa.

# Identificación

| Campo | Valor |
|---|---|
| AI System ID | AI-FRD-001 |
| Nombre | Motor de detección de fraude transaccional |
| Tipo | ML supervisado |
| Tier | Tier 1 |
| Owner | Riesgo Operacional / Fraude |
| Fecha auditoría | 2026-07-02 |

# Checklist de gobierno

| ID | Control | Evidencia | Estado |
|---|---|---|---|
| GOV-001 | Caso registrado | AI Use Case Register | Pendiente |
| GOV-002 | Riesgo aprobado | Acta AI Council | Pendiente |
| GOV-003 | Owner negocio | RACI | Pendiente |
| GOV-004 | Owner técnico | RACI | Pendiente |
| GOV-005 | Evaluación ética | Responsible AI Review | Pendiente |

# Checklist de datos

| ID | Control | Evidencia | Estado |
|---|---|---|---|
| DATA-001 | Dataset registrado | Dataset Card | Pendiente |
| DATA-002 | Lineage documentado | Data Catalog | Pendiente |
| DATA-003 | PII clasificada | Classification report | Pendiente |
| DATA-004 | PAN tokenizado | DLP report | Pendiente |
| DATA-005 | Calidad medida | DQ dashboard | Pendiente |

# Checklist de modelo

| ID | Control | Evidencia | Estado |
|---|---|---|---|
| MRM-001 | Model Card completa | Model Card | Pendiente |
| MRM-002 | Validación independiente | Validation report | Pendiente |
| MRM-003 | Métricas por segmento | Fairness report | Pendiente |
| MRM-004 | Explicabilidad | SHAP / reason codes | Pendiente |
| MRM-005 | Threshold aprobado | Threshold approval | Pendiente |

# Checklist GenAI

| ID | Control | Evidencia | Estado |
|---|---|---|---|
| GENAI-001 | Prompt versionado | Prompt Registry | Pendiente |
| GENAI-002 | Hallucination eval | Eval report | Pendiente |
| GENAI-003 | Grounding eval | RAG eval | Pendiente |
| GENAI-004 | Prompt injection test | Red Team report | Pendiente |
| GENAI-005 | DLP activo | Gateway logs | Pendiente |

# Checklist de seguridad

| ID | Control | Evidencia | Estado |
|---|---|---|---|
| SEC-001 | Autenticación fuerte | IAM policy | Pendiente |
| SEC-002 | Autorización por rol | RBAC matrix | Pendiente |
| SEC-003 | Secrets en vault | Vault config | Pendiente |
| SEC-004 | Logs inmutables | SIEM evidence | Pendiente |
| SEC-005 | Threat model IA | Threat model | Pendiente |

# Resultado

| Resultado | Definición |
|---|---|
| Aprobado | Sin hallazgos críticos ni altos |
| Aprobado con observaciones | Hallazgos medios o bajos |
| Aprobado condicionado | Hallazgos altos con plan aprobado |
| No aprobado | Hallazgo crítico o control clave ausente |
