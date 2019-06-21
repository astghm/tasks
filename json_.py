import subprocess
import json
import os


subprocess.run("""sed -i "s/OFFLOAD_END_PLACEHOLDER/$(date '+%Y-%m-%d')/g" session_file.json""", shell=True, check=True)
subprocess.run("sed -i 's/INPROGRESS/OK/g' session_file.json", shell=True, check=True)
subprocess.run("""sed -i "s/COMPONENTSPLACEHOLDER/$(echo $(cat compoent_file.json))/g" session_file.json""", shell=True, check=True)





