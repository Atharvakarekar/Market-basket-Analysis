# import pandas as pd
# from mlxtend.preprocessing import TransactionEncoder
# from mlxtend.frequent_patterns import apriori, association_rules
#
# # Load the dataset
# df = pd.read_csv(
#     r'C:\Users\Pratima\Downloads\market basket analysis\market basket analysis\market-basket-analysis.csv',
#     on_bad_lines='skip'
# )
# # Preprocess the dataset
# transactions = []
# for _, row in df.iterrows():
#     transaction = []
#     for col in df.columns:
#         if pd.notnull(row[col]):
#             transaction.append(col)
#     transactions.append(transaction)
#
# # Convert transaction data to one-hot encoded format
# te = TransactionEncoder()
# te_ary = te.fit_transform(transactions)
# df_encoded = pd.DataFrame(te_ary, columns=te.columns_)
#
# # Generate frequent itemsets
# frequent_itemsets = apriori(df_encoded, min_support=0.01, use_colnames=True)
#
# # Generate association rules
# association_rules = association_rules(frequent_itemsets, metric='lift', min_threshold=1)
#
# # Print frequent itemsets
# print("Frequent Itemsets:")
# print(frequent_itemsets)
#
# # Print association rules
# print("\nAssociation Rules:")
# print(association_rules)


# import pandas as pd
# from mlxtend.preprocessing import TransactionEncoder
# from mlxtend.frequent_patterns import apriori, association_rules
# import streamlit as st
#
# # Load the dataset
# @st.cache
# def load_data():
#     df = pd.read_csv(
#         r'C:\Users\Pratima\Downloads\market basket analysis\market basket analysis\market-basket-analysis.csv',
#         on_bad_lines='skip'
#     )
#     return df
#
# df = load_data()
#
# # Preprocess the dataset
# transactions = []
# for _, row in df.iterrows():
#     transaction = []
#     for col in df.columns:
#         if pd.notnull(row[col]):
#             transaction.append(col)
#     transactions.append(transaction)
#
# # Convert transaction data to one-hot encoded format
# te = TransactionEncoder()
# te_ary = te.fit_transform(transactions)
# df_encoded = pd.DataFrame(te_ary, columns=te.columns_)
#
# # Generate frequent itemsets
# frequent_itemsets = apriori(df_encoded, min_support=0.01, use_colnames=True)
#
# # Generate association rules
# association_rules = association_rules(frequent_itemsets, metric='lift', min_threshold=1)
#
# # Display results in Streamlit
# st.title("Market Basket Analysis")
# st.header("Frequent Itemsets")
# st.dataframe(frequent_itemsets)
#
# st.header("Association Rules")
# st.dataframe(association_rules)



# import pandas as pd
# from mlxtend.preprocessing import TransactionEncoder
# from mlxtend.frequent_patterns import apriori, association_rules
# import streamlit as st
#
# # Load the dataset
# df = pd.read_csv(r'C:\Users\Pratima\Downloads\market basket analysis\market basket analysis\market-basket-analysis.csv', on_bad_lines='skip')
#
# # Preprocess the dataset
# transactions = []
# for _, row in df.iterrows():
#     transaction = []
#     for col in df.columns:
#         if pd.notnull(row[col]):
#             transaction.append(col)
#     transactions.append(transaction)
#
# # Convert transaction data to one-hot encoded format
# te = TransactionEncoder()
# te_ary = te.fit_transform(transactions)
# df_encoded = pd.DataFrame(te_ary, columns=te.columns_)
#
# # Sidebar for user inputs
# st.sidebar.title("Parameters")
# min_support = st.sidebar.slider("Minimum Support", 0.01, 0.5, 0.01)
# min_threshold = st.sidebar.slider("Minimum Threshold", 0.5, 2.0, 1.0)
#
# # Generate frequent itemsets
# frequent_itemsets = apriori(df_encoded, min_support=min_support, use_colnames=True)
#
# # Generate association rules
# association_rules = association_rules(frequent_itemsets, metric='lift', min_threshold=min_threshold)
#
# # Display frequent itemsets
# st.write("Frequent Itemsets:")
# st.write(frequent_itemsets)
#
# # Display association rules
# st.write("Association Rules:")
# st.write(association_rules)


import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
import streamlit as st


st.title("Market Basket Analysis")
# Load the dataset
df = pd.read_csv(r'C:\Users\Pratima\Downloads\market basket analysis\market basket analysis\market-basket-analysis.csv', on_bad_lines='skip')

# Preprocess the dataset
transactions = []
for _, row in df.iterrows():
    transaction = []
    for col in df.columns:
        if pd.notnull(row[col]):
            transaction.append(col)
    transactions.append(transaction)

# Convert transaction data to one-hot encoded format
te = TransactionEncoder()
te_ary = te.fit_transform(transactions)
df_encoded = pd.DataFrame(te_ary, columns=te.columns_)

# Sidebar for user inputs
st.sidebar.title("Parameters")
min_support = st.sidebar.slider("Minimum Support", 0.01, 0.5, 0.01)
min_threshold = st.sidebar.slider("Minimum Threshold", 0.5, 2.0, 1.0)

# Generate frequent itemsets
frequent_itemsets = apriori(df_encoded, min_support=min_support, use_colnames=True)

# Generate association rules
association_rules = association_rules(frequent_itemsets, metric='lift', min_threshold=min_threshold)

# Display frequent itemsets
st.write("Frequent Itemsets:")
st.write(frequent_itemsets)

# Display association rules
st.write("Association Rules:")
st.dataframe(association_rules)
