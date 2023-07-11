import logging


class Logger:
    _instance = None

    @staticmethod
    def get_instance():
        if Logger._instance is None:
            Logger._instance = Logger()
        return Logger._instance

    def __init__(self):
        self.logger = logging.getLogger("MultiLogin")
        self.logger.setLevel(logging.INFO)
        self.formatter = logging.Formatter('[%(asctime)s] %(levelname)s - Thread %(thread)d: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

        # Add console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        # Add file handler
        fh = logging.FileHandler("multilogin.log")
        fh.setLevel(logging.INFO)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)
