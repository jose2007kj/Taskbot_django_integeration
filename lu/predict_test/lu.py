# coding: utf-8
import json,re
from .once import run_once
from keras.models import Sequential, Model, load_model
from predict.kj_predict import KerasModel

from django.conf import settings

from datetime import datetime

def multi_turn_lu3(user_id, sentence, reset=False):
    
    single_turn_lu_setup_new()
    #testing sentance parsing
    line = sentence.lower()
    removed = re.sub(r",\s+", " ", line)#for removing hello, I am also taking care of 23,000
    dot = re.sub(r"\.+", " ", removed)#for removing one or more dots
    
    remov = re.sub(r"\?+", " ", dot)# remove ?
    exc = re.sub(r"\!+", " ", remov)#remove !
    exc =exc.rstrip()
    pattern = re.compile(r'\s+')
    final = re.sub(pattern," ", exc) #for removing extra spaces
    final= final.replace('$',"") #for removing $
    utt = final
    temp_utt = list()
    temp_tags = list()
    mywords = utt.split()
    utterances=list()#comment this to have previous conversations
    # mytags = t.split()
    # now add the words and tags to word and tag dictionaries
    # also save the word and tag sequence in training data sets
    for i in xrange(len(mywords)):
        if mywords[i] not in getWordVocab:
            temp_utt.append(1) #i.e. append unknown word
        else:
            temp_utt.append(getWordVocab[mywords[i]])
        # if mytags[i] not in tag2id:
        # 	temp_tags.append(1)
        # else:
        # 	temp_tags.append(tag2id[mytags[i]])
    # utt_count += 1
    utterances.append(temp_utt)

    # testing sentance parsing
    test = KerasModel()
    test.run(utterances,getWordVocabSize,getTagVocabSize,getIndex2Tag,model)
    
    return 'semantics', 'status', 'action',test.slots



@run_once
def single_turn_lu_setup_new():
    global model,emptyIndex,getWordVocab,getTagVocab,getIndex2Word,utterances,tags,starts,startid,getIndex2Tag,getWordVocabSize,getTagVocabSize
    # global emptyVocab = {}
    emptyIndex = list()
    getWordVocab = []
    getTagVocab = []
    getIndex2Word = []
    utterances = list()
    tags = list()
    starts = list()
    startid = list()
    getIndex2Tag=[]
    utt_count = 0
    temp_startid = 0
    print("hhhhh",getWordVocab)
    # trainData = dataSet(self.training_file,'train',emptyVocab,emptyVocab,emptyIndex,emptyIndex)
    with open('%s/predict/wordDictionary.json'% settings.BASE_DIR) as json_data:
        print("indisdeeeee")
        getWordVocab= json.load(json_data)
        # = json.load(json_data)
        # print("ddddd",d)
        getWordVocabSize = len(getWordVocab)
    with open('%s/predict/tagDictionary.json'% settings.BASE_DIR) as json_data:
        getTagVocab = json.load(json_data)
        getTagVocabSize = len(getTagVocab)
    with open('%s/predict/id2word.json'% settings.BASE_DIR) as json_data:
        getIndex2Word = json.load(json_data)
    with open('%s/predict/id2tag.json'% settings.BASE_DIR) as json_data:
        getIndex2Tag = json.load(json_data)
    
    # load model
    model = load_model('%s/predict/train.h5' % settings.BASE_DIR)
    print('[Info]done........ model loaded.')
    return
