from typing import List

from project.document import Document
from project.topic import Topic
from project.category import Category


class Storage:
    categories: List[Category] = []
    topics: List[Topic] = []
    documents: List[Document] = []

    def add_category(self, category: Category):
        if category not in Storage.categories:
            Storage.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in Storage.topics:
            Storage.topics.append(topic)

    def add_document(self, document: Document):
        if document not in Storage.documents:
            Storage.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category = next(filter(lambda c: c.id == category_id, self.categories))
        category_idx = self.categories.index(category)
        self.categories[category_idx].edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = next(filter(lambda t: t.id == topic_id, self.topics))
        topic_idx = self.topics.index(topic)
        self.topics[topic_idx].edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        document = next(filter(lambda d: d.id == document_id, self.documents))
        document_idx = self.documents.index(document)
        self.documents[document_idx].edit(new_file_name)

    def delete_category(self, category_id):
        category = next(filter(lambda c: c.id == category_id, self.categories))
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = next(filter(lambda t: t.id == topic_id, self.topics))
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = next(filter(lambda d: d.id == document_id, self.documents))
        self.documents.remove(document)

    def get_document(self, document_id):
        document = next(filter(lambda d: d.id == document_id, self.documents))
        return document

    def __repr__(self):
        documents = '\n'.join([document.__repr__() for document in self.documents])
        return documents
