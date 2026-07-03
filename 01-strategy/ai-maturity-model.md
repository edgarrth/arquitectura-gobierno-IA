# AI Maturity Model

# Propósito

Evaluar el nivel de madurez de una organización en gobierno, riesgo, datos, modelos, GenAI, operación y auditoría de IA.

# Niveles de madurez

| Nivel | Nombre | Descripción |
|---:|---|---|
| 1 | Inicial | IA experimental, sin inventario ni controles consistentes |
| 2 | Gestionado | Existen políticas iniciales, casos registrados y revisiones manuales |
| 3 | Estandarizado | Procesos, templates y controles comunes para toda la empresa |
| 4 | Medido | Monitoreo continuo, KPIs, evidencia y auditoría recurrente |
| 5 | Optimizado | Gobierno automatizado, assurance continuo y mejora basada en métricas |

# Dominios evaluados

| Dominio | Nivel objetivo mínimo |
|---|---:|
| Estrategia y sponsorship ejecutivo | 3 |
| AI policy y principios éticos | 3 |
| Inventario de casos de uso | 4 |
| Data governance para IA | 3 |
| Model risk management | 4 |
| GenAI y agent governance | 3 |
| Seguridad de IA | 4 |
| MLOps / LLMOps | 4 |
| Auditoría y evidencias | 4 |
| Métricas de valor | 3 |

# Assessment

## Estrategia

| Pregunta | Puntaje 1-5 |
|---|---:|
| ¿Existe una estrategia de IA aprobada por dirección? |  |
| ¿Existe un CAIO o función equivalente? |  |
| ¿Hay presupuesto y roadmap priorizado? |  |

## Gobierno

| Pregunta | Puntaje 1-5 |
|---|---:|
| ¿Existe AI Policy corporativa? |  |
| ¿Existe AI Council multidisciplinario? |  |
| ¿Todos los casos de uso están registrados? |  |

## Riesgo

| Pregunta | Puntaje 1-5 |
|---|---:|
| ¿Los modelos se clasifican por riesgo? |  |
| ¿Los modelos críticos tienen validación independiente? |  |
| ¿Existen controles para sesgo, drift y explicabilidad? |  |

# Ejemplo de resultado

| Dominio | Puntaje | Nivel |
|---|---:|---|
| Estrategia | 3.4 | Estandarizado |
| Gobierno | 2.8 | Gestionado |
| Datos | 2.5 | Gestionado |
| Modelos | 3.1 | Estandarizado |
| GenAI | 2.2 | Gestionado |
| Seguridad | 3.6 | Estandarizado |
| Auditoría | 2.4 | Gestionado |

# Interpretación

Una empresa regulada no debería operar casos Tier 1 si su madurez de Model Risk, Seguridad y Auditoría está por debajo de 3.

# Plan de mejora

| Brecha | Acción | Plazo |
|---|---|---:|
| Inventario incompleto | Crear AI Use Case Registry | 30 días |
| Sin model cards | Adoptar template obligatorio | 60 días |
| Sin monitoreo de drift | Implementar ModelOps baseline | 90 días |
| Sin comité formal | Formalizar AI Council | 30 días |
