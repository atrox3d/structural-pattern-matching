from runners import printer
from runners import simplematch

def main(run) -> None:
    while True:
        command = input('$ ')
        run(command)


if __name__ == '__main__':
    runner = simplematch.run
    main(runner)
