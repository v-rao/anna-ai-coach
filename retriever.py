from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class KnowledgeRetriever:
    def __init__(self, kb_path):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        with open(kb_path, 'r') as f:
            self.docs = [line.strip() for line in f if line.strip()]
        self.embeddings = self.model.encode(self.docs)
        self.index = faiss.IndexFlatL2(self.embeddings.shape[1])
        self.index.add(np.array(self.embeddings))
    
    def search(self, query, k=2):
        q_emb = self.model.encode([query])
        distances, idxs = self.index.search(np.array(q_emb), k)
        return "\n".join([self.docs[i] for i in idxs[0]])
