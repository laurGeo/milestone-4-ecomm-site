[![Build Status](https://travis-ci.org/laurGeo/milestone-4-ecomm-site.svg?branch=master)](https://travis-ci.org/laurGeo/milestone-4-ecomm-site)
# Full Stack Frameworks Project with Django #

- [Full Stack Frameworks Project with Django](#full-stack-frameworks-project-with-django)
  * [OverView](#overview)
  * [UX](#ux)
  * [Features](#features)
  * [Features Left to Implement](#features-left-to-implement)
  * [Technologies Used](#technologies-used)
  * [Testing](#testing)
  * [Deployment](#deployment)
  * [Credits](#credits)
  
## OverView ##
My project is called hiSTOREy. It is an online store for historic artifacts. 
The site owner can upload an image of their artifact for customers to see and to buy. Site owner will also provide details such as the price, the name, the short description and also some historic events that the product has lived through.

Users can search for a product that they want out of all the existing ones.What makes this site different is that customers can create their own profiles, and keep track of their purchases. 
This is ideal for history enthusiasts, and also the general public.

## UX ##
This website is not just for a history enthusiast, but for the general public who have an interest in history. Although it is aimed at those who have more knowledge about historic artifacts, the simple design and UI makes it accessible to anyone curious to look at it.

The UI is very simple. The colours are light, and i chose to use the bootstrap 'error' yellow to use as the background for the footer and the header. These stick out compared to the pale background. All items are displayed using cards, which are easy on the eye. The font is a google font that is slightly different but also very legible.

The general flow of the site is very simple. The user will visit the site, and whether or not they are logged in they can browse through the products. The products page is paginated so that not too many products show up at once.

Once the user tries to add something to their card, the validation will apply to check if the user is a member, and if not, prompt them to create an account/log in immediately. 
As a user I want to
- Search for products based on my criteria
- View detailed information about the product
- Create my own profile on the website
- Buy a product
- Hold a product in my basket
- Make a successful purchase
- Make a comment on the product

Wireframes are in the wireframes directory

## Features ##
1. Homepage - this page is the landing page for the user. It contains all the products on the site. This is paginated, so only top 5 products appear. 

The design is simple, with a row for each product. This contains the image and the description of the product. 
When the user clicks the quick add icon, a slide up appears where the user can choose to add the item to cart.

2. Cart - The user has a cart they can view. This contains all the items the user has added to cart. It also has the ability to modify the amount of objects they want.

3. Checkout - This is where the user can put in their credit card details and make the purchase
Account - This is where the user accounts are stored. The user can click on the ‘Profile’ button on the nav bar to view their profile. This contains information about the user such as the name and email address. In an ideal world this would contain all previous orders made by the users and the orders that the site are currently processing for the user. This would contain details such as the status of the process, and information such as the price and date of purchase.
 
 4. Products - The home page is a list of all the products available on the site. When a user clicks to See More details about a product, it goes on to a separate page where more details are available. The customer can add an item to the cart from this part. A user can also view all comments related to the product from here, as well as adding their own
 
 5. Search - From the homepage a user can search for products. This searches via the product name.
 
 6. Pagination - The top 5 products are shown, and the user can skip on to the next set of pages if needs be. This jsut means there is not too much information on the screen at once.
 
 7 Comments - Users may comment on products. This is to help other users when purchasing. User must fill out a form of username, comment, rating. When a user visits a products specific page they can view comments on that particular producr, and can see who wrote them. They have the oppertunity to comment themselves also.
 
 8 Orders - when a user makes an order it is saved in the backend. It is associated with that user based on who is logged in. So a user will have an order history which can be viewed from their Profile.
  
 9 Profile - A user can see their information from the profile page. This has basic information such as the info the user used to sign up with like name and email. Users may also view their order history. This is a table that appears containing the dates of the orders, and who made the purchase as well as the full name on the credit card that made the purchase.
 
## Features Left to Implement ##
Allowing a user to bid on the products - the idea behind this is to add the functionality onto the ‘quick add’ menu on the products page. The user would have the option to purchase the product immediately for a high price or start bidding. 

## Technologies Used ##
- jQuery - dom manipulation
- Stripe API - payments
- Javascript - dom manipulation
- Materialize - User Interface for consistency
- Python - to do business logic
- Django - web framework
- Travis CI - for contnuous integration, automated on each push to master
- Postgres db - database for storing all the objects
- Whitenoise - for storing static files on Heroku

## Testing ##
Chrome Dev tools:
I tested the different screen sizes to make sure they display correctly. I also used a Samsung phone.

Manual Testing:

- Adding a new product from the Django backend, make sure it is fully visible on the front end
- Adding products to basket, to see that the notificiation button appears beside the cart, and also so that when a user visits their cart the item is there
- purchasing an item so that it adds to basket, and the user can then purchase the items in the basket
- Exceeding max number which is 100
- Adding 0 products and trying to purchase
- Creating products that do not pass validation, al forms have  some form of validation on them
- Using int instead of string
- Using string instead of int
- Using over 2 decimal places
- Using over 254 characters
- Clicking on every link on the page, ensuring there are no dead links and that each one works as it should
- Adding comments
- Adding comments to the same products, using different accounts
- Running code through the html validator

Automated Testing:

Ideally all these tests should have been created in python, and run on the CI build. Ideally using a test framework such as jasmin.

## Deployment ##
My project is deployed on Heroku.
https://ecomm-store.herokuapp.com/
 It is configured that after every CI build, it is re published to heroku. All of my configuration values are stored here. These include my secret keys, and api keys for stripe. 
 
Those vars are stored in a file that is included in gitignore in order to run locally.
It is using Travis Continuous Integration. This is to ensure that with every push the build passes.
Heroku Deployment
Instructions :

Create a requirements.txt file using the terminal command pip freeze > requirements.txt.

Create a Procfile with the terminal command echo web: python app.py > Procfile.

On Heroku create a new app, "Deploy" > "Deployment method" > GitHub.

Link to your Github repository you want to use

To look for your configuration variables in Heroku, click on "Settings" > "Reveal Config Vars".

Set your configuration variables:

Key	Value
HOSTNAME	
SECRET_KEY	
STRIPE_CANCEL_URL	
STRIPE_PUBLISHABLE	
STRIPE_SECRET
STRIPE_SUCCESS_URL	


In your heroku dashboard, in Deploy, choose whether you want to deploy after a Continuous Integration build has passed. I selected true as i have Travis CI running.

Click View App

For running this code locally:

1. Go to the repository main page
2. Select Clone with HTTPS
3. Copy link
4. Open git bash in desired directory
5. type git clone and the URL from step 2
6. Press Enter

## Credits ##
 
Media
The photos used in this site were obtained from google and materialize
Acknowledgements
A lot of this project is a combination of the CodeInstitute projects ‘Blog all about it’ and ‘Ecommerce app’. I have adapted my own changes to it but fully understand that I have taken some direct pieces from other projects.

