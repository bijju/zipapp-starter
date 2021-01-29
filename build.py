import zipapp
import os
import shutil
import logging
import traceback
import sys
from pathlib import Path

# --------------------------------------------------------------------
# Default Variables for ZipApp Build
# --------------------------------------------------------------------
program_name = os.path.basename(__file__)
version = "0.0.1"

# --------------------------------------------------------------------
# Logging
# --------------------------------------------------------------------
formatter = logging.Formatter(
    '[%(asctime)s] [%(filename)s] [%(levelname)s] [%(lineno)d:%(funcName)s] >> %(message)s'
)
lg = logging.getLogger(__file__)
ch = logging.StreamHandler()
ch.setFormatter(formatter)
lg.addHandler(ch)
lg.setLevel(logging.DEBUG)
lg.info("# =======================================================================================")
lg.info(f"# Starting Zipapp: {program_name}")
lg.info(f"# Version: {version}")
lg.info("# =======================================================================================")

# --------------------------------------------------------------------
# Zipapps build code
# --------------------------------------------------------------------
try:
    target_directory_name = "dist"
    source_directory_name = "src"
    source_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), source_directory_name)
    target_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), target_directory_name)
    lg.info(f"BASE: {source_directory}")
    if not os.path.exists(source_directory):
        raise NotADirectoryError(f"Source directory does not exists: " + str(source_directory))
    if os.path.exists(target_directory):
        shutil.rmtree(target_directory)

    os.makedirs(target_directory)
    app_name = "app.pyz"
    abs_app_path = os.path.join(target_directory, app_name)
    zipapp.create_archive(
        source_directory
        , target=abs_app_path
        , compressed=True
    )
except FileNotFoundError:
    exc_type, exc_value, exec_traceback = sys.exc_info()
    lg.error(f"Unknown Exception or Error occurred: {str(exc_type)}")
    lg.error(f"Exception Type: {exc_type}")
    lg.error(f"Exception Value: {exc_value}")
    lg.error(traceback.print_exception(exc_type, exc_value, exec_traceback))
    sys.exit(255)
except NotADirectoryError:
    exc_type, exc_value, exec_traceback = sys.exc_info()
    lg.error(f"Unknown NotADirectoryError occurred: f{str(exc_type)}")
    lg.error(f"Exception Type: {exc_type}")
    lg.error(f"Exception Value: {exc_value}")
    lg.error(traceback.print_exception(exc_type, exc_value, exec_traceback))
    sys.exit(255)
except Exception:
    exc_type, exc_value, exec_traceback = sys.exc_info()
    lg.error(f"Unknown Exception or Error occurred!")
    lg.error(f"Exception Type: {str(exc_type)}")
    lg.error(f"Exception Value: {exc_value}")
    lg.error(traceback.print_exception(exc_type, exc_value, exec_traceback))
    sys.exit(255)
lg.info(f"Zipapp package build successful: {app_name} [Full Path: {abs_app_path}]")
lg.info("Shutting down build process!")


