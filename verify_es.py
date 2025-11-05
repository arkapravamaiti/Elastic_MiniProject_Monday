import os
from dotenv import load_dotenv
from elasticsearch import Elasticsearch

load_dotenv()

def verify_data():
    """Verify data in Elasticsearch."""
    endpoint = os.getenv("ES_ENDPOINT")
    api_key = os.getenv("ES_API_KEY")
    index = os.getenv("ES_INDEX", "incident_tickets")
    
    # Connect to Elasticsearch
    es = Elasticsearch(endpoint, api_key=api_key, verify_certs=False)
    
    # Check if index exists
    if es.indices.exists(index=index):
        print(f" Index '{index}' exists!")
        
        # Get count of documents
        count = es.count(index=index)
        print(f" Total documents: {count['count']}")
        
        # Get a sample document
        result = es.search(index=index, size=1)
        if result['hits']['hits']:
            print("\n Sample document:")
            doc = result['hits']['hits'][0]['_source']
            print(f"  Ticket Number: {doc.get('Ticket Number')}")
            print(f"  Status: {doc.get('Ticket Status')}")
            print(f"  Priority: {doc.get('Ticket Priority')}")
            print(f"  Hostname: {doc.get('Hostname')}")
            print(f"  Opened Date: {doc.get('Opened Date')}")
        
        # Get statistics
        print("\nStatistics:")
        
        # Count by status
        status_agg = es.search(
            index=index,
            size=0,
            aggs={
                "statuses": {
                    "terms": {"field": "Ticket Status.keyword", "size": 10}
                }
            }
        )
        print("\n  Tickets by Status:")
        for bucket in status_agg['aggregations']['statuses']['buckets']:
            print(f"    - {bucket['key']}: {bucket['doc_count']}")
        
    else:
        print(f"Index '{index}' does not exist!")
        print("\nAvailable indices:")
        indices = es.cat.indices(format='json')
        for idx in indices:
            print(f"  - {idx['index']}")

if __name__ == "__main__":
    verify_data()
