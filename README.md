[![Build Status](https://travis-ci.org/laurGeo/milestone-4-ecomm-site.svg?branch=master)](https://travis-ci.org/laurGeo/milestone-4-ecomm-site)
# Full Stack Frameworks Project with Django #
My project is called hiSTOREy. It is an online store for historic artifacts. 
The site owner can upload an image of their artifact for customers to see and to buy. Site owner will also provide details such as the price, the name, the short description and also some historic events that the product has lived through.

Users can search for a product that they want out of all the existing ones.What makes this site different is that customers can create their own profiles, and keep track of their purchases. 
This is ideal for history enthusiasts, and also the general public.

## UX ##
This website is not just for a history enthusiast, but for the general public who have an interest in history. Although it is aimed at those who have more knowledge about historic artifacts, the simple design and UI makes it accessible to anyone curious to look at it.

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
Homepage - this page is the landing page for the user. It contains all the products on the site. This is paginated, so only top 5 products appear. 

The design is simple, with a row for each product. This contains the image and the description of the product. 
When the user clicks the quick add icon, a slide up appears where the user can choose to add the item to cart.

Cart - The user has a cart they can view. This contains all the items the user has added to cart. It also has the ability to modify the amount of objects they want.

Checkout - This is where the user can put in their credit card details and make the purchase
Account - This is where the user accounts are stored. The user can click on the ‘Profile’ button on the nav bar to view their profile. This contains information about the user such as the name and email address. In an ideal world this would contain all previous orders made by the users and the orders that the site are currently processing for the user. This would contain details such as the status of the process, and information such as the price and date of purchase.
 
## Bugs (or features?..) ##
Admittedly, my purchasing using the Stripe API does not work. This is a bug that has occurred many times throughout the Slack group but no specific result has worked. Suggested solutions included moving the stripe js file, re installing stripe, upgrading stripe, different test data.
I believe it may be something to do with the combination of the Django/Stripe and Python versions causing something funny to happen. The issue is that the hidden field that is stripe id is not showing up. 
Now, whitenoise is not co operating

My comments do not currently work. If a user tries to add a comment it gives an error message.
 
## Existing Features ##
 
## Features Left to Implement ##
Allowing a user to bid on the products - the idea behind this is to add the functionality onto the ‘quick add’ menu on the products page. The user would have the option to purchase the product immediately for a high price or start bidding. 

Allowing users to view their previous purchases. This would be added onto the users profile. This could involve adding a new db entry for each purchase made. This could have a primary key of user id, which is how it would link to the customer.

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
I tested the different screen sizes to make sure they display correctly

Manual Testing:

- Adding a new product from the Django backend
- Adding products to basket
- Exceeding max number which is 100
- Adding 0 products
- Creating products that do not pass validation
- Using int instead of string
- Using string instead of int
- Using over 2 decimal places
- Using over 254 characters
- Clicking on every link on the page

Automatic Testing:

Ideally all these tests should have been created in python, and run on the CI build. Ideally using a test framework such as jasmin.

## Deployment ##
My project is deployed on Heroku.
https://ecomm-store.herokuapp.com/
 It is configured that after every CI build, it is re published to heroku. All of my configuration values are stored here. These include my secret keys, and api keys for stripe. 
 
Those vars are stored in a file that is included in gitignore in order to run locally.
It is using Travis Continuous Integration. This is to ensure that with every push the build passes.
## Credits ##
 
Media
The photos used in this site were obtained from google and materialize
Acknowledgements
A lot of this project is a combination of the CodeInstitute projects ‘Blog all about it’ and ‘Ecommerce app’. I have adapted my own changes to it but fully understand that I have taken some direct pieces from other projects.

