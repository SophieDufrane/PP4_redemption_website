# RedeemIt - Your Employee Recognition Platform

## 1. **Introduction**

[RedeemIt](https://redemption-website-ec86c7604627.herokuapp.com/) is a mock employee recognition platform inspired by the solutions offered by [Workhuman](https://www.workhuman.com). It allows employees to view their points balance, browse a catalogue of gift cards, and redeem rewards. Administrators can manage the catalogue and access to employee profile (personal information, point balances…), ensuring a structured and efficient rewards process.  

Built using the **Django framework**, this project serves as a learning and portfolio exercise, demonstrating full-stack development skills in designing a functional and user-friendly web application.  

![Mockup](images-documentation/readme_images/mockup_responsive.png)

## Demo Login

To test the app easily:

**Username:** `sam.redeemington`  
**Password:** `sampass123`

The test account has points available so you can explore the full authentification (login - logout) and reward redemption process.


## 2. **User Experience - UX**

### **2.1. Scope and Structure**

#### **Scope**    

This project focuses on two main user roles:  

- **Employees** – Can view their **points balance**, browse the **gift card catalogue**, and **redeem rewards**.  
- **Administrators** – Can **manage the gift card catalogue** and **update employee profiles and point balances** through the admin panel.  

The platform is designed to provide a **clear redemption flow** and an **efficient management system** while ensuring an **intuitive user experience**.  

#### **Structure**  

The project is structured around three key areas:  

- **User Flow** – A simple and logical process for browsing, selecting, and redeeming gift cards.  
- **Admin Management** – A straightforward interface for adding, updating, removing items, as well as accessing employee's profile and redemption records.  
- **Clean & Responsive Design** – A structured layout that ensures clarity, accessibility, and ease of use across all devices.

### **2.2. User Stories**  

The project follows a user-centric approach, ensuring a smooth and intuitive experience for both employees and administrators. To structure the development process, **user stories are grouped into EPICs**, each focusing on a key aspect of the platform, such as redemption process, administrative management, and employee access.  

#### **EPIC - User Access**  
1. **Employee Register** *(must have)*  
  Allows an unregistered employee to create an account with a user name, email, and password to access the redemption platform.

2. **Employee Login** *(must have)*  
  Provides secure login functionality for employees to access the redemption platform.

3. **Employee Logout** *(must have)*  
  Allows employees to securely log out of their session once they are done using the platform.

4. **Admin Superuser Access to Panel** *(must have)*  
  Enables the admin superuser to log in and access the redemption platform and admin panel, for managing catalogue and employees profile.

5. **Employees View Profile Details** *(could have)*  
  Employees can view their profile page, including basic personal information, login details, redemption records and points balance.  

---

#### **EPIC - Admin Management**  
1. **Add New Reward** *(must have)*  
  Admins can add new items to the gift card catalogue, including details like name, description, points required, etc...

2. **Edit Existing Reward** *(should have)*  
  Admins can modify details of existing gift card, such as updating the item name, description, or point value.

3. **Delete Reward** *(should have)*  
  Admins can remove gift card from the catalogue to keep the list up-to-date and relevant.

4. **Access to Full Catalogue** *(should have)*  
  Admins can view the full catalogue from the platform, including items with zero stock, so they can manage inventory effectively.

5. **Manage User's Points Balance** *(should have)*  
  Admin can view, add, or deduct points from an employee’s balance for reward redemption.

6. **Manage Redemption Records** *(should have)*  
  Admin can view, search, modify, or cancel redemption records to ensure accurate transaction history and points balance adjustments.

---

#### **EPIC - Redemption Process**  
1. **Browse Available Gift Card** *(must have)*  
  Employees can view the full list of available gift card.

2. **Access Detailed Page** *(should have)*  
  Employees can view detailed information about a specific gift card, including its description and points required.

3. **Add Gift Card to Cart** *(must have)*  
  Employees can add gift card to their cart before proceeding to redeem.

4. **View Cart** *(must have)*  
  Employees can review the list of gift card added to their cart, including the total points required.

5. **Modify Cart** *(should have)*  
  Employees can update the quantity or delete gift card from their cart before finalising the redemption.

6. **Redeem Items** *(must have)*  
  Employees can finalise the redemption process, confirming their selected gift cards and updating their points balance.  

---

### **2.4. Visual Design**

#### **Wireframes**  

Wireframes were designed to outline the layout and functionality of each page and to help visualise the user flow. This ensures the platform’s structure is logical, responsive, and user-friendly.  
[Balsamiq](https://balsamiq.com/?gad_source=1&gclid=CjwKCAiAm-67BhBlEiwAEVftNlJTamA65VQDctZEK7owZeyEq-JZFKrhXC3gEYcO3MafEUiVCTYcwBoCwXQQAvD_BwE) was utilised to craft the detailed wireframes. These initial sketches served as the foundation for the app’s final structure and layout.

  <details>
    <summary>Login Page Wireframe</summary>
    <img src="images-documentation/wireframes/log-in_page.png">
  </details>  

  <details>
    <summary>Catalogue Home Page Wireframe</summary>
    <img src="images-documentation/wireframes/plateform_landing_page.png">
  </details>  

  <details>
    <summary>Gift Card Details Page Wireframe</summary>
    <img src="images-documentation/wireframes/plateform_product_details_page.png">
  </details>  

  <details>
    <summary>Cart Page Wireframe</summary>
    <img src="images-documentation/wireframes/cart_page.png">
  </details>

#### **UI Design Approach**  

The platform follows a **modern, clean design** with an emphasis on usability and accessibility.  

- **Mobile-First Approach** – Optimised for all screen sizes.  
- **Workhuman-Inspired Colour Palette** – Uses corporate colours for branding consistency.  
- **Typography Choices** – Ensures readability and modern aesthetics.

---

#### **Typography & Colours**
For this project, I aimed to offer a **fresh and distinct** version of the existing platform while keeping the functionalities simple and user-friendly.    
The colour palette also draws inspiration from the tech industry and current **design trends**, creating a clean, professional, and modern aesthetic.  
The chosen typography ensures **readability** and enhances the overall user experience, while the colour scheme provides a visually appealing and accessible interface.


![Colour Inspiration](images-documentation/readme_images/color_scheme.png)

| **Colour** | **Name**             |  
|------------|----------------------|  
| #300E82  | Persian Indigo       |
| #586BBE  | Savoy Blue           |
| #9B6B82  | Mountbatten Pink     |
| #DECD62  | Citron               |
| #484848  | Davy's Grey          |

</br>

<details>
  <summary>Click to view inspiration from Workhuman website</summary>
  <img src="images-documentation/readme_images/colours_inspiration_from_workhuman.png">
</details>

<details>
  <summary>Click to view inspiration from Unlocking Colour Communication</summary>
  <img src="images-documentation/readme_images/trends.webp">
</details>

---

To ensure readability and maintain a clean, modern look, the following fonts were chosen:

- **Primary Font**: *Poppins*  
  - Applied to the **main body text** for a clean and professional look.  

- **Secondary Font**: *Quicksand*  
  - Used for **decorative elements** and **highlighted text**, adding a modern touch.  

---

### **2.5. Project Planning and Agile Approach**

The development of **RedeemIt** followed an **Agile methodology**, allowing for incremental improvements, flexibility, and structured task management. 
By breaking the project into smaller **user stories**, it ensured a smooth workflow while staying aligned with user needs.  


The following tools and techniques were used:  

- **Lucidchart**: Used to map out the user flow within the platform.  
  <details>
    <summary>Click to view Flowchart</summary>
    <img src="images-documentation/readme_images/redemption_platform_flowchart.png">
  </details>

</br>

- **GitHub Projects**: Tracked tasks with acceptance criteria and iterations, ensuring a structured development cycle.  
  <details>
    <summary>Click to view Kanban Board</summary>
    <img src="images-documentation/readme_images/kanban.png">
  </details>  
    <details>
    <summary>Click to view User Story Detail: Task & Acceptance Criteria</summary>
    <img src="images-documentation/readme_images/user_story.png">
  </details> 

</br>

- **MOSCOW Prioritization**: Applied to categorise features into Must Have, Should Have, and Could Have, ensuring that essential functionalities were developed first.

| **Priority** | **Feature - User Stories** |
|-------------|------------|
| **Must Have (53%)** | Employee Register |
|  | Employee Login |
|  | Employee Logout |
|  | Admin Superuser Access to Panel |
|  | Browse Available Gift Cards |
|  | Add Gift Card to Cart |
|  | View Cart |
|  | Redeem Items |
|  | Add New Reward (Admin) |
| **Should Have (41%)** | Access Detailed Page for Gift Card |
|  | Modify Cart (Update Quantity or Remove Item) |
|  | Edit Existing Reward (Admin) |
|  | Delete Reward (Admin) |
|  | Access to Full Catalogue (Admin) |
|  | Manage User’s Points Balance (Admin) |
|  | Manage Redemption Records (Admin) |
| **Could Have (6%)** | Site User View Profile Details |


## 3. Platform Features

### **3.1. User Interactions & Admin Functionalities**

Employees interact with the platform through an intuitive and structured redemption process:

- **Secure Authentication**  
  - Employees register, sign in and out securely using **Django Allauth**.  

    <details>
      <summary>Landing Page</summary>
      <img src="images-documentation/readme_images/features/landing_page.png">
    </details>
    
    <details>
      <summary>Register</summary>
      <img src="images-documentation/readme_images/features/register.png">
    </details> 

    <details>
      <summary>Sign In</summary>
      <img src="images-documentation/readme_images/features/sign_in.png">
    </details> 

    <details>
      <summary>Sign out</summary>
      <img src="images-documentation/readme_images/features/sign_out.png">
    </details>

    <details>
      <summary>Already Sign In</summary>
      <img src="images-documentation/readme_images/features/landing_page_logged_in.png">
    </details>

- **Browsing Rewards**  
  - Employees can view available gift cards, with access to detailed descriptions, stock and required points.  

    <details>
      <summary>Catalogue Page Employee View 1</summary>
      <img src="images-documentation/readme_images/features/catalogue_page_employee.png">
    </details>

    <details>
      <summary>Catalogue Page Employee View 2</summary>
      <img src="images-documentation/readme_images/features/catalogue_page_employee2.png">
    </details>

    <details>
      <summary>Detailed Page Employee View</summary>
      <img src="images-documentation/readme_images/features/detailed_page_employee.png">
    </details>

- **Redemption Process**  
  - Employees can add items to their cart, modify quantities, and remove items.  
  - The system ensures only users with sufficient points can redeem items.  
  - Upon redemption, points are deducted, transaction recorded in the database and cart is cleared.  
    <details>
      <summary>Cart with Insufficient balance (button disabled)</summary>
      <img src="images-documentation/readme_images/features/cart_insufficient_balance.png">
    </details>

    <details>
      <summary>Cart with Sufficient balance</summary>
      <img src="images-documentation/readme_images/features/cart_sufficient_balance.png">
    </details>

- **Responsive Feedback & Validation**  
  - Employees receive **instant feedback** during the redemption process (e.g., add item, update quantity, redemption successful), using Django messaging.
    <details>
      <summary>Message Item Added To Cart</summary>
      <img src="images-documentation/readme_images/features/added_to_cart.png">
    </details>

    <details>
      <summary>Message Updated Quantity</summary>
      <img src="images-documentation/readme_images/features/updated_quantity.png">
    </details>

    <details>
      <summary>Message Confirm Redemption</summary>
      <img src="images-documentation/readme_images/features/redemption_confirmation.png">
    </details>

    <details>
      <summary>Message Redemption Successful</summary>
      <img src="images-documentation/readme_images/features/redemption_successful.png">
    </details>

---

Admins have full control over the gift card catalogue and user profiles via the admin panel:

- **Manage Catalogue**
  - Add new gift cards with details such as name, points required, stock quantity, and T&Cs.
  - Edit existing gift cards to update descriptions, point values, or stock.
  - Delete gift cards that are no longer available.
    <details>
      <summary>Panel - Catalogue Items List</summary>
      <img src="images-documentation/readme_images/features/admin_panel_catalogue_items_list.png">
    </details>

    <details>
      <summary>Panel - Catalogue Items Detail</summary>
      <img src="images-documentation/readme_images/features/admin_panel_catalogue_items_details.png">
    </details>

- **Manage Employee Profiles**
  - Admins can update employee profiles, including points balances, first and last names.
  - Admins can view and modify redemption records to see who ordered what items, in which quantity.
    <details>
      <summary>Panel - Employee Profile List</summary>
      <img src="images-documentation/readme_images/features/admin_panel_users_list.png">
    </details>

    <details>
      <summary>Panel - Redemption Records List</summary>
      <img src="images-documentation/readme_images/features/admin_panel_redemption_list.png">
    </details>

    <details>
      <summary>Panel - Redemption Records Detail</summary>
      <img src="images-documentation/readme_images/features/admin_panel_redemption_details.png">
    </details>

- **Access to the Platform**  
  - Admins can access the panel directly from the website navigation bar.
  - View the full catalogue, including items with zero stock.  
  - See items with zero stock highlighted to assist in catalogue management. 
    <details>
      <summary>Catalogue Page Admin View 1</summary>
      <img src="images-documentation/readme_images/features/catalogue_page_admin.png">
    </details>

    <details>
      <summary>Catalogue Page Admin View 2</summary>
      <img src="images-documentation/readme_images/features/catalogue_page_admin2.png">
    </details>

    <details>
      <summary>Detailed Page Admin View</summary>
      <img src="images-documentation/readme_images/features/detailed_page_admin.png">
    </details>

---

In cases where a requested page cannot be found or an unexpected error occurs, the platform provides clear error messages to guide users.  

- **Error Pages**  
    <details>
      <summary>Error Page Not found 404</summary>
      <img src="images-documentation/readme_images/features/404_error.png">
    </details>  

    <details>
      <summary>Internal Server Error 500</summary>
      <img src="images-documentation/readme_images/features/500_error.png">
    </details>

---

### **3.2. Entity Relationship Diagram (ERD)**

The platform follows the MVC architecture (Model-View-Controller) to maintain a structured flow: 

- **Model** – Handles database logic (e.g., `CatalogueItem`, `Cart`, `CartItem` models).  
- **View** – Renders templates like `catalogue.html` or `cart.html`.  
- **Controller** – Processes user input and manages data between models and templates.  

The **Entity Relationship Diagram (ERD)** below illustrates how the database models connect and interact. It provides a visual representation of the database schema, showing the **relationships between tables** and the key fields in each table. 

![ERD Diagram](images-documentation/readme_images/redemption_platform_ERD.png)


### **3.3. CRUD Functionality** 

The platform is structured around **CRUD (Create, Read, Update, Delete) principles**, ensuring efficient interaction between employees, admins, and stored data.    

| **Action** | **Admin Functionalities - Admin Panel** | **Employee Functionalities - Front End** |  
|------------|------------------|------------------|  
| **Create** | Add new gift cards to the catalogue | Create a new cart by adding items |  
| **Read**   | View and manage all gift cards | View items in cart |  
| **Update** | Modify gift card details | Adjust items quantity in cart |  
| **Delete** | Remove gift cards from the system | Remove items from cart |  

---

### **3.4. Future Enhancements**

The current version of **RedeemIt** focuses on core functionality, but there is room for expansion and optimisation. Some potential enhancements include:

- **Create a Page for Employee Profile**  
  - Employees can access to their profile page and see their information.
  - Employees can update their personal information (e.g., first and last name).
  - Employees can view records of their past redemptions.  

- **Automated Email Notifications**  
  - New registered employee receives a confirmation by email with his profile main details.
  - Employees and admins receive confirmation emails for transactions.  

- **Cart Enhancement**  
  - Display the number of items present in the cart within the navigation icon to provide a visual cue when items have been added.  

- **Search Functionality for Catalogue**  
  - Enable employees to search for specific gift cards in the catalogue home page, improving navigation and efficiency.  

- **Pagination for Catalogue Home**  
  - Implement pagination in the catalogue home page to enhance user experience when browsing a large selection of gift cards.  

- **Admin Analytics Dashboard**  
  - A data-driven insights panel for tracking redemptions, employee engagement, and points distribution.  

## 4. Technology

### **4.1. Languages**

- **Python** – For backend logic and database interactions.  
- **HTML** – Provides the structure and content of the web pages, utilising a templating language.  
- **CSS** – Handles the styling and layout.  
- **JavaScript** – Enables interactive elements, in this project specifically for displaying Django messages. 

---

### **4.2. Frameworks & Librairies**
 
- **Bootstrap 5** – Used for responsive design and styling components.  
- **Django** – The main web framework used for handling authentication, database management, and routing.  
- **Django Allauth** – Handles user authentication, login, logout, and account management.  
- **dj-database-url** – Simplifies PostgreSQL database configuration via environment variables.  
- **PostgreSQL** – The database storing all user profiles, rewards, and transactions.  
- **psycopg2** – A PostgreSQL adapter allowing Django to interact with the database.  
- **Cloudinary** – Used for storing and managing media files.  
- **Whitenoise** – Enables serving static files in production.  
- **Gunicorn** – A WSGI HTTP server for running the Django application in production.

---

### **4.3. Development & Deployment Tools**

- **GitHub** – Version control system for storing the repository and managing project tasks.  
- **GitPod** – Cloud-based development environment used for initial coding.  
- **VSCode** – Local development environment used after switching from GitPod.  
- **Heroku** – Platform for deploying and hosting the application in a live environment.  

---

### **4.4. Testing & Optimisation Tools**

- **HTML Validator** – Checked for syntax errors in HTML files.  
- **W3C CSS Validator** – Ensured the CSS followed best practices.  
- **JSHint** – Analysed JavaScript code.  
- **Lighthouse** – Audited web pages for performance, accessibility, best practices, and SEO.  
- **Squoosh** – Optimised images by converting them to WebP format, improving loading speed.

## 5. Testing

### **5.1. Manual Testing**  

The following table summarises the key manual testings conducted along the development to ensure functionalities work as expected.  
Tests cover **admin functionalities**, **employee interactions**, **database updates** and followed the user stories and **acceptance criteria**.  


| **Test Category** | **Test** | **Expected Outcome** | **Pass/Fail** |
|------------------------|--------------------|----------------------|---------------------|
| **ADMIN - Catalogue & Employees Profile Management** | Create a new item | Item is successfully created from the panel with all required fields and displayed on the platform catalogue | PASS |
|  | View list of existing items | All items are listed on the admin panel & the redemption platform | PASS |
|  | Edit an existing item | Changes are saved and reflected on the admin panel & the platform | PASS |
|  | Delete an item | Item is removed from both the admin panel & the platform | PASS |
|  | Update Employee Points Balance | When admin updates an employee's points balance from the panel, the new balance is correctly displayed to the employee | PASS |
|  | Stock Management | Items that are out of stock are hidden from employees but remain visible to admins with a highlight indicator | PASS |
| **EMPLOYEE - Redemption Process** | Access to Reward Catalogue | Only in-stock items are displayed, showing key details such as name, points cost, and availability | PASS |
|  | View detailed page of an item | Users can click on an item from the home page to access a detailed view displaying full information | PASS |
|  | Click "Add to Cart" button | The item is added to the cart and the cart page reflects the item | PASS |
|  | Add the same item again | The quantity of the item in the cart increases by 1 | PASS |
|  | View the cart page | The cart displays all added items, their quantity, and total points cost | PASS |
|  | Modify item quantity in cart | Quantity updates correctly, and total points cost is recalculated | PASS |
|  | Update Qty with non-accepted values (<0, letters) | An error message is displayed, preventing invalid values from being submitted | PASS |
|  | Delete an item using the delete icon | Item is removed from the cart | PASS |
|  | Redeem with sufficient balance | Employee's balance is updated in the navigation bar, the cart is cleared, and the *"Continue Shopping"* button is displayed. | PASS |
|  | Redeem with insufficient balance | Button is disabled, and *Oops, xxx points short!* message is shown | PASS |
| **Register, Login, Logout** | User Registration | A new user fills out the registration form and submits it | PASS |
|  | Login with Valid Credentials | A registered user enters the correct username and password and gains access to the redemption platform | PASS |
|  | Login with Invalid Credentials | A user enters an incorrect username or password and receives an error message | PASS |
|  | Logout Functionality | A logged-in user clicks the logout button, confirms logout, and is redirected to the landing page | PASS |
|  | Restricted Access After Logout | A logged-out user cannot access protected pages and is redirected to the login page | PASS |
| **Redemption Logic & Database Update** | Redemption recorded in database | Redemptions are correctly recorded in the admin panel with details including user, items, and quantities | PASS |
|  | Check balance in database | Updated balance shows correctly after redemption | PASS |
|  | Update stock in database | Stock is updated in the database after redemption | PASS |
|  | Reflect new stock in platform | New stock is reflected in both the platform catalogue and the admin panel for employees and admins | PASS |
| **Role-based Accessibility** | Admin - View Full Catalogue | Admin can see all items, including out-of-stock items, which are highlighted | PASS |
|  | Employee - View Available items | Employee sees only items that are in stock; out-of-stock items are hidden | PASS |
|  | Admin - Access Admin Panel | Admin has access to the admin panel from the navigation bar | PASS |
|  | Employee - Access Cart | Employee can view and manage their cart but does not have access to the admin panel | PASS |
| **Immediat Feedbacks** | Sign In | A message confirms *Successful sign in* | PASS |
|  | Log Out | A message confirms *Successful log out* | PASS |
|  | Add an item to cart | A message confirms *Added to cart* | PASS |
|  | Add the same item again | A message confirms *Quantity updated* | PASS |
|  | Remove an item from the cart | A message confirms *Item removed from cart* | PASS |
|  | Redemption | A message confirms *Redemption successful* followed by the order ID | PASS |
| **Error Handling** | 404 Error Page | The 404 error page displays the correct visual and the comment *Oops! Page Not Found* | PASS |
|  | 500 Error Page | The 500 error page displays the correct visual and the comment *Something Went Wrong* | PASS |

---

### **5.2. Automated Testing**
This project was also tested using **Django's** library `unittest` to validate the key functionalities of the catalogue, cart, and redemption process.

All **21 tests passed successfully**, confirming the correct implementation of:
  - **Catalogue**: Listing and viewing rewards  
  - **Cart**: Adding, updating, and removing items  
  - **Redemption Process**: Deducting points, adjusting stock, and clearing the cart  

    <details>
      <summary>Unit Test Results</summary>
      <img src="images-documentation/readme_images/validators/unittest.png">
    </details>

| **Test Category** | **Test** | **Expected Outcome** | **Pass/Fail** |
|------------------------|---------------|----------------------------------|-------|
| **Home Page (URLs)** | `test_homepage` | Confirms homepage loads successfully | PASS |
| **Home Page Template** | `test_homepage_uses_correct_template` | Confirms homepage uses the correct template | PASS |
| **Home Page Access** | `test_homepage_logged_in` | Confirms homepage displays correct access when logged in | PASS |
|  | `test_homepage_logged_out` | Confirms homepage shows login/register buttons when logged out | PASS |
| **Catalogue (URLs)** | `test_catalogue_detail_url_not_found` | Ensures non-existing reward detail page returns 404 | PASS |
|  | `test_catalogue_detail_url_found` | Ensures catalogue detail page loads existing rewards | PASS |
| **Catalogue Access** | `test_catalogue_home_requires_login` | Ensures catalogue home requires authentication | PASS |
|  | `test_catalogue_home_logged_in`  | Confirms that the catalogue home page loads for logged-in users | PASS |
| **Cart Page (URLs)** | `test_cart_page_requires_login` | Confirms that the cart page redirects to login if not logged in | PASS |
|  | `test_cart_page_logged_in` | Ensures cart page loads successfully for logged-in users | PASS |
| **Catalogue Template** | `test_catalogue_uses_correct_template` | Confirms catalogue home page uses the correct template | PASS |
| **Catalogue Display** | `test_catalogue_displays_items` | Ensures catalogue home page displays available rewards | PASS |
| **Cart Display** | `test_cart_displays_items` | Confirms cart page correctly displays added rewards | PASS |
| **Cart Actions (Catalogue Detail Page)** | `test_add_new_item_from_catalogue_detail_page` | Tests adding a new item to the cart from the detail page | PASS |
|  | `test_increase_quantity_from_catalogue_detail_page` | Confirms adding the same item increases its quantity | PASS |
| **Cart Actions (Cart Page)** | `test_increase_quantity_from_cart_page` | Ensures updating quantity from the cart page works correctly | PASS |
|  | `test_delete_item_from_cart_page` | Ensures deleting an item removes it from the cart | PASS |
| **Redemption Process** | `test_redemption_deducts_points` | Ensures user points are deducted correctly after redemption | PASS |
|  | `test_redemption_deducts_stock` | Ensures stock quantity is reduced after redemption | PASS |
|  | `test_cart_is_cleared_after_redemption` | Ensures cart is cleared after successful redemption | PASS |
|  | `test_redemption_is_recorded` | Confirms a redemption record is created after successful checkout | PASS |

#### Key Takeaways from Testing
1. **User Authentication in Tests:**  
   - A **test user** had to be logged in to pass most tests using:  
     ```
     self.client.login(username='testuser', password='testpassword')
     ```  
    Additionally, fake cart items and catalogue entries were created to simulate real interactions and ensure the tests covered expected behaviours.
   
2. **Test-Driven Development (TDD) Reflection:**  
   - Tests were written **after** features were built, rather than before, meaning it **wasn’t a strict TDD approach**.
   - This allowed for verifying existing functionality rather than driving the development process.

3. **Inconsistency Fixes During Testing:**  
   - Found and corrected an inconsistency in the **URL naming** (`redeem-cart` → `redeem_cart`).
   - This was discovered during testing and fixed across urls, views, and templates.  
   
---

### **5.3. Development Challenges & Debugging Process**

During the development process, I encountered various bugs, unexpected behaviors, and technical challenges that required debugging and fixing. These issues ranged from role-based access control problems, UI inconsistencies, and database handling errors to deployment and authentication issues.  
Each bug presented an opportunity to **understand Django better, refine my implementation, and improve code structure**.  

Here a summary of Fixed Bugs & Solutions:

| **Bug** | **Issue** | **Fix** |
|---------|----------|---------|
| Issues with URLs Path logic | View existed but no URL mapping | Added missing URL pattern in `urls.py` |
| Model Not Found Error | Forgot to import model in `views.py` | Added `from .models import ModelName` at the top of `views.py` |
| Static Files Not Loading | Missing `collectstatic` after deployment | Ran `python manage.py collectstatic` |
| Cloudinary Images Not Uploading | Incorrect API key, causing upload failures | Fixed credentials in `.env` |
| UserProfile Not Automatically Created | UserProfile was missing for new users, causing errors | Added Django **signals** (`post_save` for User) to auto-create profiles |
| Form Not Submitting | CSRF token missing, causing security error | Added `{% csrf_token %}` inside the form |
| Form Validation Not Triggering | Missing `required=True` in form field | Added `required=True` to form fields |
| Login Not Redirecting | Incorrect app structure & URL configuration prevented redirects | Restructured app URLs and ensured correct `redirect()` usage in views |
| Unrestricted Access to Catalogue | Users could access `/catalogue/` without logging in | Added `@login_required` to catalogue view |
| Cart URL Conflicting with Slug Pattern | The `/cart/` path conflicted with the catalogue slug URLs | Adjusted `urlpatterns` order in `urls.py` to avoid conflicts |
| Users Could Add Same Gift Card Twice | No distinction between new vs. updated items | Updated message to display either *"Added to cart"* or *"Quantity updated"* |
| RedeemIt Button Didn’t Disable | No validation in template | Used Django template logic to disable the button when user points were insufficient |
| RedeemIt Button Didn’t Submit Form | Redeeming an item required a `POST` request but lacked a form | Wrapped RedeemIt button inside a `<form>` element for proper submission |
| Employees Saw Admin Menu | No role check in UI allowed all users to see admin options | Fixed menu condition to check `user.userprofile.role` before rendering admin links |
| Flash Messages Not Disappearing | No timeout for alerts | Added JavaScript fade-out effect after 3 seconds |
| Admin Panel User Details Missing | Couldn’t retrieve user details (first name, last name, email) in admin view | Added `get_first_name`, `get_last_name`, and `get_email` methods to UserProfile |
| Redeeming Points Shows Incorrect Balance | Points deducted but not saved properly, or redemption processed incorrectly | Ensured `user_profile.point_balance` was updated and saved `user_profile.save()` |
| Users Could Have Multiple Active Carts | Users were allowed to create multiple active carts creating conflicts | Modified `add_to_cart` and `redeem_cart` logic to ensure only **one** active cart per user |
| Redemption Items Not Saving Correctly | Redemption process failed to save selected items | Fixed by properly handling `RedemptionItem` model in `redeem_cart` view |

---

### **5.4. Database Migration**

During development, I realised that I had mistakenly been using a database already associated with another project, which created unintended dependencies. To ensure a clean setup, I decided to migrate to a new database. While following an online guide, I encountered several challenges that required troubleshooting.   

This section outlines the steps taken, the issues faced, and how they were resolved with the valuable guidance and patience of a **Code Institute Tutor**.

#### **Steps Followed for Database Migration**  

1. **Backup Existing Data**  
  - Exported all catalogue items into a JSON file to prevent data loss:  
    ```powershell
    python manage.py dumpdata catalogue --indent 2 > catalogue/fixtures/catalogue_items.json
    ```  

2. **Create a New Database**  
  - Set up a **new PostgreSQL database** and updated the `DATABASE_URL` in both **Heroku** and the local `.env.py` file.  

3. **Reset Migrations & Apply to New Database**  
Since the new database is empty and Django does not recognize previous migrations, we had to reset migrations:  

  - **Fake-initialise migrations:**  
    ```powershell
    python manage.py migrate --fake
    ```  
    - This marks all migrations as applied without actually executing them.  
    - It prevents Django from trying to reapply migrations that were already used in the previous database.  
    - This step ensures Django recognises models without making any unwanted changes.  

  - **Delete existing migration files (except `__init__.py`) to reset migration history:**  
    ```powershell
    Get-ChildItem -Path .\* -Include "migrations" -Recurse | Remove-Item -Recurse -Force
    ```  
    - This removes all migration files across all apps, forcing Django to recreate migrations based on the current models.    

  - **Recreate migrations and apply them to the new database:**  
    ```powershell
    python manage.py makemigrations
    python manage.py migrate
    ```  

At this point, **everything started to break**, leading to migration failures.

---

#### **Issue Encountered & How We Fixed It**  

**Error Message:**  

    ```
    django.db.utils.ProgrammingError: relation "django_site" does not exist 
    LINE 1: SELECT 1 AS "a" FROM "django_site" LIMIT 1
    ```  

1. **Recreate Missing Migration Files**  
  - Manually recreated the `migrations` folders and added `__init__.py` inside each app:
    ```
    catalogue/migrations/__init__.py
    home/migrations/__init__.py
    ```  

2. **Fake-Migrate All Apps**  
  - Each app was individually fake-migrated to allow Django to recognize existing models, like with these examples below:
    ```
    python manage.py migrate home --fake
    python manage.py migrate admin --fake
    python manage.py migrate catalogue --fake
    ```  

3. **Verify Migration Status**  
  - After applying the migrations, checked the current migration status with:
    ```
    python manage.py showmigrations
    ```  

4. **Final Migration Execution**  
  - Once all migrations were properly listed, executed the final migration command:
    ```
    python manage.py migrate
    ```  

5. **Create a Superuser**  
  - Since this is a fresh database, the admin account must be recreated:  
    ```powershell
    python manage.py createsuperuser
    ```  

---

### **5.5. Validators**

#### **CSS - HTML**

To ensure the website's **HTML** and **CSS** follow web standards and best practices, I tested the code using the **W3C validation tools**.  

The [W3C HTML Validator](https://validator.w3.org/) was used to check for syntax errors and compliance with HTML5 standards. The validation returned **no errors**, ensuring that the HTML code is well-structured and correctly formatted.
<details>
  <summary>HTML Validator Results</summary>
  <img src="images-documentation/readme_images/validators/html_validator.png">
</details>  

</br>

The website's stylesheet was tested using the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) to verify CSS compliance. The validation report confirmed **no issues**, indicating that the styles are correctly implemented and follow CSS best practices.
<details>
  <summary>CSS Validator Results</summary>
  <img src="images-documentation/readme_images/validators/css_validator.png">
</details>

---

#### **JavaScript**

To ensure JavaScript code quality and compliance, I tested the file using [JSHint](https://jshint.com/).  
Since I used **ES6 features** such as `const` and arrow functions (`=>`), I also updated the JSHint configuration to **support ES6** by adding `esversion: 6`.  

Results indicate that the JavaScript file maintains **low complexity and readability**, ensuring better maintainability and performance.

<details>
  <summary>JSHint</summary>
  <img src="images-documentation/readme_images/validators/jshint.png">
</details>

---

#### **Python**

To ensure that all Python files follow best coding practices, I used **Flake8** for linting. This tool checks for **PEP 8 compliance** like syntax errors or formatting inconsistencies across the project.  

All identified issues—mostly related to **trailing spaces and minor formatting inconsistencies**—were fixed to ensure full compliance with PEP 8.

To use flake8, I ran the command `flake8` followed by each python file, example below:
```
flake8 redemption_platform/urls.py
```
---

#### **Lighthouse Performance & Best Practices Testing**

To assess web performance, accessibility, and best practices, I used **Google Lighthouse**.  

- **Performance** of home page background image initially scored below **80%**, but after optimizing compression and caching, performance improved.  
- **Best Practices** score was below **60%** due to HTTP links, which I updated to HTTPS, significantly improving the score.
- **Accessibility** improvements, such as adding ARIA labels and refining header hierarchy, helped achieve a **100%** accessibility score.  

However, pages containing images stored on **Cloudinary** received a **Best Practices score of 78%** due to a a third-party cookie warning:

> "Chrome is moving towards a new experience that allows users to choose to browse without third-party cookies."

Since this is related to Cloudinary's external content delivery, I could not find a way to fully mitigate this issue without affecting functionality. Despite this, all other performance aspects, including **accessibility and loading speed**, were optimised.

<details>
  <summary>Lighthouse Home Page</summary>
  <img src="images-documentation/readme_images/validators/lighthouse_home.png">
</details>

<details>
  <summary>Lighthouse Catalogue Page</summary>
  <img src="images-documentation/readme_images/validators/lighthouse_catalogue.png">
</details>

<details>
  <summary>Lighthouse Catalogue Detail Page</summary>
  <img src="images-documentation/readme_images/validators/lighthouse_catalogue_detail.png">
</details>

<details>
  <summary>Lighthouse Cart with items Page</summary>
  <img src="images-documentation/readme_images/validators/lighthouse_cart.png">
</details>

<details>
  <summary>Lighthouse Empty Cart Page</summary>
  <img src="images-documentation/readme_images/validators/lighthouse_empty_cart.png">
</details>

## 6. Deployment

### **6.1. Heroku**

The site was deployed successfully to [Heroku](https://redemption-website-ec86c7604627.herokuapp.com/) following the steps below:

1. In *Gitpod*, create a list of dependencies in `requirements.txt` file:
    - Run `pip3 freeze > requirements.txt` in the terminal.
2. In *Heroku* account, create the new App:
    - Select `New` and `Create a new app`.
    - Name the App and choose a region: `Europe` 
    - Click `Create App`.
3. In the new App page, access to the `Settings` section.
4. In `Config Var` add :
    - `DATABASE_URL` and its value.
    - `SECRET_KEY` and its value.
    - `CLOUDINARY_URL` and its value.
    - Click `Add`.
5. Access to the `Deploy` section.
6. Select the deployment method:
    - Select `GitHub`
    - Search for the repository by taping the name in the search barre.
    - Click on `Connect`
7. Once App deployed, the message *Your app was successfully deployed.*

The live link can be found here: [ReedemIt](https://redemption-website-ec86c7604627.herokuapp.com/)

---

### **6.2. Forking and Cloning**

Forking the repository creates a copy of this project, allowing modifications without affecting the original code. Once the repository is forked, it can be cloned to a local machine for development.</br>
Follow these steps to fork, clone, and work on the project:

- **Fork the repository**
  - Go to the repository you want to fork on [GitHub](https://github.com/).
  - In the top-right corner of the page, click `Fork`.
  - Name the new forked repository, then click `Create Fork`.
  - This creates a copy of the repository under your own GitHub account.

- **Clone the forked repository**
  - In the forked repository on GitHub, above the list of files, click `Code`.
  - Copy the URL for the repository (either HTTPS or SSH).
  - Open a terminal (or Git Bash).
  - Type `git clone`, then paste the copied URL.
  - Press `Enter`.
  - Navigate to the newly cloned repository directory: `cd` and the repository name.

## 7. Credit

### **Content & Resources**
All written content in this project was created by me, with occasional adjustments using **ChatGPT** for clarity and flow—particularly for gift card descriptions, terms & conditions, and brand presentations.

The gift card images were sourced from the respective brands' websites and are hosted via **Cloudinary** for optimised performance.

Additional images were obtained from **Freepik**.

### **Acknowledgements**
A special thanks to my mentors, **Sandeep Aggarwal** and **Julia Konovalova**, for their valuable insights and guidance throughout this project. Their feedback and expertise greatly contributed to refining the functionality and improving the overall structure of **RedeemIt**.  

A huge thanks to the **developer community**, particularly peers in **Slack** for their helpful troubleshooting assistance, **Tutor from the Code Institute**  for their patience and help with my migration mess.  

Finally, a heartfelt thank you to my **husband** for his encouragement and support throughout this project, as well as my **sister** for testing the app and redeeming a lot of points!
