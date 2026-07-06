# Clasificación de riesgo y controles mínimos

> Nota: todos los ejemplos y registros usan datos simulados realistas para una fintech. No contienen datos productivos, PII real, PAN real, secretos, credenciales ni información confidencial.

# Objetivo

Definir una metodología de riesgo proporcional para que los squads sepan qué controles aplicar sin crear documentación excesiva.

# Taxonomía de riesgo

| Tier | Riesgo | Criterio fintech | Ejemplos |
|---|---|---|---|
| Tier 0 | Prohibido | Uso no aceptado por política o regulación | manipulación, discriminación, uso oculto de PII |
| Tier 1 | Crítico | Impacta acceso a crédito, dinero, fondos, fraude, límites o derechos del cliente | scoring, fraude con retención, límites de crédito |
| Tier 2 | Alto | Impacta cliente u operación crítica con supervisión humana | KYC OCR, cobranzas, copiloto de reclamos |
| Tier 3 | Medio | Recomienda o prioriza, con bajo impacto directo | cross-sell, RAG interno, segmentación |
| Tier 4 | Bajo | Productividad interna sin datos sensibles críticos | resumen documental, clasificación interna |

# Scoring simple

Usar escala 1 a 5 por dimensión.

| Dimensión | Peso | 1 bajo | 5 alto |
|---|---:|---|---|
| Impacto en cliente | 20% | interno | afecta dinero, crédito o atención |
| Autonomía | 15% | solo informa | ejecuta o decide |
| Datos sensibles | 15% | sin PII | PII, financiera, biométrica o PCI |
| Regulación | 15% | sin obligación relevante | SBS, privacidad, PCI, AML, auditoría |
| Explicabilidad | 10% | explicable | caja negra crítica |
| Robustez | 10% | bajo impacto ante error | error genera pérdida/reclamo |
| Seguridad | 10% | aislado | expone datos, herramientas o secretos |
| Terceros | 5% | interno controlado | proveedor crítico o modelo cerrado |

# Conversión de score a tier

| Score ponderado | Tier sugerido | Tratamiento |
|---:|---|---|
| >= 4.20 | Tier 1 | AI Council + validación independiente |
| 3.20 - 4.19 | Tier 2 | AI Office + revisión de riesgo/seguridad |
| 2.20 - 3.19 | Tier 3 | Fast track + controles base |
| < 2.20 | Tier 4 | Registro + monitoreo básico |

# Controles mínimos por dominio

| ID | Control | Tier 1 | Tier 2 | Tier 3 | Tier 4 | Evidencia |
|---|---|---:|---:|---:|---:|---|
| GOV-001 | Caso registrado en AI Portfolio | Sí | Sí | Sí | Sí | use case register |
| GOV-002 | Owner negocio/técnico/riesgo | Sí | Sí | Sí | Básico | RACI |
| RSK-001 | Risk assessment | Completo | Completo | Lite | Lite | risk assessment |
| DAT-001 | Data owner y propósito autorizado | Sí | Sí | Si usa PII | No | data review |
| DAT-002 | Minimización/masking/tokenización | Sí | Sí | Si usa PII | No | privacy review |
| MOD-001 | Model/GenAI Card Lite | Sí | Sí | Sí | Opcional | model card |
| MOD-002 | Validación independiente | Sí | Según impacto | No | No | validation report |
| MOD-003 | Explainability/reason codes | Sí | Sí si cliente | Recomendado | No | explanation design |
| GEN-001 | Prompt/RAG versionado | Si aplica | Si aplica | Si aplica | Recomendado | prompt registry |
| GEN-002 | Guardrails y pruebas de alucinación | Si aplica | Si aplica | Si aplica | No | eval report |
| SEC-001 | Threat model IA | Sí | Sí | Básico | No | threat model |
| SEC-002 | DLP/secrets/logging seguro | Sí | Sí | Sí | Básico | security checklist |
| OPS-001 | Monitoreo de performance/drift | Sí | Sí | Básico | Básico | dashboard |
| OPS-002 | Rollback o kill switch | Sí | Sí | Si agente | No | runbook |
| AUD-001 | Evidence log | Sí | Sí | Sí | Sí | evidence pack |

# Ejemplo de risk assessment simulado

| Caso | Impacto | Autonomía | Datos | Regulación | Explicabilidad | Robustez | Seguridad | Terceros | Score | Tier |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| AI-UC-2026-001 Fraude CNP | 5 | 4 | 5 | 5 | 3 | 4 | 4 | 2 | 4.35 | Tier 1 |
| AI-UC-2026-003 Copiloto reclamos | 4 | 2 | 4 | 4 | 3 | 3 | 4 | 3 | 3.45 | Tier 2 |
| AI-UC-2026-004 RAG normativo | 2 | 1 | 2 | 3 | 3 | 2 | 3 | 2 | 2.20 | Tier 3 |
| AI-UC-2026-006 Cross-sell | 3 | 2 | 3 | 3 | 3 | 3 | 2 | 1 | 2.65 | Tier 3 |

# Reglas de escalamiento

Escalar al AI Council si ocurre cualquiera de estos eventos:

- el caso afecta crédito, dinero, bloqueo, acceso a servicios o atención crítica;
- usa datos sensibles, biometría o PCI;
- tiene decisión automatizada sin humano en el flujo;
- depende de proveedor estratégico o modelo cerrado;
- tiene incidente Sev1/Sev2;
- solicita excepción a controles obligatorios;
- hay drift crítico o degradación material de performance.

# Risk acceptance

| Riesgo residual | Acción |
|---|---|
| Bajo | Acepta AI Office |
| Medio | Acepta Risk Owner |
| Alto | Requiere plan de mitigación y aprobación AI Council |
| Crítico | No se libera salvo excepción formal con vencimiento |
