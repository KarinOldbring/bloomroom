# BloomRoom

[Main README.md file](/README.md)

[View live project here](https://bloomroom.herokuapp.com/)

[View GitHub repository](https://github.com/KarinOldbring/bloomroom)

***
## Contents
* [Test User Stories](#Test-user-stories)
* [Manual Testing](#Manual-testing)
* [Automated Testing](#Automated-testing)
    * [Code Validation](#Code-validation)
    * [Browser Validation](#Browser-validation)
* [User Testing](#User-testing)


***

## **Test User Stories**

1. As a site user I can search the site to easily find what I am looking for.
    * Any site user, logged in or not, can user the Search functionality in the top right corner of the site. When seraching for for example a categoriy all products matching that search criteria are displayed. The site also shows how many matching items are found for that specific search criteria and has a button to easily navigate back to All plants. 
2. As a site user I can view the products of the site so that I can see what the store offers.
    * Any site user, logged in or not, can view all products on the site. The user can either click on the Plants link in the nav-bar, or click the "Shop Here" link on the middle of the home page. This will direct the user to get a full overview of the products. 

3. As a site user I can view a specific product so that I will get more detailed information. 
    * Any site user, logged in or not, can click either the image or the name of a certain product to get redirected to a detailed product view. From here the user gets all information about that specific item, such as name, price, description, category, season and the product image. 

4. As a site user I can categorize the products so that I can filter the results.
    * Any site user, logged in or not, can categorize the products to filter the product view. This can be done either directly from the dropdown link in the nav-bar where all the categories are displayed or from the All Products view, where there are buttons linking to all the different categories. 

5. As a site user I can receive real time notifications to improve my user experience.
    * When I site user interacts with the page, adds an item to the shopping bag, edits their user profile or makes in invalid input in a form for example, a message is displayed to guide the user. There are success, alert, error and warning messages depending on the action taken. 

6. As a site user I can create a user account. 
    * Any site user can go to My Account in the nav-bar and Register an account. The registration requires a unique email-address and a unique username. If either the email-address or the username already has been used to register an account the site user will be notified and asked to choose another. 

7. As a site user I can make purchases on the site. 
    * Any site user, logged in or not, can make purchases on the site. If the user is logged in and has saved their shipping information they only need to enter Full Name and payment information. If the uer is not a registered user they will have to fill out name, shipping information and payment information. The user can then proceed to complete the order and purchase is made. 

8. As a site user I can view my shopping bag so that I have complete overview of my purchase.
    * Any site user, logged in or not, can by clicking the shopping bag icon in the nav-bar get a full overview of their Shopping bag. If the Shopping bag is empty, that is stated and clicking the "Keep Shopping" back easily directs you back to the All products page. If there are items in the bag, the user will see the image, name, price, quantity and total cost and also has the option to change quantity and/or delete items. From here the user can either keep shopping or proceed to secure checkout. 

9.  As a site user I can view and update my account, so that I can manage my account.
    * Any logged in registered user can view their Profile. By clicking My Account and choosing My Profile in the nav-bar you are directed to the Profile view. Here the user is greeted using their username ("Welcome Username") and their Profile information is presented. From here the user can update and or delete information that has previously been saved. A note at the bottom of the page instructs the user how to go about if they wish to entirely delete their profile. In the My Profile view the user also gets an overview of previous purchases. By clicking the Order number the user is directed to the purchase specification. 

10. As a site user I can sign up for a newsletter so that I can take part of news and offers.

11. As a site user I can receive emails regarding my purchases.

12. As a site owner I can log in to view the current products and their specifics on the site.

13. As a site owner I can add new products to the site.

14. As a site owner I can update products on the site.

15. As a site owner I can delete products on the site.

16. As a site owner I can send confirmation and informational emails to my customers.

[Back to content](#contents)

## **Manual-testing

[Back to content](#contents)

## **Automated-testing**

[Back to content](#contents)

#### **Code-validation**

The [W3C Markup Validator](https://validator.w3.org/) service was used to validate the HTML and CSS code used. The [PEP8 Python Validator](http://pep8online.com/) was used to validate the Python code. 

***Results:

* HTML Validation

* CSS Validation

* Python Validation

Files tested:
*Bag*
* urls.py
* contexts.py
* views.py

*Bloomroom*
* settings.py
* urls.py
* wsgi.py

*Checkout*
* admin.py
* apps.py
* forms.py
* models.py
* signals.py
* urls.py
* views.py
* webhookhandler.py
* webhooks.py

*Home*
* urls.py
* views.py

*Products*
* admin.py
* forms.py
* models.py
* urls.py
* views.py

*Profiles*
* forms.py
* models.py
* urls.py
* views.py

*env.py*

#### **Browser-validation**

## **User-testing**

[Back to content](#contents)