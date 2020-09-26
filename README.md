<div align="center">
<img src="assets/images/multidevicemockup.png" width="350">
</div>

---

# iGrow

---

## Aim of the site

This is a site for vegetable gardeners. Each gardener will have an individual profile that allows them 
to record information about the vegetables they have grown. Initially they wil record the planting details, 
then as the plant grows during the season they will record notes on the growing, finally they will record 
notes on the harvesting. The idea is that they will be able to have a record that allows them to learn from past 
mistakes and problems and become better gardeners. As results are very dependent on individual growing circumstances 
there will be no sharing of experiences with other users.

[Link to live site](https://i-grow.herokuapp.com/) opens in same tab, click back if needed
---

## User stories

"As a new user: I want to understand what the site does and how it can help me. I want to feel that the site 
will be easy and intuitive and that it will serve a purpose to me"

"As an existing user: I want a record of the vegetables I have grown over time, I want to know what has been successful and what has failed."

"As an existing user: I want to be able to update my records according to the lifecycle of plants throughout the growing season, I want to be able 
to track the various stages of growing and use this information to help me  in the future"

"As an existing user: I want this site to be specific to **my** experience and **my** growing conditions rather than using generalized information 
available on other sites"

"As an existing user: I want a record of whether what I grow can be considered a success or not"

---

## Site plan, features & wireframes

### Site plan

Click [Here](static/images/siteplan.pdf) for the site plan, opens in same tab, click back if needed

### Page 1: Landing page

This page will give an overview of what the site purpose is to the user. It will explain what the site can do 
to help them and an overview of how it works. It will also present options to login using 
an existing username & password **or** choosing a link to sign-up

- [Landing page desktop & tablet](wireframes/P1landingdesktoptablet.png) opens in same tab, press back to return
- [Landing page mobile](wireframes/P1landingmobile.png) opens in same tab, press back to return

### Page 2: Signed in page (HOME page for signed in users)

This page will have a personalised welcome, it will show the existing user saved entries in an overview format. It will also 
have buttons to "ADD" (add a record- going to page 6) and "SIGN OUT", which will return to page 1. 
Each entry overview will give the opportunity to "GO TO RECORD" (page 5), "UPDATE RECORD" (page 4) and "DELETE RECORD"

- [Signed in page desktop & tablet](wireframes/P2signedindesktoptablet.png) opens in same tab, press back to return
- [Signed in page mobile](wireframes/P2signedinmobile.png) opens in same tab, press back to return

### Page 3: Sign up page

This page will give an overview of how the site works. It will also have input fields for "NAME", "USERNAME", and "PASSWORD" as well as a 
"JOIN UP" button.

- [Sign up page desktop & tablet](wireframes/P3signupdesktoptablet.png) opens in same tab, press back to return
- [Sign up page mobile](wireframes/P3signupmobile.png) opens in same tab, press back to return

### Page 4: Update page

This page will show the chosen individual record, and allow for all fields to be updated through field entry boxes and an "UPDATE NOW" button. 
It will also have a "DELETE" button.


- [Update page desktop & tablet](wireframes/P4updatedesktoptablet.png) opens in same tab, press back to return
- [Update page mobile](wireframes/P4updatemobile.png) opens in same tab, press back to return

### Page 5: Read page

This page will show the chosen individual record. It will have "EDIT" and "HOME" buttons.


- [Read page desktop & tablet](wireframes/P5readdesktoptablet.png) opens in same tab, press back to return
- [Read page mobile](wireframes/P5readmobile.png) opens in same tab, press back to return

### Page 6: Create page

This page will give the opportunity for the user to create a planting record. It will also have buttons to give the opportunity 
to "ADD & RETURN HOME" or "ADD ANOTHER".


- [Create page desktop & tablet](wireframes/P6createdesktoptablet.png) opens in same tab, press back to return
- [Create page mobile](wireframes/P6createmobile.png) opens in same tab, press back to return

---

## Theme & typography

The site will be clean, simple and east to use. Not too busy or give the user information overload.

Chosen font used throughout is Baloo Thambi 2, chosen for the clean simple and easy to read style.

Colours are designed to be soft and pastel like, the below colour palette was generated using [coolors](https://coolors.co/)

<div align="center">
<img src="static/images/colourpalette.png" width="500">
</div>

## Database features

All data is stored in MongoDB in two collections

- Users - This stores the user's first name, username and password
- Plants - this stores the users records of plantings, designed to be created and updated at three different times:
    - Planting time:
        - Year planted, month planted, what planted, packaging image (an upload of a picture of the seed packet), planting notes
    - Growing time:
        - Growing notes
    - Harvest time:
        - Harvest date, harvest image (an upload of an image of the grown plant), harvest notes and a "Would you grow again?" option

---

## Features left to implement

- 

---

## Technologies used

- HTML, CSS & Python languages
- [Google fonts](https://fonts.google.com/) for Baloo Thambo 2 font used through all pages, opens in same tab, press back to return
- [Favicon.io](https://favicon.io/) to generate favicon,opens in same tab, press back to return
- [Gitpod](https://www.gitpod.io/) IDE used to code, opens in same tab, press back to return
- [GitHub](https://github.com/) To host the repositories for this project and the live website preview, opens in same tab, press back to return
- [Balsamiq](https://balsamiq.com/) used to design wireframes, opens in same tab, press back to return
- [Undraw](https://undraw.co/illustrations) used for cartoon images on site, opens in same tab, press back to return
- [Materialize](https://materializecss.com/) used for the site header & footer, opens in same tab, press back to return
- [Bootstrap](https://getbootstrap.com/docs/4.0/getting-started/introduction/) for layout framework, opens in same tab, press back to return
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) as a framework, opens in same tab, press back to return
- [MongoDB](https://www.mongodb.com/) as the database store
- [Coolors](https://coolors.co/) used for colour palette
- [Material Icons]
- [Hover.css](https://ianlunn.github.io/Hover/)

---

## Testing



---

## Deployment

To deploy this page to GitHub Pages from its [GitHub repository], the following steps were taken: 


 

### How to run this project locally

To clone this project from GitHub:

1. Under the repository name, click "Code".
2. In the Clone with HTTPs section, copy the clone URL for the repository. 
3. In your local IDE open Git Bash.
4. Change the current working directory to the location where you want the cloned directory to be made.
5. Type ```git clone```, and then paste the URL you copied in Step 3.
```console
git clone https://github.com/StuartCox3107/iGrow
```
6. Press Enter. Your local clone will be created.
7. Go to the cloned folder and run index.html

Further reading and troubleshooting on cloning a repository from GitHub [here](https://help.github.com/en/articles/cloning-a-repository).

---

### issues


### Credits & acknowledgements

- [Simen Daehlin](https://github.com/Eventyret) - [The Padwan Project](https://github.com/Eventyret/Padawan) for boilerplate template
- Richard Wells_lead for the README.md Deployment section

---
