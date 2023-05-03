from models.base_model import BaseModel

class InferenceModel(BaseModel):
    
    def __init__(self, FLAGS, vocab_size):
        
        super(InferenceModel,self).__init__(FLAGS, vocab_size)
