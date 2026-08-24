# Diagramas

Los diagramas Mermaid usados por el framework se renderizan directamente en la web. También puedes descargar los archivos fuente `.mmd`.

## Ciclo de vida agile de Gobierno de IA

[Descargar fuente Mermaid](diagrams/ai-governance-agile-lifecycle.mmd)

```mermaid
flowchart TD
    A[Idea IA] --> B[Intake 1 página]
    B --> C[Risk scoring]
    C --> D{Tier}
    D -->|Tier 0| X[Rechazar]
    D -->|Tier 1/2| E[AI Council]
    D -->|Tier 3/4| F[Fast Track AI Office]
    E --> G[AI Release Pack]
    F --> G[AI Release Pack Lite]
    G --> H[Build / Pilot]
    H --> I[Release Approval]
    I --> J[Operate / Monitor]
    J --> K[Audit Evidence]
    J --> L[Review / Retrain / Retire]
```

## Flujo del AI Release Pack

[Descargar fuente Mermaid](diagrams/ai-release-pack-flow.mmd)

```mermaid
flowchart LR
    A[Intake] --> P[AI Release Pack]
    B[Risk Assessment] --> P
    C[Data Review] --> P
    D[Model or GenAI Card] --> P
    E[Security Review] --> P
    F[Validation Summary] --> P
    G[Monitoring Plan] --> P
    H[Approvals] --> P
    P --> I[Release Decision]
    I --> J[Evidence Store]
```
