# otel-example-zpages

A simple sample demonstrating how to enable and use **zPages** within a local OpenTelemetry Collector setup. zPages are in‑process HTTP endpoints designed for real‑time diagnostics without requiring external telemetry backends.

## 🛠️ Overview

- Launches an OpenTelemetry Collector, configured with the `zpages` extension.
- Exposes internal debugging endpoints (Tracez, Statsz, RPCz, TraceConfigz) under `/debug/...`.
- Lets you visualize traces, metrics, and configuration live, without needing Jaeger/Zipkin/etc.

## Features
- **Tracez**: aggregate running/completed spans in buckets, view sampled span details.

---

### Launch Example (Docker)
```bash
docker compose up --build
```


### Example config.yaml:
```yaml
extensions:
  zpages:

receivers:
  otlp:
    protocols:
      grpc:
      http:

service:
  extensions: [zpages]
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlp]
    metrics:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlp]
```

### Accessing zPages
Open in browser:
http://localhost:55679/debug/tracez

