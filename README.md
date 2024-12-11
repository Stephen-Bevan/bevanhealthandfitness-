```markdown
# Bevan Health and Fitness

Welcome to **Bevan Health and Fitness**, an intuitive platform designed to help users manage their fitness goals, track progress, and achieve a healthier lifestyle. Whether you're just starting your fitness journey or are a seasoned athlete, our app provides the tools and insights to keep you on track.

Live Project: [Bevan Health and Fitness](https://bevanhealthandfitness-6624380c9483.herokuapp.com/)

---

## Table of Contents

1. [User Experience (UX)](#user-experience-ux)
2. [Features](#features)
3. [Design](#design)
4. [Technologies Used](#technologies-used)
5. [Testing](#testing)
6. [Deployment](#deployment)
7. [Future Features](#future-features)
8. [Credits](#credits)

---

## User Experience (UX)

The platform is crafted to ensure:

- Accessibility for all fitness levels.
- A streamlined user journey, from sign-up to tracking workouts.
- Motivation through engaging design and personalized content.

---

## Features

### **Hero Section**

- Engaging hero banner with a welcoming message and a clear call-to-action for registration.
- Overlay effect with prominent text and button styling to grab attention.

### **Navigation Bar**

- Fully responsive navbar with dynamic features:
  - Links to Home, Login, and Register for unauthenticated users.
  - Links to Dashboard and Logout for authenticated users.
  - Dynamic display of the logged-in user’s username.

### **Dashboard**

- A personalized space with:
  - User-specific greetings.
  - Quick links for managing workouts:
    - "My Workouts Log."
    - Create a new workout.
    - Placeholder links for future features like class booking, online personal training, and nutrition plans.

### **Workout Management**

- **Create or Update Workout Form**:
  - Fields for workout name, day, sets, reps, and weights.
  - Real-time validation with clear error messages.
  - Dynamically enabled or disabled "Save Workout" button based on form validity.
  - Options to save, cancel, or redirect.
- **Workout List**:
  - Displays all logged workouts with edit and delete options.
  - Notifications for successful operations.

### **404 Page**

- Custom 404 page with:
  - Friendly messaging to guide users.
  - Redirect button to the homepage.

---

## Design

### Wireframes

- Developed using **Balsamiq** to outline the app’s layout and functionality.
- ![Wireframe](Readme_images/Wireframe_files)

### ERD/Model

- Entity Relationship Diagram for database structure.
- ![ERD/Model](Readme_images/ERD)

### Fonts

- **Roboto (Google Font)**: Modern and highly readable.

### Color Scheme

- **Blue and White**: Evokes trust and clarity.
- **Green Accents**: Represents health and progress.

### Responsive Design

- Ensures compatibility across devices with **Bootstrap** and **CSS media queries**.

---

## Technologies Used

### **Languages**

- HTML5
- CSS3
- Python/Django
- Java

### **Database**

- ElephantSQL Postgres Database

### **Libraries & Tools**

- **Bootstrap**: For responsive design.
- **FontAwesome**: Icons for enhanced visuals.
- **GitHub**: Repository management.
- **Visual Studio Code**: Code editor.
- **Balsamiq**: Wireframe creation.

---

## Testing

### Manual Testing

| Feature                 | Action                          | Expected Outcome              | Result             |
| ----------------------- | ------------------------------- | ----------------------------- | ------------------ |
| Hero Section CTA Button | Click "Join Now"                | Redirects to Register page    | Worked as expected |
| Navigation Links        | Click navbar links              | Redirects to correct pages    | Worked as expected |
| User Registration       | Submit valid/invalid inputs     | Account created / Error shown | Worked as expected |
| Log In                  | Enter valid/invalid credentials | Logs in / Error shown         | Worked as expected |
| Dashboard Links         | Click quick links               | Navigates to target pages     | Worked as expected |
| Create Workout Form     | Fill out and submit             | Saves workout to database     | Worked as expected |
| Edit/Delete Workout     | Use respective buttons          | Updates or removes workout    | Worked as expected |
| 404 Page                | Access invalid URL              | Displays custom 404 page      | Worked as expected |

### Screen Shots of Testing Features

- ![Tests](Readme_images/Screenshots_Features_testing)

---

### Compliance Testing

- **PEP8 Compliance**: Python code adheres to PEP8 standards.
- **HTML Validation**: Templates validated for errors.
- **CSS Validation**: All stylesheets validated error-free.

### Screen Shots of Testing HTML, CSS, and Python

- ![Tests](Readme_images/Screenshots_CSS,HTML,Pyton)

---

## Future Features

### **Class Booking**

- Allow users to schedule group classes directly on the platform.

### **Online Personal Training**

- Provide virtual training sessions and personalized workout plans.

### **Nutrition Plans**

- Introduce tailored nutrition plans to complement users’ fitness goals.

---

## Credits

- **Code Institute LMS**: Guidance and templates.
- **Google**: Resources for troubleshooting and inspiration.
- **Balsamiq**: Wireframe creation.
- **FontAwesome**: Visual enhancements.
- **CRUD Mastery with Django**: [YouTube Tutorial](https://www.youtube.com/watch?v=pqWyUAT38e0\&t=2806s).
- **Davidcalikes**: Inspiration from [mypse project](https://github.com/davidcalikes/mypse.ie/blob/main/passport/views.py).
- **ChatGPT and Stack Overflow**: Bug fixes and optimization.
- **Coding Coaches at Code Institute**: @kevin\_ci.
- **John Rearden**: Contributions and insights.

---

## Key Technologies

- **asgiref**: 3.8.1
- **cloudinary**: 1.41.0
- **dj-database-url**: 0.5.0
- **dj3-cloudinary-storage**: 0.0.6
- **Django**: 4.2.16
- **gunicorn**: 20.1.0
- **psycopg**: 3.2.3
- **sqlparse**: 0.5.2
- **urllib3**: 1.26.20
- **whitenoise**: 5.3.0
- **Bootstrap**: Bootswatch themes.
```

