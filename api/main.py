from fastapi import FastAPI
from database.neo4j_connection import Neo4jConnection
from agents.search_agent import SearchAgent
from agents.db_agent import DBAgent
from agents.qa_agent import QnAAgent
from agents.future_works_agent import FutureWorksAgent

app = FastAPI()

# Initialize agents and database
neo4j_conn = Neo4jConnection("bolt://localhost:7687", "neo4j", "password")
search_agent = SearchAgent(neo4j_conn)
db_agent = DBAgent(neo4j_conn)
qa_agent = QnAAgent()
future_works_agent = FutureWorksAgent()

@app.get("/search")
def search_papers(topic: str):
    papers = search_agent.search_papers(topic)
    return {"papers": papers}

@app.get("/query_papers")
def query_papers(topic: str, start_year: int, end_year: int):
    papers = db_agent.get_papers_by_year(topic, start_year, end_year)
    return {"papers": papers}

@app.post("/qa")
def answer_question(question: str, context: str):
    answer = qa_agent.answer_question(question, context)
    return {"answer": answer}

@app.get("/future_works")
def future_works(context: str):
    suggestions = future_works_agent.generate_future_works(context)
    return {"future_works": suggestions}
