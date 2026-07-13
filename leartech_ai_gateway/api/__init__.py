# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from leartech_ai_gateway.api.chat_api import ChatApi
    from leartech_ai_gateway.api.embeddings_api import EmbeddingsApi
    from leartech_ai_gateway.api.models_api import ModelsApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from leartech_ai_gateway.api.chat_api import ChatApi
from leartech_ai_gateway.api.embeddings_api import EmbeddingsApi
from leartech_ai_gateway.api.models_api import ModelsApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
