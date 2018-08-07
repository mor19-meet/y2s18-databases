
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__ = "Knowledge"
	topic_id = Column(Integer, primary_key=True)
	topic = Column(String)
	link = Column(String)
	rating = Column(Integer)

	def __repr__(self):
		return ("topic id: {}\n"
				"topic: {}\n"
				"link: {}\n"
				"If you want to learn about {},  you should look at the Wikipedia article called {}./n"
				"We gave this article a rating of {} out of 10!").format(
					self.topic_id,
					self.topic,
					self.link,
					self.topic,
					self.link,
					self.rating)
		
	# def __init__(self, id, topic, link, rating)
	# 	self.topic_id = id
	# 	self.topic = topic
	# 	self.link = link
	# 	self.rating = rating
laith = Knowledge(topic = "dance", link =  "https://en.wikipedia.org/wiki/Dance" , rating = 8)
# print (laith)


