import logging
import sys
import pandas as pd

from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.xception import Xception
from tensorflow.keras.applications.xception import preprocess_input

from config_reader import read_config, parse_data_config, parse_train_config

logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


def train_processing(train_config_path: str = "../configs/train_config.yaml"):
    """
    Transform data, train and evaluate model and store the artifacts.
    :param train_config_path: training parameters

    :return: nothing

    """

    def make_model(learning_rate=0.1):
        base_model = Xception(
            weights='imagenet',
            include_top=False,
            input_shape=(training_params["input_size"], training_params["input_size"], 3)
        )

        base_model.trainable = False

        inputs = keras.Input(shape=(training_params["input_size"], training_params["input_size"], 3))
        base = base_model(inputs, training=False)
        vectors = keras.layers.GlobalAveragePooling2D()(base)
        outputs = keras.layers.Dense(6)(vectors)
        model = keras.Model(inputs, outputs)

        optimizer = keras.optimizers.Adam(learning_rate=learning_rate)
        loss = keras.losses.CategoricalCrossentropy(from_logits=True)

        model.compile(
            optimizer=optimizer,
            loss=loss,
            metrics=['accuracy']
        )

        return model

    config = read_config(train_config_path)
    training_params = parse_train_config(config)

    logger.info("Reading data...")
    df = pd.read_csv(training_params["input_data_path"], dtype={'Id': str})
    df['filename'] = '../data/images/' + df['Id'] + '.jpg'
    logger.info(f"  Initial dataset shape: {df.shape}.")

    threshold = int(len(df) * (1-training_params["split_test_size"]))
    df_train = df[:threshold]
    df_val = df[threshold:]

    train_Xc_datagen = ImageDataGenerator(preprocessing_function=preprocess_input,
                                          rotation_range=40,
                                          width_shift_range=0.2,
                                          height_shift_range=0.2,
                                          shear_range=0.2,
                                          zoom_range=0.2,
                                          horizontal_flip=True,
                                          fill_mode='nearest')
    train_Xc_generator = train_Xc_datagen.flow_from_dataframe(
        df_train,
        x_col='filename',
        y_col='label',
        target_size=(training_params["input_size"], training_params["input_size"]),
        batch_size=32)

    val_Xc_datagen = ImageDataGenerator(preprocessing_function=preprocess_input)
    val_Xc_generator = val_Xc_datagen.flow_from_dataframe(
        df_val,
        x_col='filename',
        y_col='label',
        target_size=(training_params["input_size"], training_params["input_size"]),
        batch_size=32
    )

    checkpoint = keras.callbacks.ModelCheckpoint(
        '../models/kitchenware_model.h5',
        save_best_only=True,
        monitor='val_accuracy',
        mode='max'
    )

    model = make_model(learning_rate=training_params["learning_rate"])
    history = model.fit(train_Xc_generator,
                        epochs=10,
                        validation_data=val_Xc_generator,
                        callbacks=[checkpoint])
    logger.info("Done.")


if __name__ == "__main__":
    train_processing()
