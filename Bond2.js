const express = require('express');
const app = express();
const port = process.env.PORT || 8080;

app.get('/translate', (req, res) => {
  // Retrieve the input from the request body
  const input = req.body.input;

  // Translate the input to integers
  const translations = [];
  for (const letter of input) {
    const asciiCode = letter.charCodeAt();
    const integer = asciiCode - 96;
    translations.push(integer);
  }

  // Convert the translations to a string and set the response
  const outputText = translations.join(', ');
  res.send({ output: outputText });
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});

