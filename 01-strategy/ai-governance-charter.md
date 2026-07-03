# AI Governance Charter

# Propósito

El AI Governance Charter formaliza la autoridad, alcance y responsabilidades de la Oficina de IA en una organización regulada. Su objetivo es asegurar que toda iniciativa de IA sea evaluada, aprobada, operada y auditada bajo criterios consistentes de valor, riesgo, cumplimiento, seguridad y ética.

# Mandato de la Oficina de IA

La Oficina de IA actúa como autoridad metodológica y de control para:

- Definir políticas corporativas de IA.
- Clasificar riesgos de casos de uso.
- Aprobar estándares de arquitectura, datos, seguridad y monitoreo.
- Mantener inventario de casos de uso, modelos, datasets y vendors.
- Coordinar validaciones independientes.
- Presentar reportes al comité de riesgos, tecnología y auditoría.

# Alcance

Aplica a iniciativas de IA desarrolladas internamente, compradas a terceros, integradas como SaaS o usadas mediante APIs externas.

Incluye:

- Modelos predictivos.
- Modelos generativos.
- Agentes autónomos o semiautónomos.
- RAG y asistentes conversacionales.
- Automatización de decisiones.
- Sistemas de recomendación.
- Sistemas de visión, OCR, voz o NLP.

# Principios de autoridad

## Autoridad de aprobación

Ningún sistema de IA de impacto alto o crítico debe pasar a producción sin aprobación formal del AI Governance Council.

## Autoridad de suspensión

La Oficina de IA puede recomendar la suspensión temporal de un modelo cuando existan señales de:

- Drift crítico.
- Sesgo material.
- Riesgo de seguridad.
- Incumplimiento regulatorio.
- Evidencia incompleta.
- Decisiones incorrectas con impacto al cliente.

## Autoridad de excepción

Las excepciones deben documentarse, aprobarse con vigencia limitada y tener plan de remediación.

# Modelo de accountability

| Rol | Accountability principal |
|---|---|
| Board / Comité de Riesgos | Supervisión del apetito de riesgo de IA |
| Chief AI Officer | Gobierno integral de IA |
| CIO / CTO | Plataforma, arquitectura y operación tecnológica |
| CRO | Riesgo de modelos y riesgo operacional |
| CISO | Seguridad, adversarial AI y protección de datos |
| Data Owner | Calidad, linaje y uso autorizado de datos |
| Model Owner | Performance, documentación y monitoreo del modelo |
| Internal Audit | Verificación independiente |

# Criterios de éxito

| Indicador | Meta |
|---|---:|
| Casos de uso registrados | 100% |
| Modelos críticos con validación independiente | 100% |
| Modelos con model card vigente | 100% |
| Modelos con monitoreo de drift | 100% |
| Incidentes IA Sev1 sin RCA | 0 |
| Excepciones vencidas | 0 |

# Ejemplo de aplicación

Una empresa financiera quiere desplegar un modelo de fraude transaccional. El caso se registra como Tier 1 porque puede bloquear operaciones de clientes. Antes de producción debe contar con model card, validación independiente, explicación SHAP, pruebas de sesgo por segmento, aprobación del AI Council y monitoreo de drift.

# Evidencias mínimas

- Acta de aprobación.
- Risk assessment.
- Model card.
- Data lineage.
- Resultado de validación independiente.
- Checklist de seguridad.
- Plan de monitoreo.
- Runbook de rollback.
