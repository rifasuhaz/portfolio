import streamlit as st # type: ignore
import pandas as pd
import numpy as np

st.subheader("Travel Journal")

df = pd.DataFrame(
    {
        "loc": ['Frankfurt', 'Cologne', 'Mainz', 'Trier', 'Luxembourg', 'Kassel', 'Karlsruhe', 'Strasbourg', 'Stuttgart','Wiesbaden',
                'Heidelberg', 'Amsterdam', 'Haarlem', 'Muiden', 'Zandvoort', 'Basel', 'Ingolstadt', 'Munich',
                 "Salzburg", "Königssee", "Bergamo", "Milan", "Monza", "Venice", "Göttingen", "Barcelona", "Blanes", "Brussels",
                  "Dubai", "Pune", "Calicut" ],
        "lat": [50.1109, 50.9375, 49.9929, 49.7499, 49.6117, 51.312, 49.0069, 48.5734, 48.7758, 50.0826, 49.3988, 52.3676,52.3874,52.3308,52.3731,47.5596,
                 48.7651,48.1351, 47.8095, 47.5831, 45.6983, 45.4642, 45.5845, 45.4408, 51.5413, 41.3874, 41.6745, 50.8503,25.276987, 18.519570, 11.2588],
        "lon": [8.6821, 6.9603, 8.2473, 6.6371, 6.1319, 9.4797, 8.4037, 7.7521, 9.1829, 8.2493, 8.6724, 4.9041,4.6462,5.0688,4.5339,7.5886,11.4237,
                 11.5820, 13.0550, 12.9901, 9.6773, 9.1900, 9.2744, 12.3155, 9.9158, 2.1686, 2.7902, 4.3517,55.296249, 73.855350, 75.7804],
        "col": np.random.rand(31, 4).tolist()
    }
)

st.map(df, latitude="lat", longitude="lon", size=10000, color='col')
