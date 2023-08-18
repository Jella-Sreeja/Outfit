import random
import pandas as pd

# Define attributes for men and women
men_body_types = ["Athletic", "Slim", "Regular","Ectomorph","Mesomorph","Endomorph","Straight","Pear","Oval","Diamond","Lean and Muscular","Circular","Tall and Slim","Short and Stocky","Athletic","lanky","Sturdy","Hourglass"]
women_body_types = ["Hourglass", "Straight", "Pear","Full Bust","Petite","Tall","Short","Athletic","Curvy","Diamond","Oval","Lean and Slim","Full-Figured","Long Torso","Short Legs","Broad Shoulders","Narrow Shoulders","Slim Hips"]
styles = ["Casual", "Formal", "Classic", "Vintage", "Bohemian","Minimalist","Grunge","Preppy","Sporty","BOho-Chic","Rock or Punk","Urban","Romantic","Eclectic","Trendy","Retro","Chic","Edgy","Gothic","Prairie","Country","Western","Artsy","Futuristic"]
colors = ["Red", "Blue", "Black", "White","Grey","Blue","Yellow","Beige","Peach","Pink","Green","Purple","Sage","Teal","Orange","Navy","Mint","Marron","Brown","Lavender","hot pink","vibrant yellow","olive green","mustard yellow","gold","silver","terracotta"]
occasions = ["Casual", "Formal", "Party", "Ethnic","Professional","Semi-Formal","Cocktail","Beach","Smart Casual","Festive","Sporty","Holiday","Outdoor events","Winter Fashion","Bohemian Fashion","Dance outfits","Sporty looks","Layering","Business Casual","Vacation","Date Night","Garden Party","Prom","Picnic","Graduation","Maternity","Formal Cruise Night","Cultural Events","Concert","Retro Party","Weddings","Religious Ceremonies"]

# CATEGORIES[Winter Wear,Topwear,Bottomwear,Raincoats,Dresses and Gowns,Clothing Accessories,Jumpsuits and Dungarees,Kurtas,Ethnic Sets and Bottoms,Fabrics,Sarees and Saree Essentials,Kid's Combos and Costumes,Lehenge Cholis,Windcheaters,Sleepwear,Innerwear and Swimwear,Tracksuits,(Blazers,Waistcoats and Suits),Co-ords]


# Define categories and their subcategories with attributes      
categories = {
    "Men": {
        "Men's Top wear": {
            "Shirts": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": men_body_types
            },
            "T shirts": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": men_body_types
            }
        },
        "Men's Winter Wear": {
           "Sweatshirts": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": men_body_types
            },
           "Jackets": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": men_body_types
            },
           "Sweaters": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": men_body_types
            },
           "Shrugs": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": men_body_types
            },
           "Gloves": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": men_body_types
            },
           "Shawls": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": men_body_types
            },
           "Mufflers": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": men_body_types
            },
           "Scarves": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": men_body_types
            },
           "Thermals": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": men_body_types
            },
           "Arm Warmers": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": men_body_types
            },
           "Leg Warmers": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": men_body_types
            }                                                           

        },
        "Men's Bottom wear": {
           "Shorts": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": men_body_types
            },
           "Harem Pants": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": men_body_types
            },
           "Three-Fourths": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": men_body_types
            },
           "Jeans": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": men_body_types
            },
           "Tights": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": men_body_types
            },
           "Cargos": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": men_body_types
            },
           "Trousers": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": men_body_types
            },
           "Track Pants": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": men_body_types
            },

           
        },
        "Men's Raincoats": {
           "Men Raincoats": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": men_body_types
            },
           "Boy's Raincoats": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": men_body_types
            }       
           
        },
        "Men's Clothing Accessories": {
           "Turbans": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": men_body_types
            },
           "Suspenders": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": men_body_types
            },
           "Garters": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": men_body_types
            },
           "Stoles": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": men_body_types
            },
           "Caps": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": men_body_types
            },
           "Bandanas": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": men_body_types
            },
           "Handkerchiefs": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": men_body_types
            },
           "Hats": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": men_body_types
            },
           "Wristbands": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": men_body_types
            },
           "Ties and Cufflins": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": men_body_types
            },
           "Dupattas": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": men_body_types
            },
           "Socks": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": men_body_types
            }                                                           

        },
        "Men's Kurtas, Ethnic Sets and Bottoms": {
           "Sherwanis": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": men_body_types
            },
           "Salwars and Patialas": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": men_body_types
            },
           "Ethnic Sets": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": men_body_types
            },
           "Palazzos": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": men_body_types
            },
           "Dhotis": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": men_body_types
            },
           "Ethnic Pyjamas": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": men_body_types
            },
           "Kurtas": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": men_body_types
            }

        },
        "Men's Fabrics": {
           "Shirt and Trouser Fabrics": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": men_body_types
            },
           "Formal Suit Fabrics": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": men_body_types
            },
           "Dress Materials": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": men_body_types
            }

        },

        "Men's WindCheaters": {
           "Men's Windcheaters": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": men_body_types
            }

        },
        "Men's Sleepwear": {
           "Night Suits": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": men_body_types
            },
           "Pyjamas and Lounge Pants": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": men_body_types
            }

        },  
        "Men's Inner wear and Swimwear": {
           "Briefs and Trunks": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": men_body_types
            },
           "Swimsuits": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": men_body_types
            },
           "Vests": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": men_body_types
            },
           "Boxers": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": men_body_types
            }
                          
        },
        "Men's Tracksuits": {
           "Men's Tracksuits": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": men_body_types
            }

        },
        "Men's Blazers,Waistcoats and Suits": {
           "Coats": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": men_body_types
            },
           "Suits": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": men_body_types
            },
           "Blazers": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": men_body_types
            },
           "Waistcoats": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": men_body_types
            }
                          
        },
        "Men's Footwear": {

           "Casual Shoes": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": men_body_types
            },
           "Sports Shoes": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": men_body_types
            },
           "Formal Shoes": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": men_body_types
            },
           "Sandals & Floaters": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": men_body_types
            },
           "Flip Flops": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": men_body_types
            },
           "Loafers": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": men_body_types
            },
           "Boots": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": men_body_types
            },
           "Running Shoes": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": men_body_types
            },
           "Sneakers": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": men_body_types
            },
           "Slippers": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": men_body_types
            }

        },
        "Men's Accessories": {

           "Backpacks": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": men_body_types
            },
           "Wallets": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": men_body_types
            },
           "Belts": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": men_body_types
            },
           "Sunglasses": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": men_body_types
            },
           "Luggage & Travel": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": men_body_types
            },
           "Frames": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": men_body_types
            },
           "Jewellery": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": men_body_types
            }

        },
        "Men's Watches": {

           "Smart Watches": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": men_body_types
            },
           "Chain Watches": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": men_body_types
            },
           "Analog Watches": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": men_body_types
            },
           "Digital Watches": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": men_body_types
            },
           "Quartz Watches": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": men_body_types
            },
           "Chronograph Watches": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": men_body_types
            },
           "Swiss Watches": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": men_body_types
            },
           "Tactile Watches": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": men_body_types
            }

        },


    },
    
    "Women": {
        "Women's Topwear": {
            "Tops": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
            "Shirts": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
            "Tshirts": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            }
        },   
        "Women's Winter Wear": {
           "Sweatshirts": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": women_body_types
            },
           "Jackets": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": women_body_types
            },
           "Sweaters": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Shrugs": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Gloves": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types":women_body_types
            },
           "Shawls": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": women_body_types
            },
           "Mufflers": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": women_body_types
            },
           "Scarves": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": women_body_types
            },
           "Thermals": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": women_body_types
            },
           "Ponchos": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": women_body_types
            },
           "Arm Warmers": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": women_body_types
            },
           "Leg Warmers": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": women_body_types
            }                                                           

        },     
        "Women's Bottowear": {
           "Shorts": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Harem Pants": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Three-Fourths": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Jeans": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Tights": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Cargos": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Trousers": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Track Pants": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Capris": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Skirts": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Jeggings": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            }
           
        },
        "Women's Raincoats": {
           "Women's Raincoats": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": women_body_types
            },
           "Girl's Raincoats": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": women_body_types
            }       
           
        },

        "Women's Dresses and Gowns": {
           "Gowns": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Dresses": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            }       
           
        },
        "Women's Clothing Accessories": {
           "Turbans": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Suspenders": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Garters": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Stoles": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Caps": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": women_body_types
            },
           "Bandanas": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Handkerchiefs": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": women_body_types
            },
           "Hats": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Wristbands": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Ties and Cufflins": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": women_body_types
            },
           "Dupattas": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Socks": {
                "styles": styles,
                "colors": colors,
                "occasions": "NA",
                "body_types": women_body_types
            },
           "Stockings": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            }, 
           "Sarong": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },                                                        

        },
        "Women's Jumpsuits and Dungarees":{
           "Women Jumpsuits and Dungarees": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },       
        },

        "Women's Kurtas,Ethnic Sets and Bottoms": {
           "Leggings and Churidars": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Salwars and Patialas": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Ethnic Sets": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Palazzos": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Dhoti Pants": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Ethnic Pyjamas": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Kurtas": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            }

        },

        "Women's Fabrics": {
           "Shirt and Trouser Fabrics": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Formal Suit Fabrics": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Dress Materials": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Blouse Material": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
                                 
        },
        "Women's Sarees and Saree Essentials": {
           "Blouses": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Sarees": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Saree Falls": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Petticoats": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            }
                           
        },
        "Women's Lehenge Cholis":{
           "Girl's Lehenge Cholis": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },       
        },
        "Women's Sleepwear": {
           "Night Suits": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Pyjamas and Lounge Pants": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Night Dresses and Nighties": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
                          
        },
        "Women's Innerwear and Swimwear": {
           "Camisoles and Slips": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Swimsuits": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Vests": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Boxers": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Bras": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Panties": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Bras": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
                          
        },
        "Women's Tracksuits": {
           "Women Tracksuits": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            }

        },
        "Women's Blazers,Waistcoats and Suits": {
           "Coats": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Suits": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Blazers": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Waistcoats": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            }
                          
        },
        "Women's Footwear": {

           "Casual Shoes": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Sports Shoes": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Formals": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Sports Sandals": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Slippers & Flip Flops": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Flats": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Boots": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Running Shoes": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Ethnic Shoes": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Heels": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },                                                     
           "Ballerinas": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            }                                                      
 
        },
       "Women's Watches": {

           "Smart Watches": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Casual Watches": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Two-Tone Watches": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Interchangable Watches": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Luxury Watches": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Chronograph Watches": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Sport Watches": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Hybrid Watches": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Digital Watches": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Chain Watches": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            }
       },


        "Women's Jewellery": {

           "Gemstones,Coins & Bars": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Precious Jewellery": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Artificial jewellery": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Silver jewellery": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Precious Articles": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },

        },


        "Women's Accessories":{

           "Handbags": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Shoulder Bags": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Totes": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Sling bags": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Luugage & Travel": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Clutches": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Wallets & Belts": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Sunglasses": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            },
           "Frames": {
                "styles": styles,
                "colors": colors,
                "occasions": occasions,
                "body_types": women_body_types
            }

        },

    

    }


    
}


# Generate simulated product data for different genders, categories, and subcategories
simulated_products = []

def generate_product_data():
    products = []
    for _ in range(100):  # Number of products
        gender = random.choice(["Men", "Women"])
        category = random.choice(list(categories[gender].keys()))
        subcategory = random.choice(list(categories[gender][category].keys()))
        sub_attributes = categories[gender][category][subcategory]
        product = {
            "ProductID": f"{gender[:1]}-{category[:2]}-{subcategory[:2]}",
            "Category": category,
            "Subcategory": subcategory,
            "Gender": gender,
            "Style": random.choice(sub_attributes["styles"]),
            "Color": random.choice(colors),
            "Occasion": random.choice(sub_attributes["occasions"]),
            "BodyType": random.choice(sub_attributes["body_types"])
        }
        products.append(product)
    return products

# Generate product data
simulated_products.extend(generate_product_data())

# Create a DataFrame from the simulated product data
product_df = pd.DataFrame(simulated_products)

# Save the DataFrame to a CSV file
product_df.to_csv("simulated_product_data.csv", index=False)