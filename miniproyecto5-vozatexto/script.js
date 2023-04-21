const startBtn = document.getElementById('start-btn');
const resultDiv = document.getElementById('result');

window.SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

if (!window.SpeechRecognition) {
  resultDiv.innerHTML = 'Lo siento, tu navegador no soporta la API de reconocimiento de voz.';
} else {
  const recognition = new SpeechRecognition();
  recognition.interimResults = true;
  recognition.lang = 'es-ES';

  startBtn.addEventListener('click', () => {
    recognition.start();
  });

  recognition.addEventListener('result', (event) => {
    const transcript = Array.from(event.results)
      .map((result) => result[0].transcript)
      .join('');

    resultDiv.innerHTML = transcript;
  });

  recognition.addEventListener('end', () => {
    startBtn.disabled = false;
  });

  recognition.addEventListener('error', () => {
    resultDiv.innerHTML = 'Se ha producido un error al intentar acceder al micrófono.';
  });
}
