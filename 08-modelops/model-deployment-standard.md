# Estándar de Despliegue de Modelos

# Propósito

Definir patrones seguros para promover modelos desde desarrollo hasta producción.

# Ambientes

| Ambiente | Uso |
|---|---|
| dev | exploración y experimentación |
| test | integración |
| staging | validación preproducción |
| prod | inferencia productiva |

# Estrategias de despliegue

| Estrategia | Uso recomendado |
|---|---|
| shadow | validar sin impactar clientes |
| canary | liberar a porcentaje controlado |
| blue/green | rollback rápido |
| champion/challenger | comparar modelos |

# Checklist preproducción

- model card aprobado,
- validación independiente,
- pruebas de seguridad,
- monitoreo configurado,
- rollback probado,
- owner operativo definido,
- runbook publicado.

# Ejemplo realista

```yaml
deployment_id: DEPLOY-FRD-2025-021
model: FRD-XGB-TRANSACTION-v3.3
strategy: champion_challenger
traffic_candidate: 10%
rollback_model: FRD-XGB-TRANSACTION-v3.2
approval: AI Office + Fraud Owner + Model Risk
```
