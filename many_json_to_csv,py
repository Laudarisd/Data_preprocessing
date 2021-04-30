import glob
import json 
import csv
import os

dir = "./"

with open(os.path.join(dir, 'test.csv'), 'w', newline='') as f_csv:
    csv_output = csv.writer(f_csv)
    csv_output.writerow(["file_name", "key", "label", "xmin", "ymin", "xmax", "ymax"])
    
    for single_file in glob.glob("./labels/*.json"):
        #print(single_file)
        change_name = os.path.basename(single_file)
        filename = change_name.split( ".", 2) [0] + ".jpg"
        
        with open(single_file) as f_json:
            json_data = json.load(f_json)

        for object in json_data["objects"]:
            done = csv_output.writerow([
                #single_file,
                filename,
                object["key"],
                object["label"],
                object["bbox"]["xmin"],
                object["bbox"]["ymin"],
                object["bbox"]["xmax"],
                object["bbox"]["ymax"]
            ])
            if done:
                print("Csv is saved")
            else:
                print("can't write csv")
