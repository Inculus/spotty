from argparse import Namespace, ArgumentParser
from spotty.commands.abstract_config_command import AbstractConfigCommand
from spotty.commands.writers.abstract_output_writrer import AbstractOutputWriter
from spotty.providers.abstract_instance_manager import AbstractInstanceManager


class StatusCommand(AbstractConfigCommand):

    name = 'status'
    description = 'Print information about the instance'

    def configure(self, parser: ArgumentParser):
        super().configure(parser)
        parser.add_argument('--ip', action='store_true', help='Show public ip address')

    def _run(self, instance_manager: AbstractInstanceManager, args: Namespace, output: AbstractOutputWriter):
        if args.ip == True:
            output.write(instance_manager.get_public_ip_address())
        else:
            output.write(instance_manager.get_status_text())
