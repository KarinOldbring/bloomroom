# **BloomRoom**

![BloomRoom](/static/site_images/amiresponsive.png)

[View the live project here](https://bloomroom.herokuapp.com/)

## Contents
* **[Introduction](#Introduction)**
    * [Business Plan](#Business-Plan)
    * [Planning Stage](#Planning-Stage)
    * [Project Goals](#Project-Goals)
    * [User Stories](#User-Stories)
    * [Design Goals](#Design-Goals)
    * [Design Choices](#Design-Choices)
        * Font
        * Color Scheme
        * Logo BloomRoom
        * Images
    * [Wireframes](#Wireframes)

* **[Features](#Features)**
    * [Existing Features](#Existing-Features)
    * [General Features](#General-Features)
    * [Future Features](#Future-Features)

* **[SEO Implementation](#SEO-Implementation)**

* **[Marketing Techniques](#Marketing-Techniques)**

* **[Testing](#Testing)**

* **[Bugs](#Bugs)**

* **[Technology Used](#Technology-Used)**
    * [Main Languages Used](#Main-Languages-Used)
    * [Frameworks, Libraries and Programs Used](#Frameworks-Libraries-and_Programs-Used)
    

* **[Deployment](#Deployment)**
    * [Deploying on Heroku](#Deploying-on-Heroku)

* **Credits** 
    * [Media](#Media)
    * [Code](#Code)
    * [Acknowledgements](#Acknowledgements)


# **BloomRoom**

## **Introduction**

BloomRoom is a website where you can buy plants and have them delivered to your home! BloomRoom offers high quality plants and ship all over Europe. Users can create their own profiles so that their shipping and billing information is saved. As a customer you can also see your previous orders and update or delete your profile. 
Orders over 40$ have free delivery and users can easily see when they have reached the free shipping limit. Products can be added to the cart and can be purchased using card payment. Order confirmation is sent to the email address provided by the customer. Users can also stay updated with all the latest and exclusive offers by following BloomRooms Facebook page and by subscribing to the monthly newsletter.

### **Business Plan**

The fact that more and more trade is conducted online hardly comes as news to anyone. Especially since the pandemic more people wish to do their shopping from home to avoid crowded stores. Also, with more flexible working hours it's become more important to be able to do your shopping whenever it suits you, without having to adjust to opening hours. The pandemic was turbulent in many ways but for the flower/plant industry it has been blooming to say the least, and there's no sign of it slowing down! Lots of people staying home more than usual made them pay more attention to their home environment and wanting to invest more in their homes. Even though a lot of our everyday shopping has been online since many years the plant industry is falling behind. There are not that many online plant shops and that's why there certainly is room for a new actor! 
The business model for this store would be a B2C (Business to Customer) model, as the business would be selling products directly from ourselves to the customer. The strategy is to offer popular, high quality plants and full support for our costumers. Customers can call or email to get help and advice regarding already purchased products or if they wish to have recommendations regarding suitable plants for their homes. A userfriendly website, easy to navigate with secure and fast checkout will make our users loyal customers! 

[Back to content](#contents)

### **Planning Stage**

The initial step in this project was to create a visual general idea of what the page should look like. Although it can be fun to get creative and come up with lots of ideas when it comes to designing a webpage as a user it is very convenient to feel "at home" even the first time you visit the site. With that said I wanted to create a unique looking site but I wanted the common features to be presented and placed in conventional spots on the page, for example the search bar should be on top of the page, always easy to find. 
Early on I also created wireframes for the site, to have a better idea of what I was aiming for. I also created all my user stories to make sure I applied all functionalities I wanted. 
One of many things I take away from this project is that you can't plan too much. Looking back I should have spent more time planning to be able to structure my work better and probably some time as well. With that said, overall I stuck to the inital plan regarding the project. 

[Back to content](#contents)

### **Project Goals**

The app is designed as an e-commerce application that encourages users to make purchases. My goal for this project was to create a userfriendly site for people who want to shop plants online, by offering a neat site that is easy to navigate and make purchases. 

[Back to content](#contents)

### **User Stories**

*Agile methodology was used to create user stories.*
*GitHub’s Kanban feature was used to track the progress of user stories.*

| User Story:                                                                                 | User story satisfied through: |
|---------------------------------------------------------------------------------------------|-------------------------------|
| As a site user I can search the site to easily find what I am looking for.                  | Search field                  |
| As a site user I can view the products of the site so that I can see what the store offers. | Products App                  |
| As a site user I can view a specific product so that I will get more detailed information.  | Products App                  |
| As a site user I can categorize the products so that I can filter the results.              | Products App                  |
| As a site user I can receive real time notifications to improve my user experience.         | Django messages               |
| As a site user I can create an account so that I can shop from the store.                   | Profiles App                  |
| As a site user I can view my shopping bag so that I have complete overview of my purchase.  | Bag App                       |
| As a site user I can view and update my account, so that I can manage my account.           | Profiles App                  |
| As a site user I can sign up for a newsletter so that I can take part of news and offers.   | Newsletter signup             |
| As a site user I can receive emails regarding my purchases.                                 | Checkout App                  |
| As a site owner I can log in to view the current products and their specifics on the site.  | Products App                  |
| As a site owner I can add new products to the site.                                         | Products App                  |
| As a site owner I can update products on the site.                                          | Products App                  |
| As a site owner I can delete products on the site.                                          | Products App                  |
| As a site owner I can send confirmation and informational emails to my customers.           | Checkout App                  |

[Back to content](#contents)

### **Design Goals**

Since the site features lots of images of plants and flowers I wanted a very subtle touch, and no sharp background colors that can disturb and take away focus from the product images. It was also  important to me that the site looks good and functions well on all devices, regardless of screen size. One of the main focuses of the site is naturally to sell products, and I believe that keeping the design clean and well structured is a good way to encourage shopping and making the customers wanting to come back. 

### **Design Choices**

* Font

To stay aligned with my aim to present a clean and sophisticated site I chose an elegant font called Bellefair as the Heading font and the classic Source Sans Pro for all other text. 

![Google Font](/static/site_images/font.png)

* Color Scheme

Due to the very nature of the products sold on the site there was no need for lots of extra color and distraction. To keep the site visually appealing I chose to give the header and footer a light grey-blue background, and the logo and front page welcome text was given a very dark green color. Besides these colors I chose to keep the background color white and the text black. 

- Light grey/blue: #e9edf1
- Dark green: #253224
- White: #ffffff
- Black: #000000

![Color Scheme](/static/site_images/color.png)

* Logo BloomRoom

The BloomRoom logo was created using [Canva.com](https://www.canva.com/). Since the logo was too detailed to use as a Favicon I chose to design a special Favicon logo with the letters BR, short for the company name BloomRoom. 

![Logo](/static/site_images/logo.png)

![Favicon-logo](/static/site_images/favicon-logo.png) - Favicon Logo


* Images

All images on the site are taken from [Pexels.com](https://www.pexels.com/). Pexels provides high quality and completely free stock photos licensed under the Pexels license. 

[Back to content](#contents)

## **Wireframes**

Site moc-ups were designed using [Balsamiq Wireframes](https://balsamiq.com/). Since the site is built to be fully responsive one of the design goals was that the user should recognize the different pages and sections of the page no matter what size they were using. 

*Front Page*

![Front Page](/static/site_images/wf-index.png)

The front page is designed to give the user an instant understanding of the purpose of the page. From the home page you can easily access all product, account features, shopping bag etc. 

*About Page*

![About Page](/static/site_images/wf-about.png)

The about page is strictly for informational purpose. Here you can find information about BloomRoom and read about why to choose BloomRoom as your plant supplier. 

*Products*

![Products](/static/site_images/wf-products.png)

When clicking on Products, either from the dropdown menu in the navigation bar or from the Shop Here link on the middle of the home page, you reach the items that are being sold now. Here you get an overview of the products, an image, name and price. 


*Product Detail*

![Product Detail](/static/site_images/wf-product-detail.png)

When viewing all products, the user can easily access the full information regarding a specific product by clicking on the image or the name of the product. This redirects the user to the product detail page, where the user can see all information. From here the user can go back to the products page or choose to add the item in the bag. 

*Sign Up*

![Sign Up](/static/site_images/wf-signup.png)

The is a simple and easy page for users to sign up for an account to be able to shop more easily and keep track of their previous purchases. 

*Sign In*

![Sign In](/static/site_images/wf-signin.png)

From here users who already have an account can sign in to access their profile page. 

*Log Out*

![Log Out](/static/site_images/wf-logout.png)

When logged in users are done on the page they can choose to log out from their user account. 

*Profile*

![Profile](/static/site_images/wf-profile.png)

Logged in users can go to their profile page. Here they can view, update and delete information. On this page the user also gets an overview of previous purchases and has to option to view those in detail. 

*Shopping Bag*

![Shopping Bag](/static/site_images/wf-bag.png)

By clicking on the bag icon in the navigation bar, logged in users can easily access their shopping bag. From here they can see the content in the bag and product information of their selected items. From here they can also update and/or delete items as well as proceed to checkout or keep shopping. 

*Checkout*

![Checkout](/static/site_images/wf-checkout.png)

When the customer is done shopping they can click on the checkout to complete their purchase. From this view they can see either their prefilled information, add new information or update if they wish. The customer is asked to provide billing details such as credit card information to complete the purchase. 

[Back to content](#contents)

## **Information Architecture**

### **Database Models**

***ERD - Entity Relationship Diagram***


*Products*
| Key:       | Name:       | Type:        |
|------------|-------------|--------------|
| ForeignKey | Category    | User Model   |
|            | Sku         | CharField    |
|            | Name        | CharField    |
|            | Price       | DecimalField |
|            | Description | TextField    |
|            | Season      | TextField    |
|            | image_url   | URLField     |
|            | image       | ImageField   |

*Categories*
| Key: | Name:         | Type:     |
|------|---------------|-----------|
|      | name          | CharField |
|      | friendly_name | CharField |

*Order*
| Key:       | Name:                    | Type:         |
|------------|--------------------------|---------------|
|            | order_number             | CharField     |
| ForeignKey | user_profile             | User Model    |
|            | full_name                | CharField     |
|            | email                    | EmailField    |
|            | phone_number             | CharField     |
|            | country                  | CountryField  |
|            | postcode                 | CharField     |
|            | town_or_city             | CharField     |
|            | street_address1          | CharField     |
|            | street_address2          | CharField     |
|            | county                   | CharField     |
|            | additional_shipping_info | TextField     |
|            | date                     | DateTimeField |
|            | delivery_cost            | DecimalField  |
|            | order_total              | DecimalField  |
|            | grand_total              | DecimalField  |
|            | original_bag             | TextField     |
|            | stripe_pid               | CharField     |

*OrderLineItem*
| Key:       | Name:          | Type:        |
|------------|----------------|--------------|
| ForeignKey | order          | User Model   |
| ForeignKey | product        | User Model   |
|            | quantity       | IntegerField |
|            | lineitem_total | DecimalField |

*UserProfile*
| Key:          | Name:           | Type:      |
|---------------|-----------------|------------|
| OneToOneField | User            | User Model |
|               | street_address1 | CharField  |
|               | street_address2 | CharField  |
|               | postcode        | CharField  |
|               | town_or_city    | CharField  |
|               | county          | CharField  |
|               | email           | EmailField |
|               | phone_number    | CharField  |
|               | date            | DateField  |

[Back to content](#contents)

## **Features**

### **Existing Features**

### Header

#### Navigation menu

![Navbar Desktop](/static/site_images/navbar-1.png)     ![Navbar Mobile](/static/site_images/navbar-2.png)

The wide nav-bar is with links and icons is displayed on desktop screens. In the left corner is the BloomRoom logo, which when clicked takes you to the home page. Following the logo are several links to different parts of the site. First there is a link for "Home" whih has the same effect as clicking the logo but I still chose to add it for better UX experience and easier navigation. Next comes a link to the About section (more on that furhter down). After that there are links for the products. A dropdown link where you can either choose to view all products or select a specific category. The last link on the left hand side of the nav-bar is also a dropdown where users can manage their accounts. Depending on whether they are logged in or not, different options are displayed. The right hand side of the nav-bar contain the shopping bag to start with. A widely used icon symbolizing a shopping bag represents the bag under underneath it is the current shopping amount of the bag. Last but not least there is a search field. From here users can easily access items on the site by searching. The nav-bar toggles on smaller, mobile screens. The logo is still in the top left corner, and clicking it will direct you to the home page. The Home, About, Products and My Account links are toggled in to a burger icon, where you easily can access the different pages of the site. Beneath those are the shoppingbag icon and the searchfield. The nav-bar is always visible, no matter which device the user has. 

#### Footer

![Footer Desktop](/static/site_images/footer-1.png)     ![Footer Mobile](/static/site_images/footer-2.png)

The footer contains links to the BloomRoom Facebook page and Instagram. On desktop screens the logo and en email address is also presented, clicking the logo takes you back to the home page. On the right hand side of the footer there is a sign up form for subscribing to the newsletter. The footer looks basically the same on mobile screens, apart from the mid section containing the logo and email address, that are hidden on smaller screens. 

#### Front Page

![Front Page](/static/site_images/frontpage.png)

The home page aims to be eye catching and explanatory at the same time. A sophisticated image showing popular plants greets the user. On the image there is a short description of the page and also a link to get directly to the products. 

#### About Page

![About Page](/static/site_images/about-page.png)

On the About page the users can get more information about BloomRoom and why you should choose BloomRoom as your plant supplier. There is also contact information so that the user can easily can get in touch with BloomRoom. On smaller screens the image is hidden for better UX. 

#### All Products

![Products Page](/static/site_images/plants-page.png)

Clicking on the link for All Products in the nav-bar or the Shop Here link on the Home page will take you to the product view. Here you get an overview of all products, image, name and price. On this site you can choose to view a certain category by clicking on one of the category buttons on the top of the page. You can also sort the products by price, ascending and descending or by name. 

#### Product Detail

![Product Detail](/static/site_images/product-detail-page.png)

When clicking on either a product image or its name you are directed to the product detail view. From here you get all information regarding the plant and you can also choose to add it in your shopping bag. There is also a button to redirect you back to the All products page. If the user is a superuser, there are also options to edit and/or delete the product directly from here. 

#### Manage Product

![Manage Product](/static/site_images/manage-product-page.png)

As a superuser you can easily navigate to manage specific products by clicking the Edit or Delete button. Clicking the Delete button removes the item immediately whilst clicking Edit takes you to the page displayed above. Here the superuser can update all details regarding the product. 

#### User Profile

![User Profile 1](/static/site_images/userprofile-page-1.png)     ![User Profile 2](/static/site_images/userprofile-page-2.png)

Choosing My Profile under the My Account link takes the user to their Profile. This action requires that the user is logged in, if not they will be asked to login or register. From here the user can update all information or delete it, and also get an overview of previous purchases. If the order number is clicked the user will be redirected to the specifications of that particular purchase.

#### Sign Up / In / Log Out

![Sign Up/In/Out](/static/site_images/signup-in-out-page.png)

From the nav-bar the user can easily access the different options Sign Up, Sign In or Log Out. Depending on the status of the user different options are presented, only logged in users can log out and vice versa. These pages are very straightforward and intentionally the layout is kept simple since the user is not supposed to linger here. From here users can also ask to reset their password in case they forgot it. 

#### Shopping bag

![Shopping Bag](/static/site_images/shoppingbag-page.png)

When users click on the shoppingbag icon in the nav-bar they are taken to the Shopping Bag view. If there are no items in the shopping bag a message stating that is displayed along with a button directing back to the products site. The Shopping Bag clearly displays the items currently in the bag, and an easy option to update quantity of those items or deleting them. You can also see the price for each item, the total price and whether or not you have reached the free shipping limit ($40). From the Shopping Bag view you can either go back to shopping or go further to the secure Checkout. 

#### Checkout Page

![Checkout Page 1](/static/site_images/checkout-1-page.png)      ![Checkout Page 2](/static/site_images/checkout-2-page.png)

When the user is done shopping they can go to the Checkout Page. From here they get to either fill in their shipping and billing information, or just complete the missing parts if they have information saved since before. Besides basic information like address the user can also add additional shipping information, for example in Sweden it is very common that you provide a code for the building front door. After filling out all information, the total amount that will be charged is clearly displayed and the user can then complete the checkout or go back to adjust the bag. 

#### Order Confirmation

![Order Confirmation](/static/site_images/order-confirmation-page.png)

After the user has completed the purchase, the user is directed to the Order Confirmation page. From here the user get a full overview of the purchase, shipping and billing information, as well as additional information if that was added. 

#### Newsletter Subscription

![Newsletter Subscription](/static/site_images/newsletter.png)

Any site user can easily sign up for Newsletter subscription to take part of news, offers etc. By entering their email they will receive newsletters. This service is handled by the [MailChimp Service](https://mailchimp.com).

[Back to content](#contents)

### **General Features**

* Alert Message

![Alert Message](/static/site_images/alert.png)

Whenever the user interacts with the page, ie logs in, adds a product to the shopping bag updates their userprofile etc, an alert is displayed. This is a general feature that applies all over the page. 

[Back to content](#contents)

### **Future Features**

* A future version of BloomRoom could feature an option to comment and or rate products on the site. It could be a good way to involve the customers more. 
* Another feature that could quite easily be managed by the site owner is special offers or even gifts for customers on their birthdays. I included the option to add your date of birth in your Profile, which would enable the site owner to use that information. 
* As of now if a user wishes to delete their user profile, they are advised to send an email. This is not optimal and a future version would definitely include this option for the user. 
* Other products related to plants and flowers such as, flower pots, fertilizer etc could be added to the product list. 

[Back to content](#contents)

## **SEO Implementation**

I used the following words as Meta keywords to optimize SEO:

- BloomRoom
- Plant
- Plant store
- Flower store
- Plant shop
- Plant home delivery
- Household plants
- Flower interior
- Plant decoration
- Greenery

*Meta Description Tag:*

 - "BloomRoom, A high-quality online plant store that offers fast home delivery all over Europe"

All images displayed on the page have descriptive alternative text for better search engine optimzation. 

[Back to content](#contents)

### **Sitemap**




[Back to content](#contents)

### **Robots**




[Back to content](#contents)

## **Marketing Techniques**

### **Target Audience**

The site owner imagines their typical customer to be a person of the age of somewhere between 20-50 years. The typical customer probably lives in an urban environment and does not have easy access to regular plant retailers. They are used to online shopping an appreciate the convenience of conducting their shopping online. This type of audience make Social Media platforms an extremely important place to advertise and be visible. 

### Social Media

#### Facebook

[BloomRoom Facebook Page](https://www.facebook.com/BloomRoom-110804875024055/?ref=pages_you_manage)
*Since Facebook regularly deletes mock-up pages I can not guarantee that the page will still be there, hence I have taken screen shots of the created page. Although I have written the content of the page in English, the rest of the site is in Swedish since it was created in connection to my personal account.*

![Facebook 1](/static/site_images/FB-1.png)
![Facebook 2](/static/site_images/FB-2.png)
![Facebook 3](/static/site_images/FB-3.png)

#### Instagram

Although this site does not yet have an Instagram account, creating one would be on the very top of my marketing strategies list. Lots of younger people today do not use Facebook in such extent and many customers turn to Instagram first. If the timeframe would have allowed it I would have created an Instagramm account for this site as well. 

### Newsletter

The BloomRoom site has a Newsletter Subscription form, which means that the site owner can send emails regarding special offers, upcoming campaigns, inspo and much more. By enabling the site users to sign up for the Newsletter, it is easy for the site owner to reach their customers with targeted advertising and hence encouraging potential customers to revisit the site again. 

[Back to content](#contents)

## **Testing**

Testing was done manually throughout the development process. The full rundown of the testing can be found in a separate [testing.md file](/testing.md). 

[Back to content](#contents)

## **Bugs**

* **Bug:** Stripe Webhooks throwing throwing signature error
    
    **Solution:** I had pasted the stripe public and secret key in my Gitpod variables, but not the webhook key. After consulting tutor support I was adviced to put them in my env.py file instead along with the wh-key. 

* **Bug:**: Emails not being sent out
    
    **Solution:** I was trying to send emails from a gmail which doesn't work on the development server, after I put DEVELOPMENT="True" in my env.py file the emails were sent out as expected. 

* **Bug:** When trying to view order history an Error regarding unexpected keyword argument 'order_number' was thrown. 
    
    **Solution:** It turned out I had the wrong URL path for the order_history instead of views.order_history I had views.profile. 

* **Bug:** When trying to checkout from the deployed app on Heroku, an error was thrown stating no API key was provided. 
    
    **Solution:** I added the stripe keys to my Config Vars on Heroku which fixed the error. 

* **Bug:** The webhook stripes started throwing errors again when making purchases. The payment itself went through but not the webhooks. 
    
    **Solution:** It turned out I had to remove the trailing slash from the checkout urls.py.

* **Bug:** When clicking all plants I wanted the different sub-categories to show up, but All Plants also showed up as a button. 

    **Solution:** Initially I had entered All plants as its own category, but I later realized that was abundant and hence removed that category entirely which took care of the issue. 

* **Bug:** My biggest and most challenging bug was when I decided to make a switch from Cloudinary Storage to AWS. I encountered an etag error when using cloudinary and since not even the excellent help at Tutor support managed to combat that bug I decided to get rid of cloudinary and start over with aws. After making the setup the images and css was still not rendering correctly. After lots of troubleshooting and with amazing help from John Traas from CI he discovered two bugs in my setup. 

    **First solution:** - The Secret Access Key I got from AWS contained a forward slash (/) which causes an error that not even Amazon are able to tackle apperently. 
    **Second solution:** - The name I had chosen for my bucket was the same as my heroku app name which caused a name error. Hence I had to create a new bucket and do the setup etc once more. 
    **Third solution:** After this the site was rendering correctly apart from all the product images. This was because the media folder where the images are stored were not downloaded into the bucket automatically. After manually creating a media folder in the bucket, and uploading all of the images to it, the site was functioning as expected. 

[Back to content](#contents)

## **Technology Used**

### **Main Languages Used**

- HTML5
- CSS3
- JavaScript
- jQuery
- Python
- Django

[Back to content](#contents)

### **Frameworks, Libraries and Programs Used**

- [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/ "Link to Bootstrap page")
     - Bootstrap was used to implement the responsiveness of the site, using bootstrap classes, but also other styling such as buttons etc.
- [AWS Storage](https://aws.amazon.com/ "Link to AWS")
     - AWS Bucket Storage was used to store static and media files. 
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/ "Link to the Crispy Forms documentation")
    - Crispy Forms was used to style the add and edit recipe forms, allowing more than one field to occupy a line on the form.
- [Google Fonts](https://fonts.google.com/ "Link to Google Fonts")
    - Google fonts were used to import the fonts "Playfair Display" and "Lato" into the style.css file. These fonts were used throughout the project.
- [Font Awesome](https://fontawesome.com/ "Link to FontAwesome")
     - Font Awesome was used on all pages throughout the website to import icons (e.g. social media icons) for UX purposes.
- [Git](https://git-scm.com/ "Link to Git homepage")
     - Git was used for version control by utilizing the GitPod terminal to commit to Git and push to GitHub.
- [GitHub](https://github.com/ "Link to GitHub")
     - GitHub was used to store the project after pushing
- [Am I Responsive?](http://ami.responsivedesign.is/# "Link to Am I Responsive Homepage")
     - Am I Responsive was used to see responsive design throughout the process and to generate mockup imagery to be used.
- [Balsamiq Wireframes](https://balsamiq.com/learn/articles/what-are-wireframes/ "Link to Balsamiq Wireframes")
     - Balsamiq Wireframes was used to create the wireframes for the project.  
- [tinypng.com](https://tinypng.com/ "Link to tinypng")
     - Tinypng was used to compress images. 
- [Canva.com](https://www.canva.com/ "Link to Canva")
     - Canva was used to make the BloomRoom Logo

[Back to content](#contents)

## **Deployment**

### Deployment to heroku

**In your app** 

1. Add the list of requirements by writing in the terminal "pip3 freeze --local > requirements.txt"
2. Git add and git commit the changes made

**Log into heroku**

3. Log into [Heroku](https://dashboard.heroku.com/apps) or create a new account and log in

4. Top right-hand corner click "New" and choose the option Create new app, if you are a new user, the "Create new app" button will appear in the middle of the screen

5. Write app name - it has to be unique, it cannot be the same as this app
6. Choose Region - I am in Europe
7. Click "Create App"

**The page of your project opens.**

8. Go to Resources Tab, Add-ons, search and add Heroku Postgres

9. Choose "settings" from the menu on the top of the page

10. Go to section "Config Vars" and click button "Reveal Config Vars". 

11. Add the below variables to the list

    * Database URL will be added automaticaly
    * Secret_key - is the django secret key and it can be generated [here](https://miniwebtool.com/django-secret-key-generator/). 

**Go back to your code**

12. Procfile needs to be created in your app
```
web: gunicorn bloomroom.wsgi
```

13. In settings in your app add Heroku to ALLOWED_HOSTS

14. Add and commit the changes in your code and push to github

**Final step - deployment**

15. Next go to "Deploy" in the menu bar on the top 

16. Go to section "deployment method", choose "GitHub"

17. New section will appear "Connect to GitHub" - Search for the repository to connect to

18. Type the name of your repository and click "search"

19. Once Heroku finds your repository - click "connect"

20. Scroll down to the section "Automatic Deploys"

21. Click "Enable automatic deploys" or choose "Deploy branch" and manually deploy

22. Click "Deploy branch"

Once the program runs you should see the message: "The app was sussesfully deployed"

23. Click the button "View"

The live link can be found [here](https://bloomroom.herokuapp.com/).

### Forking the GitHub Repository

By forking the GitHub Repository you will be able to make a copy of the original repository on your own GitHub account allowing you to view and/or make changes without affecting the original repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/KarinOldbring/bloomroom)
2. At the top of the Repository (not top of page) just above the "Settings" button on the menu, locate the "Fork" button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/KarinOldbring/bloomroom)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open commandline interface on your computer
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/KarinOldbring/bloomroom
```

7. Press Enter. Your local clone will be created.

### Setting up your local enviroment

1. Create Virtual enviroment on your computer or use gitpod built in virtual enviroment feature.

2. Create env.py file. It needs to contain those 5 variables.

* DATABASE_URL can be obtained from [heroku](https://dashboard.heroku.com/), add PostgreSQL as an add on when creating an app. 
* SECRET_KEY - is the django secret key can be generated [here](https://miniwebtool.com/django-secret-key-generator/). 
* STRIPE_PUBLIC_KEY
* STRIPE_SECRET_KEY
* STRIPE_WH_SECRET

PostgreSQL and AWS keys are needed only on Heroku, not in local IDE

3. Run command 
```
pip3 install -r requirements.txt
```

### Getting Stripe keys
Go to developers tab. On side menu you will find API keys. Copy STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY.

Go to Webhooks. Click Add Endpoint button in top right hand corner.
Add endpoint URL (your local or deployed URL)
Add all events 
Then click add endpoint
You should be redirected to this webhooks page. Reveal webhook sign in secret key and copy to Settings and to heroku as STRIPE_WH_SECRET variable

### Getting email variables from gmail

- Log into gmail account
- Go to Settings and than See all settings
- Top menu go to Accounts and import
- Find on the list Other google account settings
- Left side menu - Security
- Turn on two step verification: add phone number and follow instructions
- Go back to security
App passwords - Select Mail, Select Device - Other, Django, Copy app password.

In Heroku 
EMAIL_HOST_PASS is the password copied from above.
EMAIL_HOST_USER is the gmail email address

### Setting AWS bucket

1. Go to [Amzon Web Services](https://aws.amazon.com/) page and login or register

2. You should be redirected to AWS Management Console, if not click onto AWS logo in top left corner or click Services icon and choose Console Home

3. Below the header AWS Services click into All Services and find **S3** under Storage

4. Create New Bucket using **Create Bucket** button in top right hand corner

- **Configuration:** Type in your chosen name for the bucket (preferably matching your heroku app name, but it should not be identical) and AWS Region closest to you

- **Object ownership:** ACLs enabled, Bucket owner preferred

- **Block Public Access settings:** Uncheck to allow public access, Acknowledge that the current settings will result that the objects within the bucket will become public

- Click **Create Bucket**

5. You are redirected to Amazon S3 with list of your buckets. Click into the name of the bucket you just created

6. Find the tab **Properties** on the top of the page:
**Static website hosting** at the bottom of the properties page: clik to edit, click enable, fill in index document: index.html and error.html for error

7. On the **Permissions** tab:
- Cross-origin resource sharing (**CORS**) Paste in the below code as configuration and save

[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]

- **Bucket Policy** within permissions tab: Edit bucket policy
Click AWS Policy Generator (top right conrner)

Select type of policy: S3 Bucket policy
Principal: * (allows all)
Actions: Get object
Amazon Resource Name (ARN): Paste from the Edit bucket policy page in permissions
Click Add statement then click Generate Policy and copy the policy into bucket policy editor. 
In the policy code find "Resource" key and add "/*" after the name of the bucket to enable all
Save changes

- **Access control list (ACL)** within permissions tab: click Edit

Find Everyone (public access) and check List box and save

8. Identity and Access Management (IAM)
Go back to the AWS Management Console and find IAM in AWS Services

- Side menu - User Groups and click **Create Group**
Name group "manage-your-app-name" and click Create group

- Side menu - Policies and click **Create Policy**
Click import managed policy - find AmazonS3FullAccess
Copy ARN again and paste into "Resource" add list containing two elements "[ "arn::..", ""arn::../*]" First element is for bucket itself, second element is for all files and folders in the bucket

Click bottom right Add Tags, than Click bottom right Next: Review
Add name of the policy and description

Click bottom right Create policy

9. Attach policy to the group we created:
- Go to User Groups on side menu
- Select your group from the list
- Go to permissions tab and add permissions drop down and choose **Attach policies**
- Find the policy created above and click button in bottom right Add permissions

10. Create User to go in the group
- **Users** in the side menu and click add users

User name: your-app-staticfiles-user
Check option: Access key - Programmatic access
Click button at the bottom right for Next
- Add user group and add user to the group you created earlier
Click Next Tags and Next: review and Create user
- Download .csv file

11. Connect django to AWS S3 bucket
- Install boto3
- Install django-storages
- Freeze to requirements.txt
- Add storages to installed apps in settings.py

# Bucket Config
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_REGION_NAME = 'eu-north-1'
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

12. Go to heroku to set up enviromental variables

Open CSV file downloaded earlier and copy each variable into heroku Settings

    AWS_STORAGE_BUCKET_NAME
    AWS_ACCESS_KEY_ID from csv
    AWS_SECRET_ACCESS_KEY from csv
    USE_AWS = True
    remove DISABLE_COLLECTSTATIC variable from heroku

13. Create file in root directory custom_storages.py

from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION

class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION

14. Go to settings.py, add the AWS settings

# Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

# Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

15. To load the media files to S3 bucket

- Go to your S3 bucket page on AWS. Create new folder "media"
- Go to the media folder and click Upload

[Back to content](#contents)

## **Credits**

### **Media**

* All images on the site are taken from [Pexels](https://www.pexels.com/sv-se/). 

[Back to content](#contents)

### **Code**

References used and Inspiration:

* [Bootstrap](https://getbootstrap.com/)
* [Django Docs](https://docs.djangoproject.com/en/4.0/)
* [Stack Overflow](https://stackoverflow.com/)
* [w3 Schools](https://www.w3schools.com/)
* [Crispy Forms Docs](https://django-crispy-forms.readthedocs.io/en/latest/)
* [Markdown Tables Generator](https://www.tablesgenerator.com/)
* [Project Boutique Ado from Code Institute](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+EA101+2021_T1/courseware/eb05f06e62c64ac89823cc956fcd8191/3adff2bf4a78469db72c5330b1afa836/)

### **Acknowledgements**

[Back to content](#contents)