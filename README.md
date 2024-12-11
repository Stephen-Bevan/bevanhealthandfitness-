# Bevan Health and Fitness

Welcome to **Bevan Health and Fitness**, an intuitive platform designed to help users manage their fitness goals, track progress, and achieve a healthier lifestyle. Whether you're just starting your fitness journey or are a seasoned athlete, our app provides the tools and insights to keep you on track.

Live Project: [Bevan Health and Fitness](https://bevanhealthandfitness-6624380c9483.herokuapp.com/)

---

## Index

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

## Features

### **Hero Section**
- Engaging hero banner with a welcoming message and call-to-action button for registration.
- Overlay effect with prominent text and button styling.

### **Navigation Bar**
- Responsive navbar with:
  - Links to Home, Login, and Register pages for unauthenticated users.
  - Links to Dashboard and Logout for authenticated users.
  - Dynamic display of the logged-in user's username.

### **Dashboard**
- A welcoming dashboard with:
  - Personalized greeting for the logged-in user.
  - Quick links to manage workouts:
    - View "My Workouts Log".
    - Create a new workout.
    - Placeholder links for future features like class booking, online personal training, and nutrition plans.

### **Workout Management**
- **Create or Update Workout Form**:
  - Fields for workout name, day, sets, reps, and weights.
  - Real-time form validation with custom error messages for missing or invalid inputs.
  - A "Save Workout" button dynamically enabled or disabled based on input validity.
  - Redirect to a workout list or cancel action.
- **Workout List**:
  - List of all logged workouts with options to edit or delete.
  - Notifications for successful creation, update, or deletion.

### **Features Section**
- Highlights of the app, including:
  - **State-of-the-Art Equipment**: Details about the quality and variety of fitness equipment.
  - **Personalized Programs**: One-to-one training, group sessions, and online training plans.
  - **About Me**: A story of the founder's fitness journey and professional credentials.

### **404 Page**
- Custom 404 error page with:
  - A friendly message indicating the page is not found.
  - A call-to-action button to redirect users back to the homepage.

---

## Design

### Wireframes
- Created using **Balsamiq** to visualize the layout and functionality.
- ![Wireframe](path_to_your_wireframe_image)

### Mockup
- Image of the site
- ![Site Image](path_to_site_image)

### ERD/Model
- Image of the ERD/Model
- ![ERD/Model](path_to_erd_image)

### Fonts
- **Roboto (Google Font)**: Chosen for its readability and modern appeal.

### Color Scheme
- **Blue and White**: Represents trust, clarity, and cleanliness.
- **Green Accents**: Symbolizes health and progress.

### Responsive Design
- Ensures optimal user experience across different screen sizes using **Bootstrap** and **CSS media queries**.

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
- **FontAwesome**: Icons for features and navigation.
- **GitHub**: Repository management.
- **Visual Studio Code**: Code editor.
- **Balsamiq**: Wireframe creation.

---

## Testing

### Manual Testing

| Feature                      | Action                        | Expected Outcome             | Result       |
|------------------------------|-------------------------------|------------------------------|--------------|
| Hero Section CTA Button      | Click "Join Now"             | Redirects to the Register page| Worked as expected |
| Navigation Links             | Click each link in the navbar| Redirects to the correct page| Worked as expected |
| User Registration            | Submit valid/invalid inputs   | Creates account / Shows error| Worked as expected |
| Log In                       | Enter valid/invalid credentials| Logs in / Shows error         | Worked as expected |
| Dashboard Links              | Click quick links on Dashboard| Navigates to respective pages | Worked as expected |
| Create Workout Form          | Fill out form and submit      | Saves workout to database     | Worked as expected |
| Edit/Delete Workout          | Click respective buttons      | Updates or removes workout    | Worked as expected |
| 404 Page                     | Access invalid URL            | Displays custom 404 page      | Worked as expected |

---

## Future Features

### **Class Booking**
- Enable users to book group classes directly from the platform.

### **Online Personal Training**
- Launch an online personal training feature with custom workout plans.

### **Nutrition Plans**
- Provide personalized nutrition plans to complement fitness goals.

---

## Credits

- **Code Institute LMS**: For guidance and templates.
- **Google**: Resources for troubleshooting and inspiration.
- **Balsamiq**: Wireframe creation.
- **FontAwesome**: Icons used for visual enhancements.
- **CRUD mastery with Django | Build a CRM application**: [YouTube Tutorial](https://www.youtube.com/watch?v=pqWyUAT38e0&t=2806s)
- **Davidcalikes**: Inspiration from [mypse project](https://github.com/davidcalikes/mypse.ie/blob/main/passport/views.py)
- **ChatGPT and Stack Overflow**: For bug fixes.
- **Coding Coaches at Code Institute**: @kevin_ci
- **John Rearden**

---

## Technologies Used

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
- **Bootstrap**: For theming with Bootswatch

---

## Compliance Testing

- **PEP8 Compliance**: Verified that all Python code meets PEP8 standards.
- **HTML Validation**: Ensured all templates are error-free using HTML validation tools.
- **CSS Validation**: Confirmed that all CSS stylesheets pass through Jigsaw with no validation errors.

These technologies and tools were thoroughly tested and validated to ensure a robust and error-free application.