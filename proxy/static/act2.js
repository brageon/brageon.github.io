function translate() {
    const inputText = document.getElementById('input').value;
    const translations = [];
    for (const letter of inputText) {
      const asciiCode = letter.charCodeAt();
      const integer = asciiCode - 96;
      translations.push(integer); }
    const outputText = translations.join(', ');
    document.getElementById('output').value = outputText; }
    const input = document.getElementById('input');
    input.addEventListener('keyup', translate);
  document.getElementById('translateButton').addEventListener('click', translate);
