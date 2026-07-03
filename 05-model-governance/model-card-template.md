# Model Card Template

# Identificación

| Campo | Valor |
|---|---|
| Model ID | MOD-FRAUD-XGB-003 |
| Nombre | Fraud Detection XGBoost |
| Versión | 3.2.0 |
| Owner negocio | Prevención de Fraude |
| Owner técnico | AI Engineering |
| Tier | Tier 1 |
| Estado | Validado / Producción |

# Propósito

Detectar transacciones con alta probabilidad de fraude y recomendar acción de autorización: aprobar, desafiar, retener o rechazar.

# Alcance

| Incluye | No incluye |
|---|---|
| transacciones POS y e-commerce | decisiones finales sin reglas de negocio |
| tarjetas activas | investigación manual de fraude |
| scoring near real-time | reclamos post-fraude |

# Datos

| Dataset | Periodo | Uso |
|---|---|---|
| DS-FRAUD-TRANSACTIONS-2024 | 2024-01 a 2024-12 | entrenamiento |
| DS-FRAUD-TRANSACTIONS-2025Q1 | 2025-01 a 2025-03 | validación temporal |

# Features principales

| Feature | Descripción | Sensibilidad |
|---|---|---|
| amount_local | monto de transacción | confidencial |
| merchant_category_code | rubro comercio | confidencial |
| velocity_5m | transacciones últimos 5 minutos | confidencial |
| geo_distance_last_tx_km | distancia vs última transacción | confidencial |
| device_risk_score | riesgo dispositivo | confidencial |

# Métricas

| Métrica | Valor | Umbral |
|---|---:|---:|
| AUC | 0.94 | >= 0.85 |
| Precision | 0.91 | >= 0.80 |
| Recall | 0.86 | >= 0.80 |
| FPR | 1.9% | <= apetito aprobado |
| P95 latency | 32 ms | <= 50 ms |

# Explainability

Método: SHAP global y reason codes por transacción.

Reason codes permitidos:

- monto inusual para cliente
- comercio de alto riesgo
- múltiples intentos recientes
- cambio geográfico no esperado
- dispositivo no reconocido

# Limitaciones

- Fraudes nuevos pueden no estar representados.
- El modelo depende de calidad de labels de chargeback.
- El modelo no debe usarse como única evidencia para reclamos.

# Monitoreo

| Métrica | Frecuencia | Umbral |
|---|---|---|
| PSI features críticas | semanal | < 0.25 |
| Recall estimado | mensual | >= 0.80 |
| FPR | diario | según apetito |
| Latencia P95 | continuo | <= 50 ms |

# Aprobaciones

| Rol | Estado |
|---|---|
| Business Owner | aprobado |
| Model Risk | aprobado |
| AI Office | aprobado |
| Security | aprobado |
| Compliance | aprobado |
