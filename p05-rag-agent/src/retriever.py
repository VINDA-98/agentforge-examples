from __future__ import annotations

from pathlib import Path
import json
import re


STOP_CHARS = set("的了是我你他她它在和与就再都很还吗呢啊把让用会能要先后再去做第章个里")


def load_knowledge_base(knowledge_path: str) -> list[dict[str, str]]:
    return json.loads(Path(knowledge_path).read_text(encoding="utf-8"))


def tokenize(text: str) -> set[str]:
    english_tokens = re.findall(r"[A-Za-z0-9]+", text.lower())
    chinese_tokens = [
        char
        for char in text
        if "\u4e00" <= char <= "\u9fff" and char not in STOP_CHARS
    ]
    return set(english_tokens + chinese_tokens)


def build_chunks(knowledge_path: str) -> list[dict[str, object]]:
    chunks: list[dict[str, object]] = []
    for document in load_knowledge_base(knowledge_path):
        sentences = [item.strip() for item in document["content"].split("。") if item.strip()]
        for index, sentence in enumerate(sentences, start=1):
            text = f"{sentence}。"
            chunks.append(
                {
                    "source": document["title"],
                    "chunk_id": f"{document['id']}-{index}",
                    "text": text,
                    "tokens": tokenize(text),
                }
            )
    return chunks


def retrieve_chunks(question: str, knowledge_path: str, top_k: int = 2) -> list[dict[str, object]]:
    question_tokens = tokenize(question)
    scored_chunks: list[dict[str, object]] = []

    for chunk in build_chunks(knowledge_path):
        score = len(question_tokens & set(chunk["tokens"]))
        if score > 0:
            scored_chunks.append(
                {
                    "source": chunk["source"],
                    "chunk_id": chunk["chunk_id"],
                    "text": chunk["text"],
                    "score": score,
                }
            )

    scored_chunks.sort(key=lambda item: item["score"], reverse=True)
    return scored_chunks[:top_k]
