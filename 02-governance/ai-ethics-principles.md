# AI Ethics Principles

# Propósito

Definir principios éticos aplicables al diseño, uso y operación de IA.

# Principios

## 1. Beneficio claro

Todo sistema de IA debe tener un propósito legítimo, medible y alineado a la estrategia corporativa.

## 2. No discriminación

Los modelos no deben generar impactos injustificados por ubicación, género, edad, condición socioeconómica u otras variables sensibles directas o indirectas.

## 3. Transparencia proporcional

Las personas afectadas por decisiones relevantes deben recibir una explicación comprensible y proporcional al impacto.

## 4. Responsabilidad humana

Siempre debe existir un responsable humano por los resultados, decisiones y operación del sistema.

## 5. Privacidad por diseño

La IA debe minimizar datos personales, proteger información sensible y respetar finalidad, consentimiento y retención.

## 6. Seguridad

Los sistemas deben protegerse contra fuga de datos, prompt injection, manipulación, abuso, extracción de modelos y accesos indebidos.

## 7. Robustez

Los modelos deben operar dentro de condiciones conocidas y degradarse de forma segura cuando encuentren datos anómalos.

## 8. Auditabilidad

Toda IA relevante debe mantener evidencias suficientes para revisión interna, auditoría y respuesta ante regulador.

# Ejemplos de aplicación

## Fraude

Un modelo puede bloquear una transacción sospechosa, pero debe existir canal de revisión para falsos positivos y trazabilidad del motivo.

## Scoring

Un modelo puede recomendar una línea de crédito, pero debe entregar factores principales y permitir revisión bajo reglas de negocio.

## Copiloto

Un copiloto puede sugerir respuesta a un asesor, pero no debe inventar políticas ni prometer beneficios sin fuente.

# Evaluación ética mínima

| Pregunta | Respuesta requerida |
|---|---|
| ¿El caso tiene propósito legítimo? | Sí |
| ¿Puede afectar a clientes o colaboradores? | Identificar impacto |
| ¿Usa variables sensibles? | Justificar o eliminar |
| ¿Existe explicación? | Documentar mecanismo |
| ¿Existe revisión humana? | Definir flujo |
| ¿Existe canal de reclamo? | Definir owner |

# Indicadores éticos

| Métrica | Umbral |
|---|---:|
| Diferencia de recall entre segmentos | <= 5% |
| Respuestas GenAI sin fuente en procesos críticos | 0 |
| Decisiones críticas sin explicación | 0 |
| Incidentes por uso indebido de IA | 0 |
