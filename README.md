# EasyOCRTextBoxRecognizer
EasyOCR Text Box Reconginizer

This a simple command line client EasyOCR.<br>

<h2> 
1 Install 
</h2>
We use Python3 venv on Windows11 OS.
Please create a python venv (virtual env).<br>
<pre>
python -m ven c:\py38-ocr
</pre>
, and run the following command to activate the venv.<br>
<pre>
c:\py38-ocr\scripts\activate
</pre>


<br>
<h2>
2 Install python packages
</h2>
<pre>
pip install easyocr
pip uinstall pip uninstall opencv-python-headless
pip install -U opencv-python
</pre>


<h2>
3 Sample Program
</h2>
Please open Windows Powershell console, and run the following command in the console window.<br>

> python EasyOCRTextBoxRecognizer.py

<br>
This EasyOCRTextBoxRecognizer.py script reads the following recognition.conf file.<br>
<pre>
[parameter]
images_dir       = "./samples"
output_dir       = "./outputs"
image_format     = ".png"
gpu              = False
language_hints   = ['ja','en']

[preprocessor]
preprocessing    = True
gray_image       = True
image_scaling    = 3
constrast        = 2
sharpness        = 3

[visualizer]
font_name        = "BIZ-UDMinchoM.ttc"
draw_boundingbox = True

</pre>

Please note that we specify the language_hints in this config file to be "ja" to recognize Japanese text.<br>
You have to change this language_hints property depending on your text language.<br>

Example 1: 参考・教育漢字を除く常用漢字<br>
<img src="./samples/Jyouyou-Kanji.png" width="1280" height="auto"><br>
<br>


Text Box Recognition:<br>
<img src="./outputs/preprocessed_scaling_3_contrast_2_sharpness_3_Jyouyou-Kanji.png"
     width="1280" height="auto">
<br>

Example 2: 付録常用漢字の一覧_付表<br>
<img src="./samples/Jyouyo-Kanji_fuhyou.png" width="1280" height="auto"><br>
<br>

Text Box Recognition:<br>
<img src="./outputs/preprocessed_scaling_3_contrast_2_sharpness_3_Jyouyo-Kanji_fuhyou.png"
     width="1280" height="auto">
<br>


Example 3: 半角カタカナ一覧<br>
<img src="./samples/Hankaku-katakana.png" width="1280" height="auto"><br>
<br>


Text Box Recognition:<br>
<img src="./outputs/preprocessed_scaling_3_contrast_2_sharpness_3_Hankaku-katakana.png"
     width="1280" height="auto">
<br>

Example 4: VSCodeScreenShot<br>
<img src="./samples/VSCodeScreenShot.png" width="1280" height="auto"><br>
<br>


Text Box Recognition:<br>
<img src="./outputs/preprocessed_scaling_3_contrast_2_sharpness_3_VSCodeScreenShot.png"
     width="1280" height="auto">
<br>

Example 5: Symbols_Kakana<br>
<img src="./samples/Symbols_Kakana.png" width="1280" height="auto"><br>
<br>


Text Box Recognition:<br>
<img src="./outputs/preprocessed_scaling_3_contrast_2_sharpness_3_Symbols_Kakana.png"
     width="1280" height="auto">
<br>


