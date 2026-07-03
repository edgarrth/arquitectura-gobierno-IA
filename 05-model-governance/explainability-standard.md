# Explainability Standard

# Propósito

Definir estándares de explicabilidad para modelos de IA usados en decisiones relevantes, especialmente en entornos regulados.

# Principios

| Principio | Descripción |
|---|---|
| Comprensible | explicaciones entendibles para usuario objetivo |
| Trazable | explicación conectada a datos y features |
| Consistente | misma entrada debe producir explicación equivalente |
| No engañosa | no debe ocultar limitaciones |
| Accionable | permite revisión, reclamo o mejora |

# Niveles de explicación

| Nivel | Audiencia | Ejemplo |
|---|---|---|
| Técnica | data science, model risk | SHAP, PDP, feature importance |
| Operativa | analistas de negocio | reason codes |
| Cliente | consumidor final | explicación simple y no discriminatoria |
| Auditoría | auditor interno/regulador | evidencia reproducible |

# Métodos permitidos

| Modelo | Técnica sugerida |
|---|---|
| scorecard | coeficientes y puntos |
| árbol/boosting | SHAP, feature importance |
| redes neuronales | saliency, embeddings analysis según caso |
| LLM/RAG | citas, grounding, trace de documentos |
| agentes | trace de plan, tools, decisiones y aprobaciones |

# Ejemplo: credit scoring

## Reason codes internos

| Código | Motivo |
|---|---|
| RC-001 | alto uso de línea disponible |
| RC-002 | historial reciente de mora |
| RC-003 | ingresos insuficientes respecto a deuda |
| RC-004 | antigüedad crediticia limitada |

## Explicación para cliente

```text
La solicitud requiere revisión adicional porque el nivel de endeudamiento reportado y el uso de líneas disponibles superan los límites de la política crediticia vigente.
```

# Prohibiciones

No usar explicaciones que:

- revelen reglas exactas explotables por fraude
- usen atributos sensibles injustificados
- sean demasiado técnicas para cliente final
- oculten que fue una recomendación de IA
- inventen razones no soportadas por el modelo

# Requisitos por tier

| Requisito | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|---|---:|---:|---:|---:|
| explicación local | Sí | Sí | Según caso | No |
| explicación global | Sí | Sí | Sí | No |
| reason codes | Sí | Sí | Según caso | No |
| documentación auditoría | Sí | Sí | Sí | No |
| explicación cliente | Si impacta cliente | Si impacta cliente | Según caso | No |
