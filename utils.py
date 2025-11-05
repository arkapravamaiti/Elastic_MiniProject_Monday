import os
from dotenv import load_dotenv
from elasticsearch import Elasticsearch

load_dotenv()

def get_es_client():
    """Return Elasticsearch client using endpoint + API key."""
    endpoint = os.getenv("ES_ENDPOINT")
    api_key = os.getenv("ES_API_KEY")
    if not endpoint or not api_key:
        raise ValueError("Please set ES_ENDPOINT and ES_API_KEY in .env")
    # For demo only (skip SSL verification)
    return Elasticsearch(endpoint, api_key=api_key, verify_certs=False)
