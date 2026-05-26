from PIL import Image
import numpy as np

names = ["ball2", "ball1", "shielded_jar", "shield", "bomb", "candy", "cheese", "coin", "jar"]

for name in names:
    if name == "candy":
        for i in range(1, 7):
            im = Image.open(f"candy{i}.png").convert("RGBA")

            alpha = im.split()[-1]

            data = np.array(im)
            r, g, b, a = data.T

            a[(a == 1)] = 0

            img_new = Image.fromarray(data)
            img_new.save('output.png')

            bbox = img_new.getbbox()
            im2 = im.crop(bbox)

            im2.save(f"candy{i}_cropped.png")
    else:
        im = Image.open(f"{name}.png").convert("RGBA")

        alpha = im.split()[-1]

        data = np.array(im)
        r, g, b, a = data.T

        a[(a == 1)] = 0

        img_new = Image.fromarray(data)
        img_new.save('output.png')

        bbox = img_new.getbbox()
        im2 = im.crop(bbox)

        im2.save(f"{name}_cropped.png")