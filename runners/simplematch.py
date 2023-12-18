def run(command: str) -> None:
    print(f'simple matching {command}...')

    match command:
        case 'quit':
            print('quitting...')
            quit()
        case 'reset':
            print('resetting...')
            pass
        case _:
            print(f'Unknown command {command!r}')
