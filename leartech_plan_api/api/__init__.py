# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from leartech_plan_api.api.example_api import ExampleApi
    from leartech_plan_api.api.health_api import HealthApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from leartech_plan_api.api.example_api import ExampleApi
from leartech_plan_api.api.health_api import HealthApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
