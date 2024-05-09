const mySecret = process.env.DULL
const promptButton = document.getElementById('promptButton');
promptButton.addEventListener('click', async () => {
  const userInput = await prompt('Enter your message:');
  if (!userInput) { return; }
  try { const response = await fetch(mySecret, {
    method: 'POST', body: userInput,
    headers: { 'Content-Type': 'text/plain' }});
    window.open('https://ddarwin.s3.eu-north-1.amazonaws.com/dove.txt', '_blank');
    if (!response.ok) {
      throw new Error(`Error triggering workflow: ${response.statusText}`); }
    setTimeout(() => { window.location.reload(); }, 15000); 
  } catch (error) { console.error('Error:', error);
    alert('An error occurred. Please try again.'); }});