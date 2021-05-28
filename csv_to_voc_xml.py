import pandas as pd
import numpy as np
from lxml import etree
import xml.etree.ElementTree as ET
import csv


#change these lines
save_path = "./test/xmls"
filename = './test/labels.csv'

if not os.path.exists(save_path):
    os.mkdir(save_path)


bbox_list = []


with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        count = 0
        #print(row[7])
        filename = row[0] #check file name in csv column
        width = row[1]  #check width in csv column
        height = row[2] #check height in csv column
        classes = row[3] #check class in csv column
        xmin = row[4] #check xmin in csv column
        ymin = row[5] #check ymin in csv column
        xmax = row[6] #check xmax in csv column
        ymax = row[7]  #check ymax in csv column
        
        for i in range(0, 2):
            height = df['height'].iloc[i]
            width = df['width'].iloc[i]
            depth = 3
            annotation = ET.Element('annotation')
            ET.SubElement(annotation, 'folder').text = 'images'
            ET.SubElement(annotation, 'filename').text = filename
            ET.SubElement(annotation, 'path').text = './test/'
            source = ET.SubElement(annotation, 'source')
            ET.SubElement(source, 'database').text = 'Unknown'
            size = ET.SubElement(annotation, 'size')
            ET.SubElement(size, 'width').text = str(width)
            ET.SubElement(size, 'height').text = str(height)
            ET.SubElement(size, 'depth').text = '3'

            #segmented = ET.SubElement(annotation, 'segmented')
            ET.SubElement(annotation, 'segmented').text = '0'
            ob = ET.SubElement(annotation, 'object')
            ET.SubElement(ob, 'name').text = classes
            ET.SubElement(ob, 'pose').text = 'Unspecified'
            ET.SubElement(ob, 'truncated').text = '0'
            ET.SubElement(ob, 'difficult').text = '0'
            bbox = ET.SubElement(ob, 'bndbox')
            ET.SubElement(bbox, 'xmin').text = str(xmin)
            ET.SubElement(bbox, 'ymin').text = str(ymin)
            ET.SubElement(bbox, 'xmax').text = str(xmax)
            ET.SubElement(bbox, 'ymax').text = str(ymax)

            fileName = str(df['filename'].iloc[i])
            tree = ET.ElementTree(annotation)
            tree.write(os.path.join(save_path, filename[:-4] + ".xml"), encoding='utf8')
            count += 1    
