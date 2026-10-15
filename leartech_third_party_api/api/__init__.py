# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from leartech_third_party_api.api.example_api import ExampleApi
    from leartech_third_party_api.api.fleet_test_api import FleetTestApi
    from leartech_third_party_api.api.health_api import HealthApi
    from leartech_third_party_api.api.providers_api import ProvidersApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from leartech_third_party_api.api.example_api import ExampleApi
from leartech_third_party_api.api.fleet_test_api import FleetTestApi
from leartech_third_party_api.api.health_api import HealthApi
from leartech_third_party_api.api.providers_api import ProvidersApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
