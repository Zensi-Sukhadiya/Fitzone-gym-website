// Real-time Form Validation for Contact Page
document.addEventListener('DOMContentLoaded', function () {
    const contactForm = document.querySelector('form[action$="/contact/"]');
    if (!contactForm) return;

    const emailInput = document.getElementById('email');
    const nameInput = document.getElementById('name');
    const messageInput = document.getElementById('message');

    // Email validation regex
    const validateEmail = (email) => {
        return String(email)
            .toLowerCase()
            .match(
                /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
            );
    };

    const setInvalid = (input, message) => {
        input.classList.add('is-invalid');
        input.classList.remove('is-valid');
        // Check if error message already exists
        let error = input.parentElement.querySelector('.invalid-feedback');
        if (!error) {
            error = document.createElement('div');
            error.className = 'invalid-feedback';
            input.parentElement.appendChild(error);
        }
        error.innerText = message;
    };

    const setValid = (input) => {
        input.classList.remove('is-invalid');
        input.classList.add('is-valid');
    };

    emailInput.addEventListener('input', () => {
        if (validateEmail(emailInput.value)) {
            setValid(emailInput);
        } else {
            setInvalid(emailInput, 'Please enter a valid email address.');
        }
    });

    nameInput.addEventListener('input', () => {
        if (nameInput.value.trim().length >= 3) {
            setValid(nameInput);
        } else {
            setInvalid(nameInput, 'Name must be at least 3 characters.');
        }
    });

    messageInput.addEventListener('input', () => {
        if (messageInput.value.trim().length >= 10) {
            setValid(messageInput);
        } else {
            setInvalid(messageInput, 'Message must be at least 10 characters.');
        }
    });

    // Form submission check
    contactForm.addEventListener('submit', function (e) {
        if (!validateEmail(emailInput.value) || nameInput.value.trim().length < 3 || messageInput.value.trim().length < 10) {
            e.preventDefault();
            alert('Please fix the errors in the form before submitting.');
        }
    });
});
