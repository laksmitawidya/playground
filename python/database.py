""" 
Database let you accessing data (read, create, delete, update)
that simultaneously from many different locations and keep
the data consistent
 """

# Relational database
""" 
- Database - contains many tables
- Relation (or table) - contains tuples and attributes
- Tuple (or row) a set of fields that generally represents an "object"
like a person or a music track
- Attribut ( column or field) one of possibly many elements of
data corresponding to the object represented by the row

A relation is defined as a set of tuples that have same attributes
A tuple usually represents an object and information about that object
Objects are typically physical objects or concepts
A relation is usually described as a table which is organized into row and columns
All the data referenced by an attribute are in the same domain and conform to the same constraints
 """


""" 
INSERT INTO Users (name, email) VALUES ("Rebecca","'Rebecca@marrie.com");
DELETE FROM Users WHERE email="xxx";
UPDATE Users SET name="Charles" WHERE email="xxx"
SELECT * FROM Users
SELECT * FROM Users where name="xxx" ORDER by email DESC
 """

""" 
Building a data model
- Drawing a picture of the data objects for our apps and then figuring out how to
represent the objects and their relationships
- Basic rule" Don't put the same string data in twice - use a relationship instead
- When there is one thing in the real world there should be one copy of that thing in the database
  """

""" 
Database normalization
  - Dont replicate data, reference data, point at data
  - Use integers for keys and for references
  - Add special key column to each Table which we will make references to (id)
"""

# Integer reference Pattern
""" Three kinds keys:
- Primary Key
- Logical key (outside world uses for lookup)
- Foreign key

Best Practices
- Never use your logical key as the primary key
- Logical keys can and do change, albeit slowly
- Relationships that are based on matching string fields are less efficient than integers

 """

#  Create Table
""" 
CREATE TABLE Artist(
	id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
	name TEXT
)

CREATE TABLE Track(
	id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
	title TEXT,
	album_id INTEGER,
	genre_id INTEGER,
	len INTEGER,  rating INTEGER, count INTEGER
)
INSERT INTO Artist (name) VALUES ('AC/DC')
INSERT INTO Genre(name) VALUES('Metal')
 """

""" Join Clause
connect 1 table to another table on 2 things connecting each other
show any possibility between 2 tables or more
SELECT Track.title, Genre.name as "Genre Name" FROM Track JOIN Genre ON Track.genre_id = Genre.id
SELECT Album.title, Album.artist_id, Artist.id, Artist.name
FROM Album 
JOIN Artist 
ON Album.artist_id = artist_id
 
  """