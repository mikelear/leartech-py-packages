# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from leartech_auth_service.api.login_api import LoginApi
    from leartech_auth_service.api.two_factor_api import TwoFactorApi
    from leartech_auth_service.api.user_api import UserApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from leartech_auth_service.api.login_api import LoginApi
from leartech_auth_service.api.two_factor_api import TwoFactorApi
from leartech_auth_service.api.user_api import UserApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
