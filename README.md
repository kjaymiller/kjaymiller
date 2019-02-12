# Render Engine
This site uses the [render_engine](https://github.com/kjaymiller/render_engine) framework

## Project Design
There are four components to the engine:
1. **Pages**
2. **Collections**
3. **Blocks**
4. **Templates**

Templates are built using Jinja2 so I won't go into too much detail on that and we will focus on the first three. 
![](https://kjaymiller.s3-us-west-2.amazonaws.com/images/pb-t32bwnbR3M.png)

### Pages: the Core Concept of the Site
Every page that someone will see is a _Page_ object of some kind.

Pages at their core are extremely simple but by subclassing into different types of pages we create some standards around them. 

#### _Examples of Page Objects:_
- Blog Posts
- Micro Blog Posts
- Podcast Episodes
