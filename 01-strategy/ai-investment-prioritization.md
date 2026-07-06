# AI Investment Prioritization

# Objetivo

Priorizar iniciativas de IA con criterios balanceados de valor, riesgo, 
factibilidad, cumplimiento y capacidad operativa.

# Principio

No toda iniciativa de IA debe aprobarse por entusiasmo tecnológico. 
La priorización debe demostrar valor medible, riesgo aceptable y capacidad de operación responsable.

# Criterios de priorización

| Criterio | Peso |
|---|---:|
| Valor económico o eficiencia | 25% |
| Impacto en cliente | 15% |
| Riesgo regulatorio | 15% |
| Disponibilidad y calidad de datos | 15% |
| Factibilidad técnica | 10% |
| Capacidad de monitoreo | 10% |
| Alineamiento estratégico | 10% |

# Escala

| Puntaje | Significado |
|---:|---|
| 1 | Muy bajo |
| 2 | Bajo |
| 3 | Medio |
| 4 | Alto |
| 5 | Muy alto |

# Fórmula

```text
Score = sum(puntaje_criterio * peso_criterio)
```

# Ejemplo de portfolio

| Caso de uso | Valor | Cliente | Riesgo | Datos | Técnica | Monitoreo | Estrategia | Score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Fraude transaccional | 5 | 5 | 4 | 5 | 4 | 5 | 5 | 4.75 |
| Copiloto de atención | 4 | 5 | 3 | 4 | 4 | 3 | 5 | 4.05 |
| Scoring crediticio ML | 5 | 4 | 5 | 4 | 4 | 4 | 5 | 4.45 |
| Resumen interno de actas | 3 | 2 | 2 | 4 | 5 | 3 | 3 | 3.25 |
| Recomendación comercial | 4 | 4 | 3 | 4 | 3 | 3 | 4 | 3.70 |

# Matriz de decisión

| Score | Decisión |
|---:|---|
| >= 4.3 | Prioridad estratégica |
| 3.5 - 4.29 | Prioridad táctica |
| 2.8 - 3.49 | Evaluar piloto controlado |
| < 2.8 | No priorizar |

# Ajuste por riesgo

Los casos con riesgo alto o crítico no se rechazan automáticamente, pero requieren:

- Business case aprobado.
- Evaluación de impacto.
- Validación independiente.
- Controles de supervisión humana.
- Monitoreo post-producción.

# Ejemplo realista de business case

## Caso: fraude transaccional

| Métrica | Valor estimado |
|---|---:|
| Transacciones anuales | 150,000,000 |
| Tasa histórica de fraude | 0.35% |
| Pérdida promedio por fraude | PEN 420 |
| Reducción esperada | 18% |
| Ahorro anual estimado | PEN 39,690,000 |

# Reglas de aprobación

| Tipo de caso | Aprobación mínima |
|---|---|
| Bajo riesgo | Product Owner + AI Office |
| Medio riesgo | AI Office + Arquitectura + Seguridad |
| Alto riesgo | AI Council |
| Crítico | AI Council + Comité de Riesgos |

# Señales de rechazo

- No existe owner claro.
- No hay datos suficientes o linaje verificable.
- El caso implica decisión crítica sin revisión humana.
- No puede monitorearse en producción.
- El vendor no entrega evidencia de seguridad o explicabilidad.
