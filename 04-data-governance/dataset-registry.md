# Dataset Registry

# Propósito

Mantener inventario auditado de datasets usados para entrenamiento, validación, evaluación, monitoreo y RAG.

# Campos obligatorios

| Campo | Descripción |
|---|---|
| Dataset ID | identificador único |
| Nombre | nombre funcional |
| Dominio | cliente, tarjeta, fraude, crédito, reclamos, marketing |
| Owner | responsable de negocio |
| Steward | responsable de calidad y definiciones |
| Clasificación | público, interno, confidencial, restringido |
| Uso permitido | entrenamiento, scoring, RAG, reporting |
| Fuente | sistemas origen |
| Frecuencia | batch, near real-time, real-time |
| Retención | tiempo aprobado |
| Lineage | link o diagrama |

# Registro ejemplo

## DS-FRAUD-TRANSACTIONS-2024

| Campo | Valor |
|---|---|
| Dominio | Fraud & Payments |
| Owner | Gerencia de Prevención de Fraude |
| Steward | Data Steward de Tarjetas |
| Clasificación | Confidencial / Restringido |
| Fuentes | switch transaccional, core tarjetas, chargebacks, device intelligence |
| Uso permitido | entrenamiento, validación, monitoreo de fraude |
| Retención | 5 años o según política corporativa |
| Actualización | near real-time para scoring; mensual para entrenamiento |

## Ejemplo de esquema

| Campo | Tipo | Clasificación | Descripción |
|---|---|---|---|
| transaction_id | string | interno | ID transacción |
| transaction_timestamp | timestamp | confidencial | fecha/hora |
| amount_local | decimal | confidencial | monto en moneda local |
| merchant_category_code | string | confidencial | MCC |
| country_code | string | confidencial | país comercio |
| card_present | boolean | confidencial | tarjeta presente |
| device_risk_score | decimal | confidencial | score de dispositivo |
| fraud_confirmed | boolean | confidencial | etiqueta confirmada |

# Datasets públicos recomendados para pruebas no productivas

| Dataset público | Uso recomendado |
|---|---|
| IEEE-CIS Fraud Detection | benchmarking de fraude transaccional |
| UCI Default of Credit Card Clients | scoring y default prediction |
| Home Credit Default Risk | originación crediticia |
| Lending Club Loan Data | riesgo de crédito y pricing |

# Política

Los datasets públicos se pueden usar para aceleración metodológica, pruebas de pipelines, documentación y capacitación, pero no reemplazan validación con datos internos aprobados.
