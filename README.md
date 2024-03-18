# Blog Site with Django

This is a Django-based blog site with various features including user authentication, blog post management, and user profile editing. The site is designed to provide a platform for users to create, read, update, and delete blog posts, while also allowing administrators to send newsletters to all users and manage user profiles.

## Features

```markdown
- **User Authentication**: Users can sign up and log in to the site securely.
- **Blog Post Management**: Only administrators can create, update, and delete blog posts.
- **Newsletter Sending**: Administrators have the capability to send newsletters to all users.
- **Profile Editing**: Users can edit their profiles to update information such as their name, email, and profile picture.
```
## Technologies Used

- **Django**: The web framework used for building the site.
- **HTML/CSS**: For front-end design and layout.
- **Bootstrap**: Used for responsive and mobile-first design.
- **SQLite**: The database management system utilized by Django for data storage.
- **JavaScript**: For client-side interactivity (if applicable).

## Setup Instructions

1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/your_username/your_project.git

   cd your_project

   python -m venv venv
   ```

 2. Activate the virtual environment.

     On Windows:
    ```
    venv\Scripts\activate
    ```
     On macOS and Linux:
    ```
    source venv/bin/activate
    ```
3. Install dependencies from requirements.txt
   ```
   pip install -r requirements.txt
   ```
4. Run migrations to create the necessary database tables
   ```
   python manage.py migrate
   ```
5. Create a superuser for accessing the admin panel
    ```
    python manage.py createsuperuser
    ```
6. Start the development server.
   ```
   python manage.py runserver
   ```
7. Open your web browser and navigate to http://127.0.0.1:8000 to view the site.
   ## Usage

```markdown
- Visit the homepage to view existing blog posts and sign up or log in to create your own posts.
- Administrators can access the admin panel by visiting `http://127.0.0.1:8000/admin` and log in with their superuser credentials.
- In the admin panel, administrators can manage blog posts, send newsletters, and edit user profiles.
```

## Contributors
- [Rahul NS](https://github.com/Rahulns21) - Developer

## License
This project is licensed under the [MIT License](LICENSE).

Feel free to contribute to the project or use it as a template for your own Django-based blog site! If you encounter any issues or have suggestions for improvements, please open an issue on GitHub. Thank you for checking out the project!

   

