# -*- coding: utf-8 -*-

from friday import friday
import click


@click.command()
def main(args=None):
    """Console script for friday"""
    assistant = friday.Friday()
    while assistant.is_active:
        request = assistant.listen()

        doable = assistant.think(request)

        successful = False
        if doable:
            successful = assistant.perform(request)
        else:
            assistant.refuse()

        if successful:
            # Decide which response the assistant should return to the user.
            assistant.choose_response()
            # Display a response to the user.
            assistant.respond()
        else:
            assistant.apologize()


if __name__ == "__main__":
    main()
