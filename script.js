// Script for Interactive Contact Form Validation and Effects
document.getElementById("contact-form").addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent the default form submission

    // Collecting form data
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const contactNumber = document.getElementById("contact-number").value;
    const recipient = document.getElementById("recipient").value;

    // Displaying a confirmation message
    alert(`Thank you, ${name}! Your message has been sent to ${recipient}.`);
    
    // Reset the form
    this.reset();
});