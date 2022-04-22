import tensorflow as tf
from configback import MODEL
from helpers import prepro_img,result


model = tf.keras.models.load_model(MODEL)

def model_prediction(uploaded_file):

    images = prepro_img(uploaded_file)

    predict = []
    for img_file in images:
        predict.append(model.predict(img_file))


    results = result(predict)
    return results
