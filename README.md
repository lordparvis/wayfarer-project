# Wayfarer-Project


## Index:
 - MVP
 - User Stories
 - Wireframes
 - Milestone
 - Dependencies

## MVP

_________________

A travel community for users to share city-specific tips ("posts" or "logs") about their favorite locations around the world.

## User Stories

___________________

### Sprint 1: Basic Auth & Profiles
A user should be able to:

#### Navigate to "/" and see a basic splash page with:
The name of the website.
Links to "Log In" and "Sign Up".
Sign up for an account.
Log in to their account if they already have one.
Be redirected to their public profile page after logging in.
On their public profile page, see their name, the current city they have set in their profile, and their join date.
See the site-wide header on every page with:
A link to "Log Out" if they're logged in.
Links to "Log In" and "Sign Up" if they're logged out.
Update their profile by making changes to their name and/or current city.
See the titles of all the posts they've contributed (start with pre-seeded data).
Click on the title of one of their posts and be redirected to a "show" page for that post.
View post "show" pages with title, author, and content.

### Bonuses

#### A user should be able to:

See a "default" profile photo on their profile page before adding their own photo.
Update their profile photo (consider using Paperclip or Uploadcare).
See their profile photo next to their posts.
Receive a welcome email after creating an account.

### Sprint 2: CRUD
A user should be able to:

#### View the "San Francisco" page (at "/cities/1") including:
The site-wide header.
The name of the city.
An iconic photo of the city.
View a list of posts on the San Francisco page:
Sorted by newest first.
With the post titles linked to the individual post "show" pages.
Use an "Add New Post" button on the San Francisco city page to pull up the new post form.
Create a new post for San Francisco.
Click "Edit" on ANY individual post, and be redirected to the edit form.
Click "delete" on ANY individual post, then:
See a pop-up that says: "Are you sure you want to delete #{title}?"
If the user confirms, delete the post.
Bonuses

#### A user should be able to:

Visit city pages via pretty urls, like "/cities/san-francisco".
Visit user profile pages via pretty urls, like "/users/james".
On a city's page:
See post content truncated to 1000 characters max, with a link to view more.
See a relative published date, e.g. "2 days ago".

## Sprint 3: Validations & Authorization
A user should be able to:

### View city pages for "London" and "Gibraltar".
Verify that a new post they create is successfully published on the correct city page.
A user CANNOT save invalid data to the database, according to the following rules:

A user CANNOT sign up with an email (or username) that is already in use.
A post's title must be between 1 and 200 characters.
A post's content must not be empty.

#### A user is authorized to perform certain actions on the site, according to the following rules:

A user MUST be logged in to create/update/destroy resources.
A user may only edit their own profile and edit/delete their own posts.
Bonuses
A user should be able to:

#### View an error message when form validations fail, for the following validations:
Title must be between 1 and 200 characters.
Content must not be empty.
View only the 10 most recent posts on a city page (pagination), with
A link/button to the "Next" 10.
A link/button to the "Previous" 10.
See a list of the city pages they've contributed to, on their public profile
See the number of posts they've written for each city, next to the city's name in their profile.
View all vagabond cities as markers/pins on a map on the site's homepage.
Click on a pin on the homepage map and be redirected to the corresponding city page.

## Sprint 4: Commenting
Bonuses
A user should be able to:

### Comment on individual posts.
See the number of comments a post has on the post's "show" page.
See the number of comments they've left, on their public profile.
Only add a comment when logged in.
Only edit/delete their own comments.



## Wireframe

__________________

![Wireframe!](https://git.generalassemb.ly/sf-sei-11/django-wayfarer/blob/master/wireframes.png?raw=true "Wireframe")


## Milestones

___________________

- Create Models

- Create Routes

- Create Frontend/Backend

- Polish Application


## Dependencies Installed

_________________________

- psycopg2

- Pillow

- virtualenv

- sqlparse

- pip


## Technologies

___________________

Frontend - HTML, CSS, JS, JQuery

Backend - Python, Django

Database - PostgreSQL


### Created by Jacky, Rock, Ryan, Parvis
