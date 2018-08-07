from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(topic , link, rating):
    article_object = Knowledge(
        topic = topic,
        link = link,
        rating = rating)
    session.add(article_object)
    session.commit()
add_article("music","https://docs.google.com/presentation/d/1oQnW76Wd-bEMCi_r1EAzgTVlL2IwgorDrYjiQeyu35E/edit#slide=id.g3df5820309_0_239 ", 7 )

def query_all_articles():
    article= session.query(
        Knowledge).all()
    return article


def query_article_by_topic(topic):
    by_topic = session.query(
        Knowledge).filter_by(
        topic=topic).first()

    return by_topic
print(query_article_by_topic("music"))

def delete_article_by_topic(topic):
    session.query(Knowledge).filter_by(
        topic= topic).delete()
    session.commit()
delete_article_by_topic("music")

def delete_all_articles():
    session.query(Knowledge).delete()
    session.commit()

def edit_article_rating(rating, topic):
    pass


# print(query_all_articles())
# g = Knowledge(topic = "music", link =  "https://github.com/mor19-meet/y2s18-databases/tree/master/exercises" , rating = 4)

# session.add(g)
# session.commit()

# articls = query_all_articles()
# for i in articls:
#     print(i.topic)