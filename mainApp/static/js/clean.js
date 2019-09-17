document.getElementById('clear').addEventListener('mouseup', clearAll, false)

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

