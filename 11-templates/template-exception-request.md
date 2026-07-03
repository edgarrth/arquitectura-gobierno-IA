# Template — AI Exception Request

> Nota de datos: los ejemplos usan datos realistas de industria financiera regulada y patrones operativos típicos de banca, tarjetas, seguros y fintech. No contienen datos productivos, PII real, PAN real ni información confidencial de ninguna empresa.

# Identificación

| Campo | Valor |
|---|---|
| Exception ID | AIEXC-2026-0001 |
| AI System ID | AI-KB-004 |
| Solicitante | AI Platform |
| Fecha solicitud | 2026-07-02 |
| Fecha expiración | 2026-08-31 |
| Estado | Pendiente |

# Control afectado

| Campo | Valor |
|---|---|
| Control ID | CTRL-GENAI-003 |
| Control | Evaluación RAG grounding >95% |
| Política | RAG Governance |

# Descripción

El sistema RAG interno se encuentra en piloto controlado con usuarios internos. El grounding actual es 93.1%, debajo del umbral, pero el caso no toma decisiones financieras ni responde directamente a clientes.

# Controles compensatorios

| Control | Descripción |
|---|---|
| Human review | Usuario valida antes de usar |
| Scope limitado | Solo documentos internos |
| Logging completo | Prompts y respuestas |
| No PII | DLP bloquea datos sensibles |
| Monitoreo semanal | Revisión de fallos |

# Plan de remediación

| Acción | Owner | Fecha |
|---|---|---|
| Mejorar chunking | AI Platform | 2026-07-15 |
| Reindexar KB | Knowledge Owner | 2026-07-20 |
| Ejecutar RAG eval | AI Quality | 2026-07-25 |
| Alcanzar 95% grounding | AI Platform | 2026-08-15 |

# Decisión

| Resultado | Selección |
|---|---|
| Aprobada | ☐ |
| Rechazada | ☐ |
| Aprobada con condiciones | ☐ |
| Requiere AI Council | ☐ |
