function EnquiryForm() {
    var Enquiry_Name = document.getElementById("enquiry_name").value;
    var Enquiry_Email = document.getElementById("enquiry_email").value;
    var Enquiry_Phone = document.getElementById("enquiry_phone").value;
    var message = document.getElementById("message").value;

    var phoneRegex = /^[0-9]{10}$/;

    if (
        Enquiry_Name == "" ||
        Enquiry_Email == "" ||
        Enquiry_Phone == "" ||
        message == ""
    ) {
        alert("All fields are required");
        return false;
    } else if (!phoneRegex.test(Enquiry_Phone)) {
        alert("Please enter a valid 10-digit phone number");
        return false;
    }
    alert("Enquiry message send successfully our executive will call you soon");
    return true;
}
