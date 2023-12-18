from runners import printer
from runners import simplematch
from runners import simpleargs

def main(run) -> None:
    while True:
        command = input('$ ')
        run(command)


if __name__ == '__main__':
    runner = simpleargs.run
    main(runner)
