function pobierzLeki(typ) {
    fetch(`http://127.0.0.1:8000/apteka/${typ}/`)
        .then(response => response.json())
        .then(data => {
            const lista = document.getElementById("lista-lekow");
            lista.innerHTML = "";
            data.forEach(lek => {
                const li = document.createElement("li");
                li.textContent = `${lek.nazwa} – ${lek.kategoria}`;
                lista.appendChild(li);
            });
        })
        .catch(error => console.error("Błąd:", error));
}
