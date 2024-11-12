async function fetchStaffData(apiUrl) {

        try {
            const response = await fetch(apiUrl);
            if (!response.ok) throw new Error("Ошибка при загрузке данных");

            const staffData = await response.json();

            // Если сервер возвращает объект с массивом items, передаем data.items
            if (staffData.response) {
                console.log("OK");
                window.location.reload();
            } else {
                console.log("NOT OK");
            }
        } catch (error) {
            console.error("Ошибка:", error);
    }
}

document.addEventListener("DOMContentLoaded", function() {
buttons = document.querySelectorAll("#open-form-button")
console.log(buttons)
for (let i = 0; i < buttons.length; i++){
    console.log(buttons[i])
    buttons[i].addEventListener('click', function(event) {
    value = event.target.value;
    const apiUrl = `http://127.0.0.1:1000/parcel/${value}`; // URL сервера для получения данных
    console.log(apiUrl);
        // Функция для получения данных о сотрудниках

    fetchStaffData(apiUrl);
})}});
