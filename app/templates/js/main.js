if (document.getElementById("app")) {
    const app = new Vue({
        el: "#app",
        data: {
            books: [],
            errored: false,
            loading: true
        },
        created() {
            var url = 'http://127.0.0.1:5000/books'
            this.fetchData(url)
        },
        methods: {
            fetchData(url) {
                fetch(url)
                    .then(response => response.json())
                    .then(data => {
                        this.books = data;
                        this.loading = false;
                    })
                    .catch(err => {
                        this.errored = true
                    })
            },
            eliminar(books) {
                const url = 'http://127.0.0.1:5000/books/' + books;
                var options = {
                    method: 'DELETE',
                }
                fetch(url, options)
                    .then(res => res.text()) // or res.json()
                    .then(res => {
                        location.reload();
                        alert("Libro eliminado");
                    })
            }
        }
    })
}
