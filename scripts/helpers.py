from PIL import Image
import numpy as np
import pandas as pd

def prepro_img(path):
    img = []
    for i in path:
        image = Image.open(r"{}".format(i)).resize((128, 128)).convert('RGBA')
        image = np.array(image)
        image = image[np.newaxis,...]
        img.append(image)
    return img

def result(prediction):
    print('np.squeeze(prediction)=', np.squeeze(prediction)[np.newaxis,...].shape)
    results = pd.DataFrame(np.squeeze(prediction)[np.newaxis,...], columns = ['Dog','Cat'])
    result = []
    for i in range(len(results)):
        if results['Dog'].iloc[i] > results['Cat'].iloc[i]:
            result.append('Is a Dog!')
        else:
            result.append('Is a Cat!')
    return result