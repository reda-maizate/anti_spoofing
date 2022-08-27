import tensorflow as tf
from keras import layers, Input, Model, Sequential
from src.dl import config as conf

with tf.device("/cpu:0"):
    data_augmentation = Sequential(
        [
            layers.RandomRotation(0.15),
        ]
    )


def resnet_model(input_shape, num_classes):
    inputs = Input(shape=input_shape)
    hidden_layer = data_augmentation(inputs)

    # Entry block
    hidden_layer = layers.Rescaling(1.0 / 255)(hidden_layer)
    hidden_layer = layers.Conv2D(32, 3, strides=2, padding="same")(hidden_layer)
    hidden_layer = layers.BatchNormalization()(hidden_layer)
    hidden_layer = layers.Activation("relu")(hidden_layer)

    hidden_layer = layers.Conv2D(64, 3, padding="same")(hidden_layer)
    hidden_layer = layers.BatchNormalization()(hidden_layer)
    hidden_layer = layers.Activation("relu")(hidden_layer)

    previous_block_activation = hidden_layer  # Set aside residual

    for size in [128, 256]:
        hidden_layer = layers.Activation("relu")(hidden_layer)
        hidden_layer = layers.SeparableConv2D(size, 3, padding="same")(hidden_layer)
        hidden_layer = layers.BatchNormalization()(hidden_layer)

        hidden_layer = layers.Activation("relu")(hidden_layer)
        hidden_layer = layers.SeparableConv2D(size, 3, padding="same")(hidden_layer)
        hidden_layer = layers.BatchNormalization()(hidden_layer)

        hidden_layer = layers.MaxPooling2D(3, strides=2, padding="same")(hidden_layer)

        # Project residual
        residual = layers.Conv2D(size, 1, strides=2, padding="same")(
            previous_block_activation
        )
        hidden_layer = layers.add([hidden_layer, residual])  # Add back residual
        previous_block_activation = hidden_layer  # Set aside next residual

    hidden_layer = layers.SeparableConv2D(512, 3, padding="same")(hidden_layer)
    hidden_layer = layers.BatchNormalization()(hidden_layer)
    hidden_layer = layers.Activation("relu")(hidden_layer)

    hidden_layer = layers.GlobalAveragePooling2D()(hidden_layer)

    hidden_layer = layers.Dropout(0.5)(hidden_layer)
    outputs = layers.Dense(num_classes, activation="softmax")(hidden_layer)
    return Model(inputs, outputs)


model = resnet_model(input_shape=conf.IMAGE_SHAPE + (3,), num_classes=conf.NUM_CLASSES)
# keras.utils.plot_model(model, show_shapes=True)
