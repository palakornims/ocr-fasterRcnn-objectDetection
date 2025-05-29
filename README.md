Command 
Object Detection

https://www.youtube.com/watch?v=yXD5_W0JPuw  yolo

https://www.youtube.com/watch?v=Rgpfk6eYxJA&t=1615s

https://github.com/EdjeElectronics/TensorFlow-Object-Detection-API-Tutorial-Train-Multiple-Objects-Windows-10


https://medium.com/@kittapas39/%E0%B8%A7%E0%B8%B4%E0%B8%98%E0%B8%B5%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%99%E0%B8%B3-tensorflow-lite-%E0%B8%A1%E0%B8%B2%E0%B9%83%E0%B8%8A%E0%B9%89%E0%B8%9A%E0%B8%99-android-%E0%B8%9C%E0%B9%88%E0%B8%B2%E0%B8%99-windows-10-%E0%B9%80%E0%B8%A3%E0%B8%B4%E0%B9%88%E0%B8%A1%E0%B8%95%E0%B8%B1%E0%B9%89%E0%B8%87%E0%B9%81%E0%B8%95%E0%B9%88%E0%B8%81%E0%B8%B2%E0%B8%A3-train-model-%E0%B8%88%E0%B8%99%E0%B8%96%E0%B8%B6%E0%B8%87-9e449647a5ce

#######################################################################################################################################

cantfind nets
run this command
set PYTHONPATH=C:\tensorflow2\models
set PYTHONPATH=C:\tensorflow2\models\research
set PYTHONPATH=C:\tensorflow2\models\research\slim

run the following commands from the C:\tensorflow2\models\research directory:

C:\tensorflow1\models\research> python setup.py build
C:\tensorflow1\models\research> python setup.py install


#######################################################################################################################################

*** set up protos before train

protoc --python_out=. .\object_detection\protos\anchor_generator.proto .\object_detection\protos\argmax_matcher.proto .\object_detection\protos\bipartite_matcher.proto .\object_detection\protos\box_coder.proto .\object_detection\protos\box_predictor.proto .\object_detection\protos\eval.proto .\object_detection\protos\faster_rcnn.proto .\object_detection\protos\faster_rcnn_box_coder.proto .\object_detection\protos\grid_anchor_generator.proto .\object_detection\protos\hyperparams.proto .\object_detection\protos\image_resizer.proto .\object_detection\protos\input_reader.proto .\object_detection\protos\losses.proto .\object_detection\protos\matcher.proto .\object_detection\protos\mean_stddev_box_coder.proto .\object_detection\protos\model.proto .\object_detection\protos\optimizer.proto .\object_detection\protos\pipeline.proto .\object_detection\protos\post_processing.proto .\object_detection\protos\preprocessor.proto .\object_detection\protos\region_similarity_calculator.proto .\object_detection\protos\square_box_coder.proto .\object_detection\protos\ssd.proto .\object_detection\protos\ssd_anchor_generator.proto .\object_detection\protos\string_int_label_map.proto .\object_detection\protos\train.proto .\object_detection\protos\keypoint_box_coder.proto .\object_detection\protos\multiscale_anchor_generator.proto .\object_detection\protos\graph_rewriter.proto .\object_detection\protos\calibration.proto .\object_detection\protos\flexible_grid_anchor_generator.proto

train model

python train.py --logtostderr --train_dir=training/ --pipeline_config_path=training/faster_rcnn_inception_v2_pets.config

tensorboard

C:\tensorflow2\models\research\object_detection>tensorboard  --logdir=training

#######################################################################################################################################

in generate_tfrecord.py change
    else:
        none
to
    else:
        0


#######################################################################################################################################

Export inference Graph

python export_inference_graph.py --input_type image_tensor --pipeline_config_path training/faster_rcnn_inception_v2_pets.config --trained_checkpoint_prefix training/model.ckpt-XXXX(number of last trained step) --output_directory inference_graph

#######################################################################################################################################

test

Full how to train model
Step 1 :
install Cuda CuDnn and anaconda and tensorflow

https://www.youtube.com/watch?v=RplXYjxgZbw

##############################################################################################################################################################

Step 2a 
Create a folder directly in C: and name it “tensorflow1”
Download the full TensorFlow object detection repository located at 
https://github.com/tensorflow/models 
by clicking the “Clone or Download”
 button and downloading the zip file. Open the downloaded zip file and extract the 
“models-master” folder directly into the C:\tensorflow1 directory you just created. 
Rename “models-master” to just “models”.


##############################################################################################################################################################

Step 2b :
download model 
https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md

##############################################################################################################################################################
Step 2c : Download this tutorial's repository from GitHub

git clone https://github.com/EdjeElectronics/TensorFlow-Object-Detection-API-Tutorial-Train-Multiple-Objects-Windows-10.git

Download the full repository located on this page (scroll to the top and click Clone or Download) and 
extract all the contents directly into the C:\tensorflow1\models\research\object_detection directory.

##############################################################################################################################################################
step 2d :
Set up new Anaconda virtual environment

conda create -n tensorflow1 pip python=3.7.4

activate tensorflow1

C:\>python -m pip install --upgrade pip

C:\> pip install --ignore-installed --upgrade tensorflow-gpu

(tensorflow1) C:\> conda install -c anaconda protobuf
(tensorflow1) C:\> pip install pillow
(tensorflow1) C:\> pip install lxml
(tensorflow1) C:\> pip install Cython
(tensorflow1) C:\> pip install contextlib2
(tensorflow1) C:\> pip install jupyter
(tensorflow1) C:\> pip install matplotlib
(tensorflow1) C:\> pip install pandas
(tensorflow1) C:\> pip install opencv-python


##############################################################################################################################################################

step 2e :
Configure PYTHONPATH environment variable

set PYTHONPATH=C:\tensorflow1\models;C:\tensorflow1\models\research;C:\tensorflow1\models\research\slim


##############################################################################################################################################################

step 2f:
Compile Protobufs and run setup.py

cd C:\tensorflow1\models\research

protoc --python_out=. .\object_detection\protos\anchor_generator.proto .\object_detection\protos\argmax_matcher.proto .\object_detection\protos\bipartite_matcher.proto .\object_detection\protos\box_coder.proto .\object_detection\protos\box_predictor.proto .\object_detection\protos\eval.proto .\object_detection\protos\faster_rcnn.proto .\object_detection\protos\faster_rcnn_box_coder.proto .\object_detection\protos\grid_anchor_generator.proto .\object_detection\protos\hyperparams.proto .\object_detection\protos\image_resizer.proto .\object_detection\protos\input_reader.proto .\object_detection\protos\losses.proto .\object_detection\protos\matcher.proto .\object_detection\protos\mean_stddev_box_coder.proto .\object_detection\protos\model.proto .\object_detection\protos\optimizer.proto .\object_detection\protos\pipeline.proto .\object_detection\protos\post_processing.proto .\object_detection\protos\preprocessor.proto .\object_detection\protos\region_similarity_calculator.proto .\object_detection\protos\square_box_coder.proto .\object_detection\protos\ssd.proto .\object_detection\protos\ssd_anchor_generator.proto .\object_detection\protos\string_int_label_map.proto .\object_detection\protos\train.proto .\object_detection\protos\keypoint_box_coder.proto .\object_detection\protos\multiscale_anchor_generator.proto .\object_detection\protos\graph_rewriter.proto .\object_detection\protos\calibration.proto .\object_detection\protos\flexible_grid_anchor_generator.proto

python setup.py build

python setup.py install


##############################################################################################################################################################

Step 3 labelImage

labelImg.py
git clone https://github.com/tzutalin/labelImg.git


##############################################################################################################################################################

Step 4 gen Data

(tensorflow1) C:\tensorflow1\models\research\object_detection> python xml_to_csv.py

For example, say you are training a classifier to detect basketballs, shirts, and shoes. You will replace the following code in generate_tfrecord.py:

# TO-DO replace this with label map
def class_text_to_int(row_label):
    if row_label == 'nine':
        return 1
    elif row_label == 'ten':
        return 2
    elif row_label == 'jack':
        return 3
    elif row_label == 'queen':
        return 4
    elif row_label == 'king':
        return 5
    elif row_label == 'ace':
        return 6
    else:
        None

** if cant use None use 0

python generate_tfrecord.py --csv_input=images\train_labels.csv --image_dir=images\train --output_path=train.record
python generate_tfrecord.py --csv_input=images\test_labels.csv --image_dir=images\test --output_path=test.record

##############################################################################################################################################################

Step 5 Create Label Map and Configure Training

The label map tells the trainer what each object is by 
defining a mapping of class names to class ID numbers. 
Use a text editor to create a new file and save it as labelmap.pbtxt in the C:\tensorflow1\models\research\object_detection\training folder. 
(Make sure the file type is .pbtxt, not .txt !) In the text editor, copy or type in the label map in the format below 
(the example below is the label map for my Pinochle Deck Card Detector):

item {
  id: 1
  name: 'nine'
}

item {
  id: 2
  name: 'ten'
}

item {
  id: 3
  name: 'jack'
}

item {
  id: 4
  name: 'queen'
}

item {
  id: 5
  name: 'king'
}

item {
  id: 6
  name: 'ace'
}

##############################################################################################################################################################S

Step 5b : Config Model
Navigate to C:\tensorflow1\models\research\object_detection\samples\configs and copy the faster_rcnn_inception_v2_pets.config file into the \object_detection\training directory.

Line 9. Change num_classes to the number of different objects you want the classifier to detect. For the above basketball, shirt, and shoe detector, it would be num_classes : 3 .

Line 106. Change fine_tune_checkpoint to:

fine_tune_checkpoint : "C:/tensorflow1/models/research/object_detection/faster_rcnn_inception_v2_coco_2018_01_28/model.ckpt"
Lines 123 and 125. In the train_input_reader section, change input_path and label_map_path to:

input_path : "C:/tensorflow1/models/research/object_detection/train.record"
label_map_path: "C:/tensorflow1/models/research/object_detection/training/labelmap.pbtxt"
Line 130. Change num_examples to the number of images you have in the \images\test directory.

Lines 135 and 137. In the eval_input_reader section, change input_path and label_map_path to:

input_path : "C:/tensorflow1/models/research/object_detection/test.record"
label_map_path: "C:/tensorflow1/models/research/object_detection/training/labelmap.pbtxt"


##############################################################################################################################################################S
Step 6 Train

Here we go! From the \object_detection directory, issue the following command to begin training:

python train.py --logtostderr --train_dir=training/ --pipeline_config_path=training/faster_rcnn_inception_v2_pets.config

plot graph
tensorboard --logdir=training


##############################################################################################################################################################
Step 7 Export influrence graph

Export Inference Graph

Now that training is complete, the last step is to generate the frozen inference graph (.pb file). 
From the \object_detection folder, issue the following command, where “XXXX” in “model.ckpt-XXXX” should be replaced with the highest-numbered .ckpt 
file in the training folder:


python export_inference_graph.py --input_type image_tensor --pipeline_config_path training/faster_rcnn_inception_v2_pets.config --trained_checkpoint_prefix training/model.ckpt-XXXX --output_directory inference_graph



This creates a frozen_inference_graph.pb file in the \object_detection\inference_graph folder. The .pb file contains the object detection classifier.


##############################################################################################################################################################

End


