# AI Council Operating Model

# Propósito

Establecer el modelo de funcionamiento del AI Governance Council como órgano de decisión y supervisión de IA.

# Objetivos del AI Council

- Aprobar políticas y estándares de IA.
- Priorizar casos estratégicos.
- Aprobar casos de alto riesgo o críticos.
- Revisar incidentes relevantes.
- Resolver excepciones.
- Supervisar KPIs de valor, riesgo y cumplimiento.

# Composición

| Miembro | Rol en el comité |
|---|---|
| CAIO | Presidente del comité |
| CIO / CTO | Tecnología y plataforma |
| CRO | Riesgo empresarial |
| CISO | Seguridad |
| Chief Data Officer | Datos y calidad |
| Legal / Compliance | Regulación y privacidad |
| Auditoría Interna | Observador independiente |
| Business Sponsor | Dueño del caso evaluado |

# Cadencia

| Sesión | Frecuencia |
|---|---|
| Sesión ordinaria | Mensual |
| Sesión de aprobación crítica | Bajo demanda |
| Revisión de portfolio | Trimestral |
| Revisión de incidentes Sev1 | Dentro de 48 horas |

# Agenda estándar

1. Revisión de acuerdos pendientes.
2. Nuevos casos de uso para aprobación.
3. Riesgos y excepciones.
4. Incidentes y lecciones aprendidas.
5. Métricas de valor y performance.
6. Decisiones y próximos pasos.

# Paquete de decisión

Todo caso de alto riesgo debe presentarse con:

- Business case.
- Risk assessment.
- Data assessment.
- Architecture review.
- Security review.
- Model card.
- Validation report.
- Monitoring plan.
- Human-in-the-loop design.
- Rollback plan.

# Decisiones posibles

| Decisión | Descripción |
|---|---|
| Approved | Puede avanzar según condiciones aprobadas |
| Approved with conditions | Avanza con controles pendientes y fecha límite |
| Deferred | Requiere información adicional |
| Rejected | No cumple criterios mínimos |
| Suspended | Se detiene temporalmente por riesgo |

# Quorum

Para aprobar casos críticos deben participar como mínimo:

- CAIO.
- CRO o delegado de riesgo.
- CISO o delegado de seguridad.
- Compliance.
- Business Sponsor.

# Acta mínima

Cada sesión debe registrar:

- Fecha.
- Participantes.
- Casos revisados.
- Riesgos identificados.
- Decisiones.
- Condiciones.
- Responsables.
- Fecha de revisión.

# Ejemplo de decisión

## Caso: Copiloto de atención para reclamos

| Campo | Valor |
|---|---|
| Riesgo | Alto |
| Decisión | Approved with conditions |
| Condiciones | Activar revisión humana para respuestas con confianza menor a 0.85 |
| Responsable | Head de Servicio al Cliente |
| Revisión | 30 días post go-live |
