class SessionMemory:
    """
    Lightweight in-memory session history for recent agent interactions.
    Stores the most recent questions and compact summaries of results.
    """

    def __init__(self, max_items: int = 5):
        self.max_items = max_items
        self.history = []

    def add_entry(self, question: str, mode: str, output_summary: str) -> None:
        entry = {
            "question": question.strip(),
            "mode": mode.strip(),
            "output_summary": output_summary.strip(),
        }
        self.history.append(entry)

        if len(self.history) > self.max_items:
            self.history.pop(0)

    def get_history(self) -> list[dict]:
        return self.history

    def get_recent_context(self) -> str:
        if not self.history:
            return "No prior session history."

        lines = []
        for i, entry in enumerate(self.history, start=1):
            lines.append(f"{i}. [{entry['mode'].upper()}] {entry['question']}")
            lines.append(f"   {entry['output_summary']}")
        return "\n".join(lines)

    def clear(self) -> None:
        self.history = []