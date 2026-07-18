class AiFactCheckerClient:
    def verify(self, statement: str, reference_sources: list) -> dict:
        stmt_lower = statement.lower()
        matches = [src for src in reference_sources if any(word in src.lower() for word in stmt_lower.split() if len(word) > 4)]
        if len(matches) >= 2:
            verdict, confidence = "TRUE", round(len(matches) / len(reference_sources), 2)
            citation = f"Supported by {len(matches)} source(s): {matches[0][:80]}..."
        elif len(matches) == 1:
            verdict, confidence = "PARTIALLY TRUE", 0.5
            citation = f"Partial support found in: {matches[0][:80]}..."
        else:
            verdict, confidence = "FALSE", 0.1
            citation = "No supporting sources found in provided references."
        return {"verdict": verdict, "confidence": confidence, "citation": citation}
