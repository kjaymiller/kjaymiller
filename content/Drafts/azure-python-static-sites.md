---
title: Deploying a Custom Python Static Site Generator to Azure 
slug: static-site-generator-with-python-azure
date: 02 Aug 2022 08:00
---

> TLDR: Connect your repo to Azure Static Web Apps and use GitHub Actions to build your site via Python.

Static Sites are a great way to provide a custom web experience with little overhead and extremely low costs. For personal sites, it allows you to focus on just creating content removing much of the serving portion of your site to your web host. Product and application developers also use static sites to scale, separating the app from the informational portion of the site. This allows allocation of resources to be directly mostly to the application experience, while still delivering information to your customers quickly.

Furthermore, writing code to build your site is often seen as a way to continuously  develop your skills over time.

I've been working on [my own static site generator][render-engine](SSG) for going on 5 years now. It's developed a lot over time, but one thing is consistent. It's modern python. 

Many folks have used tools like [github pages](https://pages.github.com), [Netlify](https://netlify.com) or [Vercel]() to host simple sites for free, but many of those services have to provide al a carte services at a fee to stay profitable. Also, these are closed systems and don't expand to other services and tools that you may also use in a more professional capacity[^1]. 

This year [I joined the Microsoft Cloud Advocacy Team](https://twitter.com/kjaymiller/). In an effort to  1.) move away from Netlify which I was not happy using and 2.) Try out Azure products, I wanted to switch to Azure Static Web Apps.

> **Disclaimer**: I do get paid to advocate for Azure products. That said my ethical stance is to show how I did a thing and I'm sure with a little effort the process I settled on can be replicated to any service.

I first learned about Static Web Apps (SWA) in my first week when the team was celebrating one year of the product. By design, the plan was to serve javascript applications (and a few notable others like Blazor and Hugo) serving any dynamic content via Azure functions. Ultimately, you could use any site generator that outputs HTML. Sadly, there isn't any official support for any Python or the ability to build my site.


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

Azure won't build out our HTML but according to the docs it just needs **ONE HTML** file in a folder to build a site. we can give it that file in one of two ways.

### Build then deploy
The first way is rather simple. Build your site locally and push it's contents to GithHub. 

