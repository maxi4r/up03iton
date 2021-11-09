import numpy as np
from ipywidgets import interact, fixed
from PIL import Image

def imshow(X, resize=None):
    """
    You should create a way to resize an image from an array X.
    The use of widgets is optional but you can take a look to interact.
    We should be able to install this package in Google Colab from your Git repo.
    """
    im = Image.fromarray(X)
    print("converted image")
    if resize:
        # assuming resize is a tuple spedifing the new size
        im.resize(resize)
    print("resized image")
    # assuming the function is supposed to also show the image since its name is imshow.
    im.show()

