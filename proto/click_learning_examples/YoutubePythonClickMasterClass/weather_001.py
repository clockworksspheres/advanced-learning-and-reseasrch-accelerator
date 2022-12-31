#!/usr/bin/env -S python -u

import click

@click.command()
@click.option('--weather', type=click.Choice(['sunny', 'rainy', 'snowy']))
def main(weather):
    print(f'I love it when the weather is {weather}')


if __name__=="__main__":
    main()


