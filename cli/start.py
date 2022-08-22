import click
import uvicorn


@click.group()
def start() -> None:
    """Запустить сервис."""


@start.command()
def api() -> None:
    """API сервис."""
    uvicorn.run("app.api.factory:create_app", factory=True, host="127.0.0.1", port=8000)
