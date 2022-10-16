# ReelIn

To create an interactive experience for users which is not only limited to buying products but also living the experiences of others.

## The problem we aim to solve

Increasing user retention by making product marketplaces more engaging and interactive using short videos.
We provide a pluggable microservice along with the accompanying frontend app which companies can integrate into their stack and instantly setup a reels-like experience for their product app directly using their user data and product data. This also gives access to the company to a load of analytics on the basis of reels engagement.

## Features

- View short videos of products (eg: Travel reels for Headout, Clothing reels for Myntra) and option to buy/book from there
- Filter videos on certain meta data (eg: City, dates for Headout experiences)
- Like, Comment, Share a video
- Follow other users of the app
- View liked products by other followed users
- View analytics for different products by video activity

## Flow

The microservice requires the company to expose certain data points from their database(for instance: product data, user data), which is then used by the microservice to generate the entire reels experience - These data points and urls are informed and configurable on first time setup of the service. (This data responsibility is left up to the company since ReelIn has to use their user data and product data but across companies these schemas and architecture vary a lot so its best to leave this abstract and configurable by the end developer)    

The frontend app is also integrated to the main app which then utilizes the API provided by the microservice to create the reels-like experience.

Users can now come on the app and scroll through and interact with the videos of different products, the analytics of which will be made available to the company.

## Codebase

`socialOutFrontend` contains the code for the frontend android app - this will in future be converted into an SDK so that it is super simple for any company to integrate it in the already existing app.    
Currently the frontend app is built on the theme assuming Headout as the company integrating ReelIn

`socialOutBackend` contains the code for the backend microservice which will be configured and run by the company.    
Within this codebase, inside core, the config file `config.py` is the initial configuration required to be completed by the company. This configuration includes mentioning the URL and endpoints of the required data API provided by the company.

`userCompany` contains a mock company API designed to explain how the entire flow would work. Here our example assumes the userCompany as Headout.
