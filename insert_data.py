#This for production and do not to use in other modules
import os

# echo "Enter product name: "
# read product_name
# echo "Enter price: "
# read price
# echo "Enter image name: "
# read image_name

data = [['Shoes','12','shoes.jpeg'],
['Lip Gloss','5','lip_gloss.jpeg'],
['Mascara','5','maskara.jpeg'],
['DISSENT Matte Lipstick','6','Oddity_-_DISSENT_Matte_Lipstick.jpeg'],
['Beautiful Chain Watch','50','Beautiful_chain_watch.jpeg'],
['Black Opium Perfume','15','perfume.jpeg']]
for i in data:
  quire = 'mysql -h 127.0.0.1 -u kali -pkali -e "INSERT INTO shopesite.products(product_name, price, quantity, describe, image_name) VALUES (\'{a}\',\'{b}\',\'5\',\'{c}\');"'.format(a=i[0],b=i[1],c=i[2])
  os.system(quire)
  print(quire)
