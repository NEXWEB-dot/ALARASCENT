import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Title & Meta
html = html.replace('HijabiThreads &mdash; Modest Fashion for Every Occasion', 'ALARA SCENT &mdash; Fragrances That Stay With You')
html = html.replace('Discover premium hijabs, abayas, prayer wear and modest fashion at HijabiThreads. Shop the latest collections crafted with elegance and care.', 'Discover handcrafted luxury Eau de Parfum, royal ouds, and signature fragrances at ALARA SCENT. Fragrances that stay with you.')

# 2. Header Logo & Home label
logo_old = '<span style="font-family: Georgia, serif; font-size:22px; font-weight:400; letter-spacing:0.03em; color:#000;">HijabiThreads</span>'
logo_new = '<div class="flex items-center gap-2.5"><img src="alara-emblem.jpg" alt="ALARA SCENT Crest" class="w-8 h-8 rounded-full border border-black/20 object-cover" /><div class="flex flex-col text-left leading-none"><span style="font-family: Georgia, serif; font-size:18px; font-weight:600; letter-spacing:0.2em; color:#000;">ALARA SCENT</span><span style="font-size:8px; font-weight:600; letter-spacing:0.12em; text-transform:uppercase; color:#c5a467; margin-top:2px;">Fragrances That Stay With You</span></div></div>'
html = html.replace(logo_old, logo_new)
html = html.replace('aria-label="HijabiThreads Home"', 'aria-label="ALARA SCENT Home"')

# Nav links
html = html.replace('>Shop<', '>All Perfumes<')
html = html.replace('>Collections<', '>Signature Blends<')
html = html.replace('>Sale<', '>Discovery Box<')

# 3. Hero Section
html = html.replace('858702253_17953616229273378_4560003239917733461_n.webp', 'img7.jpg')
html = html.replace('Woman wearing a beautiful hijab &mdash; HijabiThreads new collection', 'ALARA SCENT Signature Perfumes Collection &mdash; Badshah, Laila & Sarbuland')
html = html.replace('New Collection &mdash; Autumn 2025', '✦ Eau de Parfum &mdash; Exclusive Collection ✦')
html = html.replace('Modesty in<br/>Every Thread', 'Fragrances That<br/>Stay With You')
html = html.replace('Explore our handpicked range of premium hijabs, abayas, and modest wear designed for grace, comfort, and everyday confidence.', 'Where rare essences meet royal craftsmanship. Handcrafted with high oil concentration for an unforgettable presence and 12+ hours of lingering sillage.')
html = html.replace('Shop the Collection', 'Explore Perfumes')
html = html.replace('Explore Categories', 'View Collections')

# 4. Section 4 Heading: "New Arrivals" -> "Signature Perfumes"
html = html.replace('Curated Modest Wear for the Season', 'Handcrafted Eau de Parfum &mdash; 50 ML Flacons')

# 5. Product Card 1: Badshah
html = html.replace('731417533_17936843199273378_1406667821305969010_n.webp', 'img1.jpg')
html = html.replace('alt="Rayon Hijab in Beaver Brown"', 'alt="Badshah Eau De Parfum"')
html = html.replace('Rayon Hijab in Beaver Brown', 'Badshah Eau De Parfum')
html = html.replace('Rayon Blend &bull; Regular Fit', 'Royal Leather &bull; Black Oud &bull; Amber')
# Price update
html = html.replace('PKR 850', 'PKR 4,500')

# Product Card 2: Laila
html = html.replace('800779984_17947466250273378_2007521923048539687_n.webp', 'img2.jpg')
html = html.replace('alt="Rayon Hijab in Tan Brown"', 'alt="Laila Eau De Parfum"')
html = html.replace('Rayon Hijab in Tan Brown', 'Laila Eau De Parfum')
html = html.replace('Rayon Blend &bull; Relaxed Fit', 'Midnight Jasmine &bull; Vanilla Orchid &bull; Musk')
html = html.replace('PKR 850', 'PKR 4,800')

# Product Card 3: Alzaira
html = html.replace('800924581_17947466259273378_4258943424329358943_n.webp', 'img3.jpg')
html = html.replace('alt="Namaz Chadar Premium Prayer Wrap"', 'alt="Alzaira Eau De Parfum"')
html = html.replace('Namaz Chadar Premium Prayer Wrap', 'Alzaira Eau De Parfum')
html = html.replace('Cotton Blend &bull; Full Length', 'Warm Saffron &bull; Tonka Bean &bull; Lavender')
html = html.replace('PKR 1,200', 'PKR 4,600')

# Product Card 4: Sarbuland
html = html.replace('800924581_17947466304273378_252163861717643984_n.webp', 'img4.jpg')
html = html.replace('alt="Chiffon Hijab in Dusty Rose"', 'alt="Sarbuland Eau De Parfum"')
html = html.replace('Chiffon Hijab in Dusty Rose', 'Sarbuland Eau De Parfum')
html = html.replace('Chiffon &bull; One Size', 'Smoky Cedarwood &bull; Bergamot &bull; Cardamom')
html = html.replace('PKR 600', 'PKR 4,200')
html = html.replace('PKR 750', 'PKR 5,200')

# Product Card 5: Sarbuland Noir
html = html.replace('801199906_17947466274273378_3130519888825629821_n.webp', 'img5.jpg')
html = html.replace('alt="Georgette Dupatta in Olive Green"', 'alt="Sarbuland Noir Intense"')
html = html.replace('Georgette Dupatta in Olive Green', 'Sarbuland Noir Intense')
html = html.replace('Georgette &bull; 2.5m Length', 'Dark Vetiver &bull; Patchouli &bull; Incense')
html = html.replace('PKR 950', 'PKR 4,950')

# Product Card 6: Laila Velvet
html = html.replace('810090934_17948301408273378_4441191875684567654_n.webp', 'img6.jpg')
html = html.replace('alt="Jersey Hijab in Charcoal"', 'alt="Laila Velvet Elixir"')
html = html.replace('Jersey Hijab in Charcoal', 'Laila Velvet Elixir')
html = html.replace('Premium Jersey &bull; Stretch Fit', 'Damask Rose &bull; Ambergris &bull; Sweet Tonka')
html = html.replace('PKR 650', 'PKR 5,200')

# Product Card 7: The Alara Scent Trio
# Card 7 previously referenced webp 8587...
html = re.sub(
    r'<img src="858702253_17953616229273378_4560003239917733461_n\.webp"\s+alt="Abaya in Midnight Black"[^>]*>',
    '<img src="img7.jpg" alt="The Alara Scent Trio" class="card-img w-full h-full object-cover" loading="lazy" />',
    html
)
html = html.replace('Abaya in Midnight Black', 'The Alara Scent Trio')
html = html.replace('Nida Fabric &bull; Full Length', 'Badshah + Laila + Sarbuland (3 x 50 ML)')
html = html.replace('PKR 2,800', 'PKR 12,500')

# Product Card 8: Laila Royale
html = re.sub(
    r'<img src="731417533_17936843199273378_1406667821305969010_n\.webp"\s+alt="Prayer Set in Ivory White"[^>]*>',
    '<img src="img8.jpg" alt="Laila Royale Extrait" class="card-img w-full h-full object-cover" loading="lazy" />',
    html
)
html = html.replace('Prayer Set in Ivory White', 'Laila Royale Extrait')
html = html.replace('Soft Rayon &bull; 2-Piece Set', 'Pure Extrait De Parfum &bull; 50 ML Flacon')
html = html.replace('PKR 1,500', 'PKR 5,500')

# 6. Quick Category Links
html = html.replace('>The Show-stopper', '>Royal Ouds')
html = html.replace('>Prayer Essentials', '>Floral Nectar')
html = html.replace('>Just Arrived', '>Woody & Spiced')
html = html.replace('>Sale Picks', '>Discovery Sets')

# 7. Category Tiles (4 tiles)
html = html.replace('Shop by Category', 'Shop by Fragrance Family')

# Tile 1:
html = re.sub(
    r'<a href="#" class="category-tile" aria-label="Shop Abaya and Kaftan">\s*<img src="[^"]+"\s+alt="Woman in a beige abaya and kaftan"[^>]*>\s*<div class="cat-overlay"></div>\s*<div class="cat-label"><span>Abaya &amp; Kaftan</span></div>\s*</a>',
    '<a href="#new-arrivals" class="category-tile" aria-label="Shop Men Collection"><img src="img1.jpg" alt="Men Collection" class="cat-img" loading="lazy" /><div class="cat-overlay"></div><div class="cat-label"><span>Men\'s Bold &amp; Woody</span></div></a>',
    html
)

# Tile 2:
html = re.sub(
    r'<a href="#new-arrivals" class="category-tile" aria-label="Shop Hijab and Scarves">\s*<img src="[^"]+"\s+alt="Woman wearing a slate blue hijab scarf"[^>]*>\s*<div class="cat-overlay"></div>\s*<div class="cat-label"><span>Hijab &amp; Scarves</span></div>\s*</a>',
    '<a href="#new-arrivals" class="category-tile" aria-label="Shop Women Collection"><img src="img2.jpg" alt="Women Collection" class="cat-img" loading="lazy" /><div class="cat-overlay"></div><div class="cat-label"><span>Women\'s Floral &amp; Sweet</span></div></a>',
    html
)

# Tile 3:
html = re.sub(
    r'<a href="#prayer" class="category-tile" aria-label="Shop Chadars and Wraps">\s*<img src="[^"]+"\s+alt="Woman in a mauve chadar wrap"[^>]*>\s*<div class="cat-overlay"></div>\s*<div class="cat-label"><span>Chadars &amp; Wraps</span></div>\s*</a>',
    '<a href="#new-arrivals" class="category-tile" aria-label="Shop Unisex Collection"><img src="img3.jpg" alt="Unisex Collection" class="cat-img" loading="lazy" /><div class="cat-overlay"></div><div class="cat-label"><span>Unisex Amber &amp; Spiced</span></div></a>',
    html
)

# Tile 4:
html = re.sub(
    r'<a href="#prayer" class="category-tile" aria-label="Shop Prayer Sets">\s*<img src="[^"]+"\s+alt="Collection of prayer sets and namaz wear"[^>]*>\s*<div class="cat-overlay"></div>\s*<div class="cat-label"><span>Prayer Sets</span></div>\s*</a>',
    '<a href="#new-arrivals" class="category-tile" aria-label="Shop Discovery Sets"><img src="img7.jpg" alt="Discovery Sets" class="cat-img" loading="lazy" /><div class="cat-overlay"></div><div class="cat-label"><span>Discovery Gift Box</span></div></a>',
    html
)

# 8. Section 6: Prayer Wear -> Signature & Exclusif Collection
html = html.replace('6. NAMAZ & PRAYER COLLECTION', '6. SIGNATURE & EXCLUSIF COLLECTION')
html = html.replace('Prayer Wear &amp; Chadars', 'The Signature Flacons')
html = html.replace('Comfortable, graceful prayer sets and namaz chadars designed with care.', 'Pure concentrated perfume oil formulations designed to leave an unforgettable trail that stays with you.')

# 4 Cards in Section 6:
# Card 1: Sarbuland
html = html.replace('alt="Luxury Namaz Chadar in White"', 'alt="Sarbuland Classic"')
html = html.replace('Luxury Namaz Chadar in White', 'Sarbuland Classic')
html = html.replace('Pure Cotton &bull; Full Coverage', 'Eau De Parfum &bull; 50 ML Flacon')
html = html.replace('PKR 1,400', 'PKR 4,200')

# Card 2: Sarbuland Noir
html = html.replace('alt="Complete Prayer Set with Hijab and Abaya"', 'alt="Sarbuland Noir Intense"')
html = html.replace('Complete Prayer Set with Hijab and Abaya', 'Sarbuland Noir Intense')
html = html.replace('2-Piece Set &bull; Free Size', 'Eau De Parfum Intense &bull; 50 ML')
html = html.replace('PKR 2,200', 'PKR 4,950')

# Card 3: Laila Velvet
html = html.replace('alt="Embroidered Prayer Jananmaz"', 'alt="Laila Velvet Elixir"')
html = html.replace('Embroidered Prayer Jananmaz', 'Laila Velvet Elixir')
html = html.replace('Padded Velvet &bull; Anti-Slip', 'Eau De Parfum Elixir &bull; 50 ML')
html = html.replace('PKR 1,100', 'PKR 5,200')

# Card 4: Laila Royale
html = html.replace('alt="Soft Velvet Prayer Dupatta"', 'alt="Laila Royale Extrait"')
html = html.replace('Soft Velvet Prayer Dupatta', 'Laila Royale Extrait')
html = html.replace('Velvet Touch &bull; 2.25m', 'Extrait De Parfum &bull; 50 ML')

# Replace images in section 6
html = re.sub(r'<img src="800924581_17947466259273378_4258943424329358943_n\.webp"', '<img src="img4.jpg"', html)
html = re.sub(r'<img src="800924581_17947466304273378_252163861717643984_n\.webp"', '<img src="img5.jpg"', html)
html = re.sub(r'<img src="810090934_17948301408273378_4441191875684567654_n\.webp"', '<img src="img6.jpg"', html)
html = re.sub(r'<img src="801199906_17947466274273378_3130519888825629821_n\.webp"', '<img src="img8.jpg"', html)

# 9. Brand Story / Mission Section
html = html.replace('The HijabiThreads Promise', 'The House of ALARA SCENT')
html = html.replace('Modesty Without<br/>Compromise', 'Fragrances That<br/>Stay With You')
html = html.replace('Handpicked fabrics, thoughtful silhouettes, and styles made for the modern modest woman.', 'Under the celestial sign of the golden crescent and laurel, ALARA SCENT creates pure perfume flacons engineered to stay with you all day. Small batch artisanal aging with rare European essences and exotic oriental notes.')
html = html.replace('Shop Hijabs', 'Shop Perfumes')

# 10. Newsletter Section
html = html.replace('Join Our Community', 'The Art of Scent')
html = html.replace('Get early access to new arrivals, exclusive offers, and modest fashion inspiration &mdash; straight to your inbox.', 'Receive private access to new flacon releases, secret blends, and VIP promotions across Pakistan.')

# 11. Footer Section
footer_logo_old = '<p style="font-family:Georgia,serif; font-size:20px; font-weight:400; color:#fff; margin-bottom:14px;">HijabiThreads</p>'
footer_logo_new = '<div class="flex items-center gap-2.5 mb-3"><img src="alara-emblem.jpg" alt="ALARA SCENT Crest" class="w-9 h-9 rounded-full border border-white/20 object-cover" /><div class="flex flex-col"><span style="font-family: Georgia, serif; font-size:18px; font-weight:600; letter-spacing:0.2em; color:#fff;">ALARA SCENT</span><span style="font-size:8px; font-weight:600; letter-spacing:0.12em; text-transform:uppercase; color:#c5a467;">Fragrances That Stay With You</span></div></div>'
html = html.replace(footer_logo_old, footer_logo_new)

html = html.replace('Modest fashion crafted with love, dignity, and care for every occasion.', 'Where rare essences meet royal craftsmanship. Handcrafted in small batches with concentrated oils for 12+ hours of lingering luxury.')

html = html.replace('&copy; 2025 HijabiThreads. All rights reserved.', '&copy; 2026 ALARA SCENT. All rights reserved. Fragrances That Stay With You.')

# Replace remaining HijabiThreads mentions
html = html.replace('HijabiThreads', 'ALARA SCENT')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Successfully updated index.html with perfume images and ALARA SCENT branding!')
