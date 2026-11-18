import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. REMOVE img7.jpg COMPLETELY:
# In Hero:
html = html.replace('src="img7.jpg"', 'src="img6.jpg"')
html = html.replace('alt="ALARA SCENT Signature Perfumes Collection &mdash; Badshah, Laila & Sarbuland"', 'alt="ALARA SCENT Luxury Perfume Flacon &mdash; Laila Velvet"')

# In Product Card 7:
html = re.sub(
    r'<img src="img7\.jpg"\s+alt="The Alara Scent Trio"[^>]*>',
    '<img src="img3.jpg" alt="Alzaira Royale Edition" class="card-img w-full h-full object-cover" loading="lazy" />',
    html
)
html = html.replace('The Alara Scent Trio', 'Alzaira Royale Edition')
html = html.replace('Badshah + Laila + Sarbuland (3 x 50 ML)', 'Imperial Amber &bull; Rare Saffron &bull; Woods')
html = html.replace('PKR 12,500', 'PKR 5,400')

# In Category Tile 4:
html = html.replace('<img src="img7.jpg" alt="Discovery Sets" class="cat-img" loading="lazy" />', '<img src="img8.jpg" alt="Artisanal Flacons" class="cat-img" loading="lazy" />')
html = html.replace('<span>Discovery Gift Box</span>', '<span>Artisanal Flacons</span>')

# Any remaining img7.jpg fallback to img8.jpg or img6.jpg
html = html.replace('img7.jpg', 'img8.jpg')

# 2. Hero subtitle and top bar:
html = re.sub(
    r'Discover our latest hijabs, abayas &amp; prayer wear &mdash; crafted with intention, worn with grace\.',
    'Where rare essences meet royal craftsmanship &mdash; handcrafted with high oil concentration for 12+ hours of lingering sillage.',
    html
)
html = html.replace('Free Shipping on Orders Over PKR 2,000 &nbsp;&middot;&nbsp; Use Code <strong>HIJABI10</strong>', 'Free Express Delivery Across Pakistan on Orders Over PKR 3,000 &nbsp;&middot;&nbsp; Fragrances That Stay With You')

# 3. Product Cards <h3> titles:
html = html.replace('Rayon Hijab &mdash; Beaver Brown', 'Badshah Eau De Parfum')
html = html.replace('Rayon Hijab &mdash; Tan Brown', 'Laila Eau De Parfum')
html = html.replace('Namaz Chadar &mdash; Premium', 'Alzaira Eau De Parfum')
html = html.replace('Chiffon Hijab &mdash; Dusty Rose', 'Sarbuland Eau De Parfum')
html = html.replace('Georgette Dupatta &mdash; Olive', 'Sarbuland Noir Intense')
html = html.replace('Jersey Hijab &mdash; Charcoal', 'Laila Velvet Elixir')
html = html.replace('Abaya &mdash; Midnight Black', 'Alzaira Royale Edition')
html = html.replace('Prayer Set &mdash; Ivory', 'Laila Royale Extrait')

# Also fix the fallback plain names if present
html = html.replace('Rayon Hijab in Beaver Brown', 'Badshah Eau De Parfum')
html = html.replace('Rayon Hijab in Tan Brown', 'Laila Eau De Parfum')
html = html.replace('Namaz Chadar Premium Prayer Wrap', 'Alzaira Eau De Parfum')
html = html.replace('Chiffon Hijab in Dusty Rose', 'Sarbuland Eau De Parfum')
html = html.replace('Georgette Dupatta in Olive Green', 'Sarbuland Noir Intense')
html = html.replace('Jersey Hijab in Charcoal', 'Laila Velvet Elixir')
html = html.replace('Abaya in Midnight Black', 'Alzaira Royale Edition')
html = html.replace('Prayer Set in Ivory White', 'Laila Royale Extrait')

# 4. Section 6 titles and texts:
html = html.replace('Luxury Namaz Chadar &mdash; White', 'Sarbuland Classic')
html = html.replace('Prayer Set &mdash; Complete Set', 'Sarbuland Noir')
html = html.replace('Jananmaz &mdash; Embroidered Velvet', 'Laila Velvet')
html = html.replace('Prayer Dupatta &mdash; Soft Velvet', 'Laila Royale')

html = html.replace('Luxury Namaz Chadar in White', 'Sarbuland Classic')
html = html.replace('Complete Prayer Set with Hijab and Abaya', 'Sarbuland Noir')
html = html.replace('Embroidered Prayer Jananmaz', 'Laila Velvet')
html = html.replace('Soft Velvet Prayer Dupatta', 'Laila Royale')

html = html.replace('id="prayer"', 'id="signature"')
html = html.replace('href="#prayer"', 'href="#signature"')

# 5. Section 7 CTA strip:
html = html.replace('7. CTA STRIP &mdash; MODEST. ELEGANT. YOU.', '7. CTA STRIP &mdash; THE ALARA SCENT PROMISE')
html = html.replace('Modest. Elegant.<br/>You.', 'Fragrances That<br/>Stay With You.')

# 6. Footer Clean up:
html = html.replace('Premium modest fashion for the modern Muslim woman. Quality fabrics, timeless designs, and contemporary fits &mdash; delivered across Pakistan.', 'Where rare essences meet royal craftsmanship. Handcrafted in small batches with concentrated oils for 12+ hours of lingering luxury.')
html = html.replace('hello@hijabithreads.pk', 'orders@alarascent.pk')
html = html.replace('Hijabs &amp; Scarves', 'Badshah Pour Homme')
html = html.replace('Abayas &amp; Kaftans', 'Laila Pour Femme')
html = html.replace('Chadars &amp; Wraps', 'Sarbuland Intense')
html = html.replace('Prayer Sets &amp; Jananmaz', 'Alzaira Royale')

# Clean any remaining HijabiThreads
html = html.replace('HijabiThreads', 'ALARA SCENT')
html = html.replace('hijabithreads', 'alarascent')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('fix_images_and_text.py executed successfully!')
