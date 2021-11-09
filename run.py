import imageio as io
import matplotlib.pyplot as plt
from up03iton import function

url = 'https://www.fau.de/files/2019/07/Kollegienhaus_Malter_3-480x284.jpg'
img = io.imread(url)
plt.imshow(img)
plt.show()
function.imshow(img)
