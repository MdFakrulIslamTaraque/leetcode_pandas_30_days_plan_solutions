"""
link: https://leetcode.com/problems/rearrange-products-table/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

Table: Products

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| store1      | int     |
| store2      | int     |
| store3      | int     |
+-------------+---------+
product_id is the primary key (column with unique values) for this table.
Each row in this table indicates the product's price in 3 different stores: store1, store2, and store3.
If the product is not available in a store, the price will be null in that store's column.
 

Write a solution to rearrange the Products table so that each row has (product_id, store, price). If a product is not available in a store, do not include a row with that product_id and store combination in the result table.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Products table:
+------------+--------+--------+--------+
| product_id | store1 | store2 | store3 |
+------------+--------+--------+--------+
| 0          | 95     | 100    | 105    |
| 1          | 70     | null   | 80     |
+------------+--------+--------+--------+
Output: 
+------------+--------+-------+
| product_id | store  | price |
+------------+--------+-------+
| 0          | store1 | 95    |
| 0          | store2 | 100   |
| 0          | store3 | 105   |
| 1          | store1 | 70    |
| 1          | store3 | 80    |
+------------+--------+-------+
Explanation: 
Product 0 is available in all three stores with prices 95, 100, and 105 respectively.
Product 1 is available in store1 with price 70 and store3 with price 80. The product is not available in store2.
"""


import pandas as pd
def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    products_np_list = products.to_numpy() # converting the df to list to iterate over each entries

    res_df = pd.DataFrame({'product_id':int(), 'store':[], 'price':int()}) # declare the resulting df with demanding columns
    for idx, product in enumerate(products_np_list):
        price_list = product[1:].tolist() # the 1st col was for product_id, after that, everything was price list each row of given df
        product_id_list = [int(product[0]) for i in price_list] # copied the the product_id as per the length of price_list
        store_name_list = [f'store{it+1}' for it,price in enumerate(price_list)] # copied the store name as per the price_list and store number was retrived from index
        temp_df = pd.DataFrame({'product_id': product_id_list, 'store': store_name_list, 'price': price_list}) # created a temporary df to concat with the resulting df
        res_df = pd.concat(objs=[res_df, temp_df] # concat, ignoring the index
                        , ignore_index=True
                        )
        
    return res_df.dropna(how='any') # dropped the duplicate rows for any null value in the df