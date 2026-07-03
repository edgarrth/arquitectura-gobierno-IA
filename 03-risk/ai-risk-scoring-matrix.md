# AI Risk Scoring Matrix

# Objetivo

Estandarizar el cálculo de riesgo para iniciativas de IA y GenAI antes de inversión, desarrollo, compra o despliegue.

# Fórmula

```text
AI Risk Score = Impacto x Probabilidad x Exposición x Autonomía
```

Cada variable se califica de 1 a 5.

# Escala

| Score | Clasificación | Acción |
|---:|---|---|
| 1 - 25 | Bajo | aprobación por AI Office |
| 26 - 100 | Medio | controles mínimos + revisión técnica |
| 101 - 250 | Alto | comité de IA + risk assessment formal |
| 251 - 625 | Crítico | validación independiente + comité de riesgos |

# Dimensiones

## Impacto

| Valor | Definición |
|---:|---|
| 1 | productividad interna sin datos sensibles |
| 2 | recomendación interna reversible |
| 3 | impacto operativo limitado |
| 4 | impacto directo en cliente |
| 5 | impacto financiero, legal, reputacional o regulatorio |

## Probabilidad

| Valor | Definición |
|---:|---|
| 1 | improbable |
| 2 | baja |
| 3 | posible |
| 4 | probable |
| 5 | muy probable |

## Exposición

| Valor | Definición |
|---:|---|
| 1 | menos de 100 usuarios internos |
| 2 | área específica |
| 3 | múltiples áreas |
| 4 | clientes digitales |
| 5 | operación masiva / crítica |

## Autonomía

| Valor | Definición |
|---:|---|
| 1 | asistente informativo |
| 2 | recomendación con revisión humana |
| 3 | acción semiautomática |
| 4 | decisión automática reversible |
| 5 | decisión automática de alto impacto |

# Ejemplo 1: scoring crediticio

| Variable | Valor | Motivo |
|---|---:|---|
| Impacto | 5 | acceso a crédito |
| Probabilidad | 4 | error o bias posible por drift macroeconómico |
| Exposición | 5 | aplica a originación masiva |
| Autonomía | 4 | recomendación o decisión automática |

```text
Score = 5 x 4 x 5 x 4 = 400
Clasificación = Crítico
```

# Ejemplo 2: copilot de call center

| Variable | Valor | Motivo |
|---|---:|---|
| Impacto | 4 | puede orientar mal a clientes |
| Probabilidad | 4 | riesgo de alucinación e instrucciones incorrectas |
| Exposición | 4 | uso diario en atención |
| Autonomía | 2 | agente humano revisa respuesta |

```text
Score = 4 x 4 x 4 x 2 = 128
Clasificación = Alto
```

# Controles por score

| Control | Bajo | Medio | Alto | Crítico |
|---|---:|---:|---:|---:|
| AI intake | Sí | Sí | Sí | Sí |
| Data privacy review | Según caso | Sí | Sí | Sí |
| Security review | Según caso | Sí | Sí | Sí |
| Model card | No | Sí | Sí | Sí |
| Explainability | No | Según caso | Sí | Sí |
| Independent validation | No | No | Según caso | Sí |
| Continuous monitoring | No | Sí | Sí | Sí |
| Board/Risk reporting | No | No | Trimestral | Mensual |
