from runners import printer

def main(run) -> None:
    while True:
        command = input('$ ')
        run(command)


if __name__ == '__main__':
    main(printer.run)
