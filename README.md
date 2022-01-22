# SPIN IT

This is an e-commerce website for DEE JEEYS where they can find second hand records and devices that I create for Milestone Project 4 (Full Stack Frameworks with Django) in Code Institute, Ireland. The use of the website is for educational purposes only, however, all the functionalities work as if it is an actual e-commerce website. It is a mobile responsive website and the link to the website is available HERE [https://cnavotka-spin-it.herokuapp.com/]

![Responsive image](https://github.com/cnavotka/spinit/blob/main/static/images/all-devices-white.png)


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


THe page title wasn't showing properly, I fixed adding the class text-dark

![Bug 3](https://github.com/cnavotka/spinit/blob/main/static/images/text-dark-bug.png)



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
