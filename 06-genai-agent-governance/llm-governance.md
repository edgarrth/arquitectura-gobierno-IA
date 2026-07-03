# Gobierno de LLMs

# Propósito

Definir controles para el uso corporativo de modelos de lenguaje en una empresa regulada. Este estándar aplica a copilotos internos, asistentes de atención, generación de documentos, extracción de información, clasificación de reclamos, analítica aumentada y agentes autónomos o semi-autónomos.

# Principios

## Uso permitido

Los LLMs pueden usarse cuando existe un responsable de negocio, datos clasificados, evaluación de riesgo, controles de seguridad, monitoreo y evidencia auditable.

## Uso restringido

No se permite enviar información sensible sin controles de anonimización, tokenización o contrato de procesamiento aprobado.

## Decisión humana

Los LLMs no deben tomar decisiones finales en procesos regulados como crédito, fraude, seguros, sanciones, bloqueo de cuentas o atención de reclamos críticos sin revisión humana.

# Clasificación de casos LLM

| Nivel | Caso | Ejemplo | Control mínimo |
|---|---|---|---|
| L1 | Asistencia interna | resumen de políticas | logging básico |
| L2 | Cliente no decisional | chatbot informativo | guardrails + grounding |
| L3 | Operación sensible | asistente de reclamos | HITL + auditoría |
| L4 | Decisión regulada | recomendación de crédito | validación independiente + comité |

# Ejemplo realista

Caso: copiloto para ejecutivo de atención en tarjeta de crédito.

```json
{
  "interaction_id": "IA-CHAT-2025-10-000128",
  "business_domain": "customer_service",
  "customer_segment": "premium",
  "intent": "consulta_de_cargo_no_reconocido",
  "retrieved_policy": "POL-CHARGEBACK-VISA-2025",
  "grounding_confidence": 0.91,
  "hallucination_risk": "low",
  "human_review_required": true,
  "final_action_allowed": "draft_response_only"
}
```

# Controles obligatorios

## Entrada

- Detección de PII, PAN, CVV, claves, tokens y secretos.
- Bloqueo de prompt injection.
- Clasificación de intención.
- Validación de autorización del usuario.

## Modelo

- Registro del proveedor y versión.
- Evaluación de precisión, seguridad y sesgo.
- Pruebas de jailbreak.
- Configuración de temperatura y límites.

## Salida

- Filtro de datos sensibles.
- Verificación de grounding.
- Detección de alucinación.
- Revisión humana cuando el output afecte derechos, dinero o cumplimiento.

# Evidencia auditable

| Evidencia | Retención | Responsable |
|---|---:|---|
| prompt anonimizado | 2 años | AI Office |
| respuesta generada | 2 años | AI Office |
| fuentes RAG utilizadas | 5 años | Data Owner |
| evaluación de seguridad | 3 años | CISO |
| aprobación del caso | vida del modelo + 1 año | AI Council |

# Métricas mínimas

| Métrica | Umbral |
|---|---:|
| grounded answer rate | >= 95% |
| hallucination rate crítica | 0% |
| PII leakage | 0 |
| prompt injection blocked | >= 99% |
| satisfacción del agente humano | >= 4/5 |
