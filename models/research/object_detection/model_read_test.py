
# Import packages
import os
import cv2
import numpy as np
import tensorflow as tf
import sys


sys.path.append("..")

#สิ่งที่ต้องใช้ในการแสดงกรอบที่ได้ออกมาจากโมเดลแบบจำลอง
from utils import label_map_util
from utils import visualization_utils as vis_util
from utils import string_show as st
from utils import sort_string as ss


#ชื่อโฟลเดอร์ inference_graph ใน object detection ซึ่งใช้เก็บไฟล์ .pb ซึ่งเป็นโมเดลที่ใช้ทดสอบ
MODEL_NAME = 'inference_graph'
#ที่อยู่ของรูปภาพที่นำมาใช้ทดลอง
IMAGE_NAME = 'C:/tensorflow2/100 test example/Bad ocr/Bad OCR (14).jpg'
    

#Directory ที่ทำงานอยู่ในปัจจุบัน
CWD_PATH = os.getcwd()

#ประกาศใช้โมเดลที่อยู่ในโฟลเดอร์ inference_graph
PATH_TO_CKPT = os.path.join(CWD_PATH,MODEL_NAME,'OCR_Faster_Rcnn_Inception_V2.pb')
print(PATH_TO_CKPT)

# Path to label map file
PATH_TO_LABELS = os.path.join(CWD_PATH,'training','labelmap.pbtxt')

# Path to image
PATH_TO_IMAGE = os.path.join(CWD_PATH,IMAGE_NAME)

#ตัวเลขของคลาสทั้งหมดที่แบบจำลองสามารถทำนายได้(A-Z,0-9)
NUM_CLASSES = 36

# Load the label map.
label_map = label_map_util.load_labelmap(PATH_TO_LABELS)

#all label map id and name
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)

# Load the Tensorflow model into memory.
#สร้าง session ในการใช้งานแบบจำลองผ่าน tensorflow
detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

    sess = tf.Session(graph=detection_graph)

#ด้านล่างเป็นส่วนของการดู input และ output ที่แบบจำลองทำนายออกมาโดยจะแสดงเป็นรูปภาพและตีกรอบวัตถุโดยใช้ opencv-python

# Input tensor is the image
image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

# Output tensors ที่ได้จะมี กรอบ,เปอร์เซ็นความถูกต้อง,และคลาสที่ถูกทำนายออกมา
# Each box represents a part of the image where a particular object was detected
#แต่ละกรอบจะมีส่วนของวัตถุที่ถูกตรวจจับภายในรูปภาพ
detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')

#score คือค่าความถูกต้องที่ถูกทำนายออกมาจากแบบจำลอง
#class คือชื่อคลาสที่ถูกทำนายออกมาโดยแบบจำลอง
detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')

#จำนวนวัตถุที่ถูกตรวจจับในรูปภาพ
num_detections = detection_graph.get_tensor_by_name('num_detections:0')

# Load image using OpenCV and
# expand image dimensions to have shape: [1, None, None, 3]
# i.e. a single-column array, where each item in the column has the pixel RGB value
image = cv2.imread(PATH_TO_IMAGE)
image_expanded = np.expand_dims(image, axis=0)

#นำsession ของแบบจำลองมาใส่ข้อมูลของรูปภาพ input
(boxes, scores, classes, num) = sess.run(
    [detection_boxes, detection_scores, detection_classes, num_detections],
    feed_dict={image_tensor: image_expanded})

# วาดกรอบผลลัพธ์ของการทำนายโดยใช้ opencv (aka 'visulaize the results')

vis_util.visualize_boxes_and_labels_on_image_array(
    image,
    np.squeeze(boxes),
    np.squeeze(classes).astype(np.int32),
    np.squeeze(scores),
    category_index,
    use_normalized_coordinates=True,
    line_thickness=3,
    skip_scores=True,
    min_score_thresh=0.50)


# All the results have been drawn on image. Now display the image.
cv2.imshow('Object detector', image)



#print (([category_index.get(value) for index,value in enumerate(classes[0]) if scores[0,index] > 0.5]))

string_sort_list=[]
string_sort_list = ss.string_sort(
    np.squeeze(boxes),
    np.squeeze(classes).astype(np.int32),
    np.squeeze(scores),
    category_index,
    min_score_thresh=0.50)
#print(string_sort_list)


#OCR read and Check condition
ocrstring=ss.convert_list_to_str(string_sort_list)
print("String After Sort = "+ocrstring)
ocr_condition=ss.check_sum(ocrstring)
#print(ocr_condition)

# Press any key to close the image
cv2.waitKey(0)

# Clean up
cv2.destroyAllWindows()
