import os
import re
import getopt
import socket
import sys
import traceback
import logging


class App:
    program_name = os.path.basename(__file__)
    version = 1.0
    log_format = logging.Formatter(
        '[%(asctime)s] [%(filename)s] [%(levelname)s] [%(lineno)d: %(funcName)s >> %(message)s]'
    )
    hostname = socket.gethostname()
    log_directory = None
    log_file = None
    args_patt = re.compile(".*:.*")
    lg = None

    module = None

    env_lookup = {
        "dev": ["some-development-server.domain.com"]
        , "qa": ["some-qa-server.domain.com"]
        , "uat": ["some-uat-server.domain.com"]
        , "prod": ["some-prod-server.domain.com"]
        # Defaults to local
    }

    @staticmethod
    def usage():
        """Usage.
        :Description:
        :return:
        """
        print("""
            App.py --some options
        """)

    def main(self):
        """main.
            :description:
            :output:
        """
        self.lg = logging.getLogger(__file__)
        ch = logging.StreamHandler()
        ch.setFormatter(self.log_format)
        self.lg.addHandler(ch)
        self.lg.setLevel(logging.DEBUG)
        self.lg.info("Initializing the App:.....")

        self.lg.info("Reading Command line Options")
        try:
            opts,args = getopt.getopt(
                sys.argv[1:]
                , ""
                , [
                    "help"
                    , "module="
                ]
            )
        except getopt.GetoptError:
            exc_type, exc_value, exec_traceback = sys.exc_info()
            self.lg.error(f"Error occurred reading command line options: f{str(exc_type)}")
            self.lg.error(traceback.format_exception(exc_type, exc_value, exec_traceback))
            sys.exit(255)

        self.lg.info("Processing Command line options")
        try:
            for o, a in opts:
                if o in "--help":
                    self.usage()
                    sys.exit()
                elif o in "--module":
                    self.module = a
        except ConnectionError:
            exc_type, exc_value, exec_traceback = sys.exc_info()
            self.lg.error(f"ConnectionError occurred: f{str(exc_type)}")
            self.lg.error(traceback.format_exception(exc_type, exc_value, exec_traceback))
            sys.exit(255)
        except IOError:
            exc_type, exc_value, exec_traceback = sys.exc_info()
            self.lg.error(f"IOError occurred: f{str(exc_type)}")
            self.lg.error(traceback.format_exception(exc_type, exc_value, exec_traceback))
            sys.exit(255)
        except Exception:
            exc_type, exc_value, exec_traceback = sys.exc_info()
            self.lg.error(f"Unknown Exception or Error occurred: f{str(exc_type)}")
            self.lg.error(traceback.format_exception(exc_type, exc_value, exec_traceback))
            sys.exit(255)
        self.lg.info("Shutting down App: Done!")
