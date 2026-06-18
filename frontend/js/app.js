const API_URL = "http://127.0.0.1:8000";

async function cargarTickets() {

    try {

        const response = await fetch(`${API_URL}/tickets`);
        const tickets = await response.json();

        const tabla = document.getElementById("tablaTickets");

        tabla.innerHTML = "";

        tickets.forEach(ticket => {

            tabla.innerHTML += `
                <tr>
                    <td>${ticket.id}</td>
                    <td>${ticket.titulo}</td>
                    <td>${ticket.descripcion}</td>
                    <td>${ticket.estado}</td>
                    <td>
                        <button
                            class="btn-edit"
                            onclick="editarTicket(${ticket.id}, '${ticket.titulo}', '${ticket.descripcion}', '${ticket.estado}')"
                        >
                            Editar
                        </button>

                        <button
                            class="btn-delete"
                            onclick="eliminarTicket(${ticket.id})"
                        >
                            Eliminar
                        </button>
                    </td>
                </tr>
            `;

        });

    } catch (error) {

        console.error(error);

    }

}

document.getElementById("ticketForm")
.addEventListener("submit", async (e) => {

    e.preventDefault();

    const titulo = document.getElementById("titulo").value;
    const descripcion = document.getElementById("descripcion").value;
    const estado = document.getElementById("estado").value;

    try {

        await fetch(`${API_URL}/tickets`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                titulo,
                descripcion,
                estado
            })
        });

        document.getElementById("ticketForm").reset();

        cargarTickets();

    } catch (error) {

        console.error(error);

    }

});

async function eliminarTicket(id) {

    if (!confirm("¿Deseas eliminar este ticket?")) {
        return;
    }

    try {

        await fetch(`${API_URL}/tickets/${id}`, {
            method: "DELETE"
        });

        cargarTickets();

    } catch (error) {

        console.error(error);

    }

}

async function editarTicket(id, titulo, descripcion, estado) {

    const nuevoTitulo = prompt("Nuevo título:", titulo);

    if (nuevoTitulo === null) return;

    const nuevaDescripcion = prompt(
        "Nueva descripción:",
        descripcion
    );

    if (nuevaDescripcion === null) return;

    const nuevoEstado = prompt(
        "Nuevo estado (Abierto, En proceso, Cerrado):",
        estado
    );

    if (nuevoEstado === null) return;

    try {

        await fetch(`${API_URL}/tickets/${id}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                titulo: nuevoTitulo,
                descripcion: nuevaDescripcion,
                estado: nuevoEstado
            })
        });

        cargarTickets();

    } catch (error) {

        console.error(error);

    }

}

document
.getElementById("buscarTicket")
.addEventListener("keyup", function () {

    const filtro = this.value.toLowerCase();

    const filas = document.querySelectorAll("#tablaTickets tr");

    filas.forEach(fila => {

        const texto = fila.innerText.toLowerCase();

        fila.style.display = texto.includes(filtro)
            ? ""
            : "none";

    });

});

cargarTickets();