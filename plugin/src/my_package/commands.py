from pdm.cli.commands.base import BaseCommand


class Command(BaseCommand):
    """
    Say hello to the specified person.
    If none is given, will read from 'hello.name' config.
    """

    name = 'hello'

    def add_arguments(self, parser):
        parser.add_argument(
            '-n', '--name',
            help='The person\'s name to whom you greet.',
        )

    def handle(self, project, options):
        if not options.name:
            name = project.config['hello.name']
        else:
            name = options.name
        print(f'Hello, {name}!')
