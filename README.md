### Recipe extractor:  

This script takes transcripts of cooking videos and puts them into recipe format.  It can handle Chinese - translate it.

###Pre-requisite:  

1.  fabric AI - https://github.com/danielmiessler/fabric

2.  Using Google Gemni - so you need api key

3.  Youtube API key

### Setup fabric

copy extract_recipe_prompt.md  $HOME/.config/fabric/patterns/extract_recipe/system.md  ( make extract_recipe dir first )



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


### Chinese recipe


### Title

sixi_wanzi.txt - Four Happiness Meatballs (四喜丸子)

### Objectives
- Learn to make delicious and tender Four Happiness Meatballs.
- Master the techniques for preparing the meat mixture and shaping the meatballs.
- Understand the importance of simmering for optimal flavor and texture.

### Ingredients

- Spring bamboo shoots (春笋), diced (筷子头大小的丁)
- Sea cucumber (海参), diced (筷子头大小的丁)
- Pork (三肥七瘦肉), 8 liang (approximately 360g)
- Egg white (蛋清), 1
- Soy sauce (酱油), 20g
- Salt (盐), to taste
- MSG (味精), to taste
- Sesame oil (香油), 10g
- Dried shrimp (干海米), 15g
- Potato starch (淀粉), 25g (half liang)
- All-purpose flour (面粉), 25g
- Eggs (鸡蛋), 2-2.5
- Cooking oil (豆油)


### Instructions

1. Dice spring bamboo shoots and sea cucumber into small pieces (about the size of a chopstick head).
2. Combine pork, egg white, soy sauce, salt, MSG, and sesame oil in a bowl. Mix thoroughly until sticky and slightly stringy (about 4 minutes).
3. Add the cooked dried shrimp and stir.
4. Gradually add the potato starch and mix well.
5. Add the flour and mix for another 2 minutes.
6. Divide the mixture into small portions and shape into balls. (Wet hands to help shape the meatballs.)
7. Beat eggs with 1 liang (60g) potato starch and some flour.
8. Coat each meatball in the egg mixture.
9. Deep fry the meatballs in hot oil for 10 minutes until golden brown and cooked through.
10. In a separate pot, sauté scallions and ginger.
11. Add the fried meatballs, salt, soy sauce, and water to the pot.
12. Bring to a boil, then simmer for 20 minutes.
13. Add MSG and simmer for an additional 10 minutes.
14. Remove the meatballs and serve, drizzled with the cooking broth.  Do not add coriander or scallions.  Add more dried shrimp if the sea cucumber isn't flavorful enough.
 
### Youtube link 
 
https://www.youtube.com/watch?v=a8Xd5wsj5rg
 










