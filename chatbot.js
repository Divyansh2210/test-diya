function processInput() {
    var userInput = document.getElementById('user-input').value;
    fetch('/process-input', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: userInput })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('response-container').innerText = data.answer;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('response-container').innerText = 'Error processing your request';
    });
}
