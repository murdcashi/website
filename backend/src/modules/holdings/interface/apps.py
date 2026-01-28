from django.apps import AppConfig

class HoldingsInterfaceConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "src.modules.holdings.interface"
    label = "holdings_interface"
