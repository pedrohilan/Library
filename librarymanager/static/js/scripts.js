$(document).ready(function(){

    var deleteBtn = $('.delete-btn');
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');
    var logoutBtn = $('#logout-btn');

    //Confirm delete
    $(deleteBtn).on('click', function(e){
        e.preventDefault();
        var delLink = $(this).attr('href');
        var result = confirm('Quer deletar este livro?');

        if(result){
            window.location.href = delLink;
        }

    });

    //Confirm logout
    $(logoutBtn).on('click', function(e){
        e.preventDefault();
        var logoutLink = $(this).attr('href');
        var result = confirm('Quer mesmo sair?');

        if(result){
            window.location.href = logoutLink;
        }

    });

    //
    $(searchBtn).on('click', function(e){
        searchForm.submit();
    });
});