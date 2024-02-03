document.addEventListener('DOMContentLoaded', function () {
    const questionContainer = document.getElementById('question-container');
    const resultContainer = document.getElementById('result-container');
    let currentQuestion = 0;
    let score = 0;

    const displayQuestion = (question) => {
        questionContainer.innerHTML = `
            <h2>${question.question}</h2>
            <ul>
                ${question.options.map((option, index) => `<li onclick="submitAnswer(${index + 1})">${option}</li>`).join('')}
            </ul>
        `;
    };

    const checkAnswer = (userAnswer, correctOption) => {
        return userAnswer === correctOption;
    };

    const loadNextQuestion = () => {
        currentQuestion++;
        if (currentQuestion < initialQuestions.length) {
            displayQuestion(initialQuestions[currentQuestion]);
        } else {
            displayResult();
        }
    };

    const submitAnswer = (userAnswer) => {
        const correctOption = initialQuestions[currentQuestion].correct_option;
        const isCorrect = checkAnswer(userAnswer, correctOption);

        if (isCorrect) {
            score++;
        }

        resultContainer.innerHTML = isCorrect ? 'Correct!' : `Incorrect. The correct answer is ${correctOption}. ${initialQuestions[currentQuestion].options[correctOption - 1]}`;
        setTimeout(loadNextQuestion, 2000); // Load next question after 2 seconds
    };

    const displayResult = () => {
        resultContainer.innerHTML = `Well Done Champ! Quiz completed! Your score: ${score}/${initialQuestions.length}`;
    };

    // Initial question load
    displayQuestion(initialQuestions[currentQuestion]);
});
