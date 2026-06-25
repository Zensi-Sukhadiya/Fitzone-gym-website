function calculateBMI() {
    const weight = parseFloat(document.getElementById('weight').value);
    const height = parseFloat(document.getElementById('height').value) / 100;

    if (weight > 0 && height > 0) {
        const bmi = (weight / (height * height)).toFixed(1);
        const resultBox = document.getElementById('resultBox');
        const bmiValue = document.getElementById('bmiValue');
        const bmiStatus = document.getElementById('bmiStatus');

        bmiValue.innerText = bmi;
        resultBox.classList.remove('d-none');

        // Clear previous result classes
        bmiStatus.className = "lead fw-bold mb-0";

        if (bmi < 18.5) {
            bmiStatus.innerText = "Underweight";
            bmiStatus.classList.add("bmi-underweight");
        } else if (bmi >= 18.5 && bmi < 25) {
            bmiStatus.innerText = "Normal Weight";
            bmiStatus.classList.add("bmi-normal");
        } else if (bmi >= 25 && bmi < 30) {
            bmiStatus.innerText = "Overweight";
            bmiStatus.classList.add("bmi-overweight");
        } else {
            bmiStatus.innerText = "Obesity";
            bmiStatus.classList.add("bmi-obesity");
        }
    } else {
        alert("Please enter valid weight and height.");
    }
}

function calculateCalories() {
    const age = parseInt(document.getElementById('age').value);
    const gender = document.getElementById('gender').value;
    const weight = parseFloat(document.getElementById('c-weight').value);
    const height = parseFloat(document.getElementById('c-height').value);
    const activity = parseFloat(document.getElementById('activity').value);

    if (age > 0 && weight > 0 && height > 0) {
        let bmr;
        if (gender === 'male') {
            bmr = 10 * weight + 6.25 * height - 5 * age + 5;
        } else {
            bmr = 10 * weight + 6.25 * height - 5 * age - 161;
        }

        const tdee = Math.round(bmr * activity);

        const resultBox = document.getElementById('calorieResultBox');
        const calorieValue = document.getElementById('calorieValue');

        calorieValue.innerText = tdee;
        resultBox.classList.remove('d-none');

        // Smooth scroll to result if on mobile
        if (window.innerWidth < 992) {
            resultBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }
    } else {
        alert("Please fill all fields with valid numbers.");
    }
}
