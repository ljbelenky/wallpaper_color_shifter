import numpy as np 
import os
from PIL import Image


original_directory = '/usr/share/backgrounds/pop'
new_directory = 'new_wallpaper'
fname = 'ferdinand-stohr-149422.jpg'
# fname = 'sebastien-gabriel-232361.jpg'

try:
    os.makedirs(new_directory)
except:
    pass

f = os.path.join(original_directory, fname)

image = Image.open(f)

image.show()

j = np.asarray(image)

k = 0

a, b, c = j[:,:,0], j[:,:,1], j[:,:,2]
A, B, C = 255-a, 255-b, 255-c
d = a * 0
D = d + 255

layers = [a, b, c, A, B, C, d, D]

for first in layers:
    for second in layers:
        for third in layers:
            j = np.stack([first, second, third], axis = 2)

            i = Image.fromarray(j)

            i.save(os.path.join(new_directory,f'{k}.png'))
            # i.save(f'focal_fossa/ff_{k}.png')
            k +=1