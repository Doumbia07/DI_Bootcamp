from google.colab import files
files.upload()

!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

!kaggle datasets download -d olgabelitskaya/flower-color-images

!unzip -q flower-color-images.zip

!pip install tensorflow keras pillow scipy matplotlib

import matplotlib.pyplot as plt
from PIL import Image, ImageOps
from scipy.ndimage import rotate
import numpy as np

image_path = 'flowers/flowers/19_010.png'
original_image = Image.open(image_path)

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(original_image)
plt.title('Original Image')
plt.axis('off')

def rotate_image_30_degrees(image):
    return rotate(image, 30, reshape=True)

rotated = rotate_image_30_degrees(np.array(original_image))
plt.subplot(2, 2, 2)
plt.imshow(rotated.astype(np.uint8))
plt.title('Rotated 30 degrees')
plt.axis('off')

flipped_horiz = ImageOps.mirror(original_image)
plt.subplot(2, 2, 3)
plt.imshow(flipped_horiz)
plt.title('Horizontally Flipped')
plt.axis('off')

flipped_vert = ImageOps.flip(original_image)
plt.subplot(2, 2, 4)
plt.imshow(flipped_vert)
plt.title('Vertically Flipped')
plt.axis('off')

plt.tight_layout()
plt.show()

w, h = original_image.size
zoom_factor = 1.2
new_size = (int(w * zoom_factor), int(h * zoom_factor))
zoomed = original_image.resize(new_size, Image.Resampling.LANCZOS)

center = (zoom_factor * w / 2, zoom_factor * h / 2)
left = center[0] - w/2
top = center[1] - h/2
right = center[0] + w/2
bottom = center[1] + h/2

zoomed_cropped = zoomed.crop((left, top, right, bottom))
zoomed_cropped = zoomed_cropped.resize((w, h), Image.Resampling.LANCZOS)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(original_image)
plt.title('Original')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(zoomed_cropped)
plt.title('Zoomed In (1.2x)')
plt.axis('off')
plt.show()