# GenAI Risk Framework

# Propósito

Gestionar riesgos específicos de IA generativa, LLMs, RAG, copilots y agentes autónomos.

# Riesgos principales

| Riesgo | Descripción | Ejemplo |
|---|---|---|
| Hallucination | respuesta no soportada por fuentes | inventar tasa, comisión o política |
| Prompt injection | instrucción maliciosa | ignorar reglas y revelar datos |
| Data leakage | exposición de PII o secretos | mostrar DNI, PAN, token o credencial |
| Toxicidad | respuesta ofensiva o discriminatoria | trato inadecuado al cliente |
| Overreliance | usuario confía sin validar | ejecutivo aprueba respuesta incorrecta |
| Tool misuse | agente ejecuta herramienta indebida | cerrar reclamo sin autorización |
| Retrieval error | RAG recupera documento incorrecto | política desactualizada |

# Clasificación GenAI

| Clase | Descripción | Control requerido |
|---|---|---|
| G1 | asistente interno sin PII | logging + política de uso |
| G2 | asistente interno con documentación sensible | DLP + RBAC + RAG governance |
| G3 | copilot cliente o asesor humano | guardrails + HITL + monitoreo |
| G4 | agente con tools transaccionales | aprobaciones, límites, auditoría |
| G5 | agente autónomo con impacto financiero | no permitido sin excepción CAIO + comité de riesgos |

# Evaluación de salida

| Métrica | Descripción | Umbral sugerido |
|---|---|---:|
| groundedness | respuesta soportada por contexto | >= 0.85 |
| answer relevance | pertinencia | >= 0.80 |
| hallucination score | probabilidad de invención | <= 0.10 |
| toxicity score | riesgo de contenido inapropiado | <= 0.05 |
| PII leakage | exposición de PII | 0 tolerancia |

# Ejemplo realista: copilot de reclamos

## Entrada

```text
Cliente indica que le cobraron una membresía anual que no reconoce y solicita exoneración.
```

## Respuesta permitida

```text
Según la política vigente de exoneración de membresía, debes validar segmento, consumo acumulado, mora vigente y campañas aplicables antes de ofrecer una exoneración. No prometas reverso inmediato si no existe elegibilidad confirmada.
```

## Respuesta prohibida

```text
Sí, confirma al cliente que la membresía será exonerada y que el ajuste se verá mañana.
```

# Controles mínimos

| Control | G1 | G2 | G3 | G4 |
|---|---:|---:|---:|---:|
| system prompt versionado | Sí | Sí | Sí | Sí |
| evaluación offline | No | Sí | Sí | Sí |
| RAG con fuentes versionadas | No | Sí | Sí | Sí |
| DLP entrada/salida | No | Sí | Sí | Sí |
| human-in-the-loop | No | No | Sí | Sí |
| tool permissioning | No | No | Según caso | Sí |
| audit trail | Básico | Sí | Sí | Sí |

# Política de autonomía

Un agente GenAI no puede ejecutar acciones financieras, cambios contractuales, reversos, bloqueos o aprobación de crédito sin control explícito de autorización, trazabilidad y confirmación humana.
