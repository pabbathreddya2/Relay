
import os, logging
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.instrumentation.django import DjangoInstrumentor
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.instrumentation.celery import CeleryInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
#from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor
#

def configure_opentelemetry():

    # if os.environ.get('JAEGER_ENABLED') == "True":
    #     logging.info("starting up jaeger telemetry")
    #
    # jaeger_host = os.environ.get('JAEGER_HOST', 'jaeger-otel-agent')
    # jaeger_port = int(os.environ.get('JAEGER_PORT', '6831'))

    resource = Resource(attributes={
        "service.name": "ARS"
    })

    trace.set_tracer_provider(TracerProvider(resource=resource))

    tracer_provider = trace.get_tracer_provider()

    # Configure Jaeger Exporter
    jaeger_exporter = JaegerExporter(
        agent_host_name="localhost",
        agent_port=6831,
    )

    span_processor = BatchSpanProcessor(jaeger_exporter)
    tracer_provider.add_span_processor(span_processor)

    # tracer = trace.get_tracer(__name__)

    # Optional: Console exporter for debugging
    console_exporter = ConsoleSpanExporter()
    tracer_provider.add_span_processor(BatchSpanProcessor(console_exporter))

    DjangoInstrumentor().instrument()
    CeleryInstrumentor().instrument()
    RequestsInstrumentor().instrument()
    #instrument HTTPX clients to enable distributed tracing
    #HTTPXClientInstrumentor().instrument()
    #