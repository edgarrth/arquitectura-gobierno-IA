# Template — AI Risk Assessment

> Nota de datos: los ejemplos usan datos realistas de industria financiera regulada y patrones operativos típicos de banca, tarjetas, seguros y fintech. No contienen datos productivos, PII real, PAN real ni información confidencial de ninguna empresa.

# Identificación

| Campo | Valor |
|---|---|
| Assessment ID | AIRISK-2026-0001 |
| AI System ID | AI-SCR-002 |
| Nombre | Credit Scoring |
| Owner negocio | Riesgo Crediticio |
| Owner técnico | Data Science |
| Evaluador | Model Risk |
| Fecha | 2026-07-02 |

# Contexto

Modelo de scoring para estimar probabilidad de incumplimiento en solicitudes de tarjeta de crédito.

# Clasificación

| Criterio | Valor |
|---|---|
| Impacta acceso a crédito | Sí |
| Usa PII | Sí |
| Usa datos sensibles | No |
| Toma decisión automática | Parcial |
| Requiere explicabilidad | Sí |
| Requiere supervisión humana | Sí |
| Tier propuesto | Tier 1 |

# Matriz de riesgos

| Riesgo | Probabilidad | Impacto | Score | Tratamiento |
|---|---:|---:|---:|---|
| Sesgo por segmento | 3 | 5 | 15 | Mitigar |
| Drift macroeconómico | 4 | 4 | 16 | Mitigar |
| Data leakage | 2 | 5 | 10 | Mitigar |
| Falta explicabilidad | 3 | 5 | 15 | Mitigar |
| Rechazo erróneo masivo | 2 | 5 | 10 | Mitigar |

# Controles obligatorios

| Control | Requerido |
|---|---|
| AI Council approval | Sí |
| Independent validation | Sí |
| Model Card | Sí |
| Dataset Card | Sí |
| SHAP / reason codes | Sí |
| Manual review channel | Sí |
| Customer appeal process | Sí |
| Monitoring dashboard | Sí |

# Decisión

| Resultado | Seleccionar |
|---|---|
| Aprobado | ☐ |
| Aprobado condicionado | ☐ |
| Rechazado | ☐ |
| Requiere rediseño | ☐ |
