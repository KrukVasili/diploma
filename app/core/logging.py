import structlog


def setup_logging(debug: bool = False):
    processors = [
        structlog.contextvars.merge_contextvars,
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        (
            structlog.dev.ConsoleRenderer()
            if debug
            else structlog.processors.JSONRenderer()
        ),
    ]
    structlog.configure(
        processors=processors,
        wrapper_class=structlog.make_filtering_bound_logger(0 if debug else 20),
        cache_logger_on_first_use=True,
    )
