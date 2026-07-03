# AI Controls Catalog

# Propósito

Catálogo estándar de controles para gobierno, riesgo, datos, modelos, seguridad, operación y auditoría de IA.

# Estructura del control

| Campo | Descripción |
|---|---|
| Control ID | identificador único |
| Dominio | gobierno, riesgo, datos, modelo, GenAI, seguridad |
| Objetivo | qué riesgo reduce |
| Evidencia | artefacto verificable |
| Frecuencia | cuándo se ejecuta |
| Owner | responsable |

# Controles de gobierno

| ID | Control | Evidencia | Frecuencia |
|---|---|---|---|
| GOV-001 | Todo caso de IA debe registrarse en AI Use Case Register | registro aprobado | por caso |
| GOV-002 | Todo caso Tier 1/2 debe tener business owner y model owner | RACI firmado | por caso |
| GOV-003 | Todo uso de IA debe tener clasificación de riesgo | risk assessment | por caso |
| GOV-004 | El AI Council revisa KPIs y riesgos críticos | acta de comité | mensual |

# Controles de datos

| ID | Control | Evidencia | Frecuencia |
|---|---|---|---|
| DAT-001 | Dataset usado por IA debe tener owner, steward y clasificación | dataset registry | por dataset |
| DAT-002 | PII debe ser minimizada, tokenizada o enmascarada | privacy review | por release |
| DAT-003 | Data lineage debe cubrir origen, transformación y consumo | diagrama lineage | por modelo |
| DAT-004 | Features críticas deben tener reglas de calidad | quality report | diario/semanal |

# Controles de modelo

| ID | Control | Evidencia | Frecuencia |
|---|---|---|---|
| MOD-001 | Todo modelo Tier 1/2 requiere model card | model card | por versión |
| MOD-002 | Todo modelo debe registrar métricas de entrenamiento y validación | experiment log | por versión |
| MOD-003 | Modelos Tier 1 requieren validación independiente | validation report | por versión |
| MOD-004 | Todo modelo productivo debe estar en model registry | registry record | continuo |

# Controles GenAI

| ID | Control | Evidencia | Frecuencia |
|---|---|---|---|
| GEN-001 | System prompts deben estar versionados | prompt registry | por cambio |
| GEN-002 | RAG debe usar fuentes aprobadas y versionadas | knowledge base inventory | por release |
| GEN-003 | Deben existir pruebas de hallucination y groundedness | eval report | por release |
| GEN-004 | Agentes con tools deben tener permisos por acción | tool policy | por release |

# Controles de seguridad

| ID | Control | Evidencia | Frecuencia |
|---|---|---|---|
| SEC-001 | No se permite enviar PAN completo ni secretos a LLMs | DLP logs | continuo |
| SEC-002 | APIs de inferencia deben usar autenticación fuerte | security review | por release |
| SEC-003 | Logs deben proteger PII | log masking evidence | continuo |
| SEC-004 | Prompt injection debe probarse antes de producción | red team report | por release |

# Controles de operación

| ID | Control | Evidencia | Frecuencia |
|---|---|---|---|
| OPS-001 | Monitoreo de drift para modelos productivos | drift dashboard | continuo |
| OPS-002 | Rollback documentado para modelos Tier 1/2 | runbook | por release |
| OPS-003 | SLOs de inferencia definidos | SLO document | por servicio |
| OPS-004 | Incidentes IA se clasifican y reportan | incident record | por evento |
