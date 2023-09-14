#creando mi propia excepcion
class MiExcepcion(Exception):
    def __init__(self,err):
        print(f'cometiste el siguiente error {err}')
        

#manejandola
try:
    raise MiExcepcion('como te equivocas')
except:
    print('enserio te equivocaste?')