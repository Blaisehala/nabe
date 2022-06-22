# B L U E B R A V E

#### Author 

[Blaise Hala](https://github.com/Blaisehala)

## Description

BlueBrave  is a trusted environment where all neighbors are verified, making it safe to share online the kinds of things you'd be okay sharing with your neighbours

- Users get can view different posts from their neighborhood
- Users can find neighbourhood business information, police contact and health information 

# GETTING STARTED
* Type the following command in your terminal to clone the repository

 `https://github.com/Blaisehala/nabe.git`

* If you are using SSH, use the following command

` git@github.com:Blaisehala/nabe.git`

When you run the commands successfully, you should have a local version of this repository.

## Pre-requisites 

The vAwwards project requires a prerequisite understanding of the following:
- Django Framework
- Python Virtual environment
- Python3.8
- Postgres Database

[Get more instructions here](https://realpython.com/installing-python/)



## Setup and installation

#### Clone the Repo
####  Activate virtual environment
Activate virtual environment using python3.8 as default handler
    `virtualenv -p /usr/bin/python3.8 venv && source venv/bin/activate`
####  Install dependancies
Install dependancies that will create an environment for the app to run `pip3 install -r requirements.txt`
####  Create the Database
    - psql
    - CREATE DATABASE <databsename>;
####  .env file
Create .env file and paste paste the following filling where appropriate:

    SECRET_KEY = '<Secret_key>'
    DBNAME = 'nabe'
    USER = '<Username>'
    PASSWORD = '<password>'
    DEBUG = True
#### Run initial Migration
    python3.8 manage.py makemigrations gallery
    python3.8 manage.py migrate

#### Run the app
    python3.8 manage.py runserver
    Open terminal on localhost:8000




## Support and contact details 

To make a contribution to the code used or any suggestions you can click on the contact link and email me your suggestions.

- Email: blaisehala@gmail.com 


## Licence

MIT License

Copyright (c) [2021] [Blaise Hala Odhiambo]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, but not to sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:


The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Authors Contact
TEL : +254714775125  

 Email: blaisehala@gmail.com


##### Authors Info 

LinkedIn- [Blaise Hala](https://www.linkedin.com/in/blaise-hala-682aa511a/)

Github - [Blaisehala](https://github.com/Blaisehala)
