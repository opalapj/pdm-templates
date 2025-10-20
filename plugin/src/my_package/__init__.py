from pdm.project.config import ConfigItem

from .commands import Command


def main(core):
    core.register_command(
        command=Command,
    )
    config_item = ConfigItem(
        description="The person's name.",
        default="John",
    )
    core.add_config(name="hello.name", config_item=config_item)
