from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
def label_encoding(df):
    for column in df.columns:
        # if df[column].dtype == "object" and column != "date_str":
        if df[column].dtype == "object":
            df[column] = label_encoder.fit_transform(df[column])