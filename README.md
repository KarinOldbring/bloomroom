# **BloomRoom**

[View the live project here]()

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


**Bugs
Error: Stripe Webhooks throwing throwing signature error
Solution: I had pasted the stripe public and secret key in my Gitpod variables, but not the webhook key. After consulting tutor support I was adviced to put them in my env.py file instead along with the wh-key. 

Error: Emails not being sent out
Solution: I was trying to send emails from a gmail which doesn't work on the development server, after I put DEVELOPMENT="True" in my env.py file the emails were sent out s expected. 
