# Política y charter de IA lite

> Nota: todos los ejemplos y registros usan datos simulados realistas para una fintech. No contienen datos productivos, PII real, PAN real, secretos, credenciales ni información confidencial.

# Propósito

Definir las reglas corporativas mínimas para diseñar, comprar, integrar, operar y auditar soluciones de IA en una fintech. Este documento consolida política, charter y principios éticos en un solo artefacto.

# Alcance

Aplica a:

- modelos predictivos de fraude, crédito, cobranza, pricing, riesgo y marketing;
- soluciones GenAI, copilotos, RAG y asistentes internos;
- agentes que usan herramientas o ejecutan acciones;
- modelos open source, SaaS, APIs de terceros y modelos construidos internamente;
- datasets, prompts, features, embeddings, logs y evidencias asociadas.

# Principios corporativos

| Principio | Regla práctica |
|---|---|
| Legalidad y propósito | La IA solo usa datos con propósito autorizado y caso registrado. |
| Riesgo proporcional | Los controles se asignan por tier de riesgo. |
| Supervisión humana | Decisiones de alto impacto requieren revisión, apelación o intervención humana. |
| Transparencia | Toda decisión relevante debe ser explicable al negocio, auditoría o cliente cuando aplique. |
| Seguridad por diseño | No se exponen secretos, PAN, CVV, credenciales, tokens ni PII no autorizada. |
| Trazabilidad | Modelo, versión, datos, prompt, aprobación y resultado deben poder reconstruirse. |
| Accountability | Todo sistema de IA tiene Business Owner, Technical Owner y Risk Owner. |

# Usos permitidos

| Uso | Condición mínima |
|---|---|
| Detección de fraude | Validación, explainability, monitoreo de falsos positivos y rollback. |
| Scoring alternativo | Evaluación de sesgo, explicación, revisión humana y compliance. |
| Copiloto de atención | DLP, fuentes aprobadas, disclaimers internos y aprobación humana para acciones. |
| RAG normativo | Knowledge base versionada, trazabilidad de fuentes y medición de groundedness. |
| Automatización de conciliaciones | Agente con permisos mínimos, límites de ejecución y auditoría. |
| Segmentación comercial | Consentimiento, privacidad, monitoreo y exclusión de variables prohibidas. |

# Usos restringidos

| Uso | Restricción |
|---|---|
| Aprobación o denegación automática de crédito | Requiere Tier 1, validación independiente, explicación y human oversight. |
| Bloqueo automático de fondos o tarjeta | Requiere control transaccional, reversible, reglas de atención y monitoreo diario. |
| Fine-tuning con datos personales | Requiere privacy review, minimización, anonimización/tokenización y aprobación legal. |
| Agentes con capacidad de ejecutar acciones | Requieren tool registry, policy engine, límites, logs y kill switch. |
| Uso de proveedores externos IA | Requiere evaluación de seguridad, datos, residencia, entrenamiento y derecho de auditoría. |

# Usos prohibidos

- Cargar datos sensibles en herramientas públicas no aprobadas.
- Incluir PAN completo, CVV, claves, tokens, secretos, credenciales o llaves privadas en prompts, logs o datasets.
- Usar IA para decisiones discriminatorias o sin base de negocio legítima.
- Desplegar modelos Tier 1/2 sin AI Release Pack.
- Ejecutar agentes autónomos sin límites, logs y mecanismo de apagado.
- Usar datos personales para un propósito distinto al autorizado.
- Usar vendors IA sin evaluación de seguridad, privacidad y continuidad.

# Autoridad mínima

| Decisión | Autoridad |
|---|---|
| Aprobar política IA | Comité de Tecnología/Riesgos |
| Aprobar caso Tier 1 | AI Council |
| Aprobar caso Tier 2 | AI Council o AI Office según impacto |
| Aprobar caso Tier 3/4 | AI Office fast track |
| Suspender sistema IA | AI Lead + Risk Owner + CISO si aplica |
| Aprobar excepción crítica | Risk Owner + AI Lead + Compliance |
| Retirar modelo | Model Owner + AI Office |

# Clasificación de riesgo resumida

| Tier | Riesgo | Ejemplo fintech | Gobierno requerido |
|---|---|---|---|
| Tier 0 | Prohibido | IA discriminatoria o uso oculto de datos sensibles | Bloqueo |
| Tier 1 | Crítico | scoring crediticio, fraude con rechazo transaccional | AI Council + validación independiente |
| Tier 2 | Alto | cobranza, KYC OCR, copiloto cliente | AI Office + revisión de riesgos |
| Tier 3 | Medio | propensión comercial, RAG interno | Fast track + controles base |
| Tier 4 | Bajo | resumen interno, clasificación documental | Registro + controles mínimos |

# Criterio de incumplimiento

Un incumplimiento puede generar suspensión del sistema, retiro de acceso, plan de remediación, revisión de seguridad, reporte a Compliance o auditoría interna.

# Ejemplo realista de aplicación

| Caso | Resultado de política | Motivo |
|---|---|---|
| Copiloto que resume reclamos y redacta respuesta | Permitido con restricciones | Usa PII y puede impactar cliente; requiere HITL. |
| Modelo que ajusta límite de crédito sin revisión | Restringido/Tier 1 | Afecta acceso a producto financiero. |
| Chat público que recibe PAN completo | Prohibido | Exposición de PCI y datos sensibles. |
| RAG interno sobre manuales de cumplimiento | Permitido | Bajo impacto cliente si fuentes están controladas. |
