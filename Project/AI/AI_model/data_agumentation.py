from numpy import expand_dims
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import load_img, img_to_array
from matplotlib import pyplot as plt

img = load_img('./datasets/tmp_images/hair2/204.jpg')
data = img_to_array(img)
plt.show(img)
# samples = expand_dims(data,0)

# train_datagen = ImageDataGenerator(
#             # rescale=1./255,
#             # rotation_range=90,
#             # width_shift_range=0.5,
#             # height_shift_range=0.5,
#             # shear_range=0.1,
#             zoom_range=0.1,
#             # horizontal_flip=True,
#             # fill_mode='nearest'
#             )

# it = train_datagen.flow(samples, batch_size=1)

# fig = plt.figure(figsize=(20,20))
# for i in range(9):
#     plt.subplot(250,250,1+i)

#     batch = it.next()
#     image = batch[0].astype('uint8')
#     plt.imshow(image)
# plt.show()