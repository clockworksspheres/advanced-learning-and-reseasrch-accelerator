#!/usr/bin/env -S python -u

import click

@click.command()
@click.argument("name")
@click.option('--number', type=int, help="Number of times to print the greeting")
def main(name, number):
    for i in range(number):
        print (f"Hello {name}!")

if __name__=="__main__":
    main()



