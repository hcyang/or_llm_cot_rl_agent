
import sys

class DebuggingUtility:
    @staticmethod
    def info(message):
        print(f'INFO: {message}\n')
    @staticmethod
    def debug(message):
        print(f'DEBUG: {message}\n')
    @staticmethod
    def error(message):
        print(f'ERROR: {message}\n')

    @staticmethod
    def dump_sys_path():
        DebuggingUtility.info(f'sys.path: {sys.path}\n')

if __name__ == "__main__":
    # DebuggingUtility.info('Hello, World')
    DebuggingUtility.dump_sys_path()
