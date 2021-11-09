#### Since the collection name must be separately specified, we will use "tuples" to simplify running the queries
### If the tuple only has two entries, then the first entry is the name of the collection, and the second entry is the 'find' query
### If the tuple has three entries, then the third entry is the "projection" array
collection_and_queries = [None] * 13

### 0. Return all the entries in accounts collection
collection_and_queries[0] = ('transactions', {})

### 1. Find all information for the customer with username 'fmiller'
collection_and_queries[1] = ('customers', {})

### 2. For all customers with first name 'Natalie', return their username, name, and address
### Use 'regex' functionality to do the matching
collection_and_queries[2] = ('customers', {}, {})

### 3. Find all accounts with a 'products' array containing 'Commodity' -- return the '_id' and 'account_id'
collection_and_queries[3] = ('accounts', {}, {})

### 4. Find all accounts with either limit <= 9000 or products array exactly ["Commodity", "InvestmentStock"] in that order -- return the entire accounts information
### Use "$or" to do a disjunction
collection_and_queries[4] = ('accounts', {})

### 5. Find all accounts with limit <= 9000 AND products array exactly ["Commodity", "InvestmentStock"] in that order -- return the entire accounts information
collection_and_queries[5] = ('accounts', {})

### 6. Find all accounts where the second entry in the products array is 'Brokerage' -- return the entire accounts information
collection_and_queries[6] = ('accounts', {})

### 7. On the customers collection, use aggregation and grouping to find the number of customers born in each month
### The output will contain documents like: {'_id': 7, 'totalCount': 42} 
### Use '$month' function to operate on the dates, and use '$sum' aggregate to do the counting
### https://database.guide/mongodb-month/
collection_and_queries[7] = ('customers', [])

### 8. To Be Released
collection_and_queries[8] = ('accounts', [])

### 9. To Be Released
collection_and_queries[9] = ('accounts', [])

### 10. To Be Released
collection_and_queries[10] = ('accounts', [])

### 11. To Be Released
collection_and_queries[11] = ('accounts', [])

### 12. To Be Released
collection_and_queries[12] = ('accounts', [])
