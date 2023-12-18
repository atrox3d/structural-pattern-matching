from runners import printer
from runners import simplematch
from runners import simpleargs
from runners import simpleoptions

def main(run) -> None:
    while True:
        command = input('$ ')
        run(command)


if __name__ == '__main__':
    runner = simpleoptions.run
    main(runner)
