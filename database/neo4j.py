from neo4j import GraphDatabase

class Neo4jConnection:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def add_paper(self, title, abstract, authors, year):
        with self.driver.session() as session:
            session.run(
                """
                CREATE (p:Paper {title: $title, abstract: $abstract, authors: $authors, year: $year})
                """,
                title=title, abstract=abstract, authors=authors, year=year
            )

    def query_papers_by_year(self, topic, start_year, end_year):
        with self.driver.session() as session:
            result = session.run(
                """
                MATCH (p:Paper)
                WHERE p.title CONTAINS $topic AND p.year >= $start_year AND p.year <= $end_year
                RETURN p.title AS title, p.abstract AS abstract, p.authors AS authors, p.year AS year
                """,
                topic=topic, start_year=start_year, end_year=end_year
            )
            return [record.data() for record in result]
