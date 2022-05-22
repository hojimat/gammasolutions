window.addEventListener('DOMContentLoaded', event => {
    
    const datatablesSimple = document.getElementById('datatablesSimple');
    if (datatablesSimple) {
        new simpleDatatables.DataTable(datatablesSimple);
    }

    const datatablesPlain = document.getElementById('datatablesPlain');
    if (datatablesPlain) {
        new simpleDatatables.DataTable(datatablesPlain, {
            searchable: false,
            fixedHeight: true,
            perPageSelect: false,
        });
    }
});
