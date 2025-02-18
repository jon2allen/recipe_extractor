### Recipe extractor:  

This script takes transcripts of cooking videos and puts them into recipe format.  It can handle Chinese - translate it.

###Pre-requisite:  

1.  fabric AI - https://github.com/danielmiessler/fabric

2.  Using Google Gemni - so you need api key

3.  Youtube API key


Locate channel id of Youtube channel - hit share and copy channel_id

python3 list_channel_vids.py UCMTX9qQThpdcleLKIUm9uEw > julia_child_pbs.txt

this puts a list of youtube videos in a file

### Then run:

python3 extract_recipes_log.py  julia_child_pbs.txt  $HOME/data/julia_child/ 500 &

This has pauses in it so that you don't exceed limits or push the model too fast.

### what you get
```
rw-r--r--. 1 jon2allen jon2allen 3844 Sep 11 22:46 vanilla_chiffon_cake_jelly_roll.txt
-rw-r--r--. 1 jon2allen jon2allen 3297 Sep 11 23:02 veal_prince_orloff.txt
-rw-r--r--. 1 jon2allen jon2allen 4303 Sep 11 22:08 veal_saddle_stuffed_onions_asparagus.txt
-rw-r--r--. 1 jon2allen jon2allen 2048 Sep 11 23:54 veal_scallops.txt
-rw-r--r--. 1 jon2allen jon2allen 2719 Sep 11 23:23 veal_stuffed_braised.txt
-rw-r--r--. 1 jon2allen jon2allen 4405 Sep 11 23:40 venison_steak_with_cherry_sauce.txt
-rw-r--r--. 1 jon2allen jon2allen 3483 Sep 11 22:44 vienesse_poppy_seed_torte.txt
-rw-r--r--. 1 jon2allen jon2allen 2577 Sep 11 23:01 wedding_cake.txt
-rw-r--r--. 1 jon2allen jon2allen 3143 Sep 11 23:39 white_chocolate_cake.txt
-rw-r--r--. 1 jon2allen jon2allen  484 Sep 11 22:07 winged_victory_chicken.txt
-rw-r--r--. 1 jon2allen jon2allen 3418 Sep 11 22:48 x_cookies_pizza_rustica.txt
-rw-r--r--. 1 jon2allen jon2allen 5209 Sep 11 23:30 zaleti_biscotti_amaretti_pizzelle.txt
-rw-r--r--. 1 jon2allen jon2allen 2567 Sep 11 22:06 zucchini_recipes.txt
```
### Title

veal_scallops.txt - Veal Scallops 
### Objectives
- Learn how to prepare and cook veal scallops.
- Explore different ways to cook veal scallops.
- Understand the importance of choosing high-quality veal.

### Ingredients

- Veal scallops (about 3/8 inch thick)
- 1 1/2 tbsp butter
- 1/2 tbsp olive oil
- 2 cups sliced mushrooms
- 1 tbsp shallots (or green onions)
- 1/4 cup port wine (or Madeira or vermouth)
- 1 tbsp shallots (or green onions)
- Brown stock (or canned beef bouillon or cream)
- 1/2 tbsp tarragon
- 1 tsp cornstarch
- Water (or port wine)
- Cold beef stock
- Salt and pepper
- Butter
- 4 tbsp flour
- 3 tbsp butter
- 2 cups chicken stock (or canned chicken bouillon)
- 1/2 cup finely minced onions (cooked slowly in butter)
- 2/3 cup sautéed mushrooms
- Slices of ham
- Grated Swiss cheese

### Instructions
1. Pound veal scallops to 1/4 inch thickness between sheets of wax paper.
2. Heat olive oil and butter in a pan over medium-high heat.
3. Sauté veal scallops for about 8 minutes, ensuring they are dry before adding to the pan.
4. While veal cooks, sauté mushrooms in oil and butter.
5. Add shallots to the mushrooms and cook for about 2 minutes.
6. Remove veal scallops from the pan and set aside.
7. Deglaze the pan with port wine and scrape up the brown bits.
8. Add shallots, brown stock, tarragon, and cornstarch mixed with water or port wine.
9. Simmer sauce until thickened and add veal scallops back to the pan.
10. Season with salt and pepper and serve immediately.
11. For *Veau Gratinées*: Prepare a velouté sauce with flour, butter, and chicken stock.
12. Add cooked onions and sautéed mushrooms to the velouté sauce.
13. Arrange veal scallops and slices of ham in an oven-proof dish.
14. Pour sauce over veal and ham and sprinkle with grated Swiss cheese.
15. Bake in a hot oven for 20 minutes until bubbly and brown.
16. Serve *Veau Gratinées* with steamed rice, buttered peas, hot French bread, and red Medoc Bordeaux wine. 
### Youtube link 
 
https://www.youtube.com/watch?v=JYs79u5EmTM













