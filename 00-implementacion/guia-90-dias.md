# Guía de implementación en 90 días

# Objetivo

Implementar Gobierno de IA con enfoque agile, mínimo viable y auditable.

# Resultado esperado

Al día 90, la organización debe tener:

- inventario de casos de uso de IA, GenAI y agentes;
- política ligera aprobada;
- clasificación de riesgo por tier;
- AI Release Pack operativo;
- controles mínimos por tier;
- dashboard de KPIs y evidencia;
- comité liviano para casos Tier 1/2;
- proceso de excepción y gestión de incidentes.

# Roadmap

| Semana | Objetivo | Entregables |
|---|---|---|
| 1-2 | Alinear alcance y autoridad | Política lite, RACI, lista inicial de casos IA |
| 3-4 | Clasificar riesgos | Risk scoring, tier por caso, controles mínimos |
| 5-6 | Crear AI Release Pack | Templates intake, risk assessment, model card, exception request |
| 7-8 | Integrar con delivery agile | DoR/DoD para squads, evidencia en Jira/Git/GRC |
| 9-10 | Operación y monitoreo | Métricas ModelOps, logs, drift, incidentes, alertas |
| 11-12 | Auditoría y mejora | Dashboard, revisión de gaps, plan trimestral |

# Implementación por olas

## Ola 1: Control del inventario

Acciones mínimas:

- identificar herramientas de IA usadas por negocio y tecnología;
- registrar modelos internos, prompts críticos, RAGs, vendors y agentes;
- clasificar casos por impacto;
- bloquear shadow AI de alto riesgo.

## Ola 2: Gobierno proporcional

Regla:

- Tier 1 y 2 requieren aprobación formal.
- Tier 3 y 4 usan fast track.
- Todo caso necesita owner, tier, evidencia mínima y monitoreo proporcional.

## Ola 3: Controles embebidos en el delivery

Agregar criterios a DoR/DoD del squad:

| Ceremonia | Control de IA |
|---|---|
| Discovery | Intake + clasificación inicial |
| Refinement | riesgos, datos, seguridad, owner |
| Sprint build | pruebas, model card, prompt eval, lineage |
| Release | AI Release Pack aprobado |
| Operación | métricas, incidentes, drift, evidencia |

# Modelo mínimo de comité

El AI Council no debe revisar todo. Solo debe revisar:

- Tier 1;
- Tier 2 con impacto directo en cliente;
- agentes A3/A4;
- uso de datos sensibles;
- excepciones críticas;
- incidentes Sev1/Sev2;
- proveedores IA estratégicos.

# Definition of Ready para casos IA

Un caso puede entrar a discovery si tiene:

- sponsor de negocio;
- owner técnico;
- problema y métrica de éxito;
- fuentes de datos preliminares;
- clasificación de riesgo inicial;
- hipótesis de control humano;
- restricción legal/compliance identificada si aplica.

# Definition of Done para release IA

Un caso puede pasar a producción si tiene:

- AI Release Pack completo según tier;
- modelo, prompt, RAG o agente versionado;
- controles de seguridad implementados;
- monitoreo activo;
- rollback o kill switch documentado;
- owner operativo asignado;
- evidencia almacenada en repositorio auditable.

# Ejemplo de plan inicial con datos simulados

| Caso | Semana objetivo | Acción | Responsable |
|---|---:|---|---|
| AI-UC-2026-001 Fraude CNP | 4 | Validación Tier 1 y Release Pack completo | Riesgo Transaccional |
| AI-UC-2026-003 Copiloto reclamos | 6 | Prompt eval + DLP + HITL | Operaciones Cliente |
| AI-UC-2026-004 RAG normativo | 5 | Fuentes aprobadas + grounding | Compliance |
| AI-UC-2026-005 Agente conciliaciones | 8 | Límites de herramientas + aprobación humana | Operaciones Backoffice |

