def run(command: str) -> None:
    print(f'simple tuple matching with args : {command}...')

    match command.split():
        case 'load', filename:
            print(f'loading {filename}...')

        case 'save', filename:
            print(f'saving {filename}...')

        case 'quit' | 'exit' |'bye',:
            print('quitting...')
            quit()
            
        case _:
            print(f'Unknown command {command!r}')
