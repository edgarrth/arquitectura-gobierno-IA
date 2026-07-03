# Seguridad de IA de Terceros

# Propósito

Evaluar y controlar riesgos de modelos, APIs, plataformas y vendors externos de IA.

# Evaluación mínima

| Dimensión | Pregunta |
|---|---|
| datos | ¿usa nuestros datos para entrenar? |
| residencia | ¿dónde se procesan y almacenan los datos? |
| retención | ¿cuánto tiempo conserva prompts/respuestas? |
| seguridad | ¿tiene cifrado y controles de acceso? |
| auditoría | ¿entrega logs o reportes? |
| continuidad | ¿hay SLA y plan de salida? |

# Matriz de riesgo de proveedor

| Riesgo | Bajo | Medio | Alto |
|---|---|---|---|
| datos sensibles | no procesa | procesa anonimizados | procesa PII/PCI |
| criticidad | soporte interno | cliente no decisional | decisión regulada |
| despliegue | privado | tenant dedicado | SaaS compartido |

# Ejemplo realista

```yaml
vendor: proveedor_llm_externo
use_case: copiloto de atención
processed_data: masked_customer_case
training_on_customer_data: false
data_retention: 30_days
region: us/eu
risk_level: medium
required_controls:
  - dpa_contract
  - no_training_clause
  - pii_masking
  - audit_logs
  - exit_plan
```

# Requisitos contractuales

- cláusula de no entrenamiento con datos corporativos,
- notificación de incidentes,
- derecho a evidencias de auditoría,
- borrado de datos,
- subprocesadores declarados,
- SLA y continuidad.
