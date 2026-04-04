# Lab: SQL injection UNION attack, finding a column containing text

## Lab Description
This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables. To construct such an attack, you first need to determine the number of columns returned by the query. You can do this using a technique you learned in a previous lab. The next step is to identify a column that is compatible with string data.

## Goal
The lab will provide a random value that you need to make appear within the query results. To solve the lab, perform a SQL injection UNION attack that returns an additional row containing the value provided. This technique helps you determine which columns are compatible with string data. 

## Steps to Solve

1. Open the lab in your browser.

2. Set up proxy as Burp Suite.

3. In catagories select any one of them and in burp suite HTTP history tab find the relevant request and send it to the Reapeaer.

7. Inject the SQL query there with ORDER BY clause and send the request:
	Gifts'+ORDER+BY+1--
8. Iterate the number till an error code is received in response.
9. On 4 the error code will be received meaning that the table have 3 coloumns.
10. Finaly send : Gifts'+UNION+SELECT+'804W7M',NULL,NULL--
11. Change the position of the string until 200(ok) status code is returned, and that position accepts string data.
11. This will send the additional string value to the server.
12. Open the response in the browser.
13. Lab Solved Successfully.

## Explanation

- The payload `Gifts'+ORDER+BY+1--` orders the result by column index 1's values, so iterating the number till error is encountered will give the number of colomns.
- Iterating the string will tell which column has string data, so this techniqe can be used to determine the data type of each column.
- This can be used with UNION statement to execute desired queries.


