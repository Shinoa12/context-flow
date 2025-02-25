from datetime import datetime

def generate_metadata(url: str, title: str, chunks: list):
    timestamp = datetime.now().isoformat()
    metadata_list = []

    for index, chunk in enumerate(chunks):
        metadata = {
            "url": url,
            "title": title,
            "section": "Full Article",
            "chunk_index": index + 1,
            "timestamp": timestamp,
            "source": "Wikipedia"
        }
        metadata_list.append(metadata)

    return metadata_list
