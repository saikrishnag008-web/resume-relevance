from io import BytesIO
from typing import Any, Dict, List, Set
import re
from docx import Document


_STOPWORDS: Set[str] = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "has", "he", "in", "is", "it",
    "its", "of", "on", "that", "the", "to", "was", "were", "will", "with", "this", "those", "these",
}

_TOKEN_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9_+.#-]{1,}")


def extract_text_from_file(content: bytes, filename: str) -> str:
    name = (filename or "").lower()
    try:
        if name.endswith(".pdf"):
            try:
                # Fallback using PyPDF2
                import PyPDF2  # type: ignore
                reader = PyPDF2.PdfReader(BytesIO(content))
                parts: List[str] = []
                for page in getattr(reader, 'pages', []):
                    try:
                        parts.append(page.extract_text() or "")
                    except Exception:
                        continue
                return "\n".join([p for p in parts if p]).strip()
            except Exception:
                return ""
        if name.endswith(".docx"):
            # Use python-docx to parse DOCX from memory
            doc = Document(BytesIO(content))
            parts: List[str] = []
            for p in doc.paragraphs:
                if p.text and p.text.strip():
                    parts.append(p.text.strip())
            return "\n".join(parts).strip()
        if name.endswith(".txt"):
            return content.decode("utf-8", errors="ignore")
    except Exception:
        # Best-effort fallback; in production, consider logging the exception
        return ""
    return ""


def _tokenize(text: str) -> List[str]:
    if not text:
        return []
    tokens = [t.lower() for t in _TOKEN_RE.findall(text)]
    return [t for t in tokens if t not in _STOPWORDS]


def evaluate_resume(resume_text: str, jd_text: str) -> Dict[str, Any]:
    jd_tokens = _tokenize(jd_text)
    resume_tokens = set(_tokenize(resume_text))

    matched = [kw for kw in jd_tokens if kw in resume_tokens]
    missing = [kw for kw in jd_tokens if kw not in resume_tokens]

    total = len(jd_tokens)
    score = int((len(matched) / total) * 100) if total else 0

    if score >= 80:
        verdict = "High"
    elif score >= 50:
        verdict = "Medium"
    else:
        verdict = "Low"

    feedback = f"Consider adding: {', '.join(sorted(set(missing))[:8])}" if missing else "Excellent match!"

    return {
        "score": score,
        "verdict": verdict,
        "matched": matched,
        "missing": missing,
        "feedback": feedback,
    }
