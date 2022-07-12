# **BloomRoom**

[View the live project here](https://bloomroom.herokuapp.com/)

## Contents
* **[Introduction](#Introduction)**
    * [Business Plan](#Business-Plan)
    * [Planning Stage](#Planning-Stage)
    * [Project Goals](#Project-Goals)
    * [User Stories](#User-Stories)
    * [Design Goals](#Design-Goals)
    * [Design Choices](#Design-Choices)
        * [Font](#Font)
        * [Color Scheme](#Color-Scheme)
        * [Logo BloomRoom](#Logo-BloomRoom)
        * [Images](#Images)
    * [Wireframes](#Wireframes)
    * [Site-Map](#Site-Map)

* **[Features](#Features)**
    * [Design Features](#Design-Features)
    * [Existing Features](#Existing-Features)
    * [Future Features](#Future-Features)

* **[SEO Implementation](#SEO-Implementation)**

* **[Marketing Techniques](#Marketing-Techniques)**

* **[Testing](#Testing)**

* **[Bugs](#Bugs)**

* **[Technology Used](#Technology-Used)**
    * [Main Languages Used](#Main-Languages-Used)
    * [Additional Languages Used](#Additional-Languages-Used)
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
Orders over 40$ are free and users can easily see when shopping when they have reached the free shipping limit. Products can be added to the cart and can be purchased using card payment. Order confirmation is sent to the email address provided. Users can also stay updated with all the latest and exclusive offers by following on Facebook page and by subscribing to the monthly newsletter.

**Business Plan**

The fact that more and more trade is conducted online hardly comes as news to anyone. Especially since the pandemic more people wish to do their shopping from home to avoid crowded stores. Also, with more flexible working hours it's become more important to be able to do your shopping whenever it suits you, without having to adjust to opening hours. The pandemic was turbulent in many ways but for the flower/plant industry it has been blooming to say the least, and there's no sign of it slowing down! Lots of people staying home more than usual made them pay more attention to their home environment and wanting to invest more in their homes. Even though a lot of our everyday shopping has been online since many years the plant industry is falling behind. There are not that many online plant shops and that's why there certainly is room for a new actor! The strategy is to offer popular, high quality plants and full support for our costumers. Customers can call or email to get help and advice regarding already purchased products or if they wish to have recommendations regarding suitable plants for their homes. A userfriendly website, easy to navigate with secure and fast checkout will make our users loyal customers! 

**Planning Stage**

**Project Goals**

**User Stories**

* Agile methodology was used to create user stories.

* GitHub’s Kanban feature was used to track the progress of user stories.

**Design Goals**

**Design Choices**

* Font

* Color Scheme

* Logo BloomRoom

* Images





**Bugs
Error: Stripe Webhooks throwing throwing signature error
Solution: I had pasted the stripe public and secret key in my Gitpod variables, but not the webhook key. After consulting tutor support I was adviced to put them in my env.py file instead along with the wh-key. 

Error: Emails not being sent out
Solution: I was trying to send emails from a gmail which doesn't work on the development server, after I put DEVELOPMENT="True" in my env.py file the emails were sent out s expected. 

Error: When trying to view irder history an Error regarding unexpected keyword argument 'order_number' was thrown. 
Solution: It turned out I had the wrong URL path for the order_history instead of views.order_history I had views.profile. 

Error: When trying to checkout from the deployed app on Heroku, an error was thrown stating no API key was provided. 
Solution: I added the stripe keys to my Config Vars on Heroku which fixed the error. 
