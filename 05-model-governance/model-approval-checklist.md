# Model Approval Checklist

# Propósito

Checklist formal para aprobación de modelos antes de producción.

# Información general

| Campo | Valor |
|---|---|
| Model ID |  |
| Versión |  |
| Owner negocio |  |
| Owner técnico |  |
| Tier |  |
| Fecha |  |

# Checklist de negocio

- [ ] Caso de uso aprobado
- [ ] Beneficio esperado cuantificado
- [ ] Dueño de negocio asignado
- [ ] Criterio de éxito definido
- [ ] Impacto en cliente documentado
- [ ] Procedimiento de atención de reclamos definido

# Checklist de datos

- [ ] Dataset registrado
- [ ] Lineage documentado
- [ ] Calidad validada
- [ ] PII protegida
- [ ] No hay leakage
- [ ] Retención definida
- [ ] Accesos aprobados

# Checklist de modelo

- [ ] Model card completo
- [ ] Métricas cumplen umbral
- [ ] Validación out-of-time completada
- [ ] Bias/fairness evaluado
- [ ] Explainability disponible
- [ ] Reproducibilidad validada
- [ ] Limitaciones documentadas

# Checklist de seguridad

- [ ] Autenticación y autorización definidas
- [ ] Secrets protegidos
- [ ] Logs con masking
- [ ] Pruebas adversariales según tier
- [ ] Dependencias escaneadas
- [ ] Endpoint protegido por rate limit

# Checklist operativo

- [ ] SLOs definidos
- [ ] Monitoreo configurado
- [ ] Alertas configuradas
- [ ] Rollback probado
- [ ] Runbook operativo
- [ ] Soporte asignado

# Decisión

| Resultado | Marcar |
|---|---:|
| Aprobado | [ ] |
| Aprobado con condiciones | [ ] |
| Rechazado | [ ] |
| Requiere revalidación | [ ] |

# Condiciones

```text
Registrar condiciones, responsables y fecha compromiso.
```
