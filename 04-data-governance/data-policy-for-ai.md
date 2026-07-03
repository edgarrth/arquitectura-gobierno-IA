# Data Policy for AI

# Propósito

Definir reglas para el uso responsable, seguro, trazable y auditable de datos en iniciativas de IA.

# Principios

| Principio | Regla |
|---|---|
| Minimización | usar solo datos necesarios para el objetivo |
| Propósito legítimo | cada uso debe tener finalidad aprobada |
| Calidad | datos deben cumplir reglas mínimas de completitud y consistencia |
| Trazabilidad | origen y transformaciones deben ser auditables |
| Protección | PII, datos financieros y credenciales deben protegerse |
| Reproducibilidad | datasets de entrenamiento deben poder reconstruirse |

# Clasificación de datos

| Nivel | Ejemplo | Tratamiento |
|---|---|---|
| Público | catálogo de productos público | uso libre controlado |
| Interno | políticas internas | RBAC |
| Confidencial | comportamiento de consumo, score, reclamos | cifrado + acceso limitado |
| Restringido | PAN, CVV, DNI, biometría, secretos | tokenización, masking, DLP |

# Datos prohibidos para GenAI externo

No se permite enviar a proveedores externos de LLM:

- PAN completo
- CVV
- contraseñas
- tokens de sesión
- claves API
- DNI sin anonimización
- datos de clientes no minimizados
- información regulada sin contrato y evaluación de tercero

# Ejemplo realista: variables de transacciones

Basado en esquemas usuales de fraude de tarjetas y datasets públicos de fraude transaccional.

| Campo | Clasificación | Uso permitido |
|---|---|---|
| transaction_amount | confidencial | entrenamiento y scoring |
| merchant_category_code | interno/confidencial | feature de riesgo |
| card_token | restringido | join controlado |
| pan | restringido | no usar directamente |
| device_fingerprint | confidencial | riesgo de dispositivo |
| chargeback_label | confidencial | etiqueta supervisada |

# Reglas para entrenamiento

| Regla | Descripción |
|---|---|
| Snapshot versionado | cada dataset de entrenamiento debe tener versión |
| Data split reproducible | train/validation/test deben poder reconstruirse |
| No leakage | variables posteriores a la decisión no pueden usarse en entrenamiento |
| Consent/legal basis | datos personales requieren base legal o consentimiento aplicable |
| Retention | datasets deben tener política de retención |

# Checklist

- [ ] Dataset registrado
- [ ] Owner asignado
- [ ] Data steward asignado
- [ ] Clasificación de sensibilidad
- [ ] Reglas de calidad definidas
- [ ] Lineage documentado
- [ ] Privacy review completado
- [ ] Accesos aprobados
- [ ] Retención definida
- [ ] Evidencia almacenada
