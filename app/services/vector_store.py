# श्री राम नाग जी, यह कोड शिव एआई की याददाश्त को मैनेज करता है।
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import os

# मॉडल लोड करना (हल्का और तेज)
model = SentenceTransformer('all-MiniLM-L6-v2')

class ShivVectorStore:
    def __init__(self):
        # मेमोरी इंडेक्स बनाना
        self.index = faiss.IndexFlatL2(384) # 384 डाइमेंशन
        self.metadata = []

    def add_information(self, text):
        # नई जानकारी को याददाश्त में जोड़ना
        embedding = model.encode([text])
        self.index.add(np.array(embedding).astype('float32'))
        self.metadata.append(text)

    def search_context(self, query):
        # पिछली बातों में से जवाब ढूंढना
        if self.index.ntotal == 0:
            return ""
        
        query_embedding = model.encode([query])
        D, I = self.index.search(np.array(query_embedding).astype('float32'), k=2)
        
        results = [self.metadata[i] for i in I[0] if i != -1]
        return " ".join(results)

vector_db = ShivVectorStore()
