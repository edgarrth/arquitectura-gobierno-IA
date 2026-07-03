# AI Value Realization

> Nota de datos: los ejemplos usan datos realistas de industria financiera regulada y patrones operativos típicos de banca, tarjetas, seguros y fintech. No contienen datos productivos, PII real, PAN real ni información confidencial de ninguna empresa.

# Objetivo

Medir el valor económico, operativo, regulatorio y estratégico generado por IA.

# Categorías de valor

| Categoría | Ejemplo |
|---|---|
| Revenue uplift | Next best offer |
| Cost reduction | Copiloto de atención |
| Loss avoidance | Fraud detection |
| Risk reduction | Alertas tempranas |
| Productivity | Automatización documental |
| Compliance | Auditoría continua |

# Fórmulas

## Fraude evitado

```text
Fraud Loss Avoided = Fraud Amount Prevented - False Positive Cost - Operational Cost
```

## Cobranzas

```text
Collections Uplift = Recovery With AI - Recovery Baseline - Campaign Cost
```

## Copiloto

```text
Productivity Value = AHT Reduction × Interactions × Cost per Minute
```

# Ejemplo: fraude

| Métrica | Valor |
|---|---:|
| Transacciones evaluadas/mes | 14.2MM |
| Fraude detectado adicional | PEN 1.35MM |
| Costo falsos positivos | PEN 180K |
| Costo operación IA | PEN 95K |
| Valor neto mensual | PEN 1.075MM |
| Valor anualizado | PEN 12.9MM |

# Ejemplo: contact center

| Métrica | Valor |
|---|---:|
| Interacciones mensuales | 420,000 |
| AHT baseline | 6.8 min |
| AHT con copiloto | 5.9 min |
| Reducción | 0.9 min |
| Costo por minuto | PEN 0.85 |
| Valor mensual neto | PEN 249,300 |

# Reglas de validación

## Tier 1 y Tier 2

- Finanzas valida baseline.
- Riesgos valida supuestos.
- Auditoría puede revisar trazabilidad.
- Separar valor bruto y neto.

## GenAI

- Medir tokens.
- Medir costo de inferencia.
- Medir costo humano residual.
- Medir ahorro contra baseline comparable.
