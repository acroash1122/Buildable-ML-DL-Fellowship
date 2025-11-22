import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class RAGQA:
    def __init__(self, index_path="/content/drive/MyDrive/data_now/faiss_index.bin",
                       meta_path="/content/drive/MyDrive/data_now/chunks.json"):
        self.model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
        self.index = faiss.read_index(index_path)

        with open(meta_path, "r", encoding="utf-8") as f:
            self.chunks = json.load(f)["chunks"]

        self.tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
        self.gen_model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")

    def retrieve(self, query, k=3):
        q_emb = self.model.encode([query], convert_to_numpy=True)
        _, indices = self.index.search(q_emb, k)
        return [self.chunks[i] for i in indices[0]]

    def answer(self, query):
        context = "\n".join(self.retrieve(query))
        prompt = f"""You are an agriculture expert.
        Use this context to answer.

        Context:
        {context}

        Question: {query}
        Answer:
        """
        inputs = self.tokenizer(prompt, return_tensors="pt")
        output = self.gen_model.generate(**inputs, max_new_tokens=200)
        ans = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return ans
