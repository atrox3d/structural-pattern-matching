def run(command: str) -> None:
    print(f'simple matching with args: {command}...')

    match command.split():
        case ['load', filename]:
            print(f'loading {filename}...')
        case ['save', filename]:
            print(f'saving {filename}...')
        case ['quit' | 'exit' |'bye', *rest]:
            options = '--force', '-f'
            if any(x in rest for x in options):    
                print('force quitting...')
            else:
                print('quitting...')
            quit()
        case _:
            print(f'Unknown command {command!r}')
