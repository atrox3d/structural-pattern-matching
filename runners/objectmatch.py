from dataclasses import dataclass
import shlex

@dataclass
class Command:
    command: str
    arguments: list[str]


def run(command: str) -> None:
    print(f'object matching with args: {command}...')

    cmd, *arguments = shlex.split(command)

    match Command(cmd, arguments):

        case Command('load', [filename]):
            print(f'loading {filename}...')

        case Command('save', [filename]):
            print(f'saving {filename}...')

        case Command('quit' | 'exit' |'bye', ['--force' | '-f', *rest]):
            print('force quitting...')
            quit()

        case Command('quit' | 'exit' |'bye'):
            print('quitting...')
            quit()
            
        case _:
            print(f'Unknown command {command!r}')
