# SPIN IT

This is an e-commerce website for DEE JEEYS where they can find second hand records and devices that I create for Milestone Project 4 (Full Stack Frameworks with Django) in Code Institute, Ireland. The use of the website is for educational purposes only, however, all the functionalities work as if it is an actual e-commerce website. It is a mobile responsive website and the link to the website is available HERE [https://cnavotka-spin-it.herokuapp.com/]

![Responsive image](https://github.com/cnavotka/spinit/blob/main/static/images/all-devices-white.png)


# Project Resubmission

As per feedback gave by the assesor, this are the areas to improve:

### LO1 Design, develop and implement a Full Stack web application, with a relational database, using the Django/Python Full Stack MVC framework and related contemporary technologies:

* 1.2 Inadequate UX Design: Fixed
* 1.4 Backed code for form lacks foolproof validations for incorrect user inputs, leads to poor user experience. Fixed, added in checkout, login and register.
* 1.11 Testing step are missing. Fixed, a new folder TESTING.md added

### LO2 Design and implement a relational data model, application features and business logic to manage, query and manipulate relational data to meet given needs in a particular real-world domain:

* 2.3 Validation cannot be checked since the CRUD operations for admin are not available. Fixed, Admin and superuser created.
* 2.4 CUD from CRUD cannot be accessed, since admin login isn't available. Fixed, Admin and superuser created.

### LO3 Identify and apply authorisation, authentication and permission features in a full-stack web application solution:

* 3.1 Unable to register/login, since the form is not visible properly. Fixed, user can register/login from the top navbar.
* 3.2 Registration/Login functionality broken. Fixed, User can register and login.
* 3.3 Unable to register/login, since the form is not visible properly. Fixed, user can register/login from the top navbar.

### LO4 Design, develop and integrate an e-commerce payment system in a cloud-hosted, full-stack web application:

* 4.1 No mechanism to pay for the e-commerce revenue model. Fixed, Stripe App set up
* 4.2 Does not allow for users to initiate actions based on his choice or allows but broken functionality. Fixed, Stripe App set up using the checkout.

### LO5 Document the development process through a git based version control system and deploy the full application to a cloud hosting platform:

* 5.6 Missing certain critical section in README file that are required for complete understanding of the application. Fixed, documentation to the README file added.


# User stories

We have two types of users in the website. One is shoppers that are looking for second hand devices and records in excellent conditions. The other one, is the shop owner that is trying to sell the products.

## Shopper's User Story

As a user, I would like to see what the website is about at a glance.

I want to see what the website is selling.

I would like to be able to navigate throughout the website easily.

I would like to register and login, and also see my orders history.

I would like to see details in my shopping bag.

I would like to pay easily and securely my purchase.

## Owner's User Story

As an owner, I would like to provide a simple and easy website to my customers.

I would like to add, edit, update and delete products in an easy way.

I would like to protect the website so only authorised users can take actions.




# UX planes

## Strategy 

To achieve the user's primary goals and stories outlined in the User Stories section, all the functions and features on the tables below are minimum requirements and they are implemented in the website. (On a scale of 1 [least] - 5 [most])

![Strategy Plane User](https://github.com/cnavotka/spinit/blob/main/media/user-stories.png)


Based on the requirements of achieving user's and owner's goals and stories, below is the list of required pages with the features and functions. CRUD (Create, Read, Update, and Delete) functions are implemented on the website as it is required for admin user's product management.

    Simple design Home page that the purpose of the website is obvious to anybody and even first-time users know how to navigate the website. Clearly displayed group of categories (e.g. RECORDS - TURNTABLES & ACCESORIES | STUDIO) that have categories in it (e.g. RECORDS --> LP's | EP's | 7 inches).

    Product pages by the group of categories where users can view all the products belong to the group. Users are navigated to categories in this group from this page.

    Product pages by category where users can view all the products belong to the category.

    Product details page where uses can see all the product details. Users can also select options and put the product in the bag.

    Shopping Bag page where users can see all the selected products before purchase. Users can change the quantity of the product or remove it.

    Checkout page where users can provide shipping details and credit card details.

    Checkout success page where users get confirmation of purchase.

    Register page where users can create an account to keep the shipping address saved and to view order histories.

    Login page where users can log in to the page.

    Profile page where users can see the personal details and order histories.

    Logout function that users can safely log out the website and takes users back to the home page.

    Product Management pages (admin only) where admin can add, edit, and delete products.


## Structure Plane

### Front End

The website consists of below core HTML pages and has some CSS and JavaScript

    Home (index.html)
    The main page of the website. There is a logo, search function, navigation to Group of Categories & Categories, Register & Login and Shopping Bag pages, a hero image with Shop Now button. There is a footer with some social icons. *The same header and footer are used across all html files

    Products (products.html, products/<category_name>.html)
    The pages where users can see products by a group of categories & category and have an access to the product details page.

    Product Details (product/<product_id>.html)
    The pages where users can see product details, with an option to select criteria (e.g. accesories) and add it in the shopping bag.

    Shopping Bag (bag.html)
    The page where users can view all the selected products and details. Users can adjust the quantity and there is an option to remove products. There is a button link to a checkout page for the final step of shopping.

    Checkout (checkout.html)
    The page where users can process the purchase. Stripe, which is a secured platform for credit card payment, is used on the website for processing payments.

    Checkout Success (checkout_success.html)
    The confirmation page where users are lead to when the payment process is completed. Users can see the order number, shipping address, product details. This page is accessible for registered users from Profile.

    Register (signup.html)
    The page where users can create an account to save their details for next shopping and keep their purchase histories. A form with a built-in function is created with Django Allauth package.

    Login (login.html)
    The page where users can log in to the website and access to the Profile page to see the personal details and purchase histories. A form with a built-in function is created with Django Allauth package.

    Profile (profile.html)
    The page where users can see personal details and purchase histories.

    Add Products (add_products.html)
    The page where only Admin has access and add a new product on the website.

    Edit Products (edit_products.html)
    The page where only Admin has access and edit products.

    Base Templates (base.html and base.css)
    The template documents that have core components of html and css and are used among other html files.

    Admin (/admin)
    The admin panel, which can be created with Django project, where Admin can take control of products and other data.

    CSS & JavaScript (.css & .js)
    CSS and JavaScript files of those HTML files are created within the same app folder.

### Back End

Users have options to purchase products as guest users or account holder users. Guest users cannot save personal details for their next shopping as personal details such as name, email address, shipping address etc belong to their order in the database. Account holder users who create an account with their email address and username, user name (user profile) is linked with their order so that personal details can be retrieved. Each product belongs to a category, a brand and these are identified by id. Each order has a unique order number which is generated when the order is processed and orders have shopper's and product details.
SQLite, which is Django built-in database is used for development mode and Heroku Postgre is used for production mode. AWS (Amazon Web Services) is used to hold all static files and folders for the website for production mode.


## Skeleton Plane


The website is fully responsive.
Below are the wireframes of the main pages of the website.

Home Desktop [https://github.com/cnavotka/spinit/blob/main/static/images/Home%20desktop.png]

Home iPhone [https://github.com/cnavotka/spinit/blob/main/static/images/Home%20Iphone.png]

Products Desktop [https://github.com/cnavotka/spinit/blob/main/static/images/Product%20desktop.png]

Products iPhone [https://github.com/cnavotka/spinit/blob/main/static/images/Product%20iPhone.png]

Products Desktop [https://github.com/cnavotka/spinit/blob/main/static/images/Product%20page%20desktop.png]

Products iPhone [https://github.com/cnavotka/spinit/blob/main/static/images/Product%20page%20iphone.png]

Shopping cart Desktop [https://github.com/cnavotka/spinit/blob/main/static/images/Cart%20desktop.png]

Shopping car iPhone [https://github.com/cnavotka/spinit/blob/main/static/images/Cart%20iphone.png]

Checkout [https://github.com/cnavotka/spinit/blob/main/static/images/checkout%20desktop.png]

Checkout iPhone [https://github.com/cnavotka/spinit/blob/main/static/images/checkout%20iphone.png]

Checkout Success Desktop [https://github.com/cnavotka/spinit/blob/main/static/images/checkout-success-desktop.png]

Checkout Success iPhone [https://github.com/cnavotka/spinit/blob/main/static/images/checkout-success-iphone.png]

Register Desktop [https://github.com/cnavotka/spinit/blob/main/static/images/register-desktop.png]

Register iPhone [https://github.com/cnavotka/spinit/blob/main/static/images/register-iphone.png]

Login Desktop [https://github.com/cnavotka/spinit/blob/main/static/images/login-desktop.png]

Login iPhone [https://github.com/cnavotka/spinit/blob/main/static/images/login-iphone.png]

Profile Desktop [https://github.com/cnavotka/spinit/blob/main/static/images/profile-desktop.png]

Profile iPhone [https://github.com/cnavotka/spinit/blob/main/static/images/profile-iphone.png]

Product Management Desktop [https://github.com/cnavotka/spinit/blob/main/static/images/product-management-desktop.png]

Product Management iPhone [https://github.com/cnavotka/spinit/blob/main/static/images/product-management-iphone.png]

## Surface Plane

### Colours

I went for a groupo of colours that provides good contrast, inspired by this website:
Helikon Tex [https://www.helikon-tex.com]

### Typography

I use Roboto form Google Fonts, because provides a good readability

## Website Development Plan

This is a full-stack website that contains both front-end & back-end, so many Django apps, features and functions, therefore a good website development plan is required to maximise the efficiency of the development. Below is the summary of core tasks for the website and more detailed tasks are listed on GitHub Projects. 

Follow the same process as Code Institute Mini Project, Boutique Ado

* Planning The Website with UX5 Planes
* Project Set-Up (Installing Django, Setting up Project, Testing connection, Creating Django superuser)
* Authentication & Authorisation (Installing Allauth, Testing)
* The Base Template (Creating base template)
* The Home Page (Navigation bar, Header and Footer)
* Products Set-Up (Creating Products app, Installing data, Filtering & Searching)
* The Shopping Cart (Adding and adjusting products)
* Toasts (Real-time notification)
* Checkout with Stripe (Function, Form, Testing Stripe)
* Profile (Displaying personal details and order history)
* Product Admin (CRUD function for products)
* Deployment (AWS, Heroku)
* Emails (Setting up email functionality)
* Code Refactoring (Checking code, Reviewing the design and updating)
* Testing (Testing for HTML, CSS, JavaScript, Python, User Stories, Functions and Features)
* Final Check Before Submission


## Features

### Existing Features


* Create with HTML5, CSS3 (with Material Design for Bootstrap), JavaScript, Python (Django Framework), Stripe, AWS and Heroku
* It consists of 1 product with 5 apps in Django
* It consists of 1 base html template and main html files. (Excluding sub html files and some allauth html files)
* All the features planned on Strategy Plane and Scope Plane

### Features Left to Implement

* Enlarging image when hovering
* Refinements options
* Creating an account with social media
* Product comparison



# Technologies Used

* HTML for markup
* CSS for style
* Bootstrap for mainframe
* JavaScript for interaction
* Python as a backend programming language
* Django (an open-source web framework) as the main framework of Python
* SQLite (Django built-in database) as a database in development mode
* PostgreSQL (Heroku built-in) as a database in production mode
* Google Fonts for fonts
* Font Awesome for icons
* Stripe for credit card payment
* AWS (Amazon Web Services) for hosting static files and images for the website
* Gitpod as Integrated Development Environment (IDE)
* Git for local version control, keeping the files & documents
* Github for online version control and keeping the files & documents
* Heroku for deploying the website
* Gimp for the images

## Testing
The project wasn't finished at the moment of the submission, no test were made.

# Bugs

The backgroung image was covering the full screen in the bag page. I found that I forgot the add {% block content %} in the code.

![Bug](https://github.com/cnavotka/spinit/blob/main/static/images/bug-missing-blockcontent-baghtml.png)




The Payment card wasn't working in the checkout , finiding this error when I inspected:

![Bug 2](https://github.com/cnavotka/spinit/blob/main/media/card-stripe-bug.png)

I fixed moving the stripe_elements.js file to the right location.


The page title wasn't showing properly, I fixed adding the class text-dark

![Bug 3](https://github.com/cnavotka/spinit/blob/main/static/images/text-dark-bug.png)


Confirmation email wasn't being sent, need to add HOST in Heroku config:

![Email](https://github.com/cnavotka/spinit/blob/main/static/images/mail-error.png)


# Version Control

Git as a local repository and GitHub as a remote repository are used for the project, and below is how they are used as the version control for the project.

### Setting Up

1. Create a remote repository in GitHub by clicking "New repository" on the main page
2. Use Code Institute Template, put the repository name and click Create Repository making sure to select public
3. Open the repository with Gitpod which is my Integrated Development Environment (IDE). By using Code Institue Template, initialisation including initial commit is done so no need to do git init command when open IDE, or to use git push -u origin main command for my first commit. gitignore file, which is very important for the project including some confidential information, is created with Code Institute template so not necessary to create it, however, it is checked to include files such as pycache, *.sqlite3, env.py etc

* Commitments
When a section or even a group of work is completed, it is committed in git and pushed into GitHub to make sure to keep the history of the work logged properly and not to lose the work in unexpected situations. Below commands are used for this

* git status | To check the status of new/modified folders, files, and documents
* git add . | To put all new and updated work on the stage in git
  git add <specific file> is used when different types of work are done but do not want to commit everything on the same commitment
* git commit -m "Example commit" | To commit the work on the stage in git before pushing it to GitHub
* git push | To update the repository in GitHub for main / master branch
  git push origin <branch name> is used when pushing git into GitHub for sub-branches

* Branches
When some testing is needed, create a branch and test it on the branch instead of using the main / master branch. When the testing is successful, then merge the branch into the main / master and when it is not, leave the branch unmerged and keep working on the main / master branch. Below commands are used for this

* git branch <branch name> | To create a new branch
* git checkout <branch name> | To switch branch
* git branch | To check current branch
* git merge <branch name> | To merge sub-branch into main / master, do this on main / master branch

# Deployment

The website of this project requires back-end technologies such as server, application, and database so the website is deployed in Heroku, which is a cloud platform with a service supporting several programming languages, because GitHub can only host a static website. Heroku Postgres is used for the database. AWS services, which is also a cloud-based platform, is used to store static files and images as Heroku has no files system to store new files.

Below are the processes of deploying the website to Heroku and setting up static files & images in AWS.

# Heroku

1. Create an app in Heroku. Click New, put App name and select region
2. Add Heroku Postgres for the database
3. Install dj_database_url and psycopg2-binary to use Heroku Postgres, and run pip3 freeze > requirements.txt command to add them on requirments.txt
4. Update settings.py of the product (spinit). Import dj_database_url, comment out sqlite databases and add dj databases variable temporary while the database is transferred to Heroku Postgres
5. Run python3 manage.py showmigrations command to see the status of migrations (Currently not migrated). Run python3 manage.py migrate command to migrate
6. Import all products data. Run python3 manage.py loaddata command to load the categories first, brands next and products the last. The order of loading is important as all the products are associated with categories and brands
7. Create a super user with python3 manage.py createsuperuser command for product admin
8. Install gunicorn which acts as the webserver, and freeze it into requirements file with pip3 freeze > requirements.txt command
9. Create a Procfile which specifies the commands that are executed by the app on startup
10. Temporary disable collectstatic by setting heroku config:set DISABLE_COLLECTSTATIC = 1 and host name of Heroku to allowed hosts in settings.py
11. Initialise Heroku in git with heroku: git:remote -a spinit and put git into Heroku with git push heroku master
12. Set up automatic deployment when git is pushed to GitHub. Go to Deployment on Heroku, search the GitHub repository, connect and click Enable Automatic Deploys
13. Generate a new secret key, set it up in Heroku and update settings.py. Change the setting of Debug mode that only True in Development mode
14. Check Activity Feed to see Build in Progress to confirm automatic deployment is working

# AWS

1. Open S3 and create a new bucket, which stores the files, by completing the name and region
2. Set up basic settings. Enable static website hosting so that it gives a new endpoint for accessing from the internet. Put index.html and error.html as default values
3. Set up CORS configuration which is the access between Heroku and this S3 Bucket
4. Set up Bucket Policy. Generate a policy with AWS policy generator. Add /* at the end of Resource to allow access to all resources in the bucket
5. Create a user to access the bucket. Go to IAM (Identity and Access Management) and create a group for the user to live in. Then, create a policy by importing pre-built policy
6. Attach the policy to the group
7. Create a user and add it to the group. When the user is added to the group, it creates csv file containing Access Key ID and Secret access key which are used to authenticate them from Django app. *It is very important to download the file and save it as you cannot download it again

# Django

1. Install two new packages, pip3 install boto3, pip3 install django-storages, and run pip3 freeze > requirements.txt command to add them on requirments.txt
2. Update settings.py to tell Django which bucket it should be communicating with *It is very important to keep AWS access keys secrets as these can be used to store or move data in the bucket and you will be charged by Amazon for it
3. Add these secret keys on Heroku and set USE_AWS = True
4. Create custome_storages.py to tell Django to use S3 to store static files and upload images when it is in production
5. Add AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com' to tell Django where the static files come from in production and add some settings for Static and Media files on settings.py
6. Add all the updates in git, commit it and push it to GitHub. Heroku runs python3 manage.py to collectstatic during the process which also searches through all the apps and project folders looking for static files. Then, it uses S3 domain settings in conjunction with the custom storage classes that tell the location at the URL where the things should be saved when it is in production. This can be confirmed in S3 bucket
7. Add Cache control on settings.py as static files do not change often and to improve the performance for users
8. Upload product images via S3. Create a folder, and upload images
9. Verify superuser's email address on Heroku Postgres. Login admin and check the VERIFIED and PRIMARY boxes
10. Add Stripe keys to Heroku Config Vars and create a new webhook endpoint
11. Create Gmail account, add email host pass & user to Heroku Config Vars and add code on settings.py of the product (spinit)


# Credits

### Code

I followed the Boutique Ado project that mine is based on.

### Contents

All text in the products description was writeen by myself.

### Media 

All images of products and bakcground were taken by me. For the products pictures, I used and iPhone so they can look more DIY. For the background image, I used a Cannon camera.

## Acknowledgements
I would like to thank;
* My mentor, Gurjot Singh, for going through the project with me 
* Code Institute Tutors for giving me a guidance on how to solve some issues and fellow students in the Slack Community.
* My wife, Saoirse Mc Dermott for design advice





Happy coding!
