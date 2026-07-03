# Validation Report Template

# Información del modelo

| Campo | Valor |
|---|---|
| Model ID |  |
| Versión |  |
| Tipo |  |
| Tier |  |
| Validador |  |
| Fecha |  |

# Resumen ejecutivo

```text
Describir conclusión: aprobado, aprobado con observaciones, rechazado o requiere remediación.
```

# Alcance de validación

- conceptual soundness
- calidad de datos
- performance
- estabilidad
- fairness/bias
- explainability
- seguridad
- operación

# Validación de datos

| Prueba | Resultado | Observación |
|---|---|---|
| completitud |  |  |
| consistencia |  |  |
| leakage |  |  |
| representatividad |  |  |
| outliers |  |  |

# Validación de performance

| Métrica | Train | Validation | Out-of-time | Umbral |
|---|---:|---:|---:|---:|
| AUC |  |  |  |  |
| Precision |  |  |  |  |
| Recall |  |  |  |  |
| F1 |  |  |  |  |

# Validación de estabilidad

| Variable | PSI | Estado |
|---|---:|---|
| amount_local |  |  |
| merchant_category_code |  |  |
| velocity_5m |  |  |

# Bias/Fairness

| Segmento | Métrica | Resultado | Delta |
|---|---|---:|---:|
| región | recall |  |  |
| canal | FPR |  |  |
| producto | approval rate |  |  |

# Hallazgos

| ID | Severidad | Hallazgo | Recomendación | Owner |
|---|---|---|---|---|
| VAL-001 | Alta |  |  |  |

# Decisión

| Decisión | Marcar |
|---|---:|
| Aprobado | [ ] |
| Aprobado con condiciones | [ ] |
| Rechazado | [ ] |

# Firmas

| Rol | Nombre | Fecha |
|---|---|---|
| Validador independiente |  |  |
| Model Risk |  |  |
| AI Office |  |  |
