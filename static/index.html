
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Story Generator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f7fa;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 400px;
        }
        h1 {
            text-align: center;
            color: #4CAF50;
        }
        .form-group {
            margin-bottom: 15px;
        }
        .form-group label {
            display: block;
            font-weight: bold;
        }
        .form-group input {
            width: 100%;
            padding: 8px;
            margin-top: 5px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        .form-group button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 4px;
            cursor: pointer;
            width: 100%;
        }
        .form-group button:hover {
            background-color: #45a049;
        }
        .story {
            margin-top: 20px;
            background-color: #f0f0f0;
            padding: 15px;
            border-radius: 4px;
            display: none;
        }
        .error {
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Story Generator</h1>
        <div id="form-step">
            <div class="form-group">
                <label for="age">Enter your age:</label>
                <input type="number" id="age" placeholder="Age">
            </div>
            <div class="form-group">
                <button onclick="submitAge()">Submit Age</button>
            </div>
        </div>
        <div id="verb-step" style="display: none;">
            <div class="form-group">
                <label for="first-verb">Enter a verb:</label>
                <input type="text" id="first-verb" placeholder="Verb 1">
            </div>
            <div class="form-group">
                <button onclick="submitFirstVerb()">Submit First Verb</button>
            </div>
        </div>
        <div id="second-verb-step" style="display: none;">
            <div class="form-group">
                <label for="second-verb">Enter another verb:</label>
                <input type="text" id="second-verb" placeholder="Verb 2">
            </div>
            <div class="form-group">
                <button onclick="submitSecondVerb()">Submit Second Verb</button>
            </div>
        </div>
        <div class="story" id="story">
            <p id="generated-story"></p>
        </div>
        <div id="error-message" class="error" style="display: none;"></div>
    </div>

    <script>
        function submitAge() {
            let age = document.getElementById("age").value;
            if (age === "") {
                showError("Please enter your age.");
                return;
            }
            fetch('/submit_data', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ age: age, first_verb: '', second_verb: '' })
            }).then(response => response.json())
              .then(data => {
                  document.getElementById("form-step").style.display = "none";
                  document.getElementById("verb-step").style.display = "block";
              });
        }

        function submitFirstVerb() {
            let firstVerb = document.getElementById("first-verb").value;
            if (firstVerb === "") {
                showError("Please enter the first verb.");
                return;
            }
            fetch('/submit_data', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ age: 0, first_verb: firstVerb, second_verb: '' })
            }).then(response => response.json())
              .then(data => {
                  document.getElementById("verb-step").style.display = "none";
                  document.getElementById("second-verb-step").style.display = "block";
              });
        }

        function submitSecondVerb() {
            let secondVerb = document.getElementById("second-verb").value;
            if (secondVerb === "") {
                showError("Please enter the second verb.");
                return;
            }
            fetch('/submit_data', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ age: 0, first_verb: '', second_verb: secondVerb })
            }).then(response => response.json())
              .then(data => {
                  generateStory();
              });
        }

        function generateStory() {
            fetch('/generate_story')
                .then(response => response.json())
                .then(data => {
                    if (data.story !== "Please provide all inputs first.") {
                        document.getElementById("generated-story").textContent = data.story;
                        document.getElementById("story").style.display = "block";
                    } else {
                        showError("Please provide all inputs.");
                    }
                });
        }

        function showError(message) {
            document.getElementById("error-message").textContent = message;
            document.getElementById("error-message").style.display = "block";
        }
    </script>
</body>
</html>
