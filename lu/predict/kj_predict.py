"""
RNN-based slot filling
by V. Chen, D. Hakkani-Tur & G. Tur
"""
from django.conf import settings
import os, sys, json, re
import numpy as np 
from scipy import io
# from wordSlotDataSet import dataSet, readNum
from PredefinedEmbedding import PredefinedEmbedding
from Encoding import encoding
# import argparse
from keras.preprocessing import sequence
from keras.models import Model


class KerasModel():
	
	def __init__(self):
		
		# PARAMETERS
		self.slots=''
		self.hidden_size = 50 # size of hidden layer of neurons 
		self.learning_rate = 1e-2
		# self.training_file = argparams['train_data_path']
		self.validation_file = None
		
		self.input_type = 'embedding' # options: 1hot, embedding, predefined
		
		self.arch = 'blstm'
		
		self.time_length = 60
		
		self.time_decay = False
		
		self.tag_format = 'conlleval'
		self.e2e_flag = False
		
		self.model_arch = self.arch
		if self.validation_file is None:
			self.nodev = True
		else:
			self.nodev = False
		if self.input_type == 'embedding':
			self.model_arch = self.model_arch + '+emb'
		if self.time_decay:
			self.model_arch = self.model_arch + '+T'
		if self.e2e_flag:
			self.model_arch = 'e2e-' + self.model_arch
	
	def test(self, H, X, data_type, tagDict, pad_data, model):
		
		if 'memn2n' in self.arch or self.arch[0] == 'h':
			batch_data = [H, X]
		else:
			batch_data = X

		probability = model.predict(batch_data)
		prediction = np.argmax(probability, axis=2)

		# output prediction and probability results
		fo = open("%s/st.antony1." %settings.BASE_DIR+ data_type, "wb")
		# global slots
		self.slots=''
		for i, sent in enumerate(prediction):
			for j, tid in enumerate(sent):
				if pad_data[i][j] != 0:
					if self.tag_format == 'normal':
						fo.write(tagDict[tid] + ' ')
						self.slots=self.slots+tagDict[tid] + ' '
					elif self.tag_format == 'conlleval':
						fo.write(tagDict[tid] + ' ')
						self.slots=self.slots+tagDict[tid] + ' '
			fo.write('\n')
			self.slots=self.slots+'\n'
		fo.close()
		
		print("done;;;;;;;;==========")
		

	
	def run(self,utterances,getWordVocabSize,getTagVocabSize,getIndex2Tag,model):
		
		pad_X_test = sequence.pad_sequences(utterances, maxlen=self.time_length, dtype='int32', padding='pre')
		num_sample_test, max_len = np.shape(pad_X_test)
		self.input_vocab_size = getWordVocabSize
		self.output_vocab_size = getTagVocabSize
		X_test = encoding(pad_X_test, self.input_type, self.time_length, self.input_vocab_size)
		
		if self.nodev:
			H_dev = X_dev = y_dev = None
		H_train = H_test = H_dev = None
		self.test(H=H_test, X=X_test, data_type='test', tagDict=getIndex2Tag, pad_data=pad_X_test, model=model)
		