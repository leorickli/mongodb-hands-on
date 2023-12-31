# mongodb-hr

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
  1. **Create the “LM_hr” database.**
  2. **Create the collections: “LM_DEPARTMENT”, “LM_EMPLOYEE”, “LM_DEPENDENT”.**
<img width="284" alt="Screenshot 2023-12-27 at 21 28 27" src="https://github.com/leorickli/mongodb-hr/assets/106999054/19fc8102-64ee-4960-80ed-936f4fa94c25">

  3. **Insert 3 documents for each collection. Note: At least one insertion for each collection must have one more or less attribute.**
<img width="993" alt="Screenshot 2023-12-27 at 21 30 30" src="https://github.com/leorickli/mongodb-hr/assets/106999054/aad12914-dfb4-442b-a1a1-ee393bd53a07">

  4. **Show the contents of each collection.**
<img width="418" alt="Screenshot 2023-12-27 at 21 32 14" src="https://github.com/leorickli/mongodb-hr/assets/106999054/fc2eaec4-adef-4df9-bf3c-32ef86c46c0b">
<img width="424" alt="Screenshot 2023-12-27 at 21 32 55" src="https://github.com/leorickli/mongodb-hr/assets/106999054/c2c5e09d-f5ce-4acd-9604-1304c87469f0">
<img width="392" alt="Screenshot 2023-12-27 at 21 33 13" src="https://github.com/leorickli/mongodb-hr/assets/106999054/ac5acf47-7851-49cd-a22d-01e75d17d30a">

  5. **For the "LM_DEPARTMENT" collection, create a filter based on a description of the department (equality).**
<img width="385" alt="Screenshot 2023-12-28 at 15 09 27" src="https://github.com/leorickli/mongodb-hr/assets/106999054/9477b8e8-600e-4826-942d-7f3c2c6ecc83">

  6. **For the "LM_FUNCTIONARY" collection to show employees who receive a salary above R$2000.00.**
<img width="411" alt="Screenshot 2023-12-28 at 15 11 23" src="https://github.com/leorickli/mongodb-hr/assets/106999054/a2f00bea-ccdb-48d1-9374-779b8c25b1ed">

  7. **For the "LM_DEPENDENT" collection, execute the distinct method for the name attribute.**

This one is  bit more complex so I created a Jupyter notebook with Python to make that query on my local machine.
<img width="805" alt="Screenshot 2023-12-28 at 15 56 21" src="https://github.com/leorickli/mongodb-hr/assets/106999054/6a68a3e3-41ac-4f69-b333-df774d49b1ee">
<img width="370" alt="Screenshot 2023-12-28 at 15 58 25" src="https://github.com/leorickli/mongodb-hr/assets/106999054/6c768101-11c6-4701-9082-05f3de332167">

  8. **Perform an update for one of the collections.**
<img width="556" alt="Screenshot 2023-12-28 at 16 07 32" src="https://github.com/leorickli/mongodb-hr/assets/106999054/dd477e40-390b-479a-8479-0478f847f4d0">

  9. **Perform a delete for one of the collections.**
<img width="969" alt="Screenshot 2023-12-28 at 16 33 17" src="https://github.com/leorickli/mongodb-hr/assets/106999054/78a732f1-1a61-4328-b52a-8951dccf65d7">

B. **Modeling**
  1. **Create the "LM_model" database.**
  2. **Create a small model that involves two collections with cardinalities 1-N. The name of the collections must be “LM_col1a” and “LM_col2a”. In this case, use the concept of referencing the id from one collection to another (send it to side N as if it were the primary key on side 1).**
  3. **Insert 2 documents into the collection (side 1).**
  4. **Insert 4 documents into the collection (N side). Note: Side 1 (is as if it were the mother collection) and side N (is as if it were the daughter collection). In item (B2) each document from the mother collection must reference 2 documents from the daughter collection.**
<img width="576" alt="Screenshot 2023-12-28 at 18 08 38" src="https://github.com/leorickli/mongodb-hr/assets/106999054/d78c17d9-700e-410e-9510-17a9fb1ffcad">
<img width="741" alt="Screenshot 2023-12-28 at 18 07 34" src="https://github.com/leorickli/mongodb-hr/assets/106999054/ae54e5a8-0614-456b-b6e7-9889ce82528d">
  
  5. **Create a small model that involves two collections with cardinalities N-N. The name of the collections must be “LM_col1b” and “LM_col2b”. In this case, you will indicate whether you will use the reference or whether you will embed the document in the other document.**
     1. Create two name collections (if you embark) or.
     2. Create three collections (if you use reference).
     3. If you chose option (B3a), create two collections and insert 2 documents into each collection.
     4. If you chose option (B3b), create the three collections and insert 2 documents into each of the collections.
<img width="588" alt="Screenshot 2023-12-28 at 18 08 58" src="https://github.com/leorickli/mongodb-hr/assets/106999054/322e7280-f0a2-4c99-9814-8ca08802cc99">
<img width="754" alt="Screenshot 2023-12-28 at 18 09 27" src="https://github.com/leorickli/mongodb-hr/assets/106999054/ae433622-6d36-483b-9ff2-c0c5ececdba0">

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
<img width="732" alt="Screenshot 2023-12-28 at 18 10 04" src="https://github.com/leorickli/mongodb-hr/assets/106999054/1f59bf8d-f277-488f-8572-b897ebd71c16">
<img width="953" alt="Screenshot 2023-12-28 at 18 12 06" src="https://github.com/leorickli/mongodb-hr/assets/106999054/7341d992-cc73-48c6-a2cd-b8f7f54722fc">
  
  3. **Create a second collection named "LM_indexar2" (which has at least 4 string attributes).**
     1. Create a textual index for this second collection.
     2. Insert 4 documents into this collection.
 <img width="1069" alt="Screenshot 2023-12-28 at 18 15 55" src="https://github.com/leorickli/mongodb-hr/assets/106999054/250ab328-925c-48e7-b6fa-bc0d8e8b99f3">
 <img width="906" alt="Screenshot 2023-12-28 at 18 15 24" src="https://github.com/leorickli/mongodb-hr/assets/106999054/c4a01488-c4a3-4528-ba0c-dda97f9b5928">
  
  4. **Create a third collection named "LM_Venda" (which will have the attributes: Sales_Cod, UF_Sales, Sales_Prod_Desc, Sales_Value).**
     1. Insert 16 documents (4 documents for each of the UFs - there will be 4 different UFs). Complete the 4 attributes mentioned.
<img width="965" alt="Screenshot 2023-12-28 at 18 29 09" src="https://github.com/leorickli/mongodb-hr/assets/106999054/d4b24ca0-35d0-488a-8794-2a05b5e49ca2">

     2. Create a query that shows the number of documents per UF.
<img width="504" alt="Screenshot 2023-12-28 at 18 29 38" src="https://github.com/leorickli/mongodb-hr/assets/106999054/56ef3f74-06bf-4db0-9ef0-ac145b6a4456">

     3. Create a query that shows the total value of sales per UF.
<img width="615" alt="Screenshot 2023-12-28 at 18 29 50" src="https://github.com/leorickli/mongodb-hr/assets/106999054/6bced5b8-d7eb-4ad7-bbba-64ddcaf14fe4">

     4. Create a query that shows the average sales value per state.
<img width="631" alt="Screenshot 2023-12-28 at 18 30 00" src="https://github.com/leorickli/mongodb-hr/assets/106999054/975ebc74-b32f-4ebd-bfda-3b6f99ab3d69">

     5. Create a query that shows the highest sales value per UF.
<img width="613" alt="Screenshot 2023-12-28 at 18 30 11" src="https://github.com/leorickli/mongodb-hr/assets/106999054/8b9e3526-b50d-4f2e-aeda-a12145bec4f8">

     6. Create a query that shows the lowest sales value per UF.
<img width="579" alt="Screenshot 2023-12-28 at 18 30 24" src="https://github.com/leorickli/mongodb-hr/assets/106999054/95d30dc3-0633-4cd4-8306-aff9cafd7a07">

D. **Replication**
  1. **Create the replica set "LM_rsposmit".**
  2. **Architecture drawing.**
     1. A primary.
     2. Two secondary.
     3. An arbiter.
<img width="330" alt="Screenshot 2023-12-30 at 17 02 16" src="https://github.com/leorickli/mongodb-hr/assets/106999054/13f8a1c6-1bad-47b8-ad9e-db61d29d389d">
  
  3. **On the primary node, create the “LM_col_movies” collection.**
     1. Insert 5 documents into the "LM_col_movies" collection.
<img width="558" alt="Screenshot 2023-12-30 at 17 04 36" src="https://github.com/leorickli/mongodb-hr/assets/106999054/d9759f60-4328-4498-a283-b232121b6a58">

  4. **Access one of the secondary nodes.**
     1. Insert 5 documents into the "LM_col_filmes" collection.

*If you want to insert documents into your MongoDB replica set and you're currently connected to a secondary node, you'll need to switch to the primary node to perform the write operation. MongoDB replica sets enforce a primary/secondary architecture where write operations can only be performed on the primary node to ensure data consistency across the cluster.*

E. **Partitioning**
  1. **Create a shard.**
  2. **Design an architecture.**
     1. Three config servers (on Replica Set).
     2. Four shard servers (no Replica Set).
     3. One mongos.
<img width="660" alt="Screenshot 2023-12-30 at 22 02 38" src="https://github.com/leorickli/mongodb-hr/assets/106999054/03642eff-7ffb-417d-b7e1-a464976241f4">
<img width="566" alt="Screenshot 2023-12-30 at 22 03 12" src="https://github.com/leorickli/mongodb-hr/assets/106999054/cc48493c-9328-4160-9f7b-9b0451153a96">
<img width="552" alt="Screenshot 2023-12-30 at 22 03 36" src="https://github.com/leorickli/mongodb-hr/assets/106999054/fcfd24d1-02d4-4c79-b083-cc8d53edde18">
<img width="429" alt="Screenshot 2023-12-30 at 22 04 07" src="https://github.com/leorickli/mongodb-hr/assets/106999054/dfcbe918-ab97-42d3-858d-17ebba0268d7">

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

















