function validateForm() {
    // Input elements
    var nameInput = document.getElementById("name");
    var dateInput = document.getElementById("day");
    var setsInput = document.getElementById("sets");
    var repsInput = document.getElementById("reps");
    var weightsInput = document.getElementById("weights");
    var saveButton = document.getElementById("save-button");

    var isValid = true;

    // Workout Name validation
    if (nameInput.value.trim() === "") {
        document.getElementById("name-error").style.display = "block";
        nameInput.classList.add("is-invalid");
        isValid = false;
    } else {
        document.getElementById("name-error").style.display = "none";
        nameInput.classList.remove("is-invalid");
    }

    // Day validation
    var enteredDate = new Date(dateInput.value);
    var isValidDate = !isNaN(enteredDate.getTime());
    var isReasonableYear = enteredDate.getFullYear() >= 1900 && enteredDate.getFullYear() <= 2100;

    if (!isValidDate || !isReasonableYear) {
        document.getElementById("date-error").style.display = "block";
        dateInput.classList.add("is-invalid");
        isValid = false;
    } else {
        document.getElementById("date-error").style.display = "none";
        dateInput.classList.remove("is-invalid");
    }

    // Sets validation
    if (setsInput.value < 1 || isNaN(setsInput.value)) {
        document.getElementById("sets-error").style.display = "block";
        setsInput.classList.add("is-invalid");
        isValid = false;
    } else {
        document.getElementById("sets-error").style.display = "none";
        setsInput.classList.remove("is-invalid");
    }

    // Reps validation
    if (repsInput.value < 1 || isNaN(repsInput.value)) {
        document.getElementById("reps-error").style.display = "block";
        repsInput.classList.add("is-invalid");
        isValid = false;
    } else {
        document.getElementById("reps-error").style.display = "none";
        repsInput.classList.remove("is-invalid");
    }

    // Weights validation
    if (weightsInput.value < 0 || isNaN(weightsInput.value) || weightsInput.value > 999.99) {
        document.getElementById("weights-error").style.display = "block";
        weightsInput.classList.add("is-invalid");
        isValid = false;
    } else {
        document.getElementById("weights-error").style.display = "none";
        weightsInput.classList.remove("is-invalid");
    }

    // Enable or disable the Save button based on form validity
    saveButton.disabled = !isValid;
}

// Timing out alerts
document.addEventListener("DOMContentLoaded", function () {
    // Select all alert elements
    var alerts = document.querySelectorAll(".alert");
    Array.prototype.forEach.call(alerts, function (alert) {
        setTimeout(function () {
            alert.classList.remove("show"); // Hide the alert
            alert.classList.add("fade"); // Add fade-out animation
            setTimeout(function () {
                alert.parentNode.removeChild(alert); // Remove after fade-out
            }, 150); // Remove after fade-out
        }, 5000); // Alerts disappear after 5 seconds
    });
});
