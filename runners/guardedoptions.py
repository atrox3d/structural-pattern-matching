def run(command: str) -> None:
    print(f'simple matching with args: {command}...')

    match command.split():
        case ['load', filename]:
            print(f'loading {filename}...')

        case ['save', filename]:
            print(f'saving {filename}...')

        case ['quit' | 'exit' |'bye', *rest] if any(opt in rest for opt in ('--force', '-f')):
            print('force quitting...')
            quit()

        case ['quit' | 'exit' |'bye', *rest]:
            print('quitting...')
            quit()
            
        case _:
            print(f'Unknown command {command!r}')
