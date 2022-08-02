---
title: Deploying a Custom Python Static Site Generator to Azure 
slug: static-site-generator-with-python-azure
date: 02 Aug 2022 08:00
---

> TLDR: Connect your repo to Azure Static Web Apps and use GitHub Actions to build your site via Python.

Static Sites are a great way to provide a custom web experience with little overhead and extremely low costs. For personal sites, it allows you to focus on just creating content removing much of the serving portion of your site to your web host. Product and application developers also use static sites to scale, separating the app from the informational portion of the site. This allows allocation of resources to be directly mostly to the application experience, while still delivering information to your customers quickly.

Furthermore, writing code to build your site is often seen as a way to continuously  develop your skills over time.

I've been working on [my own static site generator][render-engine](SSG) for going on 5 years now. It's developed a lot over time, but one thing is consistent. It's modern python. 

Many folks have used tools like [github pages](https://pages.github.com), [Netlify](https://netlify.com) or [Vercel]() to host simple sites for free, but many of those services have to provide al a carte services at a fee to stay profitable. Also, these are closed systems and don't expand to other services and tools that you may also use in a more professional capacity. 

This year [I joined the Microsoft Cloud Advocacy Team](https://twitter.com/kjaymiller/). In an effort to  1.) move away from Netlify which I was not happy using and 2.) Try out Azure products, I wanted to switch to Azure Static Web Apps.

> **Disclaimer**: I do get paid to advocate for Azure products. That said my ethical stance is to show how I did a thing and I'm sure with a little effort the process I settled on can be replicated to any service.

I first learned about Static Web Apps (SWA) in my first week when the team was celebrating one year of the product. By design, the plan was to serve javascript applications (and a few notable others like Blazor and Hugo) serving any dynamic content via Azure functions. Ultimately, you could use any site generator that outputs HTML.


## Setup Azure Static Web Apps
You can setup Azure Static Web Apps with VS Code following the [Azure Static Web Apps Getting Started](https://docs.microsoft.com/en-us/azure/static-web-apps/getting-started?tabs=vanilla-javascript#install-azure-static-web-apps-extension). There is provides a few options and the closest for you is the vanilla JS route. You can skip the first repo as we already have our blog. I don't want to re-hash the tutorial; here is a quick recap:

1. Open your project's repo in VS Code
2. Ensure that the Azure Extension is installed and you're logged in to your Azure account
3. Select the Azure Side bar menu in the _RESOURCES_ tab select the create icon (plus sign)
4. In the prompt select _Create Static Web App_
5. Run through the wizard
   1. connecting your GitHub account
   2. creating a name for your project
   3. select your preffered region
   4. **IMPORTANT** Selecting **CUSTOM** as the Deployment Method.


This is where things get different for us:
   1. Set your app location to the output path of your project. **If it doesn't exist yet, that's okay**. We'll add it in the next section.
   2. Make sure the build command is set to  

## Getting your site up and running

Sadly, Azure Static Web Apps don't support running python based build commands[^1] but according to the docs it just needs **ONE HTML** file in a folder to build a site. we can give it that file in one of two ways.

### Build then deploy
The first way is rather simple. Build your site locally and push it's contents to GithHub. This requires no change to your existing yaml file. But you will need to manually run the build prior to pushing your commits to version control.

### Use GitHub Actions to Build your site
The way that I build my sites is by modifying my yaml file to include build steps prior to serving the website. While this does work we need to ensure that our build is designed to use the same command everytime.

To build your environment in GH Actions you'll need to add a block to your yaml file **BEFORE** the Azure `Build and Deploy` section. You'll need to include the `setup-python` action and specify the python version you would like to use. Use the major version of your python version so `3.10` and not `3.10.5`. For more information and options on this you can check out the [Setup-Python GH actions repo](https://github.com/actions/setup-python).

Next you'll need to add the run steps. Give this section a new name and enter the commands that will need to be run each time. For multiple commands you can use the `|-` at the beginning which each command being on its own line.

```yaml
    run: |-
        pip install --upgrade pip
        pip install -r requirements.txt
        python routes.py # My run script is routes.py
```


### Optional (Using Poetry)

I prefer using an environment manager when using deployed builds. This gives me slightly more control around packages, and other environment variables. I use [Poetry](https://poetry.eustace.io/) to manage my environment. This doesn't change much of my setup other than my run becomes

```yaml
    run: |- 
        pip install --upgrade pip
        pip install poetry
        poetry install
        poetry run python routes.py
```

This does slow down my build but since most of my python projects use poetry these days it's easier for me to develop with.

## That's It?

Yeah that's it! When you push your code to GitHub. You'll be able to see your site live. Using the url it gives you.



[^1]: I tried. I spent a long time trying to get it to work, even though the documentation says it only works for Javascript (and Hugo)