import argparse
import sys

def main(args):
    parser = argparse.ArgumentParser(description='Финансовый трекер расходов')
    parser.add_argument('name', help='Что вы хотите сделать? Введите цифру, соответствующую порядковому номеру команды: 1. Добавить запись')
    parser.set_defaults(func=lambda args: print(f"Hello, {args.name}!"))

    if len(args) == 0:
        parser.print_help()
        sys.exit(1)


    args = parser.parse_args(args)
    args.func(args)

if __name__ == "__main__":
    main(sys.argv[1:])