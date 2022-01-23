# Testing

## Walkthrough Test

### Navigation and Purchase

* User navigates to: https://cnavotka-spin-it.herokuapp.com/

    *User clicks on SHOP NOW button or they use the main links to look up cars.
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

## Flake Errors

Please note that these errors are mostly related to lines being too long, being completely new to Python and Django, I was genuinely fearful of going in and trying to fix these as I was scared about breaking something within the code.


## Chrome Lighthouse

* Lighthouse Desktop
![Lighthouse Desktop](https://github.com/cnavotka/spinit/blob/main/static/images/lighthouse-desktop.png)

![Lighthouse Mobile](https://github.com/cnavotka/spinit/blob/main/static/images/lighthouse-mobile.png)


## Validations

* CSS Validator 
* HTML Validator

