# Gobierno de RAG

# Propósito

Asegurar que las arquitecturas Retrieval Augmented Generation usen fuentes confiables, vigentes, trazables y autorizadas. En empresas reguladas, RAG no es solo una técnica; es un mecanismo de control de factualidad y cumplimiento.

# Principios

## Fuente autorizada

Solo se indexan documentos aprobados por un Data Owner o Knowledge Owner.

## Trazabilidad

Toda respuesta debe poder explicar qué documentos, fragmentos y versiones fueron usados.

## Vigencia

Documentos vencidos, derogados o archivados no deben usarse para respuestas productivas.

# Registro de fuentes

| source_id | documento | dominio | dueño | vigencia | clasificación |
|---|---|---|---|---|---|
| SRC-001 | Reglamento de tarjetas 2025 | Productos | Legal | vigente | interno |
| SRC-002 | Política de chargeback 2025 | Operaciones | Operaciones | vigente | confidencial |
| SRC-003 | Manual de atención de reclamos | Customer Service | CX | vigente | interno |

# Ejemplo realista de chunk auditado

```json
{
  "chunk_id": "CH-CHARGEBACK-2025-00034",
  "source_id": "SRC-002",
  "document_version": "2025.08",
  "section": "Plazos operativos",
  "classification": "confidential",
  "embedding_model": "text-embedding-3-large",
  "created_at": "2025-08-12T14:22:31-05:00",
  "approved_for_rag": true,
  "retention_policy": "5y"
}
```

# Controles de ingesta

| Control | Regla |
|---|---|
| RAG-001 | validar clasificación documental |
| RAG-002 | remover PII innecesaria antes de indexar |
| RAG-003 | registrar versión y checksum |
| RAG-004 | ejecutar quality gate de chunks |
| RAG-005 | excluir documentos vencidos |

# Controles de recuperación

- Top-k configurable por riesgo.
- Filtro por dominio y permisos del usuario.
- Ranking híbrido semántico + keyword.
- Umbral mínimo de similitud.
- Rechazo cuando no hay evidencia suficiente.

# Política de respuesta

El LLM debe responder con una de estas categorías:

| Categoría | Condición |
|---|---|
| Answered with evidence | evidencia suficiente |
| Needs human review | evidencia parcial |
| Refused | solicitud prohibida |
| Escalated | impacto regulado |

# Métricas

| Métrica | Objetivo |
|---|---:|
| retrieval precision@5 | >= 0.85 |
| groundedness | >= 0.90 |
| stale document usage | 0 |
| unauthorized source usage | 0 |
