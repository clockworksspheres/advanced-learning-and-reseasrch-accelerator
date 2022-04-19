#!/usr/bin/env -S python -u

import click

@click.command()
@click.argument("name")
def main(name):
    print (f"Hello {name}!")

if __name__=="__main__":
    main()



