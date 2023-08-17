# PowerProtein
![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/3ef1c980-bde6-48d3-aea4-af1ed0debdd8)

## Suplements E-commerce Store.
> E-commerce website that provide a high quality products for sale as well as expert advice in your health & nutrition and a blog content to share tips to <strong>Elavate Your Health</strong>.

## Click [here](https://powerprotein-cd417ed27158.herokuapp.com/) to live site.

## Author
Giovani Fonseca

# Table of Contents
<details>
<summary>Table of Contents</summary>
  
- [UX](#ux)
  - [Target Audience](#target-audience)
  - [Goals](#goals)
  - [User Stories](#user-stories)
  - [Initial Stories](#initial-stories)
  - [Feasibility vs Importance](#feasibility-vs-importance)
  - [Scope](#scope)
  - [Design Choices](#design-choices)
  - [Wireframes](#wireframes)
- [Information Architecture](#information-architecture)
  - [Entity Relationship Diagram](#entity-relationship-diagram)
  - [Database Choice](#database-choice)
  - [Data Models](#data-models)
- [Agile Process](#agile-process)
  - [GitHub User Stories](#github-user-stories)
  - [Iterations](#iterations)
  - [Progress Boards](#progress-boards)
- [Features](#features)
  - [Implemented Features](#implemented-features)
  - [Future Features](#future-features)
- [Testing](#testing)
  - [Cross Browser and Cross Device Testing](#cross-browser-and-cross-device-testing)
  - [Accessibility Testing](#accessibility-testing)
  - [Validation Testing](#validation-testing)
  - [Automated Testing](#automated-testing)
  - [Defects](#defects)
  - [Defects of Note](#defects-of-note)
- [E-commerce Business Model](#e-commerce-business-model)
  - [Facebook Business Page](#facebook-business-page)
  - [Newsletter Signup](#newsletter-signup)
  - [Links](#links)
  - [SEO Strategy](#seo-strategy)
- [Deployment](#deployment)
  - [Prerequisits](#prerequisits)
  - [Fork and Clone the Repository](#fork-and-clone-the-repository)
  - [Development Deployment](#development-deployment)
  - [Production Deployment](#production-deployment)
- [Credits](#credits)
  - [Content](#content)
  - [Media](#media)
  - [Acknowledgments](#acknowledgments)
</details>
<hr>

# UX
PowerProtein is an e-commerce website designed to provide a seamless and empowering experience for fitness enthusiasts and health-conscious individuals. The primary goal of the website is to offer a wide range of high-quality gym supplements that cater various fitness goals, including muscle building, weight loss and overall fitness improvement. Additionally, the website aims to offer expert nutrition advice with our partners from <strong>iHealthy</strong> and valuable blog content to support users in their health journey and tips.

## Target Audience
PowerProtein consists of fitness enthusiasts, athletes, gym-goers and health-conscious individuals of all levels. Whether they are beginners seeking guidance or seasoned athletes looking for high quality products, the website caters to a diverse audience looking to elevate their fitness journey. 

## Goals
<details>
<summary>Goals Details</summary>
  
**Customer Goals:**
- <strong>Top-Quality Products:</strong> Users should easily find a wide selection of top-quality gym supplements, sports nutrition and health supplements, all carefully curated to meet their specific fitness needs.
- <strong>Shopping Experience:</strong> User should enjoy a user-friendly and intuitive shopping experience, with simple navigation, clear product descriptions and secure payment options.
- <strong>Expert Nutrition Advice:</strong> Through our user-friendly forms, User can provide your details and health preferences. Our tem of certified nutritionists from iHealthy will then carefully review your information and offer personalized nutrition advice to optimize your diet and fitness goals.
- <strong>Stay Informed & Inspired:</strong> Our regularly updated blog content will server as your source of inspiration, featuring workout routines, health tips and motivational stories to keep you informed and motivated on your health journey.

**Business Goals:**
- <strong>Enhance Customer Satisfaction:</strong> Providing expert nutrition advice showcases our commitment to customer well-being, ensuring their success and satisfaction with our products.
- <strong>Build Brand Authority:</strong> By collaborating with iHealthy's certified nutritionists, we establish ourselves as a credible and trutworthy authority in the fitness and nutrition domain.
- <strong>Customer Loyalty:</strong> At our core, we focus on providing an exceptional user experience and fostering strong customer loyalty. This approach leads to repeat purchases and establishes long-term relationships with our customers.
- <strong>Increase Social Presence:</strong> Engaging blog content and social media promotion are expected to attract more visitors, increasing overall website traffic and brand exposure.
- <strong>Never Stop Improving:</strong> Through user's feedback and data analysis, we continually enhance our offerings and services to deliver the best possible experience to our customers.

**Place Owner Goals:**
- I want to ensure that my website is easily found on the website. 
- I want users to share positive reviews and feedback about their experience with our supplements.
- I want to add and promote new supplement products to our online store's, to keep our product offering fresh and meet the diverse needs of our customers.
- I want users to purchase and try our supplement products, so I can track the popularity of each item.
- I want to have control over the product listings displayed on our store's, allowing us to add new products, update prices, description and delete products. 
- I want the ability ti easily update and manage my store's details on the website such as contact information, shipping policies and promotions.
- I want to ensure that ratings and reviews for our supplement products are genuine and reflect real customer experiences, without any misleading information.

**WebSite Goals:**
The primary goal of PowerProtein's website is to provide a seamless and user-friendly online platform for selling supplements and fitness products. The website aims to cater to fitness enthusiasts, athletes and health-conscious individuals by offering a wide range of high-quality supplements and nutritional products. In addition to serving customers, PowerProtein has several business-oriented objectives to ensure its success and growth:

1. **User Experience:**
   - Create an intuitive and visually appealing website design that allows customer to easily navigate and find the products.
   - Implement a user-friendly search and filtering system to enable customer to quickly locate specific supplements based on their fitness goals and dietary preferences.
   - Optmize the website for fast loading times and seamless performance across multiple devices to increase user satisfaction and encourage repeat visits.

2. **Trust Building:**
   - Offer informative and engaging content, such as blogs and expert advice on fitness, nutrition and health-related topics to establish PowerProtein as a reliable source of information.
   - Encourage customer reviews to build trust and credibility, showcasing the positive experiences of previous buyers.

3. **Segure & Seamless Checkout Process:**
   - Implement security measures to protect customer data and ensure a safe online shopping experience, intilling confidence in customers to make purchases.
   - Steamline the checkout process with easy-to-use payments options, fast order processig to provide a seamless shopping experience.
</details>
<hr>

## User Stories
<details>
<summary>User Stories Details</summary>

- As a new customer I want to create an account in the website so that I can easily manage my profile.
- As a registered user I want to login and logout of the website so that I can access my account securely and protect my information when I'm done using the site.
- As a User I want to recover my password so that I can regain access to my account if I forget my login credentials.
- As a new user I want to receive an email to verify my account after registering so that I can ensure the security of my account and access all the features of the website.
- As a registered user I want to have a personalized user profile so that I can update my personal information and view my order history.
- As a Shopper I want to view individual products details on the website so that I can make informed purchasing decisions, as being able to see product images, descriptions, prices and product rating.
- As a Shopper I want to view the total of my purchase on the website so that I can see the cost of all the item in my shopping bag.
- As a Shopper I want to sort products by price, rating or category so that I can easily find products that meet my preference and needs.
- As a Shopper I want to search for products on the website so that I can quickly find specific items I am interested in.
- As a Shopper I want to view all products on the Products page so that I can explore the entire range of available products in one place.
- As a Shopper/Visitor I want to be able to navigate the website easily by using the navbar to choose specific products categories so that I can quickly find products that match my interests.
- As a Shopper I want to adjust the quantity of individual items in my shopping bag so that I can easily make changes to my purchase before proceeding to checkout.
- As a Shopper I want to have a Shopping bag feature on the website so that I can easily add and manage the items I wish to purchase before checkout.
- As a Shopper I want to be able to remove items from my shopping bag so that I can easily adjust my purchase and remove any item that I don't want.
- As a Shopper I want to be able to fill the form details and securely provide my payments details so that I can complete my purchase.
- As a Shopper I want to view the order summary, including the selected products, their quantities and grand total so that I can double-check my purchase and ensure everything is correct before finalizing the transaction.
- As a Shopper-Authorized User I want to be able to write and submit product reviews so that I can share my experiences and opinions.
- As a Shopper-Authorized User user I want to be able to update or delete my product reviews so that I can edit my feedback if my opinion changes.
- As a Shopper I want to access a page that displays all the reviews so that I can read and evaluate the feedback of other users.
- As a Admin I want to have the capability to add new products to the website so that I can keep the product catalogue up-to-date.
- As a Admin I want to have the capability to edit and delete products on the website, such as name, description, price, images and category so that I can maintain accurate and relevant product information.
- As a Admin I want to have control over customers reviews on the website so that I can ensure the reviews are genuine, appropriate and helpful for other users.
- As a Admin I want to have the capability to edit and delete inappropriate or fake reviews so that I can maintain review integrity and quality of user content.
- As a Admin I want to have the capability from the panel log admin see and monitor, views customer orders, grand total and products details so that I can ensure a smooth and efficient user experience.
- As a Shopper/Visitor I want to be able to view blog posts on the website so that I can stay informed and learn valuable information.
- As a registered user I want to be able to like a blog posts so that I can express and interact with the content.
- As a Admin I want to have full control over the blog posts such as create, edit, delete, publish and unpublish so that I can manage and curate the content effectively.
- As a Shopper/Visitor I want to be able to request an expert advice form, fill out the details so that I can seek personalized advice and guidance related to fitness, nutrition or any specific health-related queries.
- As a Admin I want to have access from the panel log admin to the form submissions so that I can review and send the inquiries to our partners, who will provide personalized expert advice.
- As a Admin I want to be able to review and delete form submissions so that I can manage the list of inquiries and maintain the relevancy and organization of the data.
- As a Shopper/Visitor I want to be able to subscribe to the website's newsletter so that I can receive the latest updates, promotion and news.
- As a Admin I want to have access from Mailchimp website to the list of subscribed users so that I will be able to manage the newsletter subscriptions.
</details>
<hr>

## Feasibility vs Importance
<details>
<summary>Feasibility vs Importance Details</summary>

| **Opportunity/Feature**           | **Feasibility/Viability** | **PurposeLevel of Importance** | **In Or Out** |
|-----------------------------------|---------------------------|-----------------------------------|---------------|
| User Registration and Login       | 4                         | 5                                 | In            |
| Product Catalog                   | 5                         | 5                                 | In            |
| Product Search Functionality      | 4                         | 4                                 | In            |
| Product Details Page              | 5                         | 4                                 | In            |
| Add to Bag Functionality          | 4                         | 5                                 | In            |
| Shopping Bag (View & Edit)        | 4                         | 5                                 | In            |
| Checkout & Payment Processing     | 5                         | 5                                 | In            |
| Order Confirmation                | 5                         | 4                                 | In            |
| User Profile & Account Management | 4                         | 4                                 | In            |
| User Reviews & Rating             | 4                         | 4                                 | In            |
| Blog Section                      | 4                         | 3                                 | In            |
| Expert Advice Section             | 3                         | 4                                 | In            |
| Privacy Policy Page               | 5                         | 3                                 | In            |
| Advertisement Integration         | 3                         | 3                                 | Out           |
| Mobile App Development            | 3                         | 5                                 | Out           |
| Social Media Integration          | 4                         | 3                                 | Out           |
| User Wishlist                     | 3                         | 3                                 | Out           |
| Live Chat Support                 | 3                         | 4                                 | Out           |

**Explanation:**
- Features with high feasibility and high importance (scored 4 or 5 in both categories) are essential for the MVP and will be included.
- Features with high feasibility but lower importance (score 4 or 5 in feasibility and 3 in importance) will be considered for inclusion in the MVP but may be prioritized lower than other features.
- Features with lower feasibility (scored 2 or 3 in feasibility) will be dropped from the MVP as thet may required signifant resources.
- The "In" features represent opportunities that have a high feasibility or importance score and will be included in the MVP of the PowerProtein website.
- The "out" features represent opportunities that have a lower feasibility or importance score and will not be included in the MVP of the PowerProtein website.
- Advertisement Integration is considered "out" due to lower feasivility score 3 and complexity that might be involved, the importance level of 3 suggest is not a to priority for the MVP.
- Mobile App Development is considered "out" due to higher complexity and resource requirements it demands. As an MVP, the focus will be only the website.
- Live Chat Support is considered "out" due to relatively lower importance compared to other core features. It may be considered in the future iterations.
- Social Medial Integration and User Wishlist are considered "out" as they are additional features that are not critical for the initial release. It may be considered in the future iterations.
</details>
<hr>

## Scope
To align the project goals with the available resources and skill set, the scope has been refined to focus on delivering a MVP that prioritizes essential features and functionality.
1. **Product Catalog:** A well-organized product catalog will be at the heart of the website, allowing users to browse and search for various supplements based on categories, brands and specific health goals.
2. **User Accounts:** The website will support user accounts, enabling customers to create profiles, manage their orders and see their orders history.
3. **Shopping Bag & Checkout:** Shoppers will be able to add products to their shopping bag and proceed to a smooth and secure checkout process, ensuring a seamless buying experience.
4. **Product Reviews:** A review page will be implemented, enabling customers to provide feedback and ratings for products they have purchased. This feature will help build trust and guide future customers in their purchasing decisions.
5. **User-Friendly & Responsive Design:** The website will be optimized for various devices, ensuring a consistent and user-friendly experience for both desktop and mobile users.

## Design Choices
<details>
<summary>Design Choices Details</summary>
  
### Colors

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/8428f0b8-4245-4849-a75c-a4142908e60f)

The color palette chosen for the PowerProtein website is carefully selected to resonate with the target audience and evoke specific emotion related health, vitality and fitness. The colors aim to create a visually appealing and inviting atmosphere while maintaining a professional and trustworthy image.
- **#261F1D(Dark Brown):**  This color was taken from the hero-image, is represents stability and reliability. It provides a strong foundation for the website, portraying PowerProtein as a dependable source for fitness products.
- **#FEFEFE(White):** White is utilized for the main navigation background, ensuring clarity and simplicity. It complements the other colors and gives a clean and modern appearance, enhancing readability.
- **#182C2A(Dark Green):**  This color was taken from the hero-image, dark green signifies growth, health and balance. It adds vibrancy to the design, drawing attention to important elements and encouranging users to take action.
- **#E1D6D0(Light Beige):** Light Beige complements the other colors and provides a sense of calmness, creating a welcoming and approachable feel.
- **#CD8F73(Light Brown):** It brings warmth to the overall design and encourages user to engange with our website.
- **#000(Black):** The black color is used strategically to provide contrast and emphasize certain elements, such as buttons, brand name and headings. It creates a sense of sophistication and elegance.
  
Together, these colors work cohesively to create a visually appealing and user-friendly interface, where users can confidently explore our range of fitness products and embark on their journey to a helthier and fitter lifestyle.

### Typography
The typography on the PowerProtein website is carefully chosen to complement the overall design and enhance the user experience. The primary font used is **"Rubik"**, which offers a modern and clean appearance. It ensures readbility and consistency across diferent devices. Headings are set with appropriate font-size to grab the user's attention and guide them through the content effectively. Buttons and importat call-to-action elements have slightly large font sizes to make them stand out.

### Images
- **Hero image:** The image of a woman training in boxning embodies empowerment, strength and determination. We wanted to showcase that women are an integral part of the world of sports and fitness, breaking stereotypes and embracing their inner strength. This aligns with our vision of inclusivity and promoting gender quality in sports and fitness.
- **Logo:** The word **POWER** in the logo immediately conveys a sense of strength and energy, suggesting that our products are designed to provide a powerful boost their fitness and overall well-being. The **PROTEIN** highlights the primary focus of our brand-fitness and nutrition. It communnicates that our products are protein-based, which is essential for muscle building, recovery and maintaining a healthy lifestyle.
- **Star Icon:** The star icon is associated with excellence, achievement and recognition. In our context, using the star icon indicates that our products and services are exceptional and of high quality and also serves as a reference for users.
</details>
<hr>

### Design Elements
🚀 **merit & beyhond**

- list out the type of elements you want to use on your site, this will help you when choosing a framework and goes hand
  in hand when doing the wireframes. If you did something out of the ordinary, or think something was particularly
  clever, add a sentence and a screenshot or reference the file the code or css is in.

> - desktop navigation
> - mobile navigation
> - footer
> - containers/cards
> - buttons
> - text input
> - textarea inputs
> - dropdowns
> - modals/layers
> - check boxes
> - pagination
> - date pickers
> - maps
> - images
> - tooltips
> - icons
> - tabbed content
> - file pickers
> - video players
> - audio players

### Animations and Transitions
🚀 **merit & beyhond**

- discuss any special animations or transitions you've programmed
- special hover state effects

### Frameworks
I chose to use Bootstrap for my website because it allowed me to quickly and easily create a responsive design that works well on different devices. the pre-designed templates and components also helped me to save time in the development process.

### Custom Styles
- [Bootstrap Code (modal) - Reviews](reviews/templates/reviews/reviews.html)

### Custom Javascript
- [JS Code (quantity btn) - Products](products/templates/products/includes/quantity_input_script.html)
 Decrement and increment buttons fixed and working for both mobile and desktop.
- [JS Code (scroll-to-top btn) - Products](products/templates/products/products.html)
  A new scroll-to-top button more smooth


## Wireframes
<details>
<summary>Wireframes Details</summary>
  
**Home Page:**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/1e2c8427-c12b-413f-b735-052389f95d09)

**Add Review:**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/9a68b3c1-21a1-42bf-8b45-52040851b316)

**Edit Review:**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/6d7aac70-4005-489f-a92f-321424971c04)

**Product List:**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/951fcdad-f692-40db-b3c2-42d6c4e4c70d)

**Product Details:**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/211f5d61-5007-4bad-9850-189938a30c22)

**Expert Advice:**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/9b5dbb00-efc9-4268-a40a-794b33dee778)

**Blog:**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/4c05ad62-d2f1-4eaf-9387-976563ccb580)

**Post Detail:**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/d6abad5a-922a-498d-8a4e-85d8a1c7a4dc)

**Post Detail(with like - mobile view):**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/ac0a0019-4777-4f6b-98e0-492e5ba4eb00)

**Product List (Tablet View):**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/f2c7d22c-1d2e-40f1-a792-391052563f81)
</details>
<hr>

## Information Architecture
<details>
<summary>Information Architecture Details</summary>
  
For the Powerprotein website, I have implemented models for Blog, Expert Advice and Reviews in Django to provide engaging and informative content to users. Here is how the data model is structured:
1. **Blog Model:**
   - Title(CharField): The title of the blog post(max length: 200 characters).
   - Slug(SlugField): A URL-friendly version of the title used for the post's URL.
   - Author(ForeignKey): A reference to the user model, indicating the Author.
   - Updated On(DateTimeField): The date and time when the blog post was updated. 
   - Content(TextField): The main content of the blog post.
   - Featured image(ImageField): An optional image associated with the blog post.
   - Excerpt(TextField): A short excerpt or summary of the blog post.
   - Created On(DateTimeField): The date and time when the blog post was created.
   - Status(IntegerField): Indicates whether the post is a draft or published (0: Draft, 1: Published).
   - Likes(ManyToManyField): A relationship with user model, allowing users to like the post.
   - Cross-Sell(ForeignKey to Product): A reference to the Product model, allowing cross-selling related products in the blog post.

2. **Expert Advice:**
   - Name(CharField): The name of the user submitting the expert advice inquiry.
   - Email(EmailField): The email address of the user.
   - Message(TextField): The user's message to our nutritionist.
   - Created At(DateTimeField): The date and time when the expert advice inquiry was submitted.

3. **Reviews:**
   - Review Title(CharField): The title of review.
   - Name(CharField): The name of the user who submitted the review.
   - Featured Image(ImageField):  An optional image associated with the review.
   - Created On(DateTimeField): The date and time when the blog post was created.
   - Service Review(TextField): The text content of the review, allowing users to share their experiences with us.
   - Service Rating(IntegerField): The rating assigned to the service, ranging from 1 to 5. 
   - Approved(BooleanField): Indicates whether the review has been approved.
   - Carousel Review(BooleanField): Indicates whether the review should be featured in a carousel. 
</details>
<hr>

## Entity Relationship Diagram
<details>
<summary>Entity Relationship Diagram Details</summary>
  
1. **Blog Model:**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/7cd25dc2-c090-4189-85ff-450fe25c887c)

2. **Expert Advice:**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/5287ad70-1e26-434b-97f9-e95cc99f0a75)

3. **Reviews:**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/0cecb240-6ee1-4a1e-8545-a616eb7c8e83)
</details>
<hr>

## Database Choice
I used PostgreSQL as the database for this project. Hosting the application on Heroku allows for easy deployment and scalability, and PostgreSQL is one of the supported and recommemdede databases on the Heroku platform.

## Data Models
<details>
<summary>Data Models Details</summary>
  
### Activities Model
1. **Blog Model:**
The Blog model represents individual blog post authored by administrators. Each blog post contains information such as Title, Author, Content, Feature Image, Excerpt, Status, Likes and Cross-Sell reference.

| **DB Key**     | **Data Type**         | **Purpose**                                                                   | **Form Validation**                       | **DB Processing** |
|----------------|-----------------------|-------------------------------------------------------------------------------|-------------------------------------------|-------------------|
| title          | CharField             | Title of the blog post                                                        | Required, Max length:200 characters       | Trim              |
| slug           | SlugField             | URL-friendly version of the  title                                            | Required, Max length:200 characters       | Trim, lowercase   |
| author         | ForeignKey(User)      | A reference to the user model,  indicating the Author.                        | Reference to User Model                   | -                 |
| update_on      | DateTimeField         | The date and time when the blog  post was updated.                            | Auto-generated on update                  | -                 |
| content        | TextField             | The main content of the blog post.                                            | Required                                  | -                 |
| featured_image | ImageField            | An optional image associated with  the blog post.                             | Optional                                  | -                 |
| excerpt        | TextField             | A short excerpt or summary of the  blog post.                                 | Optional                                  | -                 |
| created_on     | DateTimeField         | The date and time when the blog post  was created.                            | Auto-generated on  creation               | -                 |
| status         | IntegerField          | Indicates whether the post is a draft  or published (0: Draft, 1: Published). | Default: 0 (draft)                        | -                 |
| likes          | ManyToManyField(User) | A relationship with user model, allowing  users to like the post.             | Reference to User model                   | -                 |
| cross_sell     | ForeignKey(Product)   | Related product for cross-selling                                             | Optional,  Reference to the Product model | -                 |

- [x] Create - Blog posts are created by administrators when drafting new content.
- [x] Read - Blog posts are read and displayed to users visiting the blog section of the website.
- [x] Update - Administrators can update existing blog posts to make changes or improvements.
- [x] Delete - Administrators can delete blog posts that are no longer needed.

2. **Expert Advice:**
The ExpertAdvice model stores user-submitted inquiries seeking expert advice from nutritionist. Each inquiry contains the user's name, email, message and the date and time when the inquiry was submitted.

| **DB Key** | **Data Type** | **Purpose**                                                      | **Form Validation**                 | **DB Processing** |
|------------|---------------|------------------------------------------------------------------|-------------------------------------|-------------------|
| name       | CharField     | The name of the user submitting  the expert advice inquiry.      | Required, Max length:100 characters | Trim              |
| email      | EmailField    | The email address of the user.                                   | Required, Valid email format        |  lowercase        |
| message    | TextField     | The user's message to our nutritionist.                          | Required                            | -                 |
| created_at | DateTimeField | The date and time when the expert advice  inquiry was submitted. | Auto-generated on creation          | -                 |

- [x] Create - Users submit inquiries, which are then stored as expert advice inquiries.
- [x] Read - Expert Advice are read and processed by administrators or nutritionits to provide responses.
- [ ] Update - Expert Advice inquiries are not typically updated, but could be marked as "answered" by administrators.
- [x] Delete - Expert Advice inquiries can be deleted by administrators if needed.

3. **Reviews:**
The Reviews model stores user-submitted service reviews, including the review title, username, feature image, content, service rating and approval status.  

| **DB Key**      | **Data Type** | **Purpose**                                                                        | **Form Validation**                 | **DB Processing** |
|-----------------|---------------|------------------------------------------------------------------------------------|-------------------------------------|-------------------|
| review_title    | CharField     | Title of the review                                                                | Required, Max length:100 characters | Trim              |
| name            | CharField     | The name of the user who  submitted the review.                                    | Max length:20 characters            | Trim              |
| featured_image  | ImageField    | An optional image associated with  the review                                      | Optional                            | -                 |
| created_on      | DateTimeField | The date and time of the  review creation.                                         | Auto-generated on creation          | -                 |
| service_review  | TextField     | The text content of the review, allowing users to share their experiences with us. | Max length:400 characters           | -                 |
| service_rating  | IntegerField  | The rating assigned to the service.                                                | Range: 1 to 5 starts                | -                 |
| approved        | BooleanField  | Indicates whether the review has been approved.                                    | Default: False                      | -                 |
| carousel_review | IntegerField  | Indicates whether the review should be featured  in a carousel.                    | Default: False                      | -                 |

- [x] Create - Users can submit reviews which are stored in the Reviews section. The review include a title, username, content, image and rating.
- [x] Read - Reviews are retrieved and displayed for user to view. Approved reviews are displayed on the website.
- [x] Update - Authorized users can update their own reviews. Administrators can also update reviews.
- [x] Delete -  Authorized users can delete their own reviews. Administrators can delete any reviews.
</details>
<hr>

### CRUD Diagrams
<details>
<summary>CRUD Diagrams Details</summary>

- **Bag:**
  
![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/54669ea0-8432-41b3-85d8-b09f609ce52f)

- **Products:**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/b48c4a09-d15c-4769-9865-5ed8a2af2049)

- **Reviews:**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/81658532-0083-4797-821b-ae518e3e8bad)
</details>
<hr>

# Agile Process

## GitHub User Stories
### User Story Templates

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/0c63c8c4-3d97-4523-8d4b-39f3f6c35f9a)


- [**LINK TO THE TEMPLATE**](https://github.com/Giov3ss/PowerProtein/issues/new/choose)

**What to keep in this section**

- include links and/or screenshots of your story template(s)

### Product Backlog
I used Gitpod to track user stories that I prioritized. Here is the link to my project board with those stories:

- [Product Backlog](https://github.com/users/Giov3ss/projects/4)

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/47ebb87c-6f27-4e67-9336-03d63888e759)

## Iterations
I only did one iteration as I act as the product owner and developer for this project.
- [Iterations](https://github.com/users/Giov3ss/projects/4)

## Progress Boards
- [Iterations](https://github.com/users/Giov3ss/projects/4)

## Features
**Navigation:**
<details>
<summary>Navigation Details</summary>

- **Desktop**
  
  ![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/54fe8e8e-37df-4ae5-adbf-cfb8ebbd94cb)
  
- **Tablet**
  
  ![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/5b521e64-6aee-40e7-950e-290126979c4e)


- **Mobile**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/981c8010-93d1-4347-8228-6718ecdbc33c)

<hr>

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/e998736c-d089-49d3-b603-bea2ca8346f6)

</details>
<hr>

**Sign in/ Sign up:**
<details>
<summary>Sign in/ Sign up Details</summary>
  
- ![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/5feaf0f5-d13b-4567-8aeb-12c45f51b1c6)

<hr>

- ![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/aebcca1c-3f59-4978-885a-4ab856c7112c)
</details>
<hr>

**Products Page:**
<details>
<summary>Products Page Details</summary>

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/4cc2ba54-7a68-4140-b5bd-66f8cc0fd099)

<hr>

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/73f7f12d-c848-4163-8550-1e0b58dfc379)

</details>
<hr>

**Bag & Checkout:**
<details>
<summary>Bag & Checkout Details</summary>

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/fc4e4215-9099-492b-8796-9932023b950b)

<hr>

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/adc838fd-2705-4ccf-9793-d16f8f3e069d)

</details>
<hr>

**Profile:**
<details>
<summary>Profile Details</summary>

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/6d97a49f-016f-4811-b028-3e4c992cefd2)

</details>
<hr>

**Blog:**
<details>
<summary>Blog Details</summary>

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/3ce7ebcd-939f-4215-82a1-1dff15de0df3)

<hr>

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/feac25df-f30c-4fc5-b9e3-3e3b8487ce41)

</details>
<hr>

**Contact Nutritionist Page:**
<details>
<summary>Contact Nutritionist Page Details</summary>

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/e5719b87-4a7f-4a8e-8c5b-47173c9277e8)

<hr>

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/f55baca9-40dd-438a-bd45-06464e72f98c)

</details>
<hr>

**Reviews:**
<details>
<summary>Reviews Details</summary>

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/e609cb76-162c-4c32-a69b-27953d53d4e7)

<hr>

- **(Authorized User - Update)**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/0048c067-28fa-4e60-b334-668e90f8483b)
![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/bb4e15fa-69eb-49c2-ba9c-e0e971a9d888)

<hr>

- **(Authorized User - Delete)**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/acde3dd4-89b6-4151-befb-51b027217450)

</details>
<hr>

**Messages Notifications:**
<details>
<summary>Messages Notifications Details</summary>

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/c4b77f3d-0143-4afe-bd7f-cb3cf0e109ec)

<hr>

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/c122a361-753b-4831-83a9-6bf72d0877e8)

<hr>

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/ab76629b-102c-43aa-a429-bf15f2700cf1)

<hr>

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/37bef96d-3184-4b8b-839f-6a70d1a89cbc)


<hr>

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/ffba0d32-da47-464a-b295-565bab1188d8)

<hr>

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/881be305-3ff4-4dea-9325-625df69194d4)

<hr>

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/f66340dd-39b7-46fa-81b8-7cff3261bd33)

<hr>

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/08cd10aa-f30a-45f4-9ae7-f74e4fc964ad)

<hr>

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/9ea811f1-d527-4aa6-bfef-56bbd7debc96)

<hr>

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/52d6993f-8bc4-4161-98a8-f18ca80fcb68)

<hr>

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/7cded3d3-c1f6-47c8-9feb-b579e5f19f85)

<hr>

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/c82ca60c-b8c3-407a-be38-6f98da133e41)

</details>
<hr>

**Admin Permissions:**
<details>
<summary>Admin Permissions Details</summary>

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/8de72ba3-76e1-4c6a-a489-a396c0b1387b)

<hr>

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/b6d90868-d41d-4560-9c75-011509ffc0e2)

<hr>

- **(As Admin we have the permission to Edit/Delete any review)**
![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/99c347a2-c9d6-430c-8a35-5c65c17a40e8)

</details>
<hr>

### Implemented Features
<details>
<summary>Implemented Features Details</summary>

- **404 Error Page:**
  
  ![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/4ab2ca63-b045-424c-86e4-62d72e3d562b)

<hr>

- **403 Error Page:**

  ![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/cdf4a535-5fb8-4b49-9a74-2a3386750410)

<hr>

- **500 Error Page:**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/e99f6f30-789a-4fb7-b336-777a61a3e550)

<hr>

- **Facebook Business page:**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/26b4edf6-a6de-45f4-9881-fe6ae6d1685e)

<hr>

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/73c02841-fad0-43b2-a1a4-c9188085cdcd)

<hr>

- **Newsletter signup Form:**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/2390c537-f4b6-41b2-b36a-56e80bcae96e)


</details>
<hr>

## Future Features

- **Wishlist & Favorites:** Implementing a feature that will allows users to favorite products for later with a wishlist, ensuring they never miss out on products.
- **Customer Support-LiveChat:** Implementing a live chat support system to provide instant assistance and answer any queries.
- **Personalized Discounts:** Offer personalized discounts based on user preferences and purchasing behavior.
- **Mobile App:** Create a mobile app to PowerProtein, providing users with convenient access to our website and other features on their smartphone.
- **Language Support:** Support to cater to a wider user base, allowing users from different regions and languages preferences to access and use the PowerProtein platform.
 
## Compatibility and Responsive Testing
I ensure my site was worked well, and looked nice on a variety of devices & browsers as noted in the table below:

| **TOOL / Device**           | **BROWSER** | **OS**                        | **SCREEN WIDTH** |
|-----------------------------|-------------|-------------------------------|------------------|
| iPhone 14 Plus v16.0        | Safari      | iOS, v16.0                    | 1284x2778 px     |
| iPhone 6S v12.1             | Safari      | iOS, v12.1                    | 375 x 559 px     |
| Samsung Galaxy A52 v11.0    | Chrome      | Android, v11.0                | 412 x 777 px     |
| Moto G9 Play v10.0          | Firefox     | Android, v10.0                | 412 x 804 px     |
| OnePlus 6T v9.0             | Edge        | Android, v9.0                 | 412 x 757 px     |
| Samsung Galaxy A10 v9.0     | Samsung     | Android, v9.0                 | 412 x 734 px     |
| Samsung Galaxy Tab S7 v11.0 | Chrome      | Android, v11.0                | 753 x 1037 px    |
| iPad Mini 4 v11.4           | Safari      | iOS, v11.4                    | 768 x 954 px     |
| windows 11                  | Firefox     | Browser Version 115.0         | 1920 x 955 px    |
| Mac Ventura                 | Safari      | Safari 15.6 on macOS Monterey | 1920 x 955 px    |
| windows 11                  | Yandex      | Yandex & Browser Version=14.12 | 1920 x 955 px   |

### Most Popular browser & Operating System

| Device             | Browser               | Operating System | Description                                              |
|--------------------|-----------------------|------------------|----------------------------------------------------------|
| iPhone             | Safari                | iOS              | Popular combination with significant market share        |
| Android Smartphone | Chrome                | Android          | Widely used browser on the Android platform              |
| Desktop/Laptop     | Chrome                | Windows          | Popular browser on the Windows operating system          |
| Desktop/Laptop     | Chrome                | MacOS            | Popular browser on the macOS operating system            |
| Desktop/Laptop     | Edge                  | Windows          | Microsoft Edge is gaining popularity among users         |
| Other              | Firefox/Samsung/Opera | Various          | Represents a compromise due to limited testing resources |

The choices in the table are base on the browser market share data provided by [gs.statcounter.com](https://gs.statcounter.com/). Chrome and Safari are the dominant browsers, so they are included for testing on different devices and operating systems. Edge is also included as it has a noticeable market share. Since firefox, Samsung Internet and Opera have smaller market shares, they are grouped under the "Other" category to represent a compromise due to limited testing resources.

| **BROWSER**      | **PERCENTAGE** |
|------------------|----------------|
| Chrome           | 63.55%         |
| Safari           | 19.95%         |
| Edge             | 5.13%          |
| Opera            | 2.99%          |
| Firefox          | 2.79%          |
| Samsung Internet | 2.38%          |

**Browser Market Share Worldwide - July 2023**

# E-commerce Business Model
## Facebook Business Page

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/26b4edf6-a6de-45f4-9881-fe6ae6d1685e)

<hr>

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/73c02841-fad0-43b2-a1a4-c9188085cdcd)


- **Audience Engagement:** The Facebook Page serves as a platform to engage with our audience directly.
- **Products Updates:** Keeping our followers informed about new product launches, restocks and upcoming collections.
- **Educational Content:** Sharing informative and educational content related to our products or industry establishes our brand as an authority in the field.
- **Feedback & Insights:** The Facebook page can be a valuable source of feedback, understanding what customers like and dislike helps us improve our products and services.

## Newsletter Signup

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/2390c537-f4b6-41b2-b36a-56e80bcae96e)

- **Audience Expansion:** The Newsletter Signup feature expands our reach beyond existing customers and allows us to engage with a wider audience.
- **Direct Communication:** Subscribers who sign up for the newsletter have explicity shown in our brand. Provide us with a direct and targeted communication channel to becomes a valuable asset for future marketing efforts. 
- **Product & Updates:** Subscribers stay informed about the latest product releases, company news and updates.
- **Relationship Building:** Regular newsletter provide an opportunity to establish a relationship with subscribers.
  
## SEO Strategy
In our SEO strategy, I worked on optimizing our website to increase its visibility in search engines. I took specific steps to refine our keyword selection, optimize descriptions and titles, and intentionally incorporate keywords into our content.

### Keywords
- I dug deep into our industry to identify the key themes, products, and services that "match" our target audience. 
- Through a comprehensive analysis of our competitors' websites, we gained insight into the keywords they target, which helped me refine our own keyword list.
- Our approach covered both short-tailed and long-tailed keywords to cater to varios search queries.

**Short-tail:** gym supplements, fitness supplements, muscle building supplements, weight loss supplements, workout supplements, pre-workout supplements, post-workout supplements, protein supplements, sports nutrition, whey protein, creatine, bcaa, pre-workout, vitamins, men's health supplements, women's health supplements, health supplements, nutritionist, expert advice, affordable prices, fitness tips, workout advice, health guidance, welness insights, nutrition advice, fitness experts, health coaching, workout strategies.

**Long-tail:** Shop high-quality gym supplements designed to enhance your workout, Elevating fitness with finest supplements in Europe, aid in muscle building, weight loss and overall fitness, Browse out extensive selection of high-quality supplements at affordable prices to achieve your fitness goals effectively, Best gym supplements for muscle building, Affordable high-quality workout supplements, Top fitness supplements for men and women, Achieve your fitness goals with quality supplements, Finest sports nutrition supplements in Europe, High-quality protein supplements for athletes, Trusted brand for gym and workout supplements.

### Description
I paid special attention to the description meta tag. These descriptions serve as a concise introduction to our content, incorporating the identified keywords. Additionally, I remain flexible in updating these descriptions whenever the content on a particular page changes.

### Title
Our website's base.html template houses the title tag, allowing us to customize titles for each page. This dynamic approach to titles enhances our SEO efforts.

### Relevant Content
I have purposefully integrated our selected keywords into various elements of our content, including H1 tags, meta data, texts, name of the products, descriptions and more. This strategic integration ensures that our content is not only optmized for search engines but also remains relevant and valuable to our users. 

### Sitemap
I've created a sitemap for the website, ensuring that when it's fully prepared, search engines like Google can efficiently crawl and index its content.
- [sitemap.xml file](https://github.com/Giov3ss/PowerProtein/blob/main/sitemap.xml)

### Robots.txt
To restrict pages that are should be searched by google, authentication and others are blocked to only allow relevant pages to be searched by google.
- [robots.txt file](https://github.com/Giov3ss/PowerProtein/blob/main/robots.txt) 

## Technologies Used
Several technologies have been used to enable this website works:
| Technology               | Description                                                                                                                                          |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Django                   | Django is the framework that has been used in the project, enables efficient development, database interactions and secure authentication.           |
| Python                   | Python is the core programming language that was used to write all of the code in this application, to make it fully functional.                     |
| JavaScript               | JavaScript was used to provide dynamic interactivity to the messages and enhancing the functionality of the  timepicker.                             |
| Bootstrap                | Bootstrap was utilized to ensure a responsive design.                                                                                                |
| Git                      | Git was utilized as the version control system for tracking changes, and maintaining the project's codebase.                                         |
| PostgreSQL               | PostgreSQL was employed as the relational database management system to store and manage the project's data.                                         |
| GitHub                   | Github was used as development environment, code management and tracking of changes.                                                                 |
| Font Awesome             | Font Awesome was used to obtain the icons of the website, enhancing the overall design.                                                              |
| Google Developer Tools   | DevTools was the primary toll for bug detection, testing the responsiveness and resolving issues across the website.                                 |
| Heroku                   | Heroku was used to deploy the website.                                                                                                               |
| CI's pep8                | CI's pep8 tool was used to validate all the python code.                                                                                             |
| Jigsaw                   | Jigsaw was used to validate CSS code.                                                                                                                |
| W3 HTML                  | W3 HTML was used to validate HTML code.                                                                                                              |
| Jshint                   | Jshint was used to validate JavaScript Code.                                                                                                         |
| Coloors                  | Coloors was utilized to generate color palette for the website design.                                                                               |
| AWS Amazon               | AWS Amazon was utilized to store all of my static files and images.                                                                                  |
| Lighthouse               | Lighthouse was used to test the accessibility of the website.                                                                                        |
| Balsamiq                 | Balsamiq was utilized as a tool for creating wireframes, providing a visual representation of the website layout and structure.                      |
| AmIResponsive            | AmIResponsive was used to generate screenshots of the website in various device sizes, allowing for a quick visual assessment of its responsiveness. |
| Markdown Table Generator | Markdown Table Generator was utilized as a tool to create tables in Markdown format.                                                                 |
| Gitpod                   | Gitpod was used to write and edit the project code.                                                                                                  |
| Mermaid                  | Mermaid was used to create all the diagrams.                                                                                                         |                                                                                           

### Languages
- HTML
- CSS
- Python
- JavaScript 

### Frameworks, Libraries & Programs Used
- Django
- Bootstrap
- Git 
- PostgreSQL
- GitHub
- Font Awesome
- Google Developer Tools
- Heroku
- CI's pep8
- W3 HTML
- Jshint
- Coloors
- AWS Amazon
- Lighthouse
- Balsamiq
- AmIResponsive
- Markdown Table Generator
- Gitpod
- Mermaid 


# Deployment
## Prerequisits
To run this project, you need a ElephantSQL & AWS Amazon account:

**ElephantSQL Set Up Account:**
1. Visit the [ElephantSQL](https://www.elephantsql.com/) website.
2. Sign up for an account if you don't have one.
3. After signing in, you will be redirected to the ElephantSQL dashboard.
4. Click on "Create New Instance" to create a new PostgreSQL database instance.
5. Choose a suitable plan for your needs.
6. Configure the database settings, such as the region and database name.
7. Click on "Create" to create the database instance.
8. Once the instance is created, you will see the details of your database, including the hostname, port, username and password.
**Retrieve the Database URL:**
1. In the ElephantSQL dashboard, locate your newly created database instance.
2. Click on the instance to view its details.
3. In the "Details" tab, you will find the connection details for your database, including the URL.
**Set Environmental Variables:**
1. After obtaining the database URL, you need to set it as an environmental variable in your development environment.
2. The specific steps to set environmental variables depend on your operating system and development environment.
3. In general, you can set the environmental variable by adding the following line to your **'env.py'** file or the environment configuration of your development enviroment: **DATABASE_URL=<YOUR_DATABASE_URL>**
4. Replace **"<YOUR_DATABASE_URL>"** with the actual database URL you obtained from ElephantSQL.

<hr>

**AWS Amazon Set Up Account/ AWS S3 Bucket:**
1. Create an [account](https://aws.amazon.com/) on AWS Amazon if you don't have one.
2. Login to your account and within the search bar type in 'S3'.
3. Within the S3 page click on the "Create Bucket".
4. Put the name that you want (i'd recommend naming your bucket to match your Heroku app name) on the bucket and select the region which is closest to you.
5. Uncheck "Block Public Access" and acknowledge that the bucket will be made public. Click on "Create Bucket"
6. Inside the bucket click on "Properties" tab. Below "Static Website Hosting" click "Edit" and change the "Static Website Hosting" hosting option to "Enabled". Copy the default values for the index and error documents and click "Save".
7. Underneath "Object Ownership" select "ACLs enabled".
10. Click on the "Permissions" tab, paste that into the Cross-origin resource sharing (CORS) section:
  ```
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
  ```
10. Within the "Bucket Policy" section. Click "Edit" and then "Policy Generator".
11. Click the "Select Type of Policy" dropdown and selet "S3 Bucket Policy" and within "Pricipal" type "*" to allow all principals. In "Actions" section select "GetObject".
12. Copy the "ARN" that is located in the previous tab.
13. Back to AWS policy generator, paste it into the "Amazon Resource Name (ARN)" box at the bottom. Click on the "Add Statement" button, then "Generate Policy".
14. Copy the policy that's been generated and paste into the "Bucket Policy Editor".
15. Before saving, add /* at the end of your "Resource Key", this will allow access to all resources within the bucket.
16. Once saved, scroll down to the "Access Control List (ACL)" and click "Edit".
17. Next to "Everyone (public access)", check the "list" checkbox and save your changes.

**Identify and Access Management (IAM) Set Up**
1. Search for IAM within the AWS navigation bar and select it.
2. Click "User Groups" that can be seen in the side bar and then click "Create group" and name the group "manage-your-project-name".
3. Click "Policies" and then "Create Policy". There is now a button to go to the next page to add tags. Tags are
optional, but you must click it to get to the review policy page.
4. Navigate to the JSON tab and click "Import Managed Policy", within here search for "S3" and select "AmazonS3FullAccess" followed by "Import".
5. Follow the exemplo bellow:
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:*",
                "s3-object-lambda:*"
            ],
            "Resource": [
                "YOUR-ARN-NO-HERE",
                "YOUR-ARN-NO-HERE/*"
            ]
        }
    ]
}

```
1. Ensure the policy has been given a name and a short description, the click "Create Policy".
2. Click "User Groups". Select your group.
3. Go to the "permissions" tab, open the "Add permissions" dropdown, and click "Attach policies".
4. Select the policy and click "Add permissions" at the bottom.

**Retrieve access keys**
1. Go to IAM and select 'Users'.
2. Select the user for whom you wish to create a CSV file.
3. Select the 'Security Credentials' tab
4. Scroll to 'Access Keys' and click 'Create access key'
5. Select 'Application running outside AWS', and click next
6. On the next screen, you can leave the 'Description tag value' blank. Click 'Create Access Key'
7. Click the 'Download .csv file' button

**Connecting AWS to the Project**
1. Within your terminal install the following packages:

```
  pip3 install boto3
  pip3 install django-storages
```

2. Freeze the requiremenst by typing:

```
  pip3 freeze > requirements.txt
```
3. Add "storages" to your installed apps within your settings.py file.
4. At the bottom of the settings.py file add the following code.
```
if 'USE_AWS' in os.environ:
   # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

  # Bucket Config
  AWS_STORAGE_BUCKET_NAME = 'bucket-name'
  AWS_S3_REGION_NAME = 'region-name'
  AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
  AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
  AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
```
5. Add the following keys in you Heroku app config Vars: 'AWS_ACCESS_KEY_ID' & 'AWS_SECRET_ACCESS_KEY'. This can be found in your CSV file.
6. Add the key "USE_AWS", and set to True in your Heroku app.
7. Remove the "DISABLE_COLLECSTATIC" variable from Heroku.
8. Inside the settings.py file, add the following code into your Bucket config if statement:
```
    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```

9. In your root directory create a file called "custom_storages.py". Add the followinfg code:
```
  from django.conf import settings
  from storages.backends.s3boto3 import S3Boto3Storage
  
  
  class StaticStorage(S3Boto3Storage):
      location = settings.STATICFILES_LOCATION
  
  
  class MediaStorage(S3Boto3Storage):
      location = settings.MEDIAFILES_LOCATION
```
10. Go back to your AWS S3 bucket and click on "Create Folder", name this folder as "Media".
11. In the "Media" file click "Upload > Add files" and select the images for your site.
12. Under "Permissions" select the option "Grant public-read access" and click  "Upload".
 
 
## Fork and Clone the Repository
To make a copy or ‘fork’ the repository:

1. Login to your own GitHub account.
2. Navigate to [my repository](https://github.com/Giov3ss/PowerProtein).
3. In the top right corner of the page, click 'fork' option to create and copy of the original.

## Making a Local Clone
1. Under the repository name, click on the ‘code’ tab.
2. In the clone box, HTTPS tab, click on the clipboard icon .
3. In your IED open GitBash.
4. Changed the current working directory to the location you want the cloned directory to be made.
5. Type ‘git clone’ and then paste the URL copied from GitHub.
6. Press enter and the local clone will be created.

## Development Deployment 
### Running From GitPod or your preferred IDE:
To get started with local development in GitPod or your preferred IDE, follow these steps:

1. Install the GitPod Chrome extension from the Chrome Web Store.
- [GitPod Chrome Extension](https://chrome.google.com/webstore/detail/gitpod-always-ready-to-co/dodmmooeoklaejobgleioelladacbeki)

2. Once the extension is installed, navigate to your forked repository on GitHub.
3. Click on the green "GitPod" button to open the repository in GitPod.
4. After the workspace is created, you can start the development process.
5. Install the Python packages by running the following command in the terminal:
- **pip3 install -r requirements.txt**
6. Create an **'env.py** file in the project's root directory to store your environment variables.
7. In the **'env.py** file, add the following variables:
```
  DATABASE_URL=<YOUR_VALUE>
  DEVELOPMENT=<YOUR_VALUE>
  SECRET_KEY=<YOUR_VALUE>
  AWS_ACCESS_KEY_ID=<YOUR_VALUE>
  AWS_SECRET_ACCESS_KEY=<YOUR_VALUE>
  EMAIL_HOST_PASS=<YOUR_VALUE>
  EMAIL_HOST_USER=<YOUR_VALUE>
```
8. Apply databse migrations to set up the database by running the following command:
```
  python3 manage.py migrate
```
9. Create a superuser account that allows you add and inspect data via Django admin by running the following command:
```
  python3 manage.py createsuperuser
```
10. Start the server by running the following command:
```
  python3 manage.py runserver
```
11. Now you can access the application by opening the provided URL in your browser.

## Production Deployment
To deploy your application on Heroku, follow the steps bellow:

1. **Create a Heroku Account:**
- Visit the [Heroku](https://signup.heroku.com/login) website.
- Sign up for a free account or log in if you already have one.

2. **Create a New Heroku App:**
- Once you are logged in to your Heroku account, click on the "New" button and select "Create new app".
- Choose a unique name for your app. This name will be used in the App's URL.
- Select the region closest to your location for better performance.

3. **Connect the App to Your Git Repository:**
- After creating the app, go to the "Deploy" tab in your app's dashboard.
- Choose the deployment method based on your Git repository: (e.g. GitHub).
- Connect your app to the appropriate repository and branch.

4. **Configure Environment Variables:**
- In the "Settings" tab of your heroku app's dashboard, locate the "Config Vars" section.
- Set the necessary enviroment variables required for your aplication: 
  - e.g DATABASE_URL,
  - AWS_ACCESS_KEY_ID,
  - USE_AWS,
  - EMAIL_HOST_PASS,
  - EMAIL_HOST_USER,
  - SECRET_KEY,
  - USE_AWS,
  - COLLECT_STATIC
- Click on the "Reveal Config Vars" button to add the key-value pairs for your enviroment variables.

5. **Deploy the Application:**
- In the "Deploy" tab, scroll down to the "Manual Deploy" section.
- Click on the "Deploy Branch" button to deploy your application.
- Heroku will start building and deploying your application based on the code from your connected Git repository.

6. **Monitor the Deployment:**
- Once the deployment process is complete, you can view the deployment logs to ensure everything is working correctly.
- In the "Activity" tab, you will find the deployment logs, which can help you identify any issues or errors that may have occured during the deployment process.

7. **Access Your Deployed Application:**
- After a successful deployment, you can access your application by visiting the URL provided in your Heroku app's dashboard.
- Click on the "Open App" button or open the URL in a web browser to see your application live. 

# Credits
🚨**Required**

To avoid plagiarism amd copyright infringement, you should mention any other projects, stackoverflow, videos, blogs, etc that you used to gather imagery or ideas for your code even if you used it as a starting point and modified things. Giving credit to other people's efforts and ideas that saved you time acknowledges the hard work others did.

-[Code Institute Template](https://github.com/Code-Institute-Org/python-essentials-template)
    - The Template for the GUI for this project was provided by Code Institute. This allows for the Command line to be shown and used within the browser.

## Content

Use bullet points to list out sites you copied text from and cross-reference where those show up on your site

## Media

Make a list of sites you used images from. If you used several sites try to match up each image to the correct site. This includes attribution for icons if they came from font awesome or other sites, give them credit.

## Acknowledgments

This is the section where you refer to code examples, mentors, blogs, stack overflow answers and videos that helped you accomplish your end project. Even if it's an idea that you updated you should note the site and why it was important to your completed project.

If you used a CodeInstitute Instructional project as a starting point. Make note of that here too.

