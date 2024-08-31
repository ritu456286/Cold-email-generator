import pandas as pd
import chromadb
import uuid

class Portfolio:
    def __init__(self, file_path="./resources/my_portfolio.csv") -> None:
       self.file_path = file_path
       self.df = pd.read_csv(file_path)
       self.chroma_client = chromadb.PersistentClient("vectorStore")
       self.collection = self.chroma_client.get_or_create_collection(name="portfolio")

    def load_portfolio(self):
        """This function loads the links documents into the portfolio collection"""
        if not self.collection.count():
            for index, row in self.df.iterrows():
                self.collection.add(documents=row['Techstack'],
                                    metadatas={'links': row['Links']},
                                    ids=[str(uuid.uuid4())])

    def query_links(self, skills):
        relevant_profile_links = self.collection.query(query_texts=skills, n_results=2).get('metadatas', [])
        return relevant_profile_links