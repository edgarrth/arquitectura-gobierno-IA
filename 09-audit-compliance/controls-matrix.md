# AI Reference Controls Matrix

> Nota de datos: los ejemplos usan datos realistas de industria financiera regulada y patrones operativos típicos de banca, tarjetas, seguros y fintech. No contienen datos productivos, PII real, PAN real ni información confidencial de ninguna empresa.

# Objetivo

Definir una matriz de controles reutilizable para gobierno, riesgo, datos, modelos, GenAI, seguridad, operación y auditoría.

# Estructura de control

| Campo | Descripción |
|---|---|
| Control ID | Identificador único |
| Dominio | Gobierno, Datos, Modelo, GenAI, Seguridad, Operación |
| Objetivo | Riesgo que reduce |
| Owner | Responsable |
| Frecuencia | Evento, mensual, trimestral, anual |
| Evidencia | Artefacto requerido |
| Marco | NIST, ISO 42001, EU AI Act, SR 11-7, PCI DSS |

# Matriz

| ID | Dominio | Control | Riesgo | Evidencia | Marco |
|---|---|---|---|---|---|
| CTRL-GOV-001 | Gobierno | Todo caso IA debe registrarse antes del diseño | Shadow AI | AI Use Case Register | NIST Govern |
| CTRL-GOV-002 | Gobierno | Owner negocio y técnico obligatorio | Falta accountability | RACI | ISO 42001 |
| CTRL-GOV-003 | Gobierno | AI Council aprueba Tier 1 y 2 | Riesgo no aceptado | Acta | NIST Govern |
| CTRL-RISK-001 | Riesgo | Clasificación obligatoria | Control insuficiente | Risk Assessment | EU AI Act |
| CTRL-DATA-001 | Datos | Dataset con owner y steward | Datos no gobernados | Dataset Card | DAMA |
| CTRL-DATA-002 | Datos | PII clasificada antes de entrenamiento | Privacidad | DLP report | ISO 27701 |
| CTRL-DATA-003 | Datos | PAN no debe enviarse a LLM externo | PCI breach | Gateway logs | PCI DSS |
| CTRL-MODEL-001 | Modelo | Model Card obligatoria | Falta transparencia | Model Card | NIST Measure |
| CTRL-MODEL-002 | Modelo | Validación independiente Tier 1 | Validación sesgada | Validation report | SR 11-7 |
| CTRL-MODEL-003 | Modelo | Explainability para crédito | Reclamos | SHAP report | EU AI Act |
| CTRL-GENAI-001 | GenAI | Prompt registry obligatorio | No reproducibilidad | Prompt version | NIST Measure |
| CTRL-GENAI-002 | GenAI | Guardrails input/output | Leakage | Guardrail config | ISO 42001 |
| CTRL-GENAI-003 | GenAI | Evaluación RAG grounding | Respuestas sin fuente | RAG eval | NIST Measure |
| CTRL-SEC-001 | Seguridad | Threat model IA | Ataques IA | Threat model | ISO 27001 |
| CTRL-SEC-002 | Seguridad | Red team GenAI | Prompt injection | Red team report | OWASP LLM |
| CTRL-OPS-001 | Operación | Monitoreo de drift | Degradación | Drift dashboard | SR 11-7 |
| CTRL-OPS-002 | Operación | Rollback probado | Indisponibilidad | Test evidence | COBIT |
| CTRL-AUD-001 | Auditoría | Evidencia preservada | Incumplimiento | Evidence pack | ISO 42001 |

# Ejemplo de evidencia

```json
{
  "control_id": "CTRL-DATA-003",
  "system_id": "AI-CSC-002",
  "event": "llm_request_blocked",
  "reason": "PAN_PATTERN_DETECTED",
  "timestamp": "2026-07-02T19:42:11-05:00",
  "decision": "BLOCK"
}
```

# Nivel de madurez

| Nivel | Descripción |
|---|---|
| 1 | Control manual y evidencia dispersa |
| 2 | Control definido |
| 3 | Control institucionalizado |
| 4 | Control medido y automatizado parcialmente |
| 5 | Control continuo y auditable |
