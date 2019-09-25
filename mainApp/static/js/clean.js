document.getElementById('clear').addEventListener('mouseup', clearAll, false)

//If we gonna group by any parameters then add 'Total' column
if (document.getElementById("formDataGroup").checked || document.getElementById("formKeyNameGroup").checked
|| document.getElementById("formDomainGroup").checked || document.getElementById("formCodeGroup").checked){
    console.log("FUCK!!")
    var total_header = document.createElement('th');
        total_header.scope = 'col';
        total_header.innerHTML = 'Total';
    document.getElementById('table_headers').append(total_header);
};


function clearAll(){
    document.getElementById('formDataInput').value = '';
    document.getElementById("formDataGroup").checked = false;
    document.getElementById('formKeyNameInput').value = '';
    document.getElementById("formKeyNameGroup").checked = false;
    document.getElementById('formDomainInput').value = '';
    document.getElementById("formDomainGroup").checked = false;
    document.getElementById('formCodeInput').value = '';
    document.getElementById("formCodeGroup").checked = false;
    document.getElementById('formSizeInput').value = '';
}

