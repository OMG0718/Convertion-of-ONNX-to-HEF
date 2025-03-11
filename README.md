# Convertion-of-ONNX-to-HEF
Derived from here: https://my.cytron.io/tutorial/raspberry-pi-ai-kit-onnx-to-hef-conversion

# Train data in Colab
First of all, you also need to **export .pt (pytorch file)** together with .onnx file in google colab.<br>
*** Can also export only .pt file ... <br>
*** You can direct use the link to GOOGLE COLAB. <br>
https://colab.research.google.com/github/OMG0718/Convertion-of-ONNX-to-HEF/blob/main/Copy_of_Raspberry_Pi_AI_Kit_Custom_YOLOV8.ipynb<br>

# Change the data from .pt to .onnx 
You need to have python (any version?? i just tried 3.11.9).<br>
Open CMD with administration, **pip install torch, onnx, and ultralytics** .<br> 
If faced error like OsError ( I forgot where the problem solved link ) .<br>
Go to regedit , **Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem**. <br>
change the **LongPathsEnabled** to **1**
<br><br>
After did these, run **main.py** You should have a file with .onnx extension.

# Ubuntu 22.04 in WSL 
Just flw all the steps as the link above , but make sure the <br>
&emsp; i) the hailo dataflow compiler version is **3.28.0**  &emsp; ### i just tried with this. <br>
&emsp; ii) the hailo model zoo version is **2.12.0**. <br>
&emsp;&emsp;  git clone -b v2.12 https://github.com/hailo-ai/hailo_model_zoo.git

# Last step 
When u reached to the last step, (maybe last few steps when transfering the .onnx file to WSL <br>
Just transfer the .onnx file you did just now from the main.py. 
<br><br> 
Now it should be work. 





