#from Singleton.LoggerBase import Logger
#from Singleton.logger import Logger
from Singleton.logger_mono import Logger
logger = Logger('./logger_mono.log')
logger.write_log("Logging with classic Singleton pattern")
logger2 = Logger("***ignored***")
logger2.write_log("Another log record. This time from [logger2]")

logger.close_log()