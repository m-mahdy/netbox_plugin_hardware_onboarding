from extras.plugins import PluginConfig


class HardwareOnboarding(PluginConfig):
    """Pluging configuration for the netbox_hardware_onboarding plugin."""

    name = "netbox_hardware_onboarding"
    verbose_name = "Device Hardware Onboarding"
    description = "A plugin for Netbox to add hardware components to a device"
    author = "Mohab Mahdy"
    author_email = "mohab.mahdy92@gmail.com"
    base_url = "hardware-onboarding"
    required_settings = []
    default_settings = {}


config = HardwareOnboarding