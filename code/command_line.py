import argparse


def command():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", help="""
        SET|GET KEY VALUE
    """)
    parser.add_argument("key", help="key")
    parser.add_argument("value", help="value")

    args = parser.parse_args()
    print(args.command)
    print(args.key)
    print(args.value)


if __name__ == '__main__':
    command()
