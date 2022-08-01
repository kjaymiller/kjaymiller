---
title: Deploying a Custom Python Static Site Generator to Azure 
slug: static-site-generator-with-python-azure
date: 02 Aug 2022 08:00
---

> TLDR: Connect your repo to Azure Static Web Apps and use GitHub Actions to build your site via Python.

Static Sites are a great way to provide a custom web experience with little overhead and extremely low costs. For personal sites, it allows you to focus on just creating content removing much of the serving portion of your site to your web host. Product and application developers also use static sites to scale, separating the app from the informational portion of the site. This allows allocation of resources to be directly mostly to the application experience, while still delivering information to your customers quickly.

Furthermore, writing code to build your site is often seen as a way to continuously  develop your skills over time.

I've been working on [my own static site generator][render-engine](SSG) for going on 5 years now. It's developed a lot over time, but one thing is consistent. It's modern python. 

Many folks have used tools like github pages, Netlify or Vercel to host simple sites for free, but many of those services have to provide al a carte services at a fee to stay profitable. Also, these are closed systems and don't expand to other services and tools that you may also use in a more professional capacity[^1]. 

This year [I joined the Microsoft Cloud Advocacy Team](https://twitter.com/kjaymiller/). In an effort to  1.) move away from Netlify which I was not happy using and 2.) Try out Azure products, I wanted to switch to Azure Static Web Apps.

> **Disclaimer**: I do get paid to advocate for Azure products. That said my ethical stance is to show how I did a thing and I'm sure with a little effort the process I settled on can be replicated to any service.

I first learned about Static Web Apps (SWA) in my first week when the team was celebrating one year of the product. By design, the plan was to serve javascript applications (and a few notable others like Blazor and Hugo) serving any dynamic content via Azure functions. Ultimately, you could use any site generator that outputs HTML. Sadly, there was a lack of official support for Python or the ability to build my site.

## Build your static site's HTML

Deploying a Static website has a few components, each with a specific role.

You start with content often written in a sub-language like [markdown](https://www.markdownguide.org). Next, you provide a template system, like [Jinja2](https://palletsprojects.com/p/jinja/). Then you pass your templates and content into a static site generator (SSG) which will convert them to HTML. From there you can combine that with static content like images, css, and javascript to create a fast rich web experience.

I built [Render Engine][render-engine] to build a website or websites using a 3-object base build system. These pieces are Page, Collection, and Site objects. You can make as many of these objects as you wish. But this requires a build script to layout the pieces. Finally, you run the build script. The HTML (and static content) for websites are generated in their defined output folders.

# Add your HTML to Azure. The Non-Automated Way
