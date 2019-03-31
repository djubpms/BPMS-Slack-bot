from .io import MagiIO
from .module import MagiModule


def hello_world(*args, **kwargs):
    return "HELLO WORLD! from MAGI MODULE."


if __name__ == '__main__':
    print('Magi Start!')
    print('='*30)
    print('MagiModule Initializing.')
    module = MagiModule.MagiModule()
    print('Complete')

    print('='*30)
    print('MagiIO Initializing.')
    io = MagiIO.MagiIO(module)
    print('Complete')
    print('='*30)

    io.set_callback_func('hello', hello_world)

    io.start()
