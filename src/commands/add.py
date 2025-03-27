import click

@click.command()
@click.argument("num1", type=int)
@click.argument("num2", type=int)
@click.pass_context
def add(ctx, num1, num2):
    """Add two numbers"""
    result = num1 + num2
    click.echo(f"The sum of {num1} and {num2} is {result}")
