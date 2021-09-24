import pandas as pd
from mock import patch
from datafram_comp import custom_df_compare




#@patch("pandas.DataFrame.__eq__", custom_df_compare)
def test_df_equal():
    
    df2 = pd.DataFrame({"id": [2, 3, 4], "name": ["b", "c", "d"]}, columns=["id", "name"]
    )

    assert all(custom_df_compare()==df2)