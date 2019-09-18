function loadOptions(url){
    var xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function(){
        if (this.readyState == 4 && this.status == 200) 
        {
            var my_json = JSON.parse(this.responseText);

            input_key = document.getElementById('formKeyNameInput')
            
            my_json[1].forEach(element => {
                console.log(element['key_name']);
                var option = document.createElement('option');
                option.value = element['key_name']
                option.innerHTML = element['key_name']
                input_key.append(option);
            });

            input_domain = document.getElementById('formDomainInput')

            console.log(my_json)

            my_json[0].forEach(element => {
                console.log(element['url_domain']);
                var option = document.createElement('option');
                option.value = element['url_domain']
                option.innerHTML = element['url_domain']
                input_domain.append(option);
            });
        }      
    }
    xhttp.open("GET", url, true);
    xhttp.send(); 
}
