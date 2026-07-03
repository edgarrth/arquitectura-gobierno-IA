# AI Policy

# Propósito

Definir las reglas corporativas para el uso responsable, seguro, trazable y auditable de Inteligencia Artificial en una empresa regulada.

# Alcance

La política aplica a colaboradores, proveedores, terceros, squads, áreas de negocio, tecnología, analítica, auditoría, seguridad y cualquier equipo que diseñe, compre, use o integre soluciones de IA.

# Definiciones

## Sistema de IA

Sistema que usa técnicas estadísticas, machine learning, deep learning, modelos fundacionales, LLMs, reglas automatizadas o agentes para generar predicciones, recomendaciones, contenido, decisiones o acciones.

## Caso de uso de alto impacto

Caso que puede afectar derechos, acceso a productos, crédito, dinero, seguridad, privacidad, reputación o cumplimiento regulatorio.

## Shadow AI

Uso de herramientas o modelos de IA fuera de los canales aprobados por la empresa.

# Política general

Toda iniciativa de IA debe:

- Registrarse antes de su desarrollo o adquisición.
- Clasificarse por riesgo.
- Contar con owner de negocio y owner técnico.
- Usar datos autorizados.
- Documentar fuentes, supuestos y limitaciones.
- Ejecutar controles de seguridad y privacidad.
- Tener monitoreo proporcional al riesgo.
- Mantener evidencia auditable.

# Usos permitidos

| Uso | Condición |
|---|---|
| Detección de fraude | Con validación independiente y monitoreo |
| Scoring crediticio | Con explicabilidad, revisión humana y cumplimiento |
| Copilotos internos | Sin exposición de datos sensibles no autorizados |
| RAG documental | Con fuentes controladas y trazabilidad |
| Automatización de back office | Con segregación de funciones |
| Marketing personalizado | Con consentimiento y reglas de privacidad |

# Usos restringidos

| Uso | Restricción |
|---|---|
| Aprobación automática de crédito | Requiere revisión humana y derecho de explicación |
| Bloqueo de transacciones | Requiere reglas de reversión y atención al cliente |
| Fine-tuning con datos personales | Requiere evaluación legal, privacidad y anonimización |
| Agentes con ejecución de pagos | Requiere controles transaccionales y límites explícitos |

# Usos prohibidos

- Cargar datos sensibles en herramientas públicas no aprobadas.
- Usar PAN completo, CVV, claves, tokens, secretos o credenciales en prompts.
- Implementar modelos críticos sin aprobación formal.
- Usar IA para decisiones discriminatorias.
- Desplegar agentes autónomos sin límites, logging y mecanismo de apagado.
- Usar modelos de terceros sin evaluación de riesgo de proveedor.

# Clasificación de riesgo

| Tier | Descripción | Ejemplos |
|---|---|---|
| Tier 1 | Crítico | Scoring, fraude, decisiones financieras |
| Tier 2 | Alto | Copilotos cliente, cobranzas, KYC |
| Tier 3 | Medio | Productividad interna, análisis documental |
| Tier 4 | Bajo | Búsqueda interna, clasificación no sensible |

# Reglas de datos

- Usar solo datos con propósito autorizado.
- Minimizar PII.
- Enmascarar datos sensibles.
- Tokenizar identificadores críticos.
- Mantener linaje y retención.
- Validar calidad antes de entrenamiento o inferencia.

# Reglas GenAI

- Todo prompt productivo debe pasar por controles de seguridad.
- Las respuestas de alto impacto deben incluir fuentes o explicación.
- Las respuestas con baja confianza deben escalar a humano.
- Todo sistema RAG debe registrar documentos recuperados.
- Los agentes deben operar con permisos mínimos.

# Incumplimiento

El incumplimiento de esta política puede generar:

- Suspensión del sistema de IA.
- Bloqueo de acceso a herramientas.
- Revisión de seguridad.
- Reporte a Compliance o Auditoría.
- Plan de remediación obligatorio.
