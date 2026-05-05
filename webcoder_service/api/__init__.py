# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from webcoder_service.api.auth_api import AuthApi
    from webcoder_service.api.health_api import HealthApi
    from webcoder_service.api.initiatives_api import InitiativesApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from webcoder_service.api.auth_api import AuthApi
from webcoder_service.api.health_api import HealthApi
from webcoder_service.api.initiatives_api import InitiativesApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
