from runners import printer
from runners import simplematch
from runners import simpleargs
from runners import simpletuple
from runners import simpleoptions
from runners import guardedoptions
from runners import simpledict

def main(run) -> None:
    while True:
        command = input('$ ')
        run(command)


if __name__ == '__main__':
    runner = guardedoptions.run
    main(runner)
