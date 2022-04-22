from os.path import abspath, dirname, join
import glob
import os


MODEL = join(dirname(dirname(abspath(__file__))), 'conv2d-first-model')

PATH_IMG = join(join(dirname(dirname(abspath(__file__))), 'dataset'),'test1')

IMG = glob.glob(join(PATH_IMG,'*.jpg'))[:1]

#IMG_CHOOSEN = join(dirname(dirname(dirname(abspath(__file__)))),'ml-frontend')
