def run(command: str) -> None:
    print(f'simple matching: {command}...')

    match command:
        case 'quit':
            print('quitting...')
            quit()

        case 'reset':
            print('resetting...')
            pass
        
        case other:
            print(f'Unknown command {other!r}')
