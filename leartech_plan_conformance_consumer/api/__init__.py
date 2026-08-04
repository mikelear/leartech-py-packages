# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from leartech_plan_conformance_consumer.api.example_api import ExampleApi
    from leartech_plan_conformance_consumer.api.fleet_test_api import FleetTestApi
    from leartech_plan_conformance_consumer.api.health_api import HealthApi
    from leartech_plan_conformance_consumer.api.maestro_api import MaestroApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from leartech_plan_conformance_consumer.api.example_api import ExampleApi
from leartech_plan_conformance_consumer.api.fleet_test_api import FleetTestApi
from leartech_plan_conformance_consumer.api.health_api import HealthApi
from leartech_plan_conformance_consumer.api.maestro_api import MaestroApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
