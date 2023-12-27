# mongodb_rh

### Part 1 - Concepts

#### 1. Describe in your own words the 3 main differences and 3 similarities between SQL databases and noSQL databases.

*Differences between SQL and NoSQL*

1. Data Structure:
    - SQL: Structured in tables with a fixed schema.
    - NoSQL: Flexible, supports various formats such as documents, key-value, etc.
2. Scalability:
    - SQL: Oriented towards vertical scalability (increasing resources on a single server).
    - NoSQL: Favors horizontal scalability (load distribution across multiple servers).
3. Transactions and Consistency:
    - SQL: Follows the ACID model, ensuring reliable transactions and strict consistency.
    - NoSQL: Generally adopts the BASE model, offering eventual consistency and high availability.

*Similarities between SQL and NoSQL*

1. Data Storage: Both store and retrieve data.
2. Indexing: They use indexing to improve query performance.
3. Security: Implement security measures to protect data.

#### 2. In your opinion, are noSQL databases better or worse than SQL databases? How do they stand out? Justify your answer.

It's not a question of them being better or worse, but rather that they meet different needs. NoSQL databases, such as MongoDB, excel in scenarios where schema flexibility, horizontal scalability and the ability to handle large volumes of unstructured or semi-structured data are critical. They are ideal for applications that require high performance in reading and writing operations and are well adapted to store data in formats such as JSON, which facilitates the development of modern applications.

On the other hand, SQL-based systems such as PostgreSQL or MySQL are excellent in scenarios that require complex transactions and data integrity guarantees, thanks to their ACID (Atomicity, Consistency, Isolation, Durability) nature. They are ideal for applications that rely on complex relationships between data and detailed queries.

Therefore, the choice between NoSQL and SQL depends on the specific project requirements. NoSQL is more about scalability and flexibility, while SQL focuses on consistency and structure.

#### 3. Describe in your own words a scenario where you would opt for a noSQL model and a scenario where you would opt for a SQL model.

In a scenario where I would opt for a NoSQL model, imagine a rapidly growing social networking application that deals with large amounts of varied and constantly changing data. In this application, data includes posts, comments, images, and user interactions, which do not follow a uniform structured format. Scalability and the ability to handle different types of data are crucial. A NoSQL database such as MongoDB would be ideal here as it offers the flexibility to handle different data formats and is designed to scale horizontally, making it easier to manage large volumes of data and user traffic.

On the other hand, in a scenario where I would choose an SQL model, consider an inventory management system for a chain of retail stores. This system needs consistent and reliable transactions to track inventory, sales, and supplies. The data here is highly structured and relational - information about products, suppliers, stores, and sales transactions. A SQL-based system such as PostgreSQL would be more appropriate due to its ability to handle complex transactions, maintain data integrity, and support complex queries and relationships between different data entities.

#### 4. In addition to the material used in class, do a little research and describe in your own words what types of noSQL databases exist on the current market, with the main usage characteristics of each type. Cite research sources.

In the current market, NoSQL databases are mainly classified into four types, each with its own specific characteristics and use cases.

1. Document-Oriented Databases: These databases, such as MongoDB and CouchDB, store data in documents (usually in JSON format). They are ideal for applications that deal with semi-structured data. Its schema flexibility allows for rapid iteration and development, making it great for scenarios such as CMS, blogs, and e-commerce applications.

2. Key-Value Stores: They are the simplest, storing data as a set of keys and values. Redis and DynamoDB are popular examples. They are extremely fast for reads and writes and are well suited for storing user sessions, configurations, and caches.

3. Column-Family Stores: Like Cassandra and HBase, these databases are optimized for queries on large volumes of data, storing it in columns instead of rows. They are ideal for systems that require analysis of large volumes of data, such as data monitoring systems and business intelligence applications.

4. Graph Databases: Neo4j and Amazon Neptune are examples that store data in the form of graphs. They are excellent for representing and querying complex relationships between data, being widely used in recommendation systems, social networks and fraud analysis.

The characteristics and examples mentioned reflect the trends and common uses of these technologies in the current market context.

### Part 2 - Hands-On

A. **Installation and creation.**
  1. **Create the “LM_rh” database.**
  2. **Create the collections: “LM_DEPARTAMENTO”, “LM_FUNCIONARIO”, “LM_DEPENDENTE”.**
  3. **Insert 3 documents for each collection. Note: At least one insertion for each collection must have one more or less attribute.**
  4. **Show the contents of each collection.**
  5. **For the "LM_DEPARTAMENTO" collection, create a filter based on a description of the department (equality).**
  6. **For the "LM_FUNCIONARIO" collection to show employees who receive a salary above R$2000.00.**
  7. **For the "LM_DEPENDENTE" collection, execute the distinct method for the name attribute.**
  8. **Perform an update for one of the collections.**
  9. **Perform a delete for one of the collections.**

B. **Modeling**
  1. **Create the "LM_modelo" database.**
  2. **Create a small model that involves two collections with cardinalities 1-N. The name of the collections must be “LM_col1a” and “LM_col2a”. In this case, use the concept of referencing the id from one collection to another (send it to side N as if it were the primary key on side 1).**
  3. **Insert 2 documents into the collection (side 1).**
  4. **Insert 4 documents into the collection (N side). Note: Side 1 (is as if it were the mother collection) and side N (is as if it were the daughter collection). In item (B2) each document from the mother collection must reference 2 documents from the daughter collection.**
  5. **Create a small model that involves two collections with cardinalities N-N. The name of the collections must be “LM_col1b” and “LM_col2b”. In this case, you will indicate whether you will use the reference or whether you will embed the document in the other document.**
     1. Create two name collections (if you embark) or.
     2. Create three collections (if you use reference).
     3. If you chose option (B3a), create two collections and insert 2 documents into each collection.
     4. If you chose option (B3b), create the three collections and insert 2 documents into each of the collections.

C. **Indexes**
  1. **Create the "LM_indeagrega" database.**
  2. **Create a collection named "LM_indexar1" that has at least 7 attributes.**
     1. Create an index (not unique and with ascending ordering).
     2. Create an index (unique and with descending ordering).
     3. Create an index (with two attributes).
     4. Create an index for an array attribute.
     5. Create a sparse index (with one attribute).
     6. Create an index with a lifetime - TTL (with an attribute and an expiration of 20 seconds).
     7. Insert 4 documents into this collection.
  3. **Create a second collection named "LM_indexar2" (which has at least 4 string attributes).**
     1. Create a textual index for this second collection.
     2. Insert 4 documents into this collection.
  4. **Create a third collection named "LM_Venda" (which will have the attributes: Sales_Cod, UF_Sales, Sales_Prod_Desc, Sales_Value).**
     1. Insert 16 documents (4 documents for each of the UFs - there will be 4 different UFs). Complete the 4 attributes mentioned.
     2. Create a query that shows the number of documents per UF.
     3. Create a query that shows the total value of sales per UF.
     4. Create a query that shows the average sales value per state.
     5. Create a query that shows the highest sales value per UF.
     6. Create a query that shows the lowest sales value per UF.

D. **Replication**
  1. **Create the replica set "LM_rsposmit".**
  2. **Architecture drawing.**
     1. A primary.
     2. Two secondary.
     3. An arbiter.
  3. **On the primary node, create the “LM_col_filmes” collection.**
     1. Insert 5 documents into the "LM_col_filmes" collection.
  4. **Access one of the secondary nodes.**
     1. Insert 5 documents into the "LM_col_filmes" collection.

E. **Partitioning**
  1. **Create a shard.**
  2. **Design an architecture.**
     1. Three config servers (on Replica Set).
     2. Four shard servers (no Replica Set).
     3. One mongos.
  3. **Connect to the mongos.**
     1. Enable partitioning for a database of your choice.
     2. Partition a collection of your choice.
     3. Insert 1,000 documents into this collection using the "for" command.
     4. Show the distribution of the created collection.

F. **Storage Engines**
  1. **Create a MongoDB instance that uses the mmapv1 storage engine.**
     1. Connect to this instance.
     2. Check the current storage engine.
     3. Create the “LM_produtos” collection and insert 4 documents.
  2. **Create a MongoDB instance that uses the wiredTiger storage engine.**
     1. Connect to this instance.
     2. Check the current storage engine.
     3. Create the “LM_places” collection and insert 4 documents.
  3. **Create a MongoDB instance that uses security (authentication and authorization)**
     1. Connect to this instance.
     2. Create the dba user with the root role.
     3. Connect with the dba user.
     4. Create the user “LM_desenv” with the role readWrite in the “LM_rh” database;
     5. Connect with user “LM_desenv”.
     6. Create the “LM_funcionarios” collection and insert 4 documents.

G. **Debugging, backup, and restore**
  1. **Create a MongoDB instance.**
  2. **Connect to this instance (access the exerc4b database).**
  3. **Create the "LM_Paises" collection and insert 4 documents.**
  4. **Run a query for the "LM_Paises" collection with a filter of your choice with explain.**
  5. **Create an index for an attribute that you filtered on the item.**
  6. **Run the same query as the item.**
  7. **Create the “LM_Numero1” collection and insert 50,000 documents in parallel; in another window run the mongostat utility.**
  8. **Create the “LM_Numero2” collection and insert 50,000 documents in parallel; in another window run the mongotop utility.**
  9. **Exit Mongo Shell and make a backup of the entire MongoDB instance.**
  10. **Kill the MongoDB process.**
  11. **Delete the MongoDB data directory.**
  12. **Restore MongoDB (the path must be created previously).**
  13. **Access the instance and go to the exerc4b database. Check the number of documents per collection.**

















