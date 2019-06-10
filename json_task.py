import json
import glob

path_to_read = "C:/Users/Home/Desktop/Freedom Data/Tasks/Task_Json/json_samples/json_samples/apps_ingest_stream_status_file/2019/05/01/"
path_to_write = "C:/Users/Home/Desktop/Freedom Data/Tasks/Task_Json/json_samples/json_samples/apps_ingest_stream_status_file/2019/05/new/"

file_list = glob.glob(path_to_read + '*.json')

for file in file_list:
    with open(file) as myfile:
        data = myfile.read().strip()
        lst = data.split("\n")
        lst_1 = []
        for l in lst:
            l = json.loads(l.strip())
            lst_1.append(l)
        lst_2 = []
        for i in lst_1:
            lst_2.append({i.pop("session_id", None):i})
        for i in lst_2:
            with open(path_to_write + f"data_file{file_list.index(file)}_{lst_2.index(i)}.json", "w") as write_file:
                json.dump(i, write_file)