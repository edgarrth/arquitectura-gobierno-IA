# Template — AI Audit Report

> Nota de datos: los ejemplos usan datos realistas de industria financiera regulada y patrones operativos típicos de banca, tarjetas, seguros y fintech. No contienen datos productivos, PII real, PAN real ni información confidencial de ninguna empresa.

# Resumen ejecutivo

| Campo | Valor |
|---|---|
| Audit ID | AIAUD-2026-0001 |
| Sistema | AI-FRD-001 |
| Nombre | Motor de fraude transaccional |
| Tier | Tier 1 |
| Periodo auditado | 2026-Q2 |
| Resultado | Aprobado condicionado |
| Hallazgos críticos | 0 |
| Hallazgos altos | 2 |
| Hallazgos medios | 3 |

# Alcance

La auditoría evaluó gobierno, datos, modelo, seguridad, operación, incidentes y compliance.

# Criterios

- AI Governance Framework interno
- NIST AI RMF
- ISO/IEC 42001
- SR 11-7
- PCI DSS cuando aplica
- Política interna de datos

# Hallazgos

## AIAUD-FND-001

| Campo | Valor |
|---|---|
| Severidad | Alta |
| Dominio | Datos |
| Control | CTRL-DATA-004 |
| Descripción | Feature `merchant_risk_score` no tiene evidencia completa de validación post-cambio. |
| Riesgo | Drift no detectado y falsos positivos elevados. |
| Recomendación | Crear quality gate obligatorio previo a despliegue. |
| Owner | Data Platform |
| SLA | 30 días |

## AIAUD-FND-002

| Campo | Valor |
|---|---|
| Severidad | Alta |
| Dominio | Modelo |
| Control | CTRL-MODEL-002 |
| Descripción | Validación independiente no actualizada para último threshold. |
| Riesgo | Decisión no aprobada formalmente. |
| Recomendación | Revalidar threshold y registrar aprobación. |
| Owner | Model Risk |
| SLA | 30 días |

# Conclusión

El sistema mantiene controles operativos adecuados, pero requiere remediar debilidades de validación independiente y quality gates antes del próximo ciclo de auditoría.
