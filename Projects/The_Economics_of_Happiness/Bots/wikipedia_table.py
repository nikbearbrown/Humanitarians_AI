import pandas as pd
import argparse
import wikipedia as wp  # pip3 install wikipedia
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--wiki_page", help="Give a wiki page to get table", required=True)
parser.add_argument("-i", "--index", help="Zero based table index", required=False, default=1)
args = parser.parse_args()
index=1
try:
	index=int(args.index)
except:
	pass
	
		
	
html = wp.page(args.wiki_page).html().encode("UTF-8")
try: 
    df = pd.read_html(html)[1]  # Try 2nd table first as most pages contain contents table first
except IndexError:
    df = pd.read_html(html)[0]

outfile=args.wiki_page+'.csv'

df.to_csv(outfile)

print(df.to_string())
print(index)

#  Usage: python wikipedia_table.py -p Wikipedia_Page_Article_Here
# python wikipedia_table.py -p ISO_3166-1
