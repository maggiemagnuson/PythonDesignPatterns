from Singleton.singleton import Singleton
import datetime

class Logger(metaclass=Singleton):
    log_file = None

    def __init__(self, path):
        if self.log_file is None:
            self.log_file = open(path, mode='a')
            self.write_log("Logger does not exist. Created.")
        else:
            self.write_log("Logger exists. Not created.")

    def write_log(self, log_record):
        now = str(datetime.datetime.now())
        self.log_file.write(f"{now} {log_record}\n")

    def close_log(self):
        if self.log_file is not None:
            self.write_log("Closing logger")
            self.log_file.close()
            self.log_file = None