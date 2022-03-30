# Importing the required libraries
import click

@click.group()
@click.pass_context

# Defining the functions for todo application
def todo(ctx):
    ctx.ensure_object(dict)
    with open('./todo.txt') as f:
        content = f.readlines()
    