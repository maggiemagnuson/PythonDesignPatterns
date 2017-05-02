import datetime

class LoggerClassic(object):
    log_file = None

    @staticmethod
    def instance():
        if '_instance' not in LoggerClassic.__dict__:
            print("Instance does not exist. Creating.")
            LoggerClassic._instance = LoggerClassic()
        else:
            print("Instance already exists. Not creating")
        return LoggerClassic._instance

    def open_log(self, path):
        self.log_file = open(path, mode='a')
        self.write_log("Opening logger")

    def write_log(self, log_record):
        now = str(datetime.datetime.now())
        self.log_file.write(f"{now} {log_record}\n")

    def close_log(self):
        if self.log_file is not None:
            self.write_log("Closing logger")
            self.log_file.close()
            self.log_file = None

logger = LoggerClassic()
logger.open_log('./logger.log')
logger.write_log("Log message")
logger.close_log()