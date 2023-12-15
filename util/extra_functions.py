import os
from config import basedir


class ExtraFunctions:

    def get_file_path_(self, file_name: str):
        """
        Allow to get the file path.
        :param file_name: Name of file with extension.
        :return: str
        """
        for r, d, f in os.walk(basedir):
            for file in f:
                if file == file_name:
                    ruta = os.path.abspath(os.path.join(r, file))
                    print(ruta)
                    return ruta
