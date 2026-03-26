from __future__ import annotations

from dataclasses import dataclass

from retriever import retrieve_chunks


@dataclass
class RagResult:
    answer: str
    passages: list[dict[str, object]]


class RagAgent:
    def __init__(self, knowledge_path: str, top_k: int = 2):
        self.knowledge_path = knowledge_path
        self.top_k = top_k

    def answer(self, question: str) -> RagResult:
        passages = retrieve_chunks(question, self.knowledge_path, self.top_k)
        if not passages:
            return RagResult(
                answer="知识库里没有找到足够相关的内容，请换个更明确的问题。",
                passages=[],
            )

        best_passage = passages[0]
        answer = f"根据《{best_passage['source']}》，{best_passage['text']}"
        return RagResult(answer=answer, passages=passages)
