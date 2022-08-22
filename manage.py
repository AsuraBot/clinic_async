import click
from cli.start import start
from cli.migrations import migrations


@click.group()
def main() -> None:
    """Команды управления приложением."""


main.add_command(start)
main.add_command(migrations)

if __name__ == "__main__":
    main()
