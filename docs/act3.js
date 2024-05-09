const promptButton = document.getElementById('promptButton');
promptButton.addEventListener('click', async () => {
  const userInput = await prompt('Reload S3 after 15 seconds:');
  if (!userInput) { return; }
  try { const response = await fetch('https://o66gcrisu76svuos65hnrembza0myxeg.lambda-url.eu-north-1.on.aws/', {
    method: 'POST', body: userInput,
    headers: { 'Content-Type': 'text/plain' }});
    window.open('https://ddarwin.s3.eu-north-1.amazonaws.com/dove.txt', '_blank');
    if (!response.ok) {
      throw new Error(`Error triggering workflow: ${response.statusText}`); }
  } catch (error) { console.error('Error:', error);
    alert('An error occurred. Please try again.'); }});