function ContactForm() {
    var Contact_Name = document.getElementById("contact_name").value;
    var Contact_Email = document.getElementById("contact_email").value;
    var Contact_Phone = document.getElementById("contact_phone").value;
    var subject = document.getElementById("subject").value;
    var message = document.getElementById("message").value;

    var phoneRegex = /^[0-9]{10}$/;

    if (
        Contact_Name == "" ||
        Contact_Email == "" ||
        Contact_Phone == "" ||
        subject == "" ||
        message == ""
    ) {
        alert("All fields are required");
        return false;
    } else if (!phoneRegex.test(Contact_Phone)) {
        alert("Please enter a valid 10-digit phone number");
        return false;
    }
    alert("message send successfully our executive will call you soon ");
    return true;
}


