# Bias and Fairness Standard

# Propósito

Definir cómo identificar, medir, mitigar y monitorear sesgos en modelos de IA.

# Alcance

Aplica a modelos que impactan:

- acceso a crédito
- límites o pricing
- fraude
- cobranza
- atención al cliente
- segmentación comercial sensible

# Atributos sensibles

La organización debe definir atributos protegidos según legislación aplicable y política interna. Cuando no puedan usarse directamente por privacidad, se pueden evaluar proxies permitidos y agregados, con aprobación de Legal/Compliance.

# Métricas

| Métrica | Uso |
|---|---|
| demographic parity | comparar tasas de aprobación o asignación |
| equal opportunity | comparar true positive rate |
| equalized odds | comparar TPR y FPR |
| calibration by group | verificar consistencia de scores |
| adverse impact ratio | detectar impacto desproporcionado |

# Ejemplo: crédito

| Segmento | Approval Rate | Default Rate | Observación |
|---|---:|---:|---|
| Lima | 42% | 3.2% | baseline |
| Provincias | 35% | 3.4% | revisar variables proxy |
| Canal digital | 48% | 3.0% | normal |
| Canal agencia | 31% | 3.8% | revisar sesgo operativo |

# Umbrales de alerta

| Señal | Acción |
|---|---|
| delta > 5 pp en métrica crítica | análisis obligatorio |
| delta > 10 pp | comité de IA |
| impacto adverso persistente | plan de mitigación |
| uso de proxy no aprobado | bloqueo del modelo |

# Mitigaciones

| Técnica | Ejemplo |
|---|---|
| pre-processing | balanceo, reweighing |
| in-processing | restricciones de fairness |
| post-processing | calibración por segmento permitida |
| governance | human review, policy override |

# Evidencia

- definición de segmentos evaluados
- justificación legal del uso de variables
- resultados por grupo
- decisión de aceptación o mitigación
- monitoreo post-producción
