from tensorflow.keras import layers
from tensorflow.keras import models
from tensorflow.keras import optimizers
from tensorflow.keras.preprocessing.image import ImageDataGenerator

'''借鉴猫狗大战，设置的四层卷积、四层池化'''
model = models.Sequential()
model.add(layers.Conv2D(32, (3,3), activation = 'relu', input_shape = (150, 150,3)))
model.add(layers.MaxPooling2D((2,2)))

model.add(layers.Conv2D(64,(3,3), activation = 'relu'))
model.add(layers.MaxPooling2D(2,2))

model.add(layers.Conv2D(128,(3,3), activation = 'relu'))
model.add(layers.MaxPooling2D(2,2))

model.add(layers.Conv2D(128,(3,3), activation = 'relu'))
model.add(layers.MaxPooling2D(2,2))

model.add(layers.Flatten())#将三维展平
model.add(layers.Dense(512,activation='relu'))
model.add(layers.Dense(12,activation = 'softmax'))


model.compile(loss='categorical_crossentropy',
              optimizer = optimizers.Adam(lr = 1e-4),
              metrics = ['acc']
              )

#图片处理
train_datagen = ImageDataGenerator(rescale = 1. / 255)
test_datagen = ImageDataGenerator(rescale = 1. / 255)
validation_datagen = ImageDataGenerator(rescale = 1. / 255)

train_generator = train_datagen.flow_from_directory(
    'face_1',
    target_size = (150,150),
    batch_size = 20,
    class_mode = 'categorical'  #"categorical"会返回2D的one-hot编码标签
)


validation_generator = validation_datagen.flow_from_directory(
    'face_test',
    target_size = (150,150),
    batch_size= 20,
    class_mode = 'categorical'
)



history = model.fit_generator(
    train_generator,
    steps_per_epoch = 1200,
    epochs = 4,
    validation_data = validation_generator,
    validation_steps = 10
)

model.save('face_training1.h5')