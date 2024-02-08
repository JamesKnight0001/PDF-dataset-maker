import json
import re

class Converter:
    @classmethod
    def add_jsonl(cls, file_path, question=None, answer=None):
        data = {"question": question, "answer": answer}
        with open(file_path, "a") as f:
            json.dump(data, f)
            f.write('\n')
    
    @classmethod
    def split_text(cls, text, chunk_size=1024):
        delimiters = r'[.!?;]'

        chunks = re.split(delimiters, text)

        chunks = [chunk.strip() for chunk in chunks if chunk.strip()]

        combined_chunks = []
        current_chunk = ''
        for chunk in chunks:
            if len(current_chunk) + len(chunk) <= chunk_size:
                current_chunk += chunk
            else:
                combined_chunks.append(current_chunk)
                current_chunk = chunk
        combined_chunks.append(f"{current_chunk}.")

        return combined_chunks
