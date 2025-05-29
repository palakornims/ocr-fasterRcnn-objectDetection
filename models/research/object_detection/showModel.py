import os
import cv2
import numpy as np
import tensorflow as tf
import sys


sys.path.append("..")


from utils import label_map_util
from utils import visualization_utils as vis_util
from utils import string_show as st
from utils import sort_string as ss

def ShowImage(PathImage,PathModel):
  
    
    IMAGE_NAME = PathImage

    # Grab path to current working directory    
    CWD_PATH = os.getcwd()

    # Path to frozen detection graph .pb file, which contains the model that is used
    # for object detection.
    PATH_TO_CKPT = os.path.join(CWD_PATH,PathModel)

    # Path to label map file
    PATH_TO_LABELS = os.path.join(CWD_PATH,'training','labelmap.pbtxt')

    # Path to image
    PATH_TO_IMAGE = os.path.join(CWD_PATH,IMAGE_NAME)

    # Number of classes the object detector can identify
    NUM_CLASSES = 36

    # Load the label map.
    # Label maps map indices to category names, so that when our convolution
    # network predicts `5`, we know that this corresponds to `king`.
    # Here we use internal utility functions, but anything that returns a
    # dictionary mapping integers to appropriate string labels would be fine
    label_map = label_map_util.load_labelmap(PATH_TO_LABELS)

    #all label map id and name
    categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
    category_index = label_map_util.create_category_index(categories)

    # Load the Tensorflow model into memory.
    detection_graph = tf.Graph()
    with detection_graph.as_default():
        od_graph_def = tf.GraphDef()
        with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')

        sess = tf.Session(graph=detection_graph)

    # Define input and output tensors (i.e. data) for the object detection classifier

    # Input tensor is the image
    image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

    # Output tensors are the detection boxes, scores, and classes
    # Each box represents a part of the image where a particular object was detected
    detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')

    # Each score represents level of confidence for each of the objects.
    # The score is shown on the result image, together with the class label.
    detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
    detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')

    # Number of objects detected
    num_detections = detection_graph.get_tensor_by_name('num_detections:0')

    # Load image using OpenCV and
    # expand image dimensions to have shape: [1, None, None, 3]
    # i.e. a single-column array, where each item in the column has the pixel RGB value
    image = cv2.imread(PATH_TO_IMAGE)
    image_expanded = np.expand_dims(image, axis=0)

    # Perform the actual detection by running the model with the image as input
    (boxes, scores, classes, num) = sess.run(
        [detection_boxes, detection_scores, detection_classes, num_detections],
        feed_dict={image_tensor: image_expanded})

    # Draw the results of the detection (aka 'visulaize the results')

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

    get_category_string=st.show_string(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
    get_compare_string=st.class_string(get_category_string)
    compare_string_from_category=[get_compare_string.get(value) for index,value in enumerate(classes[0]) if scores[0,index] > 0.5]

    #print ([category_index.get(value) for index,value in enumerate(classes[0]) if scores[0,index] > 0.5])
    #print(st.compare_string(compare_string_from_category))
    string_sort_list=[]
    string_sort_list = ss.string_sort(
        np.squeeze(boxes),
        np.squeeze(classes).astype(np.int32),
        np.squeeze(scores),
        category_index,
        min_score_thresh=0.50)
    #print(string_sort_list)

    ocrstring=ss.convert_list_to_str(string_sort_list)
    
    ocr_condition=ss.check_sum(ocrstring)
    print(ocr_condition)
    # Press any key to close the image

    #xml log

    #ss.write_to_excel(IMAGE_NAME_FOR_LOG,ocrstring,ocr_condition)

    return ocrstring,ocr_condition
    
    

if __name__=='__main__':
    print(ShowImage("D:/all crop OCR/All OCR_1 (1).jpg","C:/tensorflow2/models/research/object_detection/inference_graph/OCR_Faster_Rcnn_Inception_V2.pb"))
    
    cv2.waitKey(0)

    # Clean up
    cv2.destroyAllWindows()

