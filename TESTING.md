# Power Protein - Testing Documentation

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/3ef1c980-bde6-48d3-aea4-af1ed0debdd8)

## Accessibility Testing
To ensure our website is accessible, I have conducted extensive testing to ensure that it caters for users with disabilities.

| **PAGE**                                                         | **TEST CASE LINK**                                | **RESULT** |
|------------------------------------------------------------------|---------------------------------------------------|------------|
| Home Page - Lighthouse Audit (Desktop)                           | https://github.com/Giov3ss/PowerProtein/issues/55 | 100        |
| Home Page - Lighthouse Audit (Mobile)                            | https://github.com/Giov3ss/PowerProtein/issues/56 | 100        |
| Products Page - Lighthouse Audit (Desktop)                       | https://github.com/Giov3ss/PowerProtein/issues/57 | 100        |
| Products Page - Lighthouse Audit (Mobile)                        | https://github.com/Giov3ss/PowerProtein/issues/58 | 100        |
| Blog Page - Lighthouse Audit (Desktop)                           | https://github.com/Giov3ss/PowerProtein/issues/59 | 100        |
| Blog Page - Lighthouse Audit (Mobile)                            | https://github.com/Giov3ss/PowerProtein/issues/60 | 100        |
| Blog Post Details - Lighthouse Audit (Desktop)                   | https://github.com/Giov3ss/PowerProtein/issues/61 | 100        |
| Blog Post Details - Lighthouse Audit (Mobile)                    | https://github.com/Giov3ss/PowerProtein/issues/62 | 100        |
| Contact Nutritionist - Lighthouse Audit (Desktop)                | https://github.com/Giov3ss/PowerProtein/issues/63 | 100        |
| Contact Nutritionist - Lighthouse Audit (Mobile)                 | https://github.com/Giov3ss/PowerProtein/issues/64 | 100        |
| Contact Nutritionist (Success Page) - Lighthouse Audit (Desktop) | https://github.com/Giov3ss/PowerProtein/issues/65 | 100        |
| Contact Nutritionist (Success Page) - Lighthouse Audit (Mobile)  | https://github.com/Giov3ss/PowerProtein/issues/66 | 100        |
| Reviews - Lighthouse Audit (Desktop)                             | https://github.com/Giov3ss/PowerProtein/issues/67 | 100        |
| Reviews - Lighthouse Audit (Mobile)                              | https://github.com/Giov3ss/PowerProtein/issues/68 | 100        |
| Reviews (Add/Edit Reviews) - Lighthouse Audit (Desktop)          | https://github.com/Giov3ss/PowerProtein/issues/69 | 100        |
| Reviews (Add/Edit Reviews) - Lighthouse Audit (Mobile)           | https://github.com/Giov3ss/PowerProtein/issues/70 | 100        |
| My Profile - Lighthouse Audit (Desktop)                          | https://github.com/Giov3ss/PowerProtein/issues/71 | 97         |
| My Profile - Lighthouse Audit (Mobile)                           | https://github.com/Giov3ss/PowerProtein/issues/72 | 97         |
| Products Details - Lighthouse Audit (Desktop)                    | https://github.com/Giov3ss/PowerProtein/issues/73 | 100        |
| Products Details - Lighthouse Audit (Mobile)                     | https://github.com/Giov3ss/PowerProtein/issues/74 | 100        |

**NOTES**
- For the test case 71/72 I notice that I got a 97 with a false positive on a contrast issue around the Order Number. When I further inspected with [webaim](https://webaim.org/resources/contrastchecker/), I determined that a 20px font-size with those colors is considered large text, which actually passes WCAG AA standards of accessibility

## Manual Testing
In the Testing section of the README, I extensively conducted manual testing to ensure the functionality and usability of the PowerProtein website. The manual testing process involved following predefined scenarios and documenting the results using a custom issue template on GitHub. To view the detailed testing results, please [CLICK HERE](https://github.com/Giov3ss/PowerProtein/issues).

## Validation Testing
<details>
<summary>Validation Testing</summary>
The following site were used to aid in validation testing:

- **[CSS Validator](https://jigsaw.w3.org/css-validator/)**

**BLOG.CSS:**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/ca4c51d8-f505-4286-916a-0ecb14590416)

<hr>

**CHECKOUT.CSS:**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/586b2df2-fc4f-49d4-be38-dd8b6b9e0f9b)

<hr>

**EXPERT_ADVICE.CSS:**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/e96aa23d-16cf-419e-8a23-b4aab6a6a7c7)

<hr>

**PROFILE.CSS:**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/2329837b-b087-4ac4-b772-60c14dd2818a)

<hr>

**REVIEWS.CSS:**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/2f4bffb6-b34e-4532-a4ea-3b217bc4bcb8)

<hr>

**BASE.CSS:**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/a860d504-7955-44e6-b689-d7df91f4e911)
</details>
<hr>


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
