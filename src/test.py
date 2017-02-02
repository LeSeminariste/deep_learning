import numpy
from PIL import Image
import theano

img = Image.open(open("chemin.jpg"))

img = numpy.asarray(img, dtype='float64' /256

print numpy.shade(img)

img_ = img.transpose(2,0,1).reshape(1,3,639,516)
