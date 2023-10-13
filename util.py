import os
import shutil
from dotenv import load_dotenv


OUTPUT_DIR = os.getenv('OUTPUT_DIR')

def prep():
    os.makedirs(os.path.dirname(OUTPUT_DIR + "/static"), exist_ok=True)
    shutil.copytree("static", OUTPUT_DIR + "/static", dirs_exist_ok = True)
    shutil.copytree("favicon", OUTPUT_DIR, dirs_exist_ok = True)
    shutil.copy2("modules/modern-normalize/modern-normalize.css", OUTPUT_DIR + "/static/css/modern-normalize.css")
    shutil.copy2("modules/htmx.org/dist/htmx.min.js", OUTPUT_DIR + "/static/js/htmx.min.js")