import argparse
import os

def get_args():
    parser = argparse.ArgumentParser(prog="maki", description="Anki deck-building tool")
    subparsers = parser.add_subparsers(help="Available commands", dest="command", required=True)

    create_subparser = subparsers.add_parser("create")
    create_subparser.add_argument("path", default=os.getcwd(), nargs='?')
    build_subparser = subparsers.add_parser("build")
    preview_subparser = subparsers.add_parser("preview")


    args = parser.parse_args()


    if args.command == "create":
        print("hello")




def main():
    args = get_args()

if __name__=='__main__':
    main()
    


