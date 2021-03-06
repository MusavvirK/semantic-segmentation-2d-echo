# -*- coding: utf-8 -*-
"""ThesisV2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XOShrDKCrn157-8-1P7d-dejgJczfbgm
"""

from google.colab import drive
drive.mount('/content/drive/')

!pip install simpleITK

cd /content/drive/My Drive/echo/

# Commented out IPython magic to ensure Python compatibility.
# %tensorflow_version 1.x

!python3 src/main.py \
 --dataset_path="/content/drive/My Drive/Neural Network Dataset/" \
 --config=configs/ventricle.json