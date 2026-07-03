# AI Decision Rights RACI

# Objetivo

Definir quién propone, aprueba, valida, opera y audita las decisiones clave del ciclo de vida de IA.

# Roles

| Rol | Descripción |
|---|---|
| CAIO | Chief AI Officer o responsable corporativo de IA |
| AI Council | Comité ejecutivo multidisciplinario |
| Business Owner | Responsable del valor y resultado del caso |
| Model Owner | Responsable técnico/analítico del modelo |
| Data Owner | Responsable del dominio de datos |
| CISO | Responsable de seguridad |
| Compliance | Responsable regulatorio y legal |
| Model Risk | Validación independiente |
| Architecture Board | Revisión de arquitectura |
| Internal Audit | Auditoría independiente |

# RACI principal

| Actividad | CAIO | AI Council | Business Owner | Model Owner | Data Owner | CISO | Compliance | Model Risk | Architecture | Audit |
|---|---|---|---|---|---|---|---|---|---|---|
| Definir AI Policy | A | C | C | C | C | C | C | C | C | I |
| Registrar caso de uso | C | I | A/R | R | C | I | I | I | I | I |
| Clasificar riesgo | A | C | R | C | C | C | C | R | C | I |
| Aprobar caso crítico | C | A | R | C | C | C | C | C | C | I |
| Aprobar datos | C | I | C | C | A/R | C | C | I | I | I |
| Aprobar arquitectura | C | I | C | C | C | C | C | I | A/R | I |
| Validar modelo | C | I | I | R | C | C | C | A/R | I | I |
| Desplegar modelo | I | I | A | R | C | C | I | C | C | I |
| Monitorear producción | C | I | A | R | C | C | I | C | C | I |
| Gestionar incidente | A | C | R | R | C | C | C | C | C | I |
| Auditar sistema | I | I | I | C | C | C | C | C | C | A/R |

# Matriz de aprobación por riesgo

| Riesgo | Aprobación requerida |
|---|---|
| Bajo | Business Owner + AI Office |
| Medio | AI Office + Arquitectura + Seguridad |
| Alto | AI Council |
| Crítico | AI Council + Comité de Riesgos |

# Reglas

## Una sola accountability

Cada decisión debe tener un único accountable.

## Validación independiente

El Model Owner no puede ser el responsable final de la validación independiente del mismo modelo.

## Segregación de funciones

El equipo que desarrolla un modelo crítico no debe aprobarlo unilateralmente para producción.

# Ejemplo

Para un modelo de scoring crediticio:

- Business Owner define objetivo y acepta riesgo residual.
- Model Owner desarrolla y documenta.
- Data Owner aprueba datasets.
- Model Risk valida.
- Compliance revisa obligaciones legales.
- AI Council aprueba despliegue.
- Auditoría revisa evidencias posteriormente.
