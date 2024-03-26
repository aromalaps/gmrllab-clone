function validateForm() {
    var appointName = document.getElementById("appoint_name").value;
    var appointEmail = document.getElementById("appoint_email").value;
    var appointPhone = document.getElementById("appoint_phone").value;
    var age = document.getElementById("age").value;
    var gender = document.getElementById("gender").value;
    var address = document.getElementById("address").value;
    var message = document.getElementById("message").value;

    // Regular expression for phone number validation
    var phoneRegex = /^[0-9]{10}$/;

    if (
        appointName == "" ||
        appointEmail == "" ||
        appointPhone == "" ||
        age == "" ||
        gender == "" ||
        address == "" ||
        message == ""
    ) {
        alert("All fields are required");
        return false;
    } else if (!phoneRegex.test(appointPhone)) {
        alert("Please enter a valid 10-digit phone number");
        return false;
    }
    alert("successfully registered ");
    return true;
}

window.onload = function () {
    var timeInput = document.getElementById('appointment_time');

    // Set minimum and maximum time limits
    var minTime = '09:00';
    var maxTime = '21:00';

    // Function to validate the entered time
    function validateTime() {
        var selectedTime = timeInput.value;
        if (selectedTime < minTime || selectedTime > maxTime) {
            alert("Please select a time between 9 AM and 9 PM.");
            timeInput.value = ''; // Clear the input field
        }
    }

    // Attach event listener to input field
    timeInput.addEventListener('change', validateTime);
}
