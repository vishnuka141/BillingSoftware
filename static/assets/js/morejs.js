function create_tr(table_id) {
    let table_body = document.getElementById(table_id),
        first_tr   = table_body.lastElementChild
        tr_clone   = first_tr.cloneNode(true);

    table_body.append(tr_clone);

    clean_first_tr(table_body.lastElementChild);
    event.preventDefault();
}

function clean_first_tr(firstTr) {
    let children = firstTr.children;
    
    children = Array.isArray(children) ? children : Object.values(children);
    children.forEach(x=>{
        if(x !== firstTr.lastElementChild)
        {
            x.lastElementChild.value = '';
        }
    });
}



function remove_tr(This) {
    if(This.closest('tbody').childElementCount == 1)
    {
        alert("You Don't have Permission to Delete This ?");
    }else{
        This.closest('tr').remove();
    }
}



