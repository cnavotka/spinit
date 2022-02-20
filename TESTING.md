# Testing

## Walkthrough Test

### Navigation and Purchase

* User navigates to: https://cnavotka-spin-it.herokuapp.com/

    * User clicks on SHOP NOW button or they use the main links to look up cars.
        SHOP NOW button shows all the various different car products.

    * User selects a PRODUCT to purchase and is taken to the product detail page.

        * Here they can either KEEP BROWSING or ADD PRODUCT TO BAG.

        * Clicking on the KEEP BROWSING button takes the user to the all products page.

        * Clicking on ADD PRODUCT TO BAG displays an instant notification of the product and cost.
            * PRODUCT cost is also displayed underneath the BAG icon.

    * User then clicks on GO TO SECURE CHECKOUT and is taken to the cart page with all of the product info contained.

        * Within the product info, user sees an image.

        * The name of the PRODUCT.

        * The cost.

        * Quantity.

        * And subtotal.
            * If they want, user can remove the item from the cart.

        * The user has two options:

            * To CONTINUE BROWSING (item remains in the BAG).

            * Or they can SECURE CHECKOUT, which takes them to the checkout page.

    * With the user now on the checkout page, the user is required to fill out a form.

        * Fields marked with an (*) are required.
            * If user fails to fill out a required field, the user is altered of the error.

        * Users can either create an account or login to save the information if they wish.

        * User then enters credit card details.
            * If user enters incorrect card details, the user is instantly altered of the error.

        * User can the either adjust their cart or complete the order.

            * Clicking on the ADJUST BAG takes the user to the cart page.

            * Clicking on COMPLETE YOUR ORDER makes the purchase, providing there are no errors in the form.

            * User then receives a complete order summary.

## Form Validation

There are some forms on the website. Some of them are validated by front-end (e.g. @ mark for email input) and some by back-end (e.g. existing user name). A manual test is carried out to see if the validations and form functions work properly.

#### Search Function

The form takes any texts including special characters (e.g. £, @, [ etc) so there is no form validation for this and the search is processed when the search button is clicked as long as there is a text in the input box. It works fine when a key word exists in product names or descriptions, and when it does not it shows 0 result. When there is no text in the input field, then it displays an error message. The search function is available on all the pages and it works from anywhere on the page.
![Search Found](https://github.com/cnavotka/spinit/blob/main/static/images/search-found.png)
![Search not Found](https://github.com/cnavotka/spinit/blob/main/static/images/search-not-found.png)


#### Register and Login Forms

Users must be unique so if the email address or username already exists in the database, it displays an error message for register page. Also, when the passwords do not match, it displays an error message. This is similar for the login page that if the email or user name does not exist in the database, it displays an error message and if password is incorrect, it also displays an error message. If the registration is successful, the user receives an email with a link to confirm the registration. If already register, the user can see the personal information in the profile.
![Link](https://github.com/cnavotka/spinit/blob/main/static/images/email-confirmation.png)
![Profile](https://github.com/cnavotka/spinit/blob/main/static/images/profile.png)


#### Add Product, Checkout and Stripe

When mandatory fields are not filled in or the form is invalid, it displays an error message. For credit card details, it is validated by Stripe and if it is invalid details, it displays an error message. If the checkpout is successful, we can see a webhook confirmation on Stripe and Order confirmation in the Profile.
![Credit card not valid](https://github.com/cnavotka/spinit/blob/main/static/images/invalid-card.png)
![Webhook](https://github.com/cnavotka/spinit/blob/main/static/images/webhook-test.png)
![Order Confirmation](https://github.com/cnavotka/spinit/blob/main/static/images/order-confirmation.png)


## Functions

There are some functionalities, which are run by views.py file in each app (in some cases by contexts.py), on the website. A manual test is carried out to see if these functions work as expected.

#### Bag App:

* View Bag: Products in the bag can be viewed by clicking the bag icon or a process your order button.
* Add Bag: Products can be added from the product page by clicking an add to shopping cart button. If the same product has different sizes (and right or left for golf clubs), they are added separately.
* Adjust Bag: Products can be adjusted in the Bag. Change the quantity of the product and remove it.
* Display: Price per product, discount price and total value including shipping cost show based on the products in the bag.

#### Checkout App:

* Checkout: Checkout is done by completing the form & credit card details and clicking a complete order button. Products in the bag can be views by clicking the bag icon or a process your order button.
* Checkout Success: When the order is completed, it creates an order in the database and saves the info. It also shows checkout success page for users.
* Confirmation email: When the order is succeeded (means payment in Stripe goes through), a confirmation email is sent.
* Stripe: When the order is completed, it creates a record of payment_intent, charge.succeeded and payment_intent.succeeded

#### Products App:

* Product Display: Products are displayed by group of categories, category, brand, sale products and all products. They can be sorted by price, category and product name both ascending and descending order. Products can be searched by a keyword 
* Product Details Display: Product details can be viewed by clicking an image of the product. It displays product category, ID, description, price, size (if applicable), discount price (if applicable).
* Product Add, Edit and Delete: Only authorised user (admin) is allowed to do these.

#### Profile App

* Profile: Access to the profile page where users can update the personal details and access to the order history.
* Profile (Admin): For admin user, Edit and Delete buttons appear on each product and there is a page for Adding product.

#### Authorised Users

There are some pages that only authorised users have access to. This is to test and confirm that non-authorised users have no access to these pages.
* Profile page: Only logged in users have access to the profile page. When /profile/ is typed on URL, unless users are logged in, users are directed to the login page.
* Add Product page: Only admin has access to the page. When /products/add/ is typed on URL, if users are not logged in, users are directed to the login page. If users are logged in, then users are directed to the home page with an error message unless Admin user.
* Edit Product page and Delete product function: Same as "Add Product".
* Order History: Only the user who purchased the product has access to the order history. When the order history URL is typed and if users are not the user who purchased the product, the users are redirected to the profile page with an error message.

# HTML

As the HTML code is completed on all HTML files, a code validation test is carried out by using W3C Markup Validation Service, which is a validator by the World Wide Web Consortium that allows checking HTML and XHTML documents for well-formed markup, to check any warnings and errors.

bag-total.html
bag.html
checkout-buttons.html
product-image.html
product-info.html
quantity-form.htmlcheckout_success.html
checkout.html
index.html
custom_clearable_file_input.html
quantityt_input_script.html
add_product.html
edit_product.html
product_detail.html
products.html
profile.html
base.html
footer.html
main_nav.html
mobile_top_header.html
Minor errors found and fixed.


# CSS 

As the CSS code is completed, a code validation test is carried out by using W3C CSS Validation Service, which is a validator by the World Wide Web Consortium that allows checking Cascading Style Sheets, to make sure that CSS complies with the standards set by the World Wide Web Consortium.

base.css profile.css checkout.css 
No errors, but some warnings related to Webkit and Moz.

# Javascript

As the JavaScript code is completed, a code validation test is carried out by using JSHint, which is a static code analysis tool used in software development for checking if JavaScript source code complies with coding rules.
No errors

$ shows a warning but comming from JQuery, so I ignore them. The same as some undefined variables in Stripe JS.


# Python

As Python code is completed, a code validation test is carried out by using PEP8 (Python Enhancement Proposal) online to see if the code meets guidelines and best practices for the readability and consistency of Python code.

Please note that these errors are mostly related to lines being too long, being completely new to Python and Django, I was genuinely fearful of going in and trying to fix these as I was scared about breaking something within the code.


## Chrome Lighthouse

* Lighthouse Desktop
![Lighthouse Desktop](https://github.com/cnavotka/spinit/blob/main/static/images/lighthouse-desktop.png)

![Lighthouse Mobile](https://github.com/cnavotka/spinit/blob/main/static/images/lighthouse-mobile.png)

## Assesment Test

Here you can find the screenshots testing if the login and CRUD operations for the admin in the top navbar of the deployed site as admin/superuser works.

* Add product
![Add Product](https://github.com/cnavotka/spinit/blob/main/static/images/test-admin-add-topbar.png)

* Edit product (Change the defualt 'No image" for a reandom image)
![Edit Product](https://github.com/cnavotka/spinit/blob/main/static/images/test-admin-edit-topbar.png)

* Delete product (Search for the product after delete it)
![Delete product](https://github.com/cnavotka/spinit/blob/main/static/images/test-admin-delete-topbar.png)






