# Data Quality Framework

# Propósito

Definir dimensiones, métricas, umbrales y controles de calidad de datos para IA.

# Dimensiones

| Dimensión | Pregunta |
|---|---|
| Completitud | ¿faltan datos críticos? |
| Validez | ¿cumple formato y dominio? |
| Consistencia | ¿coincide entre sistemas? |
| Unicidad | ¿hay duplicados indebidos? |
| Oportunidad | ¿llega a tiempo? |
| Exactitud | ¿representa el hecho real? |
| Estabilidad | ¿cambia dentro de límites esperados? |

# Umbrales sugeridos

| Tipo de dato | Métrica | Umbral |
|---|---|---:|
| Feature crítica Tier 1 | completitud | >= 99.5% |
| Feature no crítica | completitud | >= 95% |
| Labels de fraude | consistencia | >= 99% |
| Datos para RAG | vigencia documental | 100% documentos vigentes |
| Datos near real-time | latencia | <= 5 min |

# Ejemplo: fraude transaccional

| Feature | Regla | Severidad |
|---|---|---|
| amount_local | no nulo y mayor a 0 | crítica |
| transaction_timestamp | no futuro y zona horaria válida | crítica |
| merchant_category_code | pertenece a catálogo MCC | alta |
| card_token | no nulo | crítica |
| device_risk_score | entre 0 y 1 | alta |
| fraud_confirmed | booleano válido | crítica para training |

# Ejemplo: crédito

| Feature | Regla | Severidad |
|---|---|---|
| debt_to_income_ratio | 0 <= valor <= 1.5 | alta |
| credit_utilization | 0 <= valor <= 1 | alta |
| days_past_due_12m | entero >= 0 | alta |
| income_verified | booleano | media |
| bureau_score | rango según bureau | alta |

# Acciones por falla

| Severidad | Acción |
|---|---|
| Crítica | bloquear entrenamiento o inferencia |
| Alta | alertar y activar fallback |
| Media | registrar issue y corregir en SLA |
| Baja | seguimiento en backlog |

# Evidencia

- reporte de calidad por dataset
- logs de reglas ejecutadas
- porcentaje de fallas
- acciones correctivas
- aprobación de excepción si aplica
