from crop_predictor import CropPredictor
from disease_detector import DiseaseDetector
from rag_qa_tool import RAGQA

class SmartFarmingAgent:
    def __init__(self):
        self.crop_tool = CropPredictor()
        self.disease_tool = DiseaseDetector()
        self.rag_tool = RAGQA()

    def route(self, query, image_path=None):
        
        q = query.lower()

        # ---- Crop Recommendation ----
        if "crop" in q and ("recommend" in q or "which" in q or "suitable" in q):
            return "crop"

        # ---- Disease Detection ----
        if image_path is not None:
            return "disease"
        if "disease" in q or "leaf" in q or "detect" in q:
            return "disease"

        # ---- Default → RAG KB ----
        return "rag"

    def answer(self, query, inputs=None, image_path=None):

        decision = self.route(query, image_path=image_path)

        if decision == "crop":
            result = self.crop_tool.predict(inputs)
            return f"Recommended crop: {result}"

        elif decision == "disease":
            result = self.disease_tool.predict(image_path)
            return f"Predicted disease: {result}"

        else:
            result = self.rag_tool.answer(query)
            return result
