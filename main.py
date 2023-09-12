

import os

import pandas as pd
import folium

from helpers import Icons

from dotenv import load_dotenv
load_dotenv()

cc_star = ['American Museum of Natural History', 'Arizona State University', 'Brookhaven National Laboratory', 'California Institute of Technology', 'Cinvestav', 'Clarkson University', 'Clemson University', 'Cybera', 'Fermi National Accelerator Laboratory', 'Florida International University', 'Florida State University', 'Franklin and Marshall College', 'Georgia Institute of Technology', 'Georgia State University', 'Great Plains Network', 'Indiana University', 'Kansas State University', 'Lafayette College', 'Lamar University', 'Lancium', 'Lehigh University', 'Louisiana State University', 'Louisiana State University Health Sciences Center', 'New Mexico State University', 'North Carolina State University', 'North Dakota State University', 'Old Dominion University', 'Oral Roberts University', 'Penn State University', 'Portland State University', 'Purdue University', 'Rhodes College', 'Rice University', 'Southern Illinois University Edwardsville', 'Syracuse University', 'Texas Advanced Computing Center', 'The College of New Jersey', 'Thomas Jefferson National Accelerator Facility', 'Tufts University', 'Universidade Estadual Paulista', 'University of Alabama', 'University of Arkansas at Little Rock', 'University of California Riverside', 'University of California San Diego', 'University of Chicago', 'University of Colorado', 'University of Colorado Denver', 'University of Connecticut', 'University of Maine System', 'University of Michigan', 'University of Mississippi', 'University of Nebraska', 'University of Notre Dame', 'University of Puerto Rico - Mayaguez', 'University of South Dakota', 'University of South Florida', 'University of Southern California', 'University of Tennessee Chattanooga', 'University of Washington', 'University of Wisconsin', 'Villanova University', 'Wayne State University', 'West Texas A&M University']

def get_restricted_df():
    df_supplemental = pd.read_csv("data/input/2023-09-12-final_w_supplemental.csv")

    df_cc_star = pd.read_csv("data/input/OSPool_CC_contributors_Sep_2022–Sep_2023-Final.csv")

    df_restricted_cc_star = df_cc_star[df_cc_star["Restricted Map"] == "X"]
    restricted_map_institutions = set(df_restricted_cc_star["Institution"].unique())

    df = df_supplemental[df_supplemental["Institution Name"].isin(restricted_map_institutions)]

    print(f"Length of restricted map institutions: {len(restricted_map_institutions)}")
    print(f"Length of df: {len(df)}")
    print(f"Is not in: {restricted_map_institutions - set(df['Institution Name'].unique())}")

    return df


def get_broader_df():
    df_supplemental = pd.read_csv("data/input/2023-09-12-final_w_supplemental.csv")

    df_cc_star = pd.read_csv("data/input/OSPool_CC_contributors_Sep_2022–Sep_2023-Final.csv")

    df_restricted_cc_star = df_cc_star[df_cc_star["Broader Map"] == "X"]
    restricted_map_institutions = set(df_restricted_cc_star["Institution"].unique())

    df = df_supplemental[df_supplemental["Institution Name"].isin(restricted_map_institutions)]

    print(f"Length of restricted map institutions: {len(restricted_map_institutions)}")
    print(f"Length of df: {len(df)}")
    print(f"Is not in: {restricted_map_institutions - set(df['Institution Name'].unique())}")

    return df

def mapped_institutions_to_map(df: pd.DataFrame, output_file: str):

    location = [39.814805864395844, -97.69559319869889]
    zoom_start = 4

    m = folium.Map(location=location, zoom_start=zoom_start, tiles=f"https://api.mapbox.com/styles/v1/mapbox/navigation-day-v1/tiles/{{z}}/{{x}}/{{y}}?access_token={os.environ['MAPBOX_KEY']}", attr="Maps via Mapbox")

    for row in df.to_dict(orient="records"):

        folium.Marker((row['LAT'], row['LON']), icon=Icons.plain(), popup=row['Institution Name']).add_to(m)

    m.save(output_file)


if __name__ == "__main__":
    restricted_df = get_restricted_df()
    unrestricted_df = get_broader_df()

    mapped_institutions_to_map(restricted_df, "index.html")
    mapped_institutions_to_map(unrestricted_df, "broader.html")