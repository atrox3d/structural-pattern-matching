def run(command: str) -> None:
    print(f'simple matching with dict: {command}...')

    def parsetodict(command: str) -> dict:
            cmd, *args =  command.split()
            param = opt = None

            for arg in args:
                if arg.startswith('-'):
                    opt = arg
                else:
                    param = arg

            return dict(cmd=cmd, param=param, opt=opt)

    match parsetodict(command): 
        case {'cmd':'load', 'param': file}:
            print(f'loading {file}...')

        case {'cmd':'save', 'param': file}:
            print(f'saving {file}...')

        case {'cmd':'quit' | 'exit' |'bye', 'opt': '-f' | '--force'}:
            print(f'force quitting')
            quit()
        
        case {'cmd':'quit' | 'exit' |'bye'}:
            print(f'quitting')
            quit()
        
        case _:
            print(f'Unknown command {command!r}')
