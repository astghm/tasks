import subprocess
import json
import os

file = os.path.join(os.getcwd(), "session_file.json")

subprocess.run("sed -i 's/OFFLOAD_END_PLACEHOLDER/date/' session_file.json", shell=True, check=True)
subprocess.run("sed -i 's/INPROGRESS/OK/' session_file.json", shell=True, check=True)
subprocess.run("sed -i '/components/r compoent_file.json' session_file.json", shell=True, check=True)
subprocess.run("sed -i '/COMPONENTSPLACEHOLDER/d' session_file.json", shell=True, check=True)


