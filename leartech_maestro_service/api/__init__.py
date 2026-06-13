# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from leartech_maestro_service.api.event_maestro_api import EventMaestroApi
    from leartech_maestro_service.api.event_registration_api import EventRegistrationApi
    from leartech_maestro_service.api.health_api import HealthApi
    from leartech_maestro_service.api.latest_events_api import LatestEventsApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from leartech_maestro_service.api.event_maestro_api import EventMaestroApi
from leartech_maestro_service.api.event_registration_api import EventRegistrationApi
from leartech_maestro_service.api.health_api import HealthApi
from leartech_maestro_service.api.latest_events_api import LatestEventsApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
