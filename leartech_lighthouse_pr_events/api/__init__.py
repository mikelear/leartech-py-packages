# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from leartech_lighthouse_pr_events.api.health_api import HealthApi
    from leartech_lighthouse_pr_events.api.webhook_api import WebhookApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from leartech_lighthouse_pr_events.api.health_api import HealthApi
from leartech_lighthouse_pr_events.api.webhook_api import WebhookApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
