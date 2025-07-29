from opentelemetry import trace, metrics
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter

trace.set_tracer_provider(
    TracerProvider(resource=Resource.create({SERVICE_NAME: "demo-service"}))
)
tracer = trace.get_tracer(__name__)

# OTLP via HTTP
otlp_exporter = OTLPSpanExporter(
    endpoint="http://otel-collector:4317/v1/traces"
)
trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(otlp_exporter)
)

while True:
    with tracer.start_as_current_span("fake-span"):
        print("Enviando trace...")
    import time
    time.sleep(1)
