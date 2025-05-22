document.addEventListener("DOMContentLoaded", function() {
    const passwordDialog = document.getElementById("password-dialog");
    const passwordInput = document.getElementById("password-input");
    const submitPasswordBtn = document.getElementById("submit-password");
    const passwordError = document.getElementById("password-error");
    const mainContent = document.getElementById("main-content");
    
    // Focus on password input when page loads
    passwordInput.focus();
    
    // Handle Enter key press
    passwordInput.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            validatePassword();
        }
    });
    
    // Handle submit button click
    submitPasswordBtn.addEventListener("click", validatePassword);
    
    function validatePassword() {
        const password = passwordInput.value;
        
        if (!password) {
            passwordError.textContent = "Please enter a password";
            return;
        }
        
        // Send password to server for validation
        fetch(`/valid_write_password?password=${encodeURIComponent(password)}`)
            .then(response => response.json())
            .then(data => {
                // Add this to the validatePassword function, after showing the main content
                if (data.valid) {
                    // Password is valid, show the content
                    passwordDialog.style.display = "none";
                    mainContent.style.display = "flex";
                    
                    // Initialize the form functionality
                    initializeForm();
                    
                    // Dispatch custom event to initialize editor
                    document.dispatchEvent(new CustomEvent('passwordValidated'));
                }
                else {
                    // Password is invalid
                    passwordError.textContent = "Incorrect password. Please try again.";
                    passwordInput.value = "";
                    passwordInput.focus();
                }
            })
            .catch(error => {
                console.error("Error validating password:", error);
                passwordError.textContent = "An error occurred. Please try again.";
            });
    }
    
    function initializeForm() {
        var categoryDropdown = document.getElementById("category-dropdown");
        var newCategoryInput = document.getElementById("new-category-input");
        var form = document.getElementById("post-form");

        // Function to handle dropdown change
        function handleDropdownChange() {
            if (categoryDropdown.value === "") {
                newCategoryInput.style.display = "inline-block";
                newCategoryInput.name = "category";  // Set name to "category"
                categoryDropdown.name = "";  // Remove name from dropdown
                newCategoryInput.focus();
            } else {
                newCategoryInput.style.display = "none";
                newCategoryInput.name = "";  // Remove name from input
                categoryDropdown.name = "category";  // Set name to "category"
            }
        }

        // Attach event listener to the dropdown
        categoryDropdown.addEventListener("change", handleDropdownChange);

        // Initial check on page load
        handleDropdownChange();

        // Ensure that the correct input is submitted based on the selected option
        form.addEventListener("submit", function (event) {
            if (categoryDropdown.value === "" && newCategoryInput.value === "") {
                event.preventDefault();
                alert("Please select a category or create a new one.");
            }
        });
        

    }
});