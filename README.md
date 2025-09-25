# Practice-API

A simple API project for university.

---

## Overview
This project is a very simple API designed to demonstrate **basic development** and **deployment** skills.  
It includes a small set of endpoints that expose information about the developer, sample projects, and basic feedback functionality.

---

## Endpoints

- **`GET /about`**  
  Returns a small section with information about the developer.

- **`GET /projects`**  
  Returns a list of sample projects (both real and fictional).

- **`POST /feedback`**  
  Allows the user to send feedback via a JSON object.  
  Example request body:  
  ```json
  {
    "message": "This API is great!"
  }
