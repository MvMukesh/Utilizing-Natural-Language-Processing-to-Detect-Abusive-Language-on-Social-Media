# Creating model architecture.
from abusive_language.constants import *
from abusive_language.entity.config_entity import ModelTrainerConfig
from keras.models import Sequential
from keras.optimizers import RMSprop
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.layers import LSTM,Activation,Dense,Dropout,Input,Embedding,SpatialDropout1D


class ModelArchitecture:
    def __init__(self):
        pass

    
    def get_model(self):
        model = Sequential()
        model.add(Embedding(MAX_WORDS, 100,input_length=MAX_LEN))
        model.add(SpatialDropout1D(0.2))
        model.add(LSTM(100,dropout=0.2,recurrent_dropout=0.2))
        model.add(Dense(1,activation=ACTIVATION))
        model.summary()
        model.compile(loss=LOSS,optimizer=RMSprop(),metrics=METRICS)
        return model
    
                        ### --- Manralai.in --- ###