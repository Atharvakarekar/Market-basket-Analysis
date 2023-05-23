# Market-basket-Analysis

This code performs Market Basket Analysis using the Apriori algorithm and streamlit for interactive visualization. Here is a breakdown of the code:

1. The necessary libraries are imported:
   - `pandas` is imported as `pd` for data manipulation and analysis.
   - `TransactionEncoder` from `mlxtend.preprocessing` is imported to convert the transaction data into a one-hot encoded format.
   - `apriori` and `association_rules` from `mlxtend.frequent_patterns` are imported for generating frequent itemsets and association rules.
   - `streamlit` is imported as `st` for creating a web-based user interface.

2. The title "Market Basket Analysis" is displayed using `st.title()`.

3. The dataset is loaded from a CSV file using `pd.read_csv()`. The path to the file is specified as `'C:\Users\Pratima\Downloads\market basket analysis\market basket analysis\market-basket-analysis.csv'`. The parameter `on_bad_lines='skip'` is used to skip any lines with errors in the CSV file.

4. The dataset is preprocessed to convert it into a list of transactions. Each transaction is represented as a list of items.

5. The transaction data is converted into a one-hot encoded format using `TransactionEncoder()`. The `fit_transform()` method is used to fit the encoder on the transactions and transform them into a binary matrix. The resulting encoded data is stored in the DataFrame `df_encoded`.

6. The user interface is created using `st.sidebar.title()` and `st.sidebar.slider()`. The sliders allow the user to adjust the minimum support and minimum threshold parameters for generating frequent itemsets and association rules.

7. Frequent itemsets are generated using the `apriori()` function. The `min_support` parameter is set to the value chosen by the user through the slider, and `use_colnames` is set to `True` to use the column names from `df_encoded` as item names.

8. Association rules are generated from the frequent itemsets using the `association_rules()` function. The `metric` parameter is set to `'lift'` to measure the strength of the rules, and the `min_threshold` parameter is set to the value chosen by the user through the slider.

9. The frequent itemsets and association rules are displayed using `st.write()` and `st.dataframe()`.

Overall, this code loads a market basket analysis dataset, preprocesses it, allows the user to adjust the parameters for generating frequent itemsets and association rules, and displays the results using the streamlit framework.


![image](https://github.com/Atharvakarekar/Market-basket-Analysis/assets/91048746/91119714-bf96-41cf-a637-338feed1cbd7)
