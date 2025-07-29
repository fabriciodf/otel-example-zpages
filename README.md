# otel-example-zpages

A simple sample demonstrating how to enable and use **zPages** within a local OpenTelemetry Collector setup. zPages are in‑process HTTP endpoints designed for real‑time diagnostics without requiring external telemetry backends.


<img width="2204" height="1199" alt="image" src="https://github.com/user-attachments/assets/14f305ce-7b24-4aeb-8aed-eb4ed3ff7ba2" />


## 🛠️ Overview

- Launches an OpenTelemetry Collector, configured with the `zpages` extension.
- Exposes internal debugging endpoints (Tracez) under `/debug/...`.
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
receivers:
  otlp:
    protocols:
      http:
        endpoint: 0.0.0.0:4317

processors:
  batch:

exporters:
  debug:
    verbosity: detailed

extensions:
  zpages:
    endpoint: 0.0.0.0:55679

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [debug]

    metrics:
      receivers: [otlp]
      processors: [batch]
      exporters: [debug]

  extensions: [zpages]
```

### Accessing zPages
Open in browser:
http://localhost:55679/debug/tracez

