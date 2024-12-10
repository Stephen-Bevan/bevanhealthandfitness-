function validateForm() {
    const nameInput = document.getElementById("name");
    const dateInput = document.getElementById("day");
    const setsInput = document.getElementById("sets");
    const repsInput = document.getElementById("reps");
    const weightsInput = document.getElementById("weights");
    const saveButton = document.getElementById("save-button");

    let isValid = true;

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
    const enteredDate = new Date(dateInput.value);
    const isValidDate = !isNaN(enteredDate.getTime());
    const isReasonableYear = enteredDate.getFullYear() >= 1900 && enteredDate.getFullYear() <= 2100;

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

    // Enable/disable the Save button
    saveButton.disabled = !isValid;
}