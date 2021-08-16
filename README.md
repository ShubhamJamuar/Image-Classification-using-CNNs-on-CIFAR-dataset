# Image-Classification-using-CNNs-on-CIFAR-dataset
Image Classification Model Built on a subset of CIFAR-10 Dataset for Classification of various images.<br>
The Sequential Model takes an image with input Size (32,32,3) and produces a output vector with 3 classes.<br>
1.Aeroplane<br>
2.Car<br>
3.Bird<br>

To Use:<br>
1.Download the GIT repository as Zip and Extract.<br>
2.Run <i>pip install requirements.txt</i> <br>
2.5.Change the working directory Command in <i>server.py</i> "os.chdir(r"C:\Users\LENOVO\Desktop\sample_project_1\Take It Out")" to os.chdir({YOUR WORKING DIRECTORY}) .<br> 
3.Run <i>server.py</i> on Terminal.<br>
4.Open <i>http://127.0.0.1:5000/index</i>

Information about the custom model:<br>
Model architecture:<br>

conv2d (Conv2D)              (None, 32, 32, 32)        896       
_________________________________________________________________
batch_normalization (BatchNo (None, 32, 32, 32)        128       
_________________________________________________________________
conv2d_1 (Conv2D)            (None, 30, 30, 32)        9248      
_________________________________________________________________
max_pooling2d (MaxPooling2D) (None, 15, 15, 32)        0         
_________________________________________________________________
dropout (Dropout)            (None, 15, 15, 32)        0         
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 15, 15, 64)        18496     
_________________________________________________________________
batch_normalization_1 (Batch (None, 15, 15, 64)        256       
_________________________________________________________________
conv2d_3 (Conv2D)            (None, 13, 13, 64)        36928     
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 6, 6, 64)          0         
_________________________________________________________________
dropout_1 (Dropout)          (None, 6, 6, 64)          0         
_________________________________________________________________
conv2d_4 (Conv2D)            (None, 6, 6, 128)         73856     
_________________________________________________________________
batch_normalization_2 (Batch (None, 6, 6, 128)         512       
_________________________________________________________________
conv2d_5 (Conv2D)            (None, 4, 4, 128)         147584    
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 2, 2, 128)         0         
_________________________________________________________________
dropout_2 (Dropout)          (None, 2, 2, 128)         0         
_________________________________________________________________
flatten (Flatten)            (None, 512)               0         
_________________________________________________________________
Output Layer


