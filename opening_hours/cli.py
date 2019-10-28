import click

from opening_hours.run import run


@click.group("back_office")
def opening_hours_main():
    """
    Command group declaration.
    Entry point for tito server command line.
    """


opening_hours_main.add_command(run)


if __name__ == "__main__":
    opening_hours_main()
