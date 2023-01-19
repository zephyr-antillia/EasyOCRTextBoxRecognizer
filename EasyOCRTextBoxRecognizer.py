# Copyright 2023 antillia.com Toshiyuki Arai
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# EasyOCRTextBoxRecognizer.py
# 2022/10/20
# This works on Windows11

import os
import sys
import time
import glob
#import csv
#from PIL import ImageDraw, ImageFont
import easyocr

import numpy as np

import traceback
#from CosineSimilarity import CosineSimilarity
from ConfigParser import ConfigParser
from ImagePreprocessor import ImagePreprocessor

from RecognizedObjectsVisualizer import RecognizedObjectsVisualizer

class EasyOCRTextBoxRecognizer:
  def __init__(self, config_file):
    self.config    = ConfigParser(config_file)
  
    PARAMETER           = "parameter"
    self.images_dir     = self.config.get(PARAMETER, "images_dir")
    self.output_dir     = self.config.get(PARAMETER, "output_dir")
    # ['ja','en']
    self.language_hints = self.config.get(PARAMETER, "language_hints")
    self.image_format   = self.config.get(PARAMETER, "image_format")
    self.gpu            = self.config.get(PARAMETER, "gpu")
    PREPROCESSOR        = "preprocessor"
    self.preprocessing  = self.config.get(PREPROCESSOR, "preprocessing") 
    self.image_scaling  = self.config.get(PREPROCESSOR, "image_scaling")
    self.contrast       = self.config.get(PREPROCESSOR, "contrast")
    self.gray_image     = self.config.get(PREPROCESSOR, "gray_image")
    self.sharpness      = self.config.get(PREPROCESSOR, "sharpness")

    VISUALIZER          = "visualizer"
    self.font_name      = self.config.get(VISUALIZER, "font_name")
    self.draw_boundingbox = self.config.get(VISUALIZER, "draw_boundingbox")

    self.reader = easyocr.Reader(self.language_hints, gpu=self.gpu)

    #self.similarity = CosineSimilarity()


  def recognize(self): 
    if not os.path.exists(self.images_dir):
      raise Exception("Not found dir " + self.images_dir)

    if not os.path.exists(self.output_dir):
      os.makedirs(self.output_dir)  

    image_files     = glob.glob(self.images_dir +  "./*" + self.image_format)
    image_files     = sorted(image_files)
    print("--- image files {}".format(image_files))
    for image_file in image_files:
      print("image_file {}".format(image_file))
      self.recognize_one(image_file, self.output_dir)


  def recognize_one(self, image_file, output_dir):
    try:
      
      preprocessor = ImagePreprocessor(gray_image=self.gray_image, preprocessing=self.preprocessing)

      img = preprocessor.read(image_file, image_scaling=self.image_scaling, 
                              contrast=self.contrast, sharpness=self.sharpness)
    
      basename = os.path.basename(image_file)
      if self.preprocessing:
        save_image_name = "preprocessed_" + "scaling_" + str(self.image_scaling) + "_contrast_" + str(self.contrast) + "_sharpness_" + str(self.sharpness) + "_" +basename
      else:
        save_image_name = "non_preprocessed_" + basename

      enhanced_image_file = os.path.join(output_dir, save_image_name)
      img.save(enhanced_image_file) #, "PNG")
      boxies = self.reader.readtext(enhanced_image_file)
      if boxies !=None:
        visualizer  = RecognizedObjectsVisualizer(self.font_name)
        visualizer.visualize(boxies, enhanced_image_file, output_dir, self.draw_boundingbox)
      
    except:
      traceback.print_exc()

# 
if __name__ == "__main__":
  
  config_file = "./recognition.conf"

  try: 
    start_time = time.time()

    recognizer = EasyOCRTextBoxRecognizer(config_file)
            
    recognizer.recognize() 
    end_time  = time.time()
    ellapsed = round(end_time - start_time, 4)
    print("--- time       = {}".format(ellapsed))
  except:
    traceback.print_exc()
