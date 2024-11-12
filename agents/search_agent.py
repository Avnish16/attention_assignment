import requests

class SearchAgent:
    def __init__(self, neo4j_conn):
        self.neo4j_conn = neo4j_conn

    def search_papers(self, topic):
        # Sample placeholder for querying Arxiv or any other academic source
        papers = [{"title": "Sample Title", "abstract": "Sample Abstract", "authors": "Sample Author", "year": 2022}]
        
        for paper in papers:
            self.neo4j_conn.add_paper(paper["title"], paper["abstract"], paper["authors"], paper["year"])
        
        return papers
