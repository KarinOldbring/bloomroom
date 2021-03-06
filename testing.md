# BloomRoom

[Main README.md file](/README.md)

[View live project here](https://bloomroom.herokuapp.com/)

[View GitHub repository](https://github.com/KarinOldbring/bloomroom)

***
## Contents
* [Test User Stories](#Test-user-stories)
* [Manual Testing](#Manual-testing)
* [Code Validation](#Code-validation)
    * [HTML](#HTML)
    * [CSS](#CSS)
    * [Python](#Python)
    * [Javascript](#Javascript)
* [Lighthouse](#Lighthouse)
* [Browser Validation](#Browser-validation)
* [User Testing](#User-testing)


***

## **Test User Stories**

1. As a site user I can search the site to easily find what I am looking for.
    * Any site user, logged in or not, can use the Search functionality in the top right corner of the site. When searching for for example a categoriy all products matching that search criteria are displayed. The site also shows how many matching items are found for that specific search criteria and has a button to easily navigate back to the products page; All plants. 
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
    * Any site user, logged in or not, can make purchases on the site. If the user is logged in and has saved their shipping information they only need to enter Full Name and payment information. If the user is not a registered user they will have to fill out name, shipping information and payment information. The user can then proceed to complete the order and the purchase is made. 

8. As a site user I can view my shopping bag so that I have complete overview of my purchase.
    * Any site user, logged in or not, can by clicking the shopping bag icon in the nav-bar get a full overview of their Shopping bag. If the Shopping bag is empty, that is stated and clicking the "Keep Shopping" back easily directs you back to the All products page. If there are items in the bag, the user will see the image, name, price, quantity and total cost and also has the option to change quantity and/or delete items. From here the user can either keep shopping or proceed to secure checkout. 

9.  As a site user I can view and update my account, so that I can manage my account.
    * Any logged in registered user can view their Profile. By clicking My Account and choosing My Profile in the nav-bar you are directed to the Profile view. Here the user is greeted by their username ("Welcome Username") and their Profile information is presented. From here the user can update and or delete information that has previously been saved. A note at the bottom of the page instructs the user how to go about if they wish to entirely delete their profile. In the My Profile view the user also gets an overview of previous purchases. By clicking the Order number the user is directed to the purchase specification. 

10. As a site user I can sign up for a newsletter so that I can take part of news and offers.
    * Any site user, logged in or not, can sign up for a Newsletter subscription. By submitting their email address in the bottom right corner in the footer they are automatically signed up. After submitting an email address an alert shows up thanking the user for subscribing. 

11. As a site user I can receive emails regarding my purchases.
    * Any site user, logged in or not, receives a confirmation email after making a purchase.

12. As a site owner I can log in to view the current products and their specifics on the site.
    * The site owner can easily access the product specifications on the site. When logged in the site owner has the opportunity to edit and delete items on the site by clicking the Edit or Delete buttons beneath each product. 

13. As a site owner I can add new products to the site.
    * The site owner can by clicking My Account in the nav-bar and choose Product Management add new items to the site. From there the site owner can fill out all fields necessary and upload an image. By clicking "Add Product" the item is added to the product list. 

14. As a site owner I can update products on the site.
    * The site owner can by clicking the Edit button under a specific product access the "Edit Product" view. The site owner will recognize this view from the Add Product view, only here the previous information is there and can be edited. The site owner can update all text and also change image. 

15. As a site owner I can delete products on the site.
    * When the site owner is logged in there is a "Delete" button presented underneath each product. By clicking it the item is automatically removed from the products list. 

16. As a site owner I can send confirmation and informational emails to my customers.
    * When a user makes a purchase a confirmation email is automatically sent to the customer. Through the Mailchimp service the site owner has access to all the site users who have signed up for the Newsletter subscription and can from there send emails. 

[Back to content](#contents)

## **Manual Testing**

### Header

#### Navigation Bar (Nav-Bar)

* Expected Outcome: The navigation bar should be visible on every page of the site. If page is rendered on smaller screens the navigation bar should toggle for better user experience. 
* Test: Visit every page of the site to check if navigation bar is visible. View the navigation bar on different size screens to check responsiveness of navigation bar and toggle function. 
* Result: The navigation bar is visible on every page of the site. When viewed on smaller screens the links are toggled for better user experience. 
* Verdict: Code functions as intented.

#### Logo

* Expected Outcome: When clicking the logo, the user should be redirected to home page.
* Test: I tried clicking the logo from all different pages of the site, both as logged in user and not. 
* Result: Every time I clicked the logo I was redirected to home page.
* Verdict: Code functions as intented.

#### Home Link

* Expected Outcome: When clicking the Home link, the user should be redirected to the Home page.
* Test: I tried clicking the Home link from all different pages on the site, both as logged in user and not.
* Result: Every time I clicked the Home link I was redirected to the home page. 
* Verdict: Code functions as intented.

#### About Link

* Expected Outcome: When clicking the About link, the user should be redirected to the About page.
* Test: I tried clicking the About link from all different pages on the site, both as logged in user and not.
* Result: Every time I clicked the About link I was redirected to the About page.
* Verdict: Code functions as intented.

##### Plants Link

* Expected Outcome: When clicking the Plants link a dropdown menu should appear, displaying the different categories. 
* Test: I tried clicking the Plants link from all different pages on the site, both as logged in user and not.
* Result: Every time I clicked the Plants link the dropdown menu apperaed. 
* Verdict: Code functions as intended. 

##### Plants Link - All Plants

* Expected Outcome: When choosing All Plants from the Plants dropdown menu, you should be redirected to the All Plants overview. 
* Test: I tried clicking the All Plants link from all different pages on the site, both as logged in user and not.
* Result: Every time I clicked the All Plants link I was redirected to the All Plants overview. 
* Verdict: Code functions as intended. 


##### Plants Link - Green Plants

* Expected Outcome: When choosing Green Plants from the Plants dropdown menu, you should be redirected to the Green Plants overview. 
* Test: I tried clicking the Green Plants link from all different pages on the site, both as logged in user and not.
* Result: Every time I clicked the Green Plants link I was redirected to the Green Plants overview. 
* Verdict: Code functions as intended.  

##### Plants Link - Blooming Plants

* Expected Outcome: When choosing Blooming Plants from the Plants dropdown menu, you should be redirected to the Blooming Plants overview. 
* Test: I tried clicking the Blooming Plants link from all different pages on the site, both as logged in user and not.
* Result: Every time I clicked the Blooming Plants link I was redirected to the Blooming Plants overview. 
* Verdict: Code functions as intended. 

##### Plants Link - Pet Friendly Plants

* Expected Outcome: When choosing Pet Friendly Plants from the Plants dropdown menu, you should be redirected to the Pet Friendly Plants overview. 
* Test: I tried clicking the Pet Friendly Plants link from all different pages on the site, both as logged in user and not.
* Result: Every time I clicked the Pet Friendly Plants link I was redirected to the Pet Friendly Plants overview. 
* Verdict: Code functions as intended. 

##### Plants Link - Larger Plants

* Expected Outcome: When choosing Larger Plants from the Plants dropdown menu, you should be redirected to the Larger Plants overview. 
* Test: I tried clicking the Larger Plants link from all different pages on the site, both as logged in user and not.
* Result: Every time I clicked the Larger Plants link I was redirected to the Larger Plants overview. 
* Verdict: Code functions as intended. 

##### Plants Link - Smaller Plants

* Expected Outcome: When choosing Smaller Plants from the Plants dropdown menu, you should be redirected to the Smaller Plants overview. 
* Test: I tried clicking the Smaller Plants link from all different pages on the site, both as logged in user and not.
* Result: Every time I clicked the Smaller Plants link I was redirected to the Smaller Plants overview. 
* Verdict: Code functions as intended. 

##### My Account Link

* Expected Outcome: When clicking the My Account link a dropdown menu should appear, displaying different options, depending on wether you are logged in or not.
* Test: I clicked the My Account link both when logged in and when not logged in. 
* Result: When clicking the My Account link when logged in the options My Profile and Log out appeared. When clicking the link when not logged in the options Register and Log In appeared. 
* Verdict: Code functions as intended. 


##### My Account Link - Site Owner

* Expected Outcome: When clicking the My Account link logged in as site owner an option of Product Management should appear, as well as My Profile and Log Out. 
* Test: Click the My Account link when logged in as superuser. 
* Result: When clicking the My Account link as a logged in superuser/site owner the option Product Management appears, as well as My Profile and Log Out. 
* Verdict: Code functions as intended.

#### Login

* Expected Outcome: When choosing Login from the My Account menu, you should be redirected to the Sign In page. 
* Test: Choose Login from the My account menu. 
* Result: When choosing Login from the My Account menu I was redirected to the Sign In page. 
* Verdict: Code functions as intended. 

#### Register

* Expected Outcome: When choosing Register from the My Account menu, you should be redirected to the Sign Up page. 
* Test: Choose Register from My Account menu. 
* Result: When choosing Register from the My Account menu I was redirected to the Sign Up Page. 
* Verdict: Code functions as intended. 

#### My Profile 

* Expected Outcome: When choosing My Profile from the My Account link, the user should be redirected to the My Profiles page. 
* Test: Clicked the My Profile option in the My Account link. 
* Result: When choosing My Profile I was redirected to the My Profile page. 
* Verdict: Code functions as intended. 

#### Product Management

* Expected Outcome: When choosing Product Management from the My Account link, the site owner should be redirected to the Product Management page. 
* Test: Clicked the Product Management option in the My Account link. 
* Result: When choosing Product Management I was redirected to the Product Management page.
* Verdict: Code functions as intended. 

#### Shopping Bag

* Expected Outcome: When clicking the Shopping Bag icon the user should be redirected to the Shopping Bag. If there are items in the bag these should be displayed, if not there should be a message stating that it is empty and a button to take the user back to the All Products view. 
* Test: Clicking the Shopping Bag, both when items are in the bag and not. 
* Result: Clicking the Shopping Bag after items have been selected takes you to the Shopping Bag where the items and information regarding price etc are displayed. Clicking the Shopping Bag when no items have been selected takes you to the Shopping Bag and a message stating that the bag is empty. The button taking you back to the shopping site is also presented. 
* Verdict: Code functions as intended. 

#### Search Field

* Expected Outcome: When entering a search criteria in the Search Field the items matching should be displayed. The number of matches should also be presented. If no items match the search criteria it should be stated that there are no products found when searching for that specific criteria. 
* Test: Entered different search criteria to test search functionality. 
* Result: When searching for the word "pet" for example, all products from the "Pet Friendly" category are presented. It is also stated that there are five items matching the search criteria. If I searched for a word in Swedish, for example Krukv??xt, the Swedish word for household plant, I got a message stating that there are no products matching. 
* Verdict: Code functions as intended. Although, as mentioned in further length in the Bugs section in the Readme, the search functionality operates a bit too well since it also includes hits where part of the word entered is present. For example if you search "car" you will get a match where the word "care" is in the description. 

### Footer

#### Footer

* Expected Outcome: The footer should be visible on all pages of the site and always be placed on the bottom of the page. 
* Test: Visit every page of the site to check if footer is visible. 
* Result: The footer is visible on every page of the site. 
* Verdict: Code functions as intented.

#### Footer Social Media Links

* Expected Outcome: The icons in the footer linking to the social media accounts are supposed to be opened up in new tabs when clicked. 
* Test: Click the social media icons in footer. 
* Result: When clicking the icons the social media is opened up in a new tab. 
* Verdict: Code functions as intented.

#### Footer Mid Section

* Expected Outcome: The mid section of the Footer, showing the logo and email address, are supposed to be visible on smaller screens and wider. In the mid section there is the BloomRoom logo, which when clicked takes the user to the homepage and also BloomRooms email address. If you are using a device where you are logged in to your mail, a new mail with BloomRoom as the receiver will open up. 
* Test: Looking at the mid section on different size screens to make sure that it is only visible on smaller screens and larger. Click both the logo and the email address to check that you are redirected as expected. 
* Result: When viewing the site on smaller deivces the mid section is hidden. When dlicking the logo you are redirected to the home page. If you are logged in to your own email on your device when clicking the email address a new email opens up with BloomRoom as the receiver. 
* Verdict: Code functions as intended. 

#### Newsletter Subscription

* Expected Outcome: When entering an email address the user should be notified that the action was successfull and the email address should be visible in the site owner Mailchimp account. 
* Test: Enter an email address to see if I get a verification that the action was successfull and tried entering an invalid email address. 
* Result: When entering an email address the user is notified that the action was successfull and the email address is added to the site owners Mailchimp account. If entering an invalid email address, for example without an @, you are asked to enter a valid email address. 
* Verdict: Code functions as intended. 

### Home Page

#### Home Page Welcome text 

* Expected Outcome: When viewing the Home page there is a welcome text with a link named "Shop Here" that should link to the All products view. 
* Test: Click the "Shop Here" link to see if I get redirected to the All Products view. 
* Result: When clicking the "Shop Here" link I am being redirected to the All Products view. 
* Verdict: Code functions as intended. 

#### Delivery Banner

* Expected Outcome: On the Home Page there is a rolling Delivery Banner stating the Free Deilvery terms. On x-small screens, the banner should not be rolling but be still for better UX. 
* Test: View the Delivery Banner on different size screens. 
* Result: When using small or larger screens the Delivery Banner is rolling, on extra small screens it is not rolling but still. 
* Verdict: Code functions as intended. 

### Products

#### All Products view

* Expected Outcome: When visiting the All Products view an overview of every product should be presented stating an image, name and price. There should also be clickable buttons that can take you to each category. 
* Test: Visit the All Products page and test the different category buttons.
* Result: All products are displayed with the right information showing. When clicking the individual category buttons you are redirected to that specific category. 
* Verdict: Code functions as intended. 

#### Sort By - Function

* Expected Outcome: When visiting either the All Products page or a specific category the user can choose to sort the products either by ascending price, descending price or name. 
* Test: Visit the All Products page and each category to try the Sort By function. 
* Result: When viewing All Products or a selected category, the Sort By function operates as intented. If the user is watching products rendering through a search result and then chooses to use the Sort By function, all products on the page are then displayed. 
* Verdict: Code functions as intended on all views accept for search result. This is mentioned in the Bugs section in the Readme. 

#### Product Detail

* Expected Outcome: When clicking either a product image or the name of a product you should be redirected to the product detail page. Here you should see all specifics about the product and also have the ablitity to add product to Shopping Bag and if so choose quantity. There should also be a "Keep Shopping" button that takes the user back to the All Products page. 
* Test: Click the different products to check if I am being redirected and all information is displayed including Add to Bag option. I also tried to go beyond the allowed quantity scope of 1-99, by using the icons or typing in number manually and typing in other caracters than digits. 
* Result: When clicking the product the user can see that items specifications and is given the option to add the item to the Shopping Bag including choosing quantity. If you try to enter more a quantity beyond the allowed scope (0-99) you are notified that the number is invalid. If I tried entering an invalid input such as letters I was instructed to enter a valid input. The "Keep Shopping button is also there and when clicked the user is redirected to the All Products page. 
* Verdict: Code functions as intended. 

### My Account

#### Register

* Expected Outcome: A site user that is not logged in to the site should be presented with the option of signing up for an account. To sign up for an account the user needs to enter a unique email address and username, as well as a password twice. If the email address or the username already has been used to sign up for an account the user should be encouraged to choose a new one. 
* Test: Try signing up for a new account using both new and already used emails and usernames or trying to leave out required information. 
* Result: When trying to sign up for an account using already used email address and/or username I am enouraged to choose a different one. When choosing a entering a new email address and username the sign up functions. Leaving input fields blank also throws an error. 
* Verdict: Code functions as intended. 

#### Login

* Expected Outcome: A site user that is not logged in and already has an account can choose to log in using either their username or email address. If the user has forgotten their password they can request to have a password reset by clicking the "Reset Password" button and an email with a link should be posted to their email. 
* Test: Try entering the correct login credentials and password, try entering wrong login credentials and/or password. Click "Reset Password" to receive reset link. 
* Result: When entering incorrect login credentials and/or password an error is thrown asking for the right input. If the correct information is given the signing in proceeds as expected. The reset link is being sent out as expected and when following the steps a new password can be set. As an additional service to the user the Username is stated in the reset password email, in case the user forgot it. 
* Verdict: Code functions as intended. 

#### Log Out

* Expected Outcome: A logged in user should be able to log out from their account and before the logout is processed the user should be asked to confirm that they wish to log out. 
* Test: When logged in try to log out. 
* Result: When clicking log out the user is being redirected to a Log Out page where the user can either confirm that they wish to log out or be redirected back to the Home page. 
* Verdict: Code functions as intended. 

### Shopping Bag & Checkout

#### Shopping Bag 

* Expected Outcome: The shopping bag aims for the user to see all items in the bag. The bag should show product info, bag total, delivery cost and grand total. Apart from that the user should be given the opportunity to change quantity of selected items or remove them entirely. From here the user should be given the option to either proceed to Secure Checkout or Keep Shopping. 
* Test: By adding items to the bag, I tried changing quantity and deleting the item entirely. I also tried to go beyond the allowed quantity scope of 1-99, by using the icons or typing in number manually and typing in other caracters than digits. 
* Result: I was able to adjust quantity and delete items completely. When doing so the total cost was adjusted. From here I could choose to Keep Shopping or go to Secure Checkout. If I tried going beyond the allowed scope I was instructed to pick a number between 1-99, or to enter a valid input if I tried entering invalid characters. 
* Verdict: Code functions as intended. 

#### Checkout

* Expected Outcome: When the user is done shopping they should be able to go to Secure Checkout to complete the purchase. From there they are supposed to fill in the missing information, if information has been saved from before it should be already filled in. After entering the necessary information, the user should be notified and an order confirmation be presented. The user should also receive the order confirmation by email. 
* Test: Make a purchase, both as previously logged in user or not. Fill out necessary information to complete the purchase and verify that email has been sent.  
* Result: When making a purchase as previously logged in user the saved information was automatically filled in. If completing the purchase when not logged in the user is informed that they can Log in or Register if they wish to save their information for future purchases. After the form is completed, the user is presented with an order confirmation. The same confirmation is also sent to the users email. 
* Verdict: Code functions as intended. 

[Back to content](#contents)

## **Code Validation**

#### **HTML**

The [W3C Markup Validator](https://validator.w3.org/) service was used to validate the HTML.

***Results:***

All files tested passed with no errors. 

Pages tested:

- Home Page
- About Page
- All Plants
    - Green Plants
    - Blooming Plants
    - Pet Friendly
    - Larger Plants
    - Smaller Plants
- My Account
    - Register
    - Sign In
    - My Profile
    - Log Out
- Shopping Bag
    - Checkout
    - Checkout Success

#### **CSS**

The [W3C Markup Validator](https://validator.w3.org/) service was used to validate the CSS.

All files tested passed with no errors. 

Files tested:

- checkout.css
- style.css

#### **Python**

The [PEP8 Python Validator](http://pep8online.com/) was used to validate the Python code. 
All files tested passed with no errors except for line 51 in Checkout models.py since it was too long. I tried breaking that line in many different ways but all my attempts ended with the code not functioning as expected hence I left it with a #noqa at the end of the line.  

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

#### **JavaScript**

The JavaScript was tested using [https://jshint.com/](https://jshint.com/). The files returned no errors except for the Stripe Javascript file that returned an error saying there is an undefined variable, Stripe. This is due to core functionality reffering to Stripe. Copy of the code was taken from older version Stripe pages that were referenced in Butique Ado.

Files tested: 

- stripe_elements.js
- quantity_input_script.html
- quantity_input_script_bag.html

[Back to content](#contents)

## **Lighthouse**

The site has been tested with Lighthouse. Performance could be further improved by analyzing the file types of images. Also since I use a free subscription for the Heroku app it starts really slowly which can affect the performance score. 

![Lighthouse](/static/site_images/lighthouse.png)

[Back to content](#contents)

## **Browser validation**

The site has been tested using the following browsers:

- Chrome
- Edge
- Firefox
- Safari

[Back to content](#contents)

## **User testing**

The site has been tested regularly during development. After the site was completed the site has been tested by several users to make sure functionality and good user experience is maintained. The site has also been tested on devices with different screen sizes and on both Android and Apple mobile phones. 

[Back to content](#contents)