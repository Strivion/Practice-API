# Practice-API

A simple API project for university.

---

## Overview
This project is a very simple API designed to demonstrate **basic development** and **deployment** skills.  
It includes a small set of endpoints that expose information about the developer, sample projects, and basic feedback functionality.

---

## Trying it out
If you'd like to try it out, you'll need a tool such as Postman, Insomnia, Hoppscotch, or even just command-line tools like curl. With your chosen tool open, insert the base URL:
- **`https://python-api-example-68ou.onrender.com`**

---

## Endpoints

- **`GET /about`**
  Set the dropdown on the url bar to:
  - **`GET`**
  Append the folling to the end of the base URL:
  - **`/about`**
  Run the search.
  Returns a small section with information about the developer.

- **`GET /projects`**
  Set the dropdown on the url bar to:
  - **`GET`**
  Append the folling to the end of the base URL:
  - **`/projects`**
  Run the search.
  Returns a list of sample projects (both real and fictional).

- **`POST /feedback`**
  Set the dropdown on the url bar to:
  - **`Post`**
  Append the folling to the end of the base URL:
  - **`/feeback`**
  Under the URL bar, select the option for:
- **`body`**
  Now, to the right, set the format to:
  - **`JSON`**
  Allows the user to send feedback via a JSON object.  
  Example request body:  
  ```json
  {
    "message": "This API is great!"
  }
