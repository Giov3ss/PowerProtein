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

## User Stories
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

## Feasibility vs Importance

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

## Scope
To align the project goals with the available resources and skill set, the scope has been refined to focus on delivering a MVP that prioritizes essential features and functionality.
1. **Product Catalog:** A well-organized product catalog will be at the heart of the website, allowing users to browse and search for various supplements based on categories, brands and specific health goals.
2. **User Accounts:** The website will support user accounts, enabling customers to create profiles, manage their orders and see their orders history.
3. **Shopping Bag & Checkout:** Shoppers will be able to add products to their shopping bag and proceed to a smooth and secure checkout process, ensuring a seamless buying experience.
4. **Product Reviews:** A review page will be implemented, enabling customers to provide feedback and ratings for products they have purchased. This feature will help build trust and guide future customers in their purchasing decisions.
5. **User-Friendly & Responsive Design:** The website will be optimized for various devices, ensuring a consistent and user-friendly experience for both desktop and mobile users.

## Design Choices
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
🚀 **merit & beyhond**

Explain why you used certain icons and images on your site

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
> - switches
> - accordions/drawers
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
🚨**Required**

- If you use bootstrap, tailwind, bulma, materialize or some other JS/CSS framework, call it out here and why you made
  that choice. (Typically I look at the design elements I want and make sure the framework supports them)

### Custom Styles
🚨**Required**

- call out any overrides you did for bootstrap styles or the framework you used, even if they are fonts and colors,
  perhaps lead assessors to the file of interest in your repo

### Custom Javascript
🚨**Required**

- call attention to any custom javascript you created to help your User Experience you can organize this by functions or
  files

## Wireframes
🚨**Required**

This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of
the design process. These files should themselves either be included as a pdf file in the project itself (in a separate
directory), or hosted elsewhere online and can be in any format that is viewable inside the browser.

- You should minimally have wireframes for desktop and mobile for the pages you are making for you register, login,
  read(list/detail), add, update, delete functionality. Adding a Tablet view will help you get into merit and
  distinction.

You can hand draw these, but CI posts a yearly license in the general channel for Balsamiq which is pretty easy to use.
Here is the [2022 announcement](https://code-institute-room.slack.com/archives/C0L316Z96/p1640099614368000)


# Information Architecture
As part of the requirements for this project you need to have at **least 3 custom data models**.  It's still under discussion what that means, but I'd make 1 original and then update the products to be custom to what you are selling and create another new one. It's this section that discusses your data and how each piece relates to another and draws out the CRUD functionality you built. You must have CREATE, READ, UPDATE & DELETE for at least one model.

## Entity Relationship Diagram
🚨**Required**

Wade Williams wrote a great blog about how to add a django extension to auto create an ERD. https://wadewilliams.com/technology-software/generating-erd-for-django-applications/ You can always draw one out by hand or google sheets. You can also draw this up by hand if you want or use a spreadsheet to show your data model.

## Database Choice
🚀 **merit & beyhond**

Just state you used postgres as the database because the data is relational and heroku serves this up realitvely easily with no cost.

## Data Models
🚨**Required**

Show the accessors you know your data. If you end up using some data models from an example project, call that out and don't be as detailed about writing those up unless you added to them.

Each data model that you created yourself should have its Fields, Field Type and any validation documented.  You should also cross-reference any code in your repository that relate to CREATE, READ, UPDATE, DELETE operations for these models.

*Below is an example of a write up for an Activities Data Model*

> ### Activities Model
> Activities is a table to hold a unique icon image and name values that users have associated with events and places. It helps with sorting events and prevents the need from carrying around two data objects in the larger Events and Places data structures. The purpose of an Activities object is to provide an imagery association to a category.
> 
> | DB Key 	| Data Type 	|          Purpose          	| Form Validation                        	| DB processing    	|
> |--------	|:---------:	|:-------------------------:	|----------------------------------------	|------------------	|
> | _id    	| ObjectId  	| unique identifier         	| None                                   	| n/a              	|
> | name   	| String    	| Name of Activity          	| Required<br>Min 1 char<br>Max 50 chars 	| trim<br>to lower 	|
> | icon   	| String    	| system path to image file 	| Required                               	|                  	|
> 
> Activity entries are used by events, places and filtering.
> 
> - [x] Create - An activity is potentially created when a user successfully creates a place, creates an event, updates an event, or updates a place.
> - [x] Read - The Activities table is read when a user is adding an event, updating an event, adding a place or updating a place, to determine if a new value should be created or not. The activities table is queried for using the name and icon pair, if it is found, the ObjectId is passed to the event and places. If no match is found, a new Activity is created and that ObjectID is passed to the the place or event.
> - [ ] Update
> - [ ] Delete
> 
>  This table has no deletion or updates associated with it. It's strictly create and read. Eventually, maintenance scripts should be written to delete unused/deprecated entries.

> The reading/writing of the activities table is housed in the [what2do2day/activities/views.py](what2do2day/activities/views.py) file.

### CRUD Diagrams
🚀 **merit & beyhond**

This is if you want to go for distinction.  You can also have CRUD diagrams to show them visually how the model is used in your site.

I used [draw.io](https://app.diagrams.net/) and hooked it up to my google drive to create the screenshot below

![image](https://user-images.githubusercontent.com/23039742/154406188-c9beb57a-2fd1-4f26-a8ed-bee320e46e3d.png)


# Agile Process

## GitHub User Stories
🚨**Required**

Now you are ready to start using Git Hub Issues to write your user stories. To get to merit levels you need to show you
have refined stories from Epics to Generic User stories.

### User Story Templates
🚨**Required**

[Here's the lesson](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+AG101+2021_T1/courseware/a4e548ca70)
on how to create a User Story Templates.

If you want a chance at **DISTINCTION**, I'd suggest the following:

- Create an Epic Story template, this would have a title, the story and children stories
- Create a User Story template, this would initially have the title, the story, and a link to the Epic. Then you'd come
  back when you are prioritizing it to include the acceptance criteria, and story points, then again when you are
  working on it and fill in the tasks and adjust the story points if needed.
- Name your stories in a way that it's easy to tie the children to the EPICS by name.

Example:
EPIC: Navigation As a user, I want to have easy to see navigation on the page, so I can intuitively interact with the
site without getting frustrated.

USER STORY: Navigation: Create Template As a developer, I don't want to have copy and paste my navigation on every page.
I want to use a template to house this information, so my code is easier to maintain.

USER STORY: Navigation: Desktop As a user I want clear navigation that is up to industry standards for my desktop
experience, so I can easily find what I need on a website.

USER STORY: Navigation: Mobile As a user I want clear navigation that is up to industry standards for my mobile
experience, so I can easily find what I need on a website without the

[Here is a quick link](https://github.com/maliahavlicek/go-hrvatska/tree/master/.github/ISSUE_TEMPLATE) to some templates I set up for these
[Here is the UX for those templates where you choose a new type of issue](https://github.com/maliahavlicek/go-hrvatska/issues/new/choose)

screenshot of EPIC new issue using template
![image](https://user-images.githubusercontent.com/23039742/165651624-7ff6c839-1824-48df-81a3-fda444f2d7f5.png)


screenshot of USER_STORY new issue using template
![image](https://user-images.githubusercontent.com/23039742/165651758-beac7bc6-f62f-42e5-b8a0-feeefafcd5b4.png)


Note: You can play around with the labels to add an EPIC one and a USER_STORY one or even ones for each MAJOR epic you have or page
https://github.com/maliahavlicek/go-hrvatska/issues/labels 
![image](https://user-images.githubusercontent.com/23039742/165651335-46ab8ff3-4014-4e55-a29d-35e1d998fb42.png)


**What to keep in this section**

- include links and/or screenshots of your story template(s)

### Product Backlog
🚨**Required**

https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+AG101+2021_T1/courseware/a4e548ca70a3473aa890ba2ab9bf612c/085f3a8e344a4cf28b5b5355399abcc1/?child=last
This is the MILESTONE where you grab stories from the issues or USER stories you created and prioritize them and order
them, leave the epics out.

**What to keep in this section**
Include a link to your Product Catalog Milestone,

an initial screenshot, mid-point and final will help document the agile process.

## Iterations
🚀 **merit & beyhond**

https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+AG101+2021_T1/courseware/a4e548ca70a3473aa890ba2ab9bf612c/71fe6c52cccf477688e924c9889f5fec/?child=first

Add links to iteration milestones (most people have ONE iteration since they are the solo worker, just state that here),
it could be that you won't have all your product backlog worked in the end, and that is ok, hte MVP might morph, you
might find other stories you want instead, it's OK.

## Progress Boards
🚀 **merit & beyhond**

https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+AG101+2021_T1/courseware/a4e548ca70a3473aa890ba2ab9bf612c/7ad7f487cc6148ecb182d77feaeda269/?child=first
Add links to Progress boards

# Features
🚨**Required**

In this section, you should go over the different parts of your project, and describe each in a sentence or so and how they tie into  your user stories.

## Implemented Features

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

It's easiest to break this section down into the header, footer, and each page/layer of your website. Call out any differences for mobile vs desktop presentations, **include a screenshot of the implemented feature** and **at least 2 bullet points of their importance**.

**Required for passing**
- Authentication Process
- Custom 404 
- Facebook Business page
- Newsletter signup Form

## Future Features
🚀 **merit & beyhond**

Use this section to discuss plans for additional features to be implemented in the future:

If you end up not developing some features you hoped to implement, you can include those in this section.

# Testing
🚨**Required**

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that
the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and
ensure that they all work as intended, with the project providing an easy and straightforward way for the users to
achieve their goals.


**At this point, you should use gitHub Issues Templates and Test Case** to track test cases and defects. Here's
a [document](https://docs.google.com/document/d/1nDS5tZeMO77Dfq85IZGMSV6C41XaPm9FwcpR3k-UTVc/edit#heading=h.3kdbr3tqbzi)
I put together for this process.

You should make sure your test cases cover the following: 
## Cross Browser and Cross Device Testing
🚨**Required**

To save time, you can create this type of table
in [markdown table generator](https://www.tablesgenerator.com/markdown_tables)

As of Feb 14, 2022 CI students can take advantage of the Student Developer Pack where you have access to great things
like [browserstack](https://education.github.com/pack/offers/#browserstack) You should have received an email about how
to activate your student Developer Pack, here's
a [slack](https://code-institute-room.slack.com/archives/C0L316Z96/p1644946870567999) with details if you can't find it
in the associated thread.

Start with a brief explanation of why you chose the mixture you did. The point is to prove that you looked at the site
across various browsers, operating systems, and viewport breakpoints. You can add a column about the spot checking path
you took or write it out here:

1. Visit https://gs.statcounter.com/browser-market-share to figure out the most popular browsers & operating system combos seen across the we for the geographic region, and platoform(s) and screen sizes you expect your users to belong to. 

1. Include a sentence about why you chose the combinations you did.

1. Create a table that lists out what devices, browsers, and operating system you tested your application on and a brief description of why you chose the mixture you did. The point is to prove that you looked at the site across various browsers, operating systems, and viewport breakpoints.

1. if you can't find the brower/device/OS combinations you want on Browserstack with your github student webpack (or you didn't activate that in time), note what you'd ideally test on then what you ended up testing on as a compromise. 

> **Example:**
> To ensure the code was functional and looked good on varoius devices I tested a couple of generic flows though my site on using the following Tool/Device combinations. The device/browser/and OS combinations were used based on reports found at [browser market share](https://gs.statcounter.com/browser-market-share) taken on MM/DD/YYYY:
>
> | TOOL / Device                 | BROWSER     | OS         | SCREEN WIDTH  |
> |-------------------------------|-------------|------------|---------------|
> | real phone: motog6            | chrome      | android    | XS 360 x 640  |
> | browser stack: iPhone5s       | safari      | iOs        | XS 320 x 568  |
> | dev tools emulator: pixel 2   | firefox     | android    | SM 411 x 731  |
> | browserstack: iPhone 10x      | Chrome      | iOs        | SM 375 x 812  |
> | browserstack: nexus 7 - vert  | Chrome      | android    | M 600 x 960   |
> | real tablet: ipad mini - vert | safari      | iOs        | M 768 x 1024  |
> | browserstack: nexus 7 - horiz | firefox     | android    | LG 960 x 600  |
> | chrome emulator: ipad - horiz | safari      | iOs        | LG 1024 x 768 |
> | browserstack                  | Chrome      | windows    | XL 1920 x 946 |
> | real computer: mac book pro   | safari 12.1 | Mohave     | XL 1400 x 766 |
> | browserstack                  | IE Edge 88  | windows 10 | XL 1920 x 964 |
>
> Here is a link to the [test case](https://github.com/maliahavlicek/ci_mentor_insights/issues/9).

Note, you might find it easier to create a test case for each tool/device and link to the test case in the table here.

## Accessibility Testing
🚨**Required**

You should have test cases for accessibility and links to them here. Start with a brief paragraph and then link to the
test cases. If you are ambitious you can record the screen of you using the keyboard, convert it to a gif and upload it
to the test case too.

**example**
> To ensure that the site was accessible to people with visual impairments, I used chrome's dev tools, lighthouse audits to ensure I had a score in the green for accessibility and that I could keyboard navigate through the page.
>
> Here are links to the test cases for each which contains the screenshot for the lighthouse audit.
> - [home page accessibility test](https://github.com/maliahavlicek/ci_mentor_insights/issues/12)
> - [experience page accessibility test](https://github.com/maliahavlicek/ci_mentor_insights/issues/13)
> - [skills page accessibility test](https://github.com/maliahavlicek/ci_mentor_insights/issues/14)
> - [recommendations page accessibility test](https://github.com/maliahavlicek/ci_mentor_insights/issues/15)
>
> To ensure the site was accessibility to people with physical impairments, I tried to navigate the site using tabbed navigation:
> - [site tabbed navigation test](https://github.com/maliahavlicek/ci_mentor_insights/issues/10)

You can totally combine the tabbed navigation in the accessibility test and have 2 expected criteria, it's all up to
you!

## Validation Testing
🚨**Required**

You should try to ensure you code is valid and follows proper indentation. In this section you should write up any
websites you used to validate your code so there is credit given to those sites. Then add links to the test cases you
put into GitHub for the validation. You can copy your validation success to those tests.

The following site were used to aid in validation testing:

- **[CSS Validator](https://jigsaw.w3.org/css-validator/)**

> If you only have one CSS file, you can just run the validator through one deployed page URL, if you have custom CSS for diffent pages, make sure you hit those different URLS

- **[HTML Validator](https://validator.w3.org/)**

> For each view you wrote, you should validate the HTML and have a test case for it linked to from here
> NOTE: You may need to right-click to view the source of each page and paste that into the validator if you need to go through authentication to get to the page.

- **[JS validation](https://jshint.com)**

> for each .js file, copy the code and paste it into this site, and have a test case for it linked to from here. You can have warnings, but no errors.
> if using ES6, add this before pasting in your file: `/*jshint esversion: 6 */ `, similarily you can update it to 7 if you see warnings about ES7 syntax `/*jshint esversion: 7 */ `

- **[CI's pep8 tool](https://pep8ci.herokuapp.com/)** 

> for each .py file you created, copy the source code and paste it into this site, and have a test case for it linked to from here.
> include a screenshot of results in the test case showing NO ERRORS. (you should do this for all .py files in your repo)
> 
> **run.py**
> 
> ![image](https://user-images.githubusercontent.com/23039742/212106175-36b2f18a-7c75-458d-94dd-9886e81c71f3.png)

> Ideally you would have no errors remaining outside of line too long which you can fix by 
> 
> adding
> ```$python 
> # noqa
> ```
> There is a space before the # and after it to skip the quality assurance for that line.
> 
> Note any errors or warnings you are ignoring and why.

- **[JSON validation](https://jsonlint.com/)**

> for each .json file, you should copy the code and paste it into this site, and have a test case for it linked to from here.

## Automated Testing
🚀 **merit & beyhond**

**NOTE: If you want MERIT or Higher, you MUST have some automated testing**
If you managed to write jasmine tests or some django tests, note those files out here and how to run them.

https://github.com/maliahavlicek/ms4_challenger/blob/master/documentation/TESTING.md is my write up about my automated testing and how I ran them, but a simple test I'd recommend is a views test that tests authentication and any views you limit to superusers or logged in users.

https://github.com/maliahavlicek/ms4_challenger/blob/master/challenges/tests/test_views.py

## Defects
🚨**Required**

At this point you really should be using GITHUB's Issues to track these as it helps you with the AGILE process
requirement as it's really easy to copy/paste screenshots in and then write up how you closed them.

[Here's a brief overview](https://docs.google.com/document/d/1nDS5tZeMO77Dfq85IZGMSV6C41XaPm9FwcpR3k-UTVc/edit#heading=h.542xzc8ufx4x)
I put together on how to do this.

is what my custom tempalte looks like in the UX
![image](https://user-images.githubusercontent.com/23039742/165650359-a352d64e-b128-473d-ab60-7df0568a44df.png)




## Defects of Note
🚀 **merit & beyhond**

Some defects are more pesky than others. Highlight 3-5 of the bugs that drove you the most nuts and how you finally
ended up resolving them. Just create a link to the issues/defect of note.

### Outstanding Defects

It's ok to not resolve all the defects you found. If you know of something that isn't quite right, list it out and
explain why you chose not to resolve it. Again, do this in gitHub and provide a link to the defects you are not closing
and ensure they have a comment in them.

# E-commerce Business Model
🚨**Required**

In this section discuss your business model, how you use  SEO to get users to your site and how you hope to generate more traffic and get sponsors to back link to your site. 

## Facebook Business Page
🚨**Required**

- copy a screenshot of the FB page
- add a couple of bulletpoints about the goals of what this fills for building out followers & special content

## Newsletter Signup
🚨**Required**

- copy a screenshot of the signup 
- add a couple of bullet oints outlining the goals of what this functionality provides for building out followers

## Links
- sponsored links are flagged with rel="sponsored"
- social links and other links that go outside domain have `rel="nofollower"` to signal to search engines that those links are not associated with our specific domain

## SEO Strategy
🚨**Required**

In this section write out the process you used to come up with short tailed and long tailed results to help refine the keywords you came up with. You should call out attention to the following:

### Keywords
Describe the process you went through identifiying keywords that you want Google and other search engines to relate to your site.

### Description
Note that you have a the meat description tag and if any of the content changes based on the page.

### Title
Call out that you have this set in your base.html so it can be changed per page

### Relevant Content
Call out how you purposefully incorporated keywords into your content, H1, meta data etc. 

### Sitemap
🚨**Required**

- [sitemap.xml file]() call out files that exist so browsers can easily crawl site

### Robots.txt
🚨**Required**

- [robots.txt file]() to restrict pages that are should be searched by google, authentication and others are blocked to only allow relevant pages to be searched by google

# Deployment
🚨**Required** 

## Prerequisits
🚀 **merit & beyond**

If the user is required to have certain keys and credentials you should include this section with directions on how to get the necessary information. ex)

1. **Gmail Account:** In order to have verification and forgot password emails sent to registered users you need a
   google account. 
  - [create a gmail accoount](https://accounts.google.com/signup) 
  - [downgrade to less secure](https://myaccount.google.com/lesssecureapps?pli=1) after you are signed into the gmail account, downgrade to less secure
2. **Couldinary URL**
  - [create an account](https://cloudinary.com/)
  - go to the dashboard and copy your API environmental variable
   
    <img width="1230" alt="image" src="https://user-images.githubusercontent.com/23039742/213839829-b4f349b3-419d-4ea2-bbca-90cf3c663bba.png">     
 
## Fork and Clone the Repository
🚀 **merit & beyond**
To keep the main reposotory for this project clean, please fork the repostiory into your own account. GitHub has [forking directions](https://docs.github.com/en/get-started/quickstart/fork-a-repo#forking-a-repository) but here's what you might do:
1. login to your own gitHub account
2. navigate to [my repository](URL OF YOUR LIVE REPOSITORY)
3. In the top right corner of the page, click fork 

![image](https://user-images.githubusercontent.com/23039742/213840378-e785eaa0-712b-468c-bcda-64fde56eae44.png)

4. set yourself as the owner
5. change the name of the repo if you want
6. add a description if you want
7. choose what to copy, typicall the main branch only
8. click the snazy green button

![image](https://user-images.githubusercontent.com/23039742/213840549-5bef12ae-198e-412b-84b6-0cc718b6fa1d.png)

9. To get files to your local environment, you need to clone it: click the code button
10. Copy the url as needed (here's gitHub instructions)[https://docs.github.com/en/get-started/quickstart/fork-a-repo#cloning-your-forked-repository}



## Development Deployment 
🚨**Required** 

This section should describe the process someone would have to go through to get the local working in GitPod, or your preferred IDE. Start from installing the chrome extension then clicking the green gitpod button in THEIR FORKED repository, the enumerate the steps to walk them through the process as if they were brand new to this proccess. **Include screenshots** where applicable.

**Key points to cover** 
- Install required python packages: `pip3 install -r requirements.txt`
- Create env.py
- What to put in the env.py, don’t disclose real values
>  - EMAIL_HOST_PASSWORD=<YOUR_VALUE>
>  - DEFAULT_FROM_EMAIL=<YOUR_VALUE>
>  - EMAIL_USERNAME=<YOUR_VALUE>
>  - SECRET_KEY=<YOUR_VALUE>
>  - CLOUDINARY_URL=<YOUR_VALUE>
>  - DEV=True
- Apply Database Migrations so the database starts up `python3 manage.py migrate`
- Create a super user so you can add and inspect things via django admin  `python3 manage.py createsuperuser`
- Preload data: Sometimes you might want to include steps to create data in the admin or preload a data dump [coderwall blog](https://coderwall.com/p/mvsoyg/django-dumpdata-and-loaddata) has examples on how to dump data and load it which saves a bunch of time when deploying the application from a local database to a hosted database but you don’t  have to do this step
- Start the server `python3 manage.py runserver`


## Production Deployment
🚨**Required** 

This section should describe the process you went through to deploy the project to a server where anyone can access the url without your machine running. This is typically Heroku. **Include screenshots** if you think they would make the process easier. Start with getting an heroku account and then setting up databases and other packages.

If you have project settings required for Heroku, provide a table of the keys and values. Do not share your personal
keys but either cut them out of the screenshot or say <YOUR_VALUE> and include links on how the user would obtain such
values.

**Key points to cover** 
- cerating new app
- setting app name
- setting region
- entering dreaded billing info
- subscribing to a plan
- setting up db
- adding environmental values- have a list or table so user has less chance of typos
>  - EMAIL_HOST_PASSWORD
>  - DEFAULT_FROM_EMAIL
>  - EMAIL_USERNAME
>  - SECRET_KEY
>  - CLOUDINARY_URL
>  - COLLECT_STATIC
- adding build packages
- deploy
- gitHub connection
- auto vs manul deploy
- monotior logs


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

