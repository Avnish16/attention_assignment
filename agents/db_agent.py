class DBAgent:
    def __init__(self, neo4j_conn):
        self.neo4j_conn = neo4j_conn

    def get_papers_by_year(self, topic, start_year, end_year):
        return self.neo4j_conn.query_papers_by_year(topic, start_year, end_year)
