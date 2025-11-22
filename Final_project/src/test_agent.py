from smart_agent import SmartFarmingAgent

agent = SmartFarmingAgent()

print("\n=== TEST 1: Crop Recommendation ===")
crop = agent.answer(
    "recommend a crop",
    inputs={
        "N": 90,
        "P": 42,
        "K": 43,
        "temperature": 25,
        "humidity": 80,
        "ph": 6.5,
        "rainfall": 120,
        "soil_fertility": 7,
        "climate_index": 8
    }
)
print(crop)

print("\n=== TEST 2: RAG Knowledge Base ===")
rag = agent.answer("Which crop grows well in clay soil?")
print(rag)
