# Lab: SQL injection UNION attack, determining the number of columns returned by the query

## Lab Description
This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables. The first step of such an attack is to determine the number of columns that are being returned by the query. You will then use this technique in subsequent labs to construct the full attack. 

## Goal
Determine the number of columns returned by the query by performing a SQL injection UNION attack that returns an additional row containing null values.

## Steps to Solve

1. Open the lab in your browser.

2. Set up proxy as Burp Suite.

3. In catagories select any one of them and in burp suite HTTP history tab find the relevant request and send it to the Reapeaer.

7. Inject the SQL query there with ORDER BY clause and send the request:
	Gifts'+ORDER+BY+1--
8. Iterate the number till an error code is received in response.
9. On 4 the error code will be received meaning that the table have 3 coloumns.
10. Finaly send : Gifts'+UNION+SELECT+NULL,NULL,NULL,NULL--
11. This will send the additional null value to the server.
12. Open the response in the browser.
13. Lab Solved Successfully.

## Explanation

- The payload `Gifts'+ORDER+BY+1--` orders the result by column index 1's values, so iterating the number till error is encountered will give the number of colomns.
- This can be used with UNION statement to execute desired queries.


