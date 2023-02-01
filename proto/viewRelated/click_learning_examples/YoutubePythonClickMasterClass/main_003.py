#!/usr/bin/env -S python -u

import click

@click.command()
@click.argument("name")
@click.option('--number', type=int)
def main(name, number):
    for i in range(number):
        print (f"Hello {name}!")

if __name__=="__main__":
    main()



