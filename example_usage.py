from client import AiFactCheckerClient
client = AiFactCheckerClient()
result = client.verify(
    statement="Python is the most popular language for AI development in 2026",
    reference_sources=[
        "Python continues to dominate AI and machine learning development in 2026 according to Stack Overflow surveys.",
        "Python usage in data science and artificial intelligence grew 23% year-over-year.",
        "JavaScript remains top for web development while Python leads in AI."
    ]
)
print(f"Verdict: {result['verdict']} (confidence: {result['confidence']})")
print(f"Citation: {result['citation']}")
