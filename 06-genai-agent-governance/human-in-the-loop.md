# Human-in-the-Loop

# Propósito

Definir cuándo y cómo una persona debe revisar, aprobar, rechazar o corregir una recomendación o acción generada por IA.

# Casos obligatorios de revisión humana

| Caso | Revisión requerida |
|---|---|
| rechazo de crédito | siempre |
| bloqueo de tarjeta | siempre |
| respuesta formal a reclamo regulado | siempre |
| ajuste de línea de crédito | siempre |
| reporte a regulador | siempre |
| acción irreversible sobre cliente | siempre |

# Niveles de revisión

| Nivel | Responsable | Ejemplo |
|---|---|---|
| H1 | operador | validar respuesta sugerida |
| H2 | supervisor | aprobar excepción |
| H3 | comité | aprobar modelo crítico |
| H4 | auditoría/riesgos | revisión independiente |

# Ejemplo realista

```json
{
  "case_id": "CLAIM-2025-004812",
  "ai_recommendation": "proceder con investigación de cargo no reconocido",
  "confidence": 0.88,
  "risk_tier": "high",
  "human_reviewer": "supervisor_operaciones",
  "decision": "approved_with_changes",
  "changes": "se ajustó plazo informado al cliente según política vigente",
  "review_timestamp": "2025-10-15T11:42:00-05:00"
}
```

# Reglas de diseño

- La interfaz debe mostrar evidencia, no solo la respuesta.
- El humano debe poder rechazar, editar o escalar.
- Cada decisión humana debe quedar registrada.
- La retroalimentación debe alimentar mejora continua.

# Métricas

| Métrica | Objetivo |
|---|---:|
| tiempo medio de revisión | < 10 min para operación |
| override rate | monitoreado por modelo |
| aprobaciones sin cambios | tendencia creciente |
| incidentes por falta de revisión | 0 |
