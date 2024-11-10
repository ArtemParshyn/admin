document.addEventListener("DOMContentLoaded", function() {
    const apiUrl = "http://127.0.0.1:2000/items"; // URL сервера для получения данных

    // Функция для получения данных о сотрудниках
    async function fetchStaffData() {
        try {
            const response = await fetch(apiUrl);
            if (!response.ok) throw new Error("Ошибка при загрузке данных");

            const staffData = await response.json();

            // Если сервер возвращает объект с массивом items, передаем data.items
            if (staffData.items) {
                populateTable(staffData.items);
            } else {
                populateTable(staffData);
            }
        } catch (error) {
            console.error("Ошибка:", error);
        }
    }

    // Функция для добавления данных в таблицу
    function populateTable(dataArray) {
        const tableBody = document.getElementById("staff-table-body");
        tableBody.innerHTML = ""; // Очистить таблицу перед заполнением

        dataArray.forEach(staff => {
            const row = document.createElement("tr");
            row.innerHTML = `
                <td><a href = "http://127.0.0.1:2000/items/${staff.name}/"><img src="http://127.0.0.1:2000/media/${staff.image}" alt="Фото ${staff.name}"></a></td>
                <td>${staff.name}</td>
                <td>£${staff.price}</td>
                <td>£${staff.price  - (staff.price / 100 * staff.discount).toFixed(2)}</td>
            `;

            tableBody.appendChild(row);
        });
    }

    fetchStaffData();
});
