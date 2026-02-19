from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


class SemanticSimilarityEngine:
    def __init__(self, texts):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.embeddings = self.model.encode(texts, convert_to_tensor=True)

    def find_best_match(self, new_text):
        new_embedding = self.model.encode([new_text], convert_to_tensor=True)

        scores = cosine_similarity(
            new_embedding.cpu(),
            self.embeddings.cpu()
        )

        best_index = scores.argmax()
        best_score = scores[0][best_index]

        return best_index, float(best_score)


