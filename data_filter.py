import pandas as pd
import requests
import io

url =f"https://api.data.gov.in/resource/239ac3d0-f08d-40d0-b03c-9b7a426a62d5?api-key=579b464db66ec23bdd0000012b6b6a4d64674b83477e03a4c0f63ab1&format=csv"

response = requests.get(url)
response.raise_for_status()
data_csv = response.text
df = pd.read_csv(io.StringIO(data_csv))
df = df.transpose()
df.columns = df.iloc[0] 
df = df.reset_index().rename(columns={'index': 'period'})
clean_df = df.iloc[3:].copy()

clean_df['ds'] = (clean_df['period'].str.replace('INDX','').apply(lambda x: pd.to_datetime(x, format='%m%Y')))
clean_df.to_csv('cleaned_data.csv', index=False)

prophet_df = clean_df[['ds','Bajra']].rename(columns={'Bajra': 'y'})
prophet_df.to_csv('Bajra_data.csv', index=False)
prophet_df_2 = clean_df[['ds','Moong']].rename(columns={'Moong': 'y'})
prophet_df_2.to_csv('Moong_data.csv', index=False)
prophet_df_3 = clean_df[['ds','Masur']].rename(columns={'Masur': 'y'})
prophet_df_3.to_csv('Masur_data.csv', index=False)
prophet_df_4 = clean_df[['ds','Cauliflower']].rename(columns={'Cauliflower': 'y'})
prophet_df_4.to_csv('Cauliflower_data.csv', index=False)
