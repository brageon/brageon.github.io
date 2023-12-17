<!DOCTYPE html>
<html>
<head>
  <title>Letter to Integer Translator</title>
  <style>
    .container {
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 20px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }

    .input-box {
      width: 40%;
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }

    .output-box {
      width: 40%;
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 4px;
      text-align: right;
    }
  </style>
</head>
<body>
  <div class="container">
    <input type="text" id="input" placeholder="Enter letters to translate" class="input-box">
    <button id="translateBtn">Translate</button>

    <div id="output" class="output-box"></div>
  </div>

  <script>
    const inputBox = document.getElementById('input');
    const outputBox = document.getElementById('output');
    const translateBtn = document.getElementById('translateBtn');

    const translateLetters = (letters) => {
      // Create a mapping from letters to integers
      const letterMap = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26
      };

      // Translate the input letters to integers
      const translatedInts = letters.split('').map(letter => letterMap[letter]);

      // Join the translated integers into a single string
      const translatedString = translatedInts.join('');

      // Display the translated string in the output box
      outputBox.textContent = translatedString;
    };

    translateBtn.addEventListener('click', () => {
      const inputText = inputBox.value;
      translateLetters(inputText);
    });
  </script>
</body>
</html>

