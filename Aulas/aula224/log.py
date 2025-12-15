from pathlib import Path
from abc import ABC, abstractmethod


LOG_FILLE = Path(__file__).parent / 'log.txt'

class Log(ABC):
    @abstractmethod
    def _log(self, msg):...


    def log_error(self, msg):
        return self._log(f'ERROR: {msg} ({self.__class__.__name__})')


    def log_sucess(self, msg):
        return self._log(f'SUCESS: {msg} ({self.__class__.__name__})')


class LogFilleMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg}'
        with open(LOG_FILLE, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')




class LogPrintMixin(Log):
    def _log(self, msg):
        print(msg)



if __name__ == "__main__":
    lp = LogPrintMixin()
    lp.log_error('Qualquer coisa')
    lp.log_sucess('Que legal')
    lf = LogFilleMixin()
    lf.log_error('Qualquer coisa')
    lf.log_sucess('Que legal')
    print(LOG_FILLE)
