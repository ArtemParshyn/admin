document.addEventListener("DOMContentLoaded", function() {
        const openFormButton = document.getElementById("open-form-button");
        const questionForm = document.getElementById("question-form");
        const cancelButton = document.getElementById("cancel-button");
        const submitButton = document.getElementById("submit-button");

        openFormButton.addEventListener("click", function() {
            questionForm.style.display = "block";
        });

        cancelButton.addEventListener("click", function() {
            questionForm.style.display = "none";
        });

        submitButton.addEventListener("click", async function() {
            const questionText = document.getElementById("question").value;
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

            try {
                const response = await fetch("create_ticket", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "X-CSRFToken": csrfToken,
                    },
                    body: JSON.stringify({ question: questionText })
                });

                if (!response.ok) throw new Error("Ошибка при отправке вопроса");

                const result = await response.json();
                console.log("Ответ сервера:", result);
                questionForm.style.display = "none"; // скрыть форму после успешной отправки

            } catch (error) {
                console.error("Ошибка:", error);
            }
        });
    });